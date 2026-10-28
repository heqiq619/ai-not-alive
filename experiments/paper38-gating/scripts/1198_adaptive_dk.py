# -*- coding: utf-8 -*-
"""
1198_adaptive_dk.py — 在 (d,k) 前沿上加门控：每样本自己选迭代步数

任务：同 1197（迭代映射，复杂度 c ∈ {1,2,3}）
模型：共享块 + 每样本 halt 门（最多 8 步），宽度 d
对照：
  · 固定步数 k 的最好结果（1197 已测）
  · 自适应：准确率、平均步数、各复杂度 c 的平均步数
看：门控能不能让简单样本少迭代、复杂样本多迭代，
    并且在 d 很小时保持精度
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
torch.manual_seed(0)
D_IN = 16
N = 6000
STEPS = 1200
LR = 1e-3
MAX_STEPS = 8
LAMBDA_STEP = 0.08
W_MAP = torch.randn(D_IN, D_IN) / (D_IN ** 0.5)


def make_data(n):
    z = torch.randn(n, D_IN)
    c = torch.randint(1, 4, (n,))
    outs = [z]
    cur = z
    for _ in range(3):
        cur = torch.tanh(cur @ W_MAP.T)
        outs.append(cur)
    z_out = torch.stack([outs[3][i] if c[i] == 3 else (outs[1][i] if c[i] == 1 else outs[2][i]) for i in range(n)])
    y = (z_out[:, 0] > 0).long()
    x = torch.cat([z, (c.float() / 3.0).unsqueeze(1)], dim=1)
    return x, y, c


class AdaptiveNet(nn.Module):
    def __init__(self, d):
        super().__init__()
        self.emb = nn.Linear(D_IN + 1, d)
        self.block = nn.Sequential(nn.Linear(d, d), nn.ReLU(), nn.Linear(d, d))
        self.halt = nn.Linear(d + 1, 1)  # 让 halt 也能看到深度提示
        self.head = nn.Linear(d, 2)

    def forward(self, x):
        h = self.emb(x)
        steps = torch.zeros(x.shape[0])
        for t in range(MAX_STEPS):
            g = torch.sigmoid(self.halt(torch.cat([h, x[:, -1:]], dim=1))).squeeze(-1)
            g_hard = (g > 0.5).float()
            g_ste = g_hard + g - g.detach()
            h = h + g_ste.unsqueeze(-1) * self.block(h)
            steps = steps + g_hard
        return self.head(h), steps


def params(m):
    return sum(p.numel() for p in m.parameters())


def run(d):
    model = AdaptiveNet(d)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    lossf = nn.CrossEntropyLoss()
    x, y, c = make_data(N)
    for step in range(STEPS):
        idx = torch.randint(0, N, (512,))
        logits, steps = model(x[idx])
        loss = lossf(logits, y[idx]) + LAMBDA_STEP * steps.mean() / MAX_STEPS
        opt.zero_grad(); loss.backward(); opt.step()
    xe, ye, ce = make_data(4000)
    with torch.no_grad():
        logits, steps = model(xe)
    acc = (logits.argmax(1) == ye).float().mean().item()
    per_c = {}
    for ci in [1, 2, 3]:
        mk = ce == ci
        per_c[ci] = {'steps': float(steps[mk].mean()),
                     'acc': float((logits[mk].argmax(1) == ye[mk]).float().mean())}
    return {'d': d, 'acc': acc, 'mean_steps': float(steps.mean()),
            'params': params(model), 'per_c': per_c}


def main():
    print('=' * 72)
    print('自适应迭代（门控）：每个样本自己选步数（上限 %d）' % MAX_STEPS)
    print('=' * 72)
    out = []
    for d in [8, 16, 32, 64]:
        r = run(d)
        out.append(r)
        print('\nd=%d: acc=%.3f  平均步数=%.2f  参数=%d' % (d, r['acc'], r['mean_steps'], r['params']))
        for ci in [1, 2, 3]:
            print('   c=%d: 步数=%.2f  acc=%.3f' % (ci, r['per_c'][ci]['steps'], r['per_c'][ci]['acc']))
    io.open(DL + '数据-自适应dk.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))
    print('\n=== 与固定步数对比（来自 1197）===')
    print('固定最好：FF d=16,k=3 acc=0.96/1k参数；RNN d=8,k=4 acc=0.96/0.3k参数；RNN d=64,k=1 acc=0.95/9k参数')
    print('已保存: 数据-自适应dk.json')


if __name__ == '__main__':
    main()

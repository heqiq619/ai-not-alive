# -*- coding: utf-8 -*-
"""
1196_iterative_steps.py — 共享块 + 按需迭代步数

任务（结构复杂度）：
  · 随机向量 z（16 维），随机固定映射 f(z) = tanh(W z)
  · 复杂度 c ∈ {1, 2, 3}：标签 y = sign( (f^c z)[0] )
  · 输入里带"深度提示"（最后一维 = c/3）
  ⇒ 需要迭代 c 步才能算对；c 越大越复杂

模型：
  · 共享块 I（同一套参数可以反复用）
  · 每步一个"继续/停"判定（halt gate）
  · 最多迭代 8 步；稀疏惩罚鼓励少迭代

测：
  · 各复杂度 c 的平均迭代步数（预期 c 越大 → 步数越多）
  · 加噪声版本（噪声大时迭代帮不上忙 → 步数应该少）
  · 对照：固定 1/2/4/8 步的准确率
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
torch.manual_seed(0)
D_IN, D_H = 16, 32
MAX_STEPS = 8
N = 8000
STEPS = 1500
LR = 1e-3
LAMBDA_STEP = 0.02
W_MAP = torch.randn(D_IN, D_IN) / (D_IN ** 0.5)


def make_data(n, noise=0.0, fixed_c=None):
    z = torch.randn(n, D_IN)
    if fixed_c is None:
        c = torch.randint(1, 4, (n,))
    else:
        c = torch.full((n,), fixed_c)
    with torch.no_grad():
        zc = z.clone()
        for _ in range(3):
            zc = torch.tanh(zc @ W_MAP.T)
        # 逐样本按 c 迭代：简化——用最大3步的结果按c选择（c=1 用 z, 2 用 f(z), 3 用 f^3(z)）
        outs = [z]
        cur = z
        for _ in range(3):
            cur = torch.tanh(cur @ W_MAP.T)
            outs.append(cur)
        z_out = torch.stack([outs[3][i] if c[i] == 3 else (outs[1][i] if c[i] == 1 else outs[2][i]) for i in range(n)])
    y = (z_out[:, 0] > 0).long()
    x = z + noise * torch.randn(n, D_IN)
    cue = (c.float() / 3.0).unsqueeze(1)
    x = torch.cat([x, cue], dim=1)
    return x, y, c


class IterNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Linear(D_IN + 1, D_H)
        self.block = nn.Sequential(nn.Linear(D_H, D_H), nn.ReLU(), nn.Linear(D_H, D_H))
        self.halt = nn.Linear(D_H, 1)
        self.head = nn.Linear(D_H, 2)

    def forward(self, x):
        h = self.emb(x)
        steps = torch.zeros(x.shape[0])
        for t in range(MAX_STEPS):
            g = torch.sigmoid(self.halt(h)).squeeze(-1)
            g_hard = (g > 0.5).float()
            g_ste = g_hard + g - g.detach()
            h = h + g_ste.unsqueeze(-1) * self.block(h)
            steps = steps + g_hard
        return self.head(h), steps


def evaluate(model, x, y, c, tag):
    with torch.no_grad():
        logits, steps = model(x)
    acc = (logits.argmax(1) == y).float().mean().item()
    res = {'tag': tag, 'acc': acc}
    for ci in [1, 2, 3]:
        m = c == ci
        res['steps_c%d' % ci] = float(steps[m].mean()) if m.any() else None
    return res


def main():
    model = IterNet()
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    lossf = nn.CrossEntropyLoss()
    x, y, c = make_data(N)
    for step in range(STEPS):
        idx = torch.randint(0, N, (256,))
        logits, steps = model(x[idx])
        loss = lossf(logits, y[idx]) + LAMBDA_STEP * steps.mean() / MAX_STEPS
        opt.zero_grad(); loss.backward(); opt.step()
    print('=' * 70)
    print('共享块 + 按需迭代（复杂度 c=1/2/3，最多 %d 步）' % MAX_STEPS)
    print('=' * 70)
    out = []
    for tag, noise in [('干净', 0.0), ('噪声 σ=2', 2.0)]:
        xe, ye, ce = make_data(4000, noise=noise)
        r = evaluate(model, xe, ye, ce, tag)
        out.append(r)
        print('\n[%s] acc=%.3f' % (tag, r['acc']))
        for ci in [1, 2, 3]:
            print('  c=%d: 平均迭代 %.2f 步' % (ci, r['steps_c%d' % ci]))
    # 对照：固定步数（用训练好的块跑固定次数）
    print('\n--- 对照：固定步数 ---')
    for fixed in [1, 2, 4, 8]:
        # 临时用门全开/全关近似：直接测 trained 模型的步骤统计即可，这里给固定步数下的 acc
        class Fixed(IterNet):
            pass
        m2 = IterNet()
        m2.load_state_dict(model.state_dict())
        # 固定门：把 halt 权重置零后按固定步数执行
        with torch.no_grad():
            for t in range(fixed):
                pass
        # 简化：用 k=固定 的方法重算 h（手动前向）
        xe, ye, ce = make_data(4000, noise=0.0)
        with torch.no_grad():
            h = m2.emb(xe)
            for _ in range(fixed):
                h = h + m2.block(h)
            logits = m2.head(h)
        acc = (logits.argmax(1) == ye).float().mean().item()
        print('  固定 %d 步: acc=%.3f' % (fixed, acc))
        out.append({'tag': '固定 %d 步' % fixed, 'acc': acc})
    io.open(DL + '数据-按需迭代.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))
    print('\n已保存: 数据-按需迭代.json')


if __name__ == '__main__':
    main()

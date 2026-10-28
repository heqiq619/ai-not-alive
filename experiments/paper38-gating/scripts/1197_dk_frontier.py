# -*- coding: utf-8 -*-
"""
1197_dk_frontier.py — 空间维度 d vs 时间步数 k 的效率前沿

任务：迭代映射任务（需要 c 步迭代，c ∈ {1,2,3}）
  z ~ N(0,1)^16；固定随机映射 f(z)=tanh(Wz)
  y = sign( (f^c z)[0] )，输入带深度提示 c/3
模型两族：
  · FF：k 层不同的前馈网络，宽度 d
  · RNN：共享一个块，迭代 k 步，宽度 d
扫：d ∈ {8,16,32,64}，k ∈ {1,2,3,4,6,8}
测：准确率、参数量
⇒ 看 (d小,k大) 能不能顶 (d大,k小)
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
torch.manual_seed(0)
D_IN = 16
N = 6000
STEPS = 600
LR = 1e-3
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
    return x, y


class FFNet(nn.Module):
    def __init__(self, d, k):
        super().__init__()
        self.emb = nn.Linear(D_IN + 1, d)
        self.layers = nn.ModuleList([nn.Sequential(nn.Linear(d, d), nn.ReLU(), nn.Linear(d, d)) for _ in range(k)])
        self.head = nn.Linear(d, 2)

    def forward(self, x):
        h = self.emb(x)
        for L in self.layers:
            h = h + L(h)
        return self.head(h)


class RNNNet(nn.Module):
    def __init__(self, d, k):
        super().__init__()
        self.emb = nn.Linear(D_IN + 1, d)
        self.block = nn.Sequential(nn.Linear(d, d), nn.ReLU(), nn.Linear(d, d))
        self.k = k
        self.head = nn.Linear(d, 2)

    def forward(self, x):
        h = self.emb(x)
        for _ in range(self.k):
            h = h + self.block(h)
        return self.head(h)


def count_params(m):
    return sum(p.numel() for p in m.parameters())


def train_eval(make_model, d, k):
    model = make_model(d, k)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    lossf = nn.CrossEntropyLoss()
    x, y = make_data(N)
    for step in range(STEPS):
        idx = torch.randint(0, N, (512,))
        loss = lossf(model(x[idx]), y[idx])
        opt.zero_grad(); loss.backward(); opt.step()
    xe, ye = make_data(4000)
    with torch.no_grad():
        acc = (model(xe).argmax(1) == ye).float().mean().item()
    return acc, count_params(model)


def main():
    ds = [8, 16, 32, 64]
    ks = [1, 2, 3, 4, 6, 8]
    print('=' * 78)
    print('空间维度 d × 时间步数 k：效率前沿（迭代映射任务）')
    print('=' * 78)
    out = []
    for family, ctor in [('FF（不同层）', FFNet), ('RNN（共享块）', RNNNet)]:
        print('\n### %s' % family)
        print('%-4s' % 'd\\k', end='')
        for k in ks:
            print('%-10s' % ('k=%d' % k), end='')
        print()
        for d in ds:
            row = {}
            print('%-4d' % d, end='')
            for k in ks:
                acc, params = train_eval(ctor, d, k)
                row[k] = {'acc': acc, 'params': params}
                print('%-10s' % ('%.2f/%dk' % (acc, params // 1000)), end='')
            print()
            out.append({'family': family, 'd': d, 'k': row})
    io.open(DL + '数据-dk前沿.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))
    print('\n（每格 = 准确率/参数量k）')
    print('已保存: 数据-dk前沿.json')

    # 找"低维多步 vs 高维少步"的等价点
    print('\n=== 空间-时间等价点（准确率接近）===')
    for family in ['FF（不同层）', 'RNN（共享块）']:
        sub = [r for r in out if r['family'] == family]
        print('\n%s:' % family)
        for d_small in [8, 16]:
            for d_big in [32, 64]:
                # 找 d_small 下 k 大 的最好准确率 与 d_big 下 k 小 的
                small = sub[[r['d'] for r in sub].index(d_small)]
                big = sub[[r['d'] for r in sub].index(d_big)]
                best_small = max(v['acc'] for v in small['k'].values())
                best_small_k = max(small['k'], key=lambda k: small['k'][k]['acc'])
                small_at = small['k'][best_small_k]
                print('  d=%d,k=%d: acc=%.2f, params=%dk  ↔  d=%d,k=1: acc=%.2f, params=%dk' % (
                    d_small, best_small_k, best_small, small_at['params'] // 1000,
                    d_big, big['k'][1]['acc'], big['k'][1]['params'] // 1000))


if __name__ == '__main__':
    main()

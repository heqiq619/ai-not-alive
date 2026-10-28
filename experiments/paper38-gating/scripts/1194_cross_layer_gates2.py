# -*- coding: utf-8 -*-
"""
1194_cross_layer_gates2.py — 跨层门控（修剪枝版）

与 1193 的区别：
· 真掩码：被剪掉的边永久关闭（mask=0，门无法再学开）
· 用进废退：每 200 步统计最近使用率，< 0.08 的边剪掉
· 训练更长（2000 步）
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
torch.manual_seed(0)
D_IN, D_H, N_LAYERS = 16, 32, 5
N_TRAIN = 8000
STEPS = 2200
LR = 1e-3
LAMBDA_SPARSE = 0.005
PRUNE_START = 800
PRUNE_EVERY = 100
PRUNE_TH = 0.25


class CrossLayerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Linear(D_IN, D_H)
        self.blocks = nn.ModuleList([nn.Sequential(
            nn.Linear(D_H, D_H), nn.ReLU(), nn.Linear(D_H, D_H)) for _ in range(N_LAYERS)])
        self.W_dist = nn.ModuleDict({str(d): nn.Linear(D_H, D_H) for d in range(1, N_LAYERS)})
        keys = ['%d_%d' % (i, j) for j in range(N_LAYERS) for i in range(j)]
        self.gate_mlp = nn.ModuleDict({k: nn.Linear(D_H + 2, 1) for k in keys})
        self.gates = nn.ParameterDict({k: nn.Parameter(torch.zeros(1)) for k in keys})
        for k in keys:
            self.register_buffer('mask_' + k, torch.ones(1))
        self.ctx = nn.Linear(2, D_H)
        self.head = nn.Linear(D_H, 2)

    def gate(self, key, hi, task_id):
        logit = self.gate_mlp[key](torch.cat([hi, task_id], -1)).squeeze(-1) + self.gates[key]
        return torch.sigmoid(logit) * getattr(self, 'mask_' + key)

    def forward(self, x, task_id):
        h = self.emb(x)
        hs = []
        usage = {}
        for j in range(N_LAYERS):
            h_in = h.clone()
            for i in range(j):
                key = '%d_%d' % (i, j)
                if i < len(hs):
                    hi = hs[i]
                else:
                    continue
                g = self.gate(key, hi, task_id)
                g_hard = (g > 0.5).float()
                g_ste = g_hard + g - g.detach() if self.training else g_hard
                h_in = h_in + g_ste.unsqueeze(-1) * self.W_dist[str(j - i)](hi)
                usage[key] = g_hard.mean().item()
            hs.append(h_in)
            h = h_in + self.blocks[j](h_in)
        return self.head(h), usage


def make_data(n, task):
    x = torch.randn(n, D_IN)
    if task == 0:
        y = (x[:, 0] + 0.5 * x[:, 1] > 0).long()
    else:
        bits = (x[:, :4] > 0).long()
        y = (bits.sum(1) % 2).long()
    return x, y


def train():
    model = CrossLayerNet()
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    lossf = nn.CrossEntropyLoss()
    xa, ya = make_data(N_TRAIN, 0)
    xb, yb = make_data(N_TRAIN, 1)
    ta = torch.tensor([1.0, 0.0]).repeat(N_TRAIN, 1)
    tb = torch.tensor([0.0, 1.0]).repeat(N_TRAIN, 1)
    keys = list(model.gate_mlp.keys())
    recent = {k: [] for k in keys}
    dead = []
    for step in range(STEPS):
        idx = torch.randint(0, N_TRAIN, (256,))
        x = torch.cat([xa[idx], xb[idx]]); y = torch.cat([ya[idx], yb[idx]])
        tid = torch.cat([ta[idx], tb[idx]])
        logits, usage = model(x, tid)
        loss = lossf(logits, y) + LAMBDA_SPARSE * sum(torch.sigmoid(model.gates[k]).sum() for k in keys) / len(keys)
        opt.zero_grad(); loss.backward(); opt.step()
        for k in keys:
            if k not in dead and k in usage:
                recent[k].append(usage[k])
                if len(recent[k]) > 100:
                    recent[k].pop(0)
        if step >= PRUNE_START and step % PRUNE_EVERY == 0:
            with torch.no_grad():
                for k in keys:
                    if k in dead:
                        continue
                    u = sum(recent[k]) / max(1, len(recent[k]))
                    if u < PRUNE_TH:
                        getattr(model, 'mask_' + k).data *= 0.0
                        dead.append(k)
            if dead:
                print('  step %d 剪掉: %s' % (step, dead[-5:]))
    out = {}
    for name, (x, y, t) in {'easy': (xa, ya, ta), 'hard': (xb, yb, tb)}.items():
        with torch.no_grad():
            logits, _ = model(x, t)
        acc = (logits.argmax(1) == y).float().mean().item()
        all_usage = {}
        for s in range(0, len(x), 1000):
            _, u = model(x[s:s + 1000], t[s:s + 1000])
            for k, v in u.items():
                all_usage.setdefault(k, []).append(v)
        out[name] = {'acc': acc, 'rates': {k: sum(v) / len(v) for k, v in all_usage.items()}}
    out['dead'] = dead
    return out


def svg_graph(name, rates):
    W, H = 640, 300
    xs = [60 + i * 130 for i in range(N_LAYERS)]
    cy = 150
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">' % (W, H),
             '<rect width="100%" height="100%" fill="white"/>']
    for (k, r) in sorted(rates.items()):
        i, j = map(int, k.split('_'))
        if r < 0.03:
            continue
        x1, x2 = xs[i], xs[j]
        if j - i == 1:
            parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#333" stroke-width="%d"/>' % (x1 + 22, cy, x2 - 22, cy, max(2, int(r * 12))))
            parts.append('<text x="%d" y="%d" font-size="11" fill="#555">%.2f</text>' % ((x1 + x2) // 2 - 10, cy - 8, r))
        else:
            arc = 40 + (j - i) * 6
            parts.append('<path d="M %d %d Q %d %d %d %d" fill="none" stroke="#c33" stroke-width="%d"/>' % (
                x1, cy - 20, (x1 + x2) // 2, cy - 20 - arc, x2, cy - 20, max(2, int(r * 10))))
            parts.append('<text x="%d" y="%d" font-size="11" fill="#c33">%.2f</text>' % ((x1 + x2) // 2 - 10, cy - 28 - arc, r))
    for i, x in enumerate(xs):
        parts.append('<circle cx="%d" cy="%d" r="22" fill="#6a9"/>' % (x, cy))
        parts.append('<text x="%d" y="%d" font-size="12" text-anchor="middle" fill="white">L%d</text>' % (x, cy + 4, i))
    parts.append('<text x="12" y="20" font-size="13" fill="black">%s：跨层组合图（修剪枝后）</text>' % name)
    parts.append('</svg>')
    return ''.join(parts)


def main():
    print('=' * 66)
    print('跨层门控（修剪枝版）：5 层，用进废退')
    print('=' * 66)
    r = train()
    print('\n结果:')
    for name in ['easy', 'hard']:
        print('%s: acc=%.3f' % (name, r[name]['acc']))
        print('  边使用率:', ' '.join('%s:%.2f' % (k, v) for k, v in sorted(r[name]['rates'].items())))
    print('\n剪掉的边 (%d 条):' % len(r['dead']), r['dead'])
    html = '<html><body style="margin:0">' + svg_graph('跨层-easy', r['easy']['rates']) + '<br/>' + svg_graph('跨层-hard', r['hard']['rates']) + '</body></html>'
    io.open(DL + '组合图-跨层2.html', 'w', encoding='utf-8').write(html)
    io.open(DL + '数据-跨层门控2.json', 'w', encoding='utf-8').write(json.dumps(r, ensure_ascii=False, indent=2))
    print('已保存: 数据-跨层门控2.json, 组合图-跨层2.html')


if __name__ == '__main__':
    main()

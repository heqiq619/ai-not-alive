# -*- coding: utf-8 -*-
"""
1192_token_gates.py — 每 token 门控 + 有效组合图

模型：4 层小网络，每 token 两个门（计算门/对应门），straight-through 硬门
任务：easy（线性）与 hard（奇偶），混合训练
输出：
· 每任务各层门的开度
· 每 token 的有效深度（算了几层）
· 有效组合图（层间实际使用率）→ SVG + PNG
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
torch.manual_seed(0)
D_IN, D_H, N_LAYERS = 16, 32, 4
N_TRAIN = 8000
STEPS = 1500
LR = 1e-3
LAMBDA_SPARSE = 0.01


class TokenGatedNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Linear(D_IN, D_H)
        self.blocks = nn.ModuleList([nn.Sequential(
            nn.Linear(D_H, D_H), nn.ReLU(), nn.Linear(D_H, D_H)) for _ in range(N_LAYERS)])
        self.gate_c = nn.ModuleList([nn.Linear(D_H + 2, 1) for _ in range(N_LAYERS)])
        self.gate_r = nn.ModuleList([nn.Linear(2 * D_H + 2, 1) for _ in range(N_LAYERS)])
        self.ctx = nn.Linear(2, D_H)
        self.head = nn.Linear(D_H, 2)

    def forward(self, x, task_id, hard=True):
        h = self.emb(x)
        ctx = self.ctx(task_id)
        used = []  # 每层：是否算（0/1）
        gates_c, gates_r = [], []
        for L in range(N_LAYERS):
            inp = torch.cat([h, task_id], dim=-1)
            gc = torch.sigmoid(self.gate_c[L](inp)).squeeze(-1)
            gc_hard = (gc > 0.5).float()
            gc_ste = gc_hard + gc - gc.detach() if hard else gc
            block_out = self.blocks[L](h)
            inp2 = torch.cat([h, ctx, task_id], dim=-1)
            gr = torch.sigmoid(self.gate_r[L](inp2)).squeeze(-1)
            gr_hard = (gr > 0.5).float()
            gr_ste = gr_hard + gr - gr.detach() if hard else gr
            h = h + gc_ste.unsqueeze(-1) * block_out
            h = h + gr_ste.unsqueeze(-1) * ctx
            used.append(gc_hard)
            gates_c.append(gc.mean().item())
            gates_r.append(gr.mean().item())
        return self.head(h), used, gates_c, gates_r


def make_data(n, task):
    x = torch.randn(n, D_IN)
    if task == 0:
        y = (x[:, 0] + 0.5 * x[:, 1] > 0).long()
    else:
        bits = (x[:, :4] > 0).long()
        y = (bits.sum(1) % 2).long()
    return x, y


def main():
    model = TokenGatedNet()
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    lossf = nn.CrossEntropyLoss()
    xa, ya = make_data(N_TRAIN, 0)
    xb, yb = make_data(N_TRAIN, 1)
    ta = torch.tensor([1.0, 0.0]).repeat(N_TRAIN, 1)
    tb = torch.tensor([0.0, 1.0]).repeat(N_TRAIN, 1)
    for step in range(STEPS):
        idx = torch.randint(0, N_TRAIN, (256,))
        x = torch.cat([xa[idx], xb[idx]]); y = torch.cat([ya[idx], yb[idx]])
        tid = torch.cat([ta[idx], tb[idx]])
        logits, used, gc, gr = model(x, tid)
        loss = lossf(logits, y) + LAMBDA_SPARSE * (sum(gc) + sum(gr)) / (2 * N_LAYERS)
        opt.zero_grad(); loss.backward(); opt.step()

    print('=' * 66)
    print('每 token 门控：有效深度与有效组合图')
    print('=' * 66)
    out = {}
    for name, (x, y, t) in {'easy': (xa, ya, ta), 'hard': (xb, yb, tb)}.items():
        with torch.no_grad():
            logits, used, gc, gr = model(x, t)
        acc = (logits.argmax(1) == y).float().mean().item()
        used_mat = torch.stack([u for u in used], 0)  # (L, N)
        depth = used_mat.sum(0)                      # 每 token 算了多少层
        # 层间使用率矩阵：i 层算了且 j 层也算了的比例
        adj = torch.zeros(N_LAYERS, N_LAYERS)
        for i in range(N_LAYERS):
            for j in range(N_LAYERS):
                adj[i, j] = (used_mat[i] * used_mat[j]).mean().item()
        out[name] = {'acc': acc, 'gates_c': gc, 'gates_r': gr,
                     'depth_hist': {int(k): int(v) for k, v in zip(*torch.unique(depth, return_counts=True))},
                     'depth_mean': float(depth.mean()),
                     'adj': [[float(x) for x in row] for row in adj],
                     'layer_open_rate': [float(used_mat[i].mean()) for i in range(N_LAYERS)]}
        print('\n[%s] acc=%.3f  平均有效深度=%.2f 层（共 %d 层）' % (name, acc, depth.mean(), N_LAYERS))
        print('  各层开门率:', ' '.join('%.2f' % v for v in out[name]['layer_open_rate']))
        print('  有效深度分布:', out[name]['depth_hist'])
        print('  层间共开率（i行j列 = 第i层与第j层同时开）：')
        for i in range(N_LAYERS):
            print('   ', ' '.join('%.2f' % adj[i, j] for j in range(N_LAYERS)))

    # 生成组合图 SVG
    def svg_graph(name, data):
        W, H = 520, 180
        xs = [70 + i * 120 for i in range(N_LAYERS)]
        cy = 90
        parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">' % (W, H),
                 '<rect width="100%" height="100%" fill="white"/>']
        for i in range(N_LAYERS - 1):
            rate = data['adj'][i][i + 1]
            w = max(1, int(rate * 10))
            parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#333" stroke-width="%d"/>' % (xs[i] + 20, cy, xs[i + 1] - 20, cy, w))
            parts.append('<text x="%d" y="%d" font-size="11" fill="#555">%.2f</text>' % ((xs[i] + xs[i + 1]) // 2 - 12, cy - 12, rate))
        for i, x in enumerate(xs):
            rate = data['layer_open_rate'][i]
            parts.append('<circle cx="%d" cy="%d" r="20" fill="rgb(%d,%d,%d)"/>' % (x, cy, int(255 * (1 - rate)), int(255 * (0.4 + 0.5 * rate)), 120))
            parts.append('<text x="%d" y="%d" font-size="11" text-anchor="middle" fill="black">L%d</text>' % (x, cy + 4, i))
            parts.append('<text x="%d" y="%d" font-size="10" text-anchor="middle" fill="#555">开%.2f</text>' % (x, cy + 38, rate))
        parts.append('<text x="12" y="20" font-size="13" fill="black">%s：有效组合图（箭头=下一层同时开启率；圆=该层开门率）</text>' % name)
        parts.append('</svg>')
        return ''.join(parts)

    svgs = {name: svg_graph(name, out[name]) for name in out}
    for name, s in svgs.items():
        io.open(DL + '组合图-%s.svg' % name, 'w', encoding='utf-8').write(s)
    html = '<html><body style="margin:0">' + svgs['easy'] + '<br/>' + svgs['hard'] + '</body></html>'
    io.open(DL + '组合图.html', 'w', encoding='utf-8').write(html)
    io.open(DL + '数据-每token门控.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))
    print('\n已保存: 数据-每token门控.json, 组合图.html/.svg')
    print('\nSVG 文件: 组合图-easy.svg / 组合图-hard.svg')


if __name__ == '__main__':
    main()

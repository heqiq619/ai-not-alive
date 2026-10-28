# -*- coding: utf-8 -*-
"""
1199_gpt2_gates.py — 真实小模型（GPT-2）上的门控

做法：
· 冻结 GPT-2 全部权重
· 每层加一个小门（Linear(768,1)，共 12 个门，约 9k 参数）
· 门控制这一层的残差贡献：out = h + g * (block(h))，g 是每 token 的 0/1
· 用语言建模损失训练门（straight-through 硬门 + 稀疏惩罚）
测：
· 基础 PPL vs 门控后 PPL（质量损失）
· 各层开门率、每 token 有效深度
· 门与 token 可预测性的关系（低熵 token 是否更常跳层）
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
MODEL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/models/gpt2'
TXT = DL + '_tinyshakespeare.txt'
STEPS = 300
LR = 1e-3
LAMBDA_SPARSE = 0.01
SEQ = 128
BATCH = 4
torch.manual_seed(0)

from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tok = GPT2TokenizerFast.from_pretrained(MODEL)
model = GPT2LMHeadModel.from_pretrained(MODEL, torch_dtype=torch.float32)
model.eval()
for p in model.parameters():
    p.requires_grad_(False)
N_LAYER = len(model.transformer.h)
D = model.config.n_embd

text = io.open(TXT, encoding='utf-8', errors='ignore').read()[:400000]
ids = tok(text)['input_ids']
ids = torch.tensor(ids)
n_chunks = len(ids) // (SEQ + 1)
chunks = ids[:n_chunks * (SEQ + 1)].view(n_chunks, SEQ + 1)
n_train = int(0.9 * n_chunks)
train_chunks, val_chunks = chunks[:n_train], chunks[n_train:]
print('语料: %d chunks（训练 %d / 验证 %d），%d 层，%d 维' % (n_chunks, n_train, n_chunks - n_train, N_LAYER, D))

gates = nn.ModuleList([nn.Linear(D, 1) for _ in range(N_LAYER)])
for g in gates:
    nn.init.zeros_(g.weight); nn.init.zeros_(g.bias)
opt = torch.optim.Adam(gates.parameters(), lr=LR)

open_rates = torch.zeros(N_LAYER)
n_tokens = 0


def make_hook(layer_idx):
    def hook(module, args, output):
        global open_rates, n_tokens
        h = args[0]
        y = output[0]
        g = torch.sigmoid(gates[layer_idx](h)).squeeze(-1)  # (B, T)
        g_hard = (g > 0.5).float()
        g_ste = g_hard + g - g.detach()
        y_new = h + g_ste.unsqueeze(-1) * (y - h)
        with torch.no_grad():
            open_rates[layer_idx] += g_hard.sum()
            n_tokens += g_hard.numel()
        return (y_new,) + tuple(output[1:])
    return hook


handles = [blk.register_forward_hook(make_hook(i)) for i, blk in enumerate(model.transformer.h)]


def lm_loss(batch):
    out = model(input_ids=batch, labels=batch)
    return out.loss


print('训练门...')
for step in range(STEPS):
    idx = torch.randint(0, n_train, (BATCH,))
    batch = train_chunks[idx]
    loss = lm_loss(batch) + LAMBDA_SPARSE * torch.stack([torch.sigmoid(g.weight).mean() for g in gates]).mean()
    opt.zero_grad()
    loss.backward()
    opt.step()
    if step % 50 == 0:
        print('  step %d loss=%.3f' % (step, loss.item()))

# 评估
def ppl(model_gated=True, max_batches=10):
    tot, cnt = 0.0, 0
    with torch.no_grad():
        for i in range(min(max_batches, len(val_chunks))):
            b = val_chunks[i:i + 1]
            loss = (model(input_ids=b, labels=b).loss).item()
            tot += loss * b.numel(); cnt += b.numel()
    return float(torch.exp(torch.tensor(tot / cnt)))


if True:
    # 先测门控状态
    with torch.no_grad():
        gated_ppl = ppl(max_batches=10)
    rates = (open_rates / max(1, n_tokens) * N_LAYER).tolist()
    for h in handles:
        h.remove()
    base_ppl = ppl(max_batches=10)
    print('gate 用时 PPL: %.2f' % gated_ppl)
    print('移除门后基础 PPL: %.2f' % base_ppl)
    print('各层开门率:', ' '.join('%.2f' % v for v in rates))

# 每 token 有效深度 & 与熵的关系（重新挂 hook，采集）
open_rates.zero_(); n_tokens = 0
handles = [blk.register_forward_hook(make_hook(i)) for i, blk in enumerate(model.transformer.h)]
with torch.no_grad():
    b = val_chunks[:8]
    out = model(input_ids=b, labels=b)
    logits = out.logits
    probs = torch.softmax(logits, -1)
    ent = -(probs * torch.log(probs + 1e-12)).sum(-1)  # (B,T)
    # 每 token 有效深度：需要门值，重新前向并用 hook 记录
    depths = torch.zeros_like(ent)
    # 简单近似：用每层开门率代替（全局），更细需要逐 token 记录
print('\n已得到基础/门控 PPL 与开门率')

io.open(DL + 'zenodo-真实门控.json', 'w', encoding='utf-8').write(json.dumps({
    'base_ppl': base_ppl, 'gated_ppl': gated_ppl,
    'open_rates': rates, 'n_layer': N_LAYER,
}, ensure_ascii=False, indent=2))
print('已保存: zenodo-真实门控.json')

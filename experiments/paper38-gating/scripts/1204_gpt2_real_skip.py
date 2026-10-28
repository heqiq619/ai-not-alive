# -*- coding: utf-8 -*-
"""
1204_gpt2_real_skip.py — 真实的按 token 减算（不是后处理丢输出）

两个阶段：
① 训练门（模拟模式）：所有 token 都算，用 STE 学每 token 的 0/1
② 真实执行（部署模式）：只把"要算的 token"挑出来送进这一层，
   不用的 token 原样传下去 —— 这才真的省算力
测：
· 基础 PPL（标准前向）
· 真实执行、全开门时的 PPL（应与基础一致，验证实现正确）
· 真实执行、学到的门：PPL + 实际激活比例（= 真实减算比例）
· 用进废退：使用率低的门永久关闭后，PPL 与省算比例
"""
import io, json
import torch
import torch.nn as nn

DL = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
MODEL = DL + 'models/gpt2'
TXT = DL + '_tinyshakespeare.txt'
SEQ = 128
BATCH = 2
TRAIN_STEPS = 200
LR = 1e-3
LAMBDA = 0.01
torch.manual_seed(0)

from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tok = GPT2TokenizerFast.from_pretrained(MODEL)
model = GPT2LMHeadModel.from_pretrained(MODEL)
model.eval()
for p in model.parameters():
    p.requires_grad_(False)
blocks = model.transformer.h
N_LAYER = len(blocks)
D = model.config.n_embd
text = io.open(TXT, encoding='utf-8', errors='ignore').read()[:400000]
ids = torch.tensor(tok(text)['input_ids'])
n_chunks = len(ids) // (SEQ + 1)
chunks = ids[:n_chunks * (SEQ + 1)].view(n_chunks, SEQ + 1)
train_chunks, val_chunks = chunks[:int(0.9 * n_chunks)], chunks[int(0.9 * n_chunks):]
print('数据: %d train / %d val chunks' % (len(train_chunks), len(val_chunks)))

gates = nn.ModuleList([nn.Linear(D, 1) for _ in range(N_LAYER)])
for g in gates:
    nn.init.zeros_(g.weight); nn.init.zeros_(g.bias)
masks = [torch.ones(1) for _ in range(N_LAYER)]


def real_forward(input_ids, gate_override=None):
    """真实按 token 减算的前向：返回 logits、各层激活 token 数"""
    B, T = input_ids.shape
    pos = torch.arange(T)
    h = model.transformer.wte(input_ids) + model.transformer.wpe(pos)
    active_counts = []
    per_layer_active = []
    for li, blk in enumerate(blocks):
        new_h = h.clone()
        n_active = 0
        act_frac = []
        for b in range(B):
            hb = h[b]
            if gate_override is not None:
                g_hard = gate_override
            else:
                g = torch.sigmoid(gates[li](hb)).squeeze(-1) * masks[li]
                g_hard = (g > 0.5).float()
            idx = (g_hard > 0.5).nonzero().squeeze(-1)
            act_frac.append(idx.numel() / T)
            n_active += idx.numel()
            if idx.numel() > 0:
                sub = hb[idx]
                out = blk(sub.unsqueeze(0), attention_mask=None, use_cache=False)[0].squeeze(0)
                new_h[b, idx] = out
        h = new_h
        active_counts.append(n_active)
        per_layer_active.append(sum(act_frac) / B)
    h = model.transformer.ln_f(h)
    logits = model.lm_head(h)
    return logits, active_counts, per_layer_active


def ppl_standard(max_batches=10):
    tot, cnt = 0.0, 0
    with torch.no_grad():
        for i in range(min(max_batches, len(val_chunks))):
            b = val_chunks[i:i + 1]
            loss = model(input_ids=b, labels=b).loss.item()
            tot += loss * b.numel(); cnt += b.numel()
    return float(torch.exp(torch.tensor(tot / cnt)))


def ppl_real(gate_override=None, max_batches=10):
    tot, cnt, act = 0.0, 0, []
    with torch.no_grad():
        for i in range(min(max_batches, len(val_chunks))):
            b = val_chunks[i:i + 1]
            logits, counts, fracs = real_forward(b, gate_override)
            loss = nn.functional.cross_entropy(
                logits[:, :-1].reshape(-1, logits.shape[-1]),
                b[:, 1:].reshape(-1))
            tot += loss.item() * (b.numel() - 1); cnt += b.numel() - 1
            act.append(sum(fracs) / N_LAYER)
    return float(torch.exp(torch.tensor(tot / cnt))), sum(act) / len(act)


print('=' * 70)
print('① 基础 PPL（标准前向）: %.2f' % ppl_standard())
open_ppl, open_act = ppl_real(gate_override=torch.ones(SEQ))
print('② 真实执行 + 全开门: PPL %.2f（应≈基础），激活比例 %.3f' % (open_ppl, open_act))

# ── 训练门（模拟模式：所有 token 都算，STE 学门） ──
opt = torch.optim.Adam(gates.parameters(), lr=LR)
print('\n训练门（模拟模式）...')
for step in range(TRAIN_STEPS):
    idx = torch.randint(0, len(train_chunks), (BATCH,))
    b = train_chunks[idx]
    h = model.transformer.wte(b) + model.transformer.wpe(torch.arange(b.shape[1]))
    for li, blk in enumerate(blocks):
        hb = h
        g = torch.sigmoid(gates[li](hb)).squeeze(-1)  # (B,T)
        g_hard = (g > 0.5).float()
        g_ste = g_hard + g - g.detach()
        out = blk(hb, attention_mask=None, use_cache=False)[0]
        h = hb + g_ste.unsqueeze(-1) * (out - hb)
    h = model.transformer.ln_f(h)
    logits = model.lm_head(h)
    loss = nn.functional.cross_entropy(logits[:, :-1].reshape(-1, logits.shape[-1]), b[:, 1:].reshape(-1))
    loss = loss + LAMBDA * torch.stack([torch.sigmoid(g.weight).mean() for g in gates]).mean()
    opt.zero_grad(); loss.backward(); opt.step()
    if step % 50 == 0:
        print('  step %d loss %.3f' % (step, loss.item()))

real_ppl, real_act = ppl_real()
print('\n③ 真实执行 + 学到的门: PPL %.2f，平均激活比例 %.3f（≈省 %.0f%% 层内计算）' % (
    real_ppl, real_act, (1 - real_act) * 100))

# 各层实际激活率
with torch.no_grad():
    b = val_chunks[:5]
    _, _, fracs = real_forward(b)
print('各层实际激活率:', ' '.join('%.2f' % v for v in fracs))

# ── 用进废退：永久关闭使用率低的门 ──
with torch.no_grad():
    b = val_chunks[:5]
    # 收集每层每 token 的门值
    usage = []
    h = model.transformer.wte(b) + model.transformer.wpe(torch.arange(b.shape[1]))
    for li, blk in enumerate(blocks):
        g = torch.sigmoid(gates[li](h)).squeeze(-1) * masks[li]
        usage.append((g > 0.5).float().mean().item())
        h = h  # 仅统计输入状态（近似）
dead = []
for li in range(N_LAYER):
    if usage[li] < 0.5:
        masks[li] *= 0.0
        dead.append(li)
print('\n④ 用进废退：关闭使用率 < 0.5 的门 →', dead if dead else '无（所有层使用率都 ≥ 0.5）')
pruned_ppl, pruned_act = ppl_real()
print('   关闭后: PPL %.2f，激活比例 %.3f' % (pruned_ppl, pruned_act))

io.open(DL + '数据-真实减算门控.json', 'w', encoding='utf-8').write(json.dumps({
    'base_ppl': ppl_standard(), 'all_open_ppl': open_ppl,
    'real_ppl': real_ppl, 'real_active_frac': real_act,
    'pruned_layers': dead, 'pruned_ppl': pruned_ppl, 'pruned_active_frac': pruned_act,
    'layer_active_rates': fracs,
}, ensure_ascii=False, indent=2))
print('\n已保存: 数据-真实减算门控.json')

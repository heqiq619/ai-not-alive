# -*- coding: utf-8 -*-
"""
gpt2_gating_lagrange.py — GPT-2 上的拉格朗日门控实验（云端运行用）

三组对照（同一数据、同一步数）：
  A 普通微调（无门，全层）
  B 冻结主干 + 只训门（拉格朗日，目标平均 6 层）
  C 主干 + 门共同训练（拉格朗日，目标平均 6 层）

评测：验证 PPL、平均计算层数、各层开启率、计算时间
"""
import io, json, time, math
import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Tokenizer

DATA = 'tinyshakespeare.txt'
SEQ = 128
BATCH = 8
STEPS = int(__import__('os').environ.get('STEPS', '1500'))
LR = 5e-5
LR_GATE = 1e-2
LR_LAMBDA = 0.02
TARGET = 6.0
DEV = 'cuda' if torch.cuda.is_available() else 'cpu'

tok = GPT2Tokenizer.from_pretrained('gpt2')
tok.pad_token = tok.eos_token

text = io.open(DATA, encoding='utf-8', errors='ignore').read()
ids = tok(text)['input_ids']
n = (len(ids) - 1) // (SEQ + 1)
chunks = torch.tensor(ids[:n * (SEQ + 1)], dtype=torch.long).view(n, SEQ + 1)
n_train = int(0.9 * n)
train_chunks, val_chunks = chunks[:n_train], chunks[n_train:]
V = len(tok)


class GatedGPT2(nn.Module):
    def __init__(self, model, n_layers, gated=True):
        super().__init__()
        self.model = model
        self.n_layers = n_layers
        self.gated = gated
        self.gates = nn.ModuleList([nn.Linear(model.config.n_embd, 1) for _ in range(n_layers)]) if gated else None
        if gated:
            for g in self.gates:
                nn.init.zeros_(g.weight)
                nn.init.constant_(g.bias, 1.0)
        self.emb = model.transformer.wte
        self.pos = model.transformer.wpe
        self.blocks = model.transformer.h
        self.lnf = model.transformer.ln_f
        self.head = model.lm_head

    def forward(self, input_ids):
        B, T = input_ids.shape
        h = self.emb(input_ids) + self.pos(torch.arange(T, device=input_ids.device))
        hard_all, soft = [], torch.zeros((B, T), device=input_ids.device)
        for li, blk in enumerate(self.blocks):
            out = blk(h)[0]
            if not self.gated:
                h = out
            else:
                p = torch.sigmoid(self.gates[li](h)).squeeze(-1)
                hard = (p > 0.5).float()
                ste = hard + p - p.detach()
                h = h + ste.unsqueeze(-1) * (out - h)
                soft = soft + p
                hard_all.append(hard)
        logits = self.head(self.lnf(h))
        return logits, hard_all, soft


def build(gated):
    base = GPT2LMHeadModel.from_pretrained('gpt2')
    return GatedGPT2(base, len(base.transformer.h), gated=gated)


def loss_ppl(model, batches):
    tot, cnt, comp = 0.0, 0, 0.0
    rate_sum = None
    with torch.no_grad():
        for b in batches:
            logits, hard, soft = model(b)
            loss = nn.functional.cross_entropy(logits[:, :-1].reshape(-1, V), b[:, 1:].reshape(-1))
            tot += float(loss) * (b.numel() - 1); cnt += b.numel() - 1
            if hard:
                stack = torch.stack(hard)  # [L,B,T]
                comp += float(stack.sum(0)[:, :-1].mean())
                r = stack.mean(dim=(1, 2)).cpu()
                rate_sum = r if rate_sum is None else rate_sum + r
    rates = (rate_sum / len(batches)).tolist() if rate_sum is not None else []
    return float(torch.exp(torch.tensor(tot / cnt))), comp / len(batches), rates


def train(mode):
    """mode: 'plain' | 'frozen_gate' | 'joint_gate'"""
    gated = mode != 'plain'
    model = build(gated).to(DEV)
    if mode == 'frozen_gate':
        for name, p in model.named_parameters():
            p.requires_grad_(name.startswith('gates'))
        params = [p for p in model.parameters() if p.requires_grad]
        opt = torch.optim.Adam(params, lr=LR_GATE)
    else:
        opt = torch.optim.Adam(model.parameters(), lr=LR)
    lam = 0.0
    t0 = time.time()
    for step in range(STEPS):
        idx = torch.randint(0, n_train, (BATCH,))
        b = train_chunks[idx].to(DEV)
        logits, hard, soft = model(b)
        lm = nn.functional.cross_entropy(logits[:, :-1].reshape(-1, V), b[:, 1:].reshape(-1))
        loss = lm
        if gated:
            cost = soft[:, :-1].mean()
            loss = lm + lam * cost
        opt.zero_grad(); loss.backward(); opt.step()
        if gated:
            with torch.no_grad():
                avg = float(torch.stack(hard).sum(0)[:, :-1].mean())
                lam = min(5.0, max(0.0, lam + LR_LAMBDA * (avg - TARGET)))
        if step % 100 == 0:
            print('  [%s] step %d lm %.3f 层均 %.2f λ %.3f' % (
                mode, step, float(lm), float(torch.stack(hard).sum(0)[:, :-1].mean()) if gated else model.n_layers, lam))
    print('  训练耗时 %.1f 分钟' % ((time.time() - t0) / 60))
    return model


def main():
    results = {}
    val_batches = [val_chunks[i:i + 1].to(DEV) for i in range(min(20, len(val_chunks)))]
    for mode in ['plain', 'frozen_gate', 'joint_gate']:
        print('\n== 训练 %s ==' % mode)
        model = train(mode)
        ppl, layers, rates = loss_ppl(model, val_batches)
        layers = layers if mode != 'plain' else model.n_layers
        print('%s: PPL %.3f, 平均层数 %.2f / %d' % (mode, ppl, layers, model.n_layers))
        results[mode] = {'ppl': ppl, 'layers': layers, 'layer_rates': rates}
    io.open('results_gpt2_gating.json', 'w', encoding='utf-8').write(json.dumps(results, ensure_ascii=False, indent=2))
    print('\n已保存 results_gpt2_gating.json')
    print(json.dumps(results, ensure_ascii=False))


if __name__ == '__main__':
    main()

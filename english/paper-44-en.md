# Paper 44 · Gating and Sparse Execution: A Set of Engineering Observations (Consolidated Version, Pending Review)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Executor Engineering (internal No. 44)
> Date: 2026-11-01
> Status: engineering observations — mostly single seed, limited data and compute; conservative conclusions, no method claims.
> Note: this paper consolidates the previously scattered executor-engineering observations (former Papers 39, 40, 41, 42 and the unpublished 43) into one paper.
> English translation of the Chinese paper (the Chinese text is authoritative).

---

## Abstract

Executor engineering studies an engineering question: **can a model "compute less" at inference time without significantly degrading quality?**

Our answer: yes, but with clear boundaries. The main observations:

1. **Gate training works for models trained from scratch**: one content gate σ(W·h+b) per layer, with a Lagrange multiplier pushing the average number of open layers toward a target. On GPT-2 small (12 layers), the gated model uses 7.48 layers on average, PPL 12.03 (plain control 16.35, not converged; no "gating is better" claim).
2. **"Sparse execution that keeps K/V" is exactly equivalent to dense gating**: only compute Q, attention output rows, and MLP for open tokens; keep all K/V. Measured PPL 12.032 vs 12.033 (lossless). This shows gating itself does not hurt quality; quality differences come from the execution scheme.
3. **Converting to MoD-style capacity routing at inference is nearly lossless**: open-first + fixed capacity K_max per layer + padding. At factor = 1.0, nominal compute savings 37.9%, PPL 12.107 (+0.6%).
4. **No real speedup was obtained**: with our own gather/indexing implementation, batch-32 wall-clock 0.89–1.01×; one early implementation measured 1.22×, showing speedup is highly implementation-dependent and cannot be a conclusion of this paper.
5. **Attention subsetting (skipped tokens do not produce K/V) costs clearly**: +6.8% PPL when switched on an already-trained model; both from-scratch attempts collapsed (PPL 350.99 / 393.71).
6. **Scale and training scheme**: from-scratch training allows 1.2M, 124M and 1.5B models to work with about 44%–50% of layers at a cost of 1%–7%; pretrained models + LoRA post-training (3B/7B) cannot compress layers and PPL rises. The key variable is the training scheme, not parameter count.

## 1. Problem and background

### 1.1 Why "compute less"

A Transformer passes every generated token through all layers. If some tokens or some layers are redundant for a given token, skipping them saves compute. This line of thought has several versions in the literature: MoD (Mixture-of-Depths, capacity routing), early exit, conditional computation, sparse experts (MoE).

We are concerned with layer gating: **a per-layer, per-token open/close decision that determines whether that layer applies its transform to that token.**

### 1.2 Our terminology (defined here; used consistently below)

- **Content gate**: one linear layer W_l per layer, taking the token's current hidden state h and outputting g = σ(W_l·h + b). So the gate is "one W_l per layer, but each token has its own decision at each layer"; after each layer's matrix transform h changes, and the next layer's gate score changes accordingly.
- **Gate open (p > 0.5)**: that layer computes and writes back for that token.
- **Gate closed (p ≤ 0.5)**: skip that layer; the token's representation passes through the residual.
- **K/V**: attention's memory; all tokens produce and keep them (our "keep K/V" version).
- **Q-side update**: each token's own query and attention output; skipped when the gate is closed.
- **Sparse execution**: compute Q/attention output/MLP only for open tokens, always keeping all K/V.
- **Capacity routing (MoD style)**: fixed capacity K per layer; take the top-K tokens by gate score to enter that layer (capacity can differ across layers).
- **Subsetting**: a stronger sparsity — skipped tokens produce no K/V, and attention is computed only within the selected subset.

### 1.3 Relation to existing work

We claim no new method. Gating, sparse execution, capacity routing and early exit belong to conditional computation; MoD has reported the feasibility of capacity routing. Our work is: under limited compute and data, walking the engineering route "gate training + sparse execution at inference," recording what works, what does not, and where the boundaries are.

## 2. Method

### 2.1 Content gate + Lagrange budget

One content gate per layer. During training, a Lagrange multiplier λ controls the average open ratio: loss = language-modeling loss + λ · average number of active layers; λ adapts to "current average active − target." This way the gate does not need a manual "which layer to close" — training learns it.

### 2.2 Two execution schemes

- **Sparse execution keeping K/V**: all K/V computed; only open tokens' Q/attention output/MLP computed.
- **Capacity routing (MoD style)**: fixed capacity K per layer, top-K tokens by score; others take the residual. For static shapes, use padding slots with fixed K_max, filled by open tokens first; unfilled slots compute but do not write back.

### 2.3 Experimental setup (common)

- Data: tinyshakespeare (~1MB) or TinyStories slices (20MB/100MB).
- Evaluation: validation PPL; best recorded (early stopping to avoid overfitting interference); single seed.
- Hardware: Alibaba Cloud PAI-DSW, single V100 16GB or A10 24GB.

## 3. Experiments and results

### 3.1 Small model (6 layers, character level, ~1.2M parameters)

Early experiment, trained from scratch:

- plain, 3 seeds: mean PPL 6.103 (6.232 / 5.999 / 6.083);
- content gate + Lagrange target 3 layers: PPL 6.028, average 2.97/6 layers (about half);
- position gate (fixed table per layer × position): target 3 → PPL 6.038, average 2.98 layers;
- with λ=0 free training, the 24-layer small model chose 5.3/24 layers itself.

**Observation**: on the small model, gating can use half the layers without degrading quality; the gate is learned, not manually specified.

### 3.2 GPT-2 small (12 layers, 124M), from scratch

**1MB Shakespeare:**

| Group | best PPL | Steps | Average layers |
|---|---|---|---|
| plain | 44.03 | 1500 | 12 |
| joint_gate | 47.01 | 1000 | 5.30 (44%) |

Cost +6.8%. With λ≈0, the gate converges to about 5.3 layers by itself.

**100MB TinyStories:**

| Group | best PPL | Steps | Average layers |
|---|---|---|---|
| plain | 4.892 | 9000 | 12 |
| joint_gate | 5.023 | 9000 | 5.81 (48%) |

Cost +2.7%. Per-layer activation rate (final): `1.00, 0.82, 0.61, 0.01, 0.12, 0.35, 0.28, 0.25, 0.25, 0.45, 0.75, 0.74`. Layer 0 fully open, layer 3 almost unused, the last two layers back to 0.74–0.75.

**Observation**: as data grows (1MB → 100MB), the layer usage ratio barely changes (56% → 52%), but the cost shrinks (6.8% → 2.7%). More data makes gating "affordable," not "more compressive."

### 3.3 Qwen2.5-1.5B (28 layers), from scratch, 100MB

| Group | final PPL | best PPL | Average layers |
|---|---|---|---|
| plain | 6.301 | 6.501 @6500 | 28 |
| joint_gate | 6.373 | 6.113 @6500 | 12.32 (44%) |

Final-epoch cost +1.1%; on best, the gated group is even lower. Per-layer activation shows **the last 9 layers (L19–L27) almost entirely closed**.

**Observation**: scaled to 1.5B, gating is still cheap (44% layers, +1.1%). This contradicts the intuition "bigger models are harder to compress" and shows again that the key variable is "trained from scratch."

### 3.4 Pretrained models + LoRA post-training: cannot compress

**3B (36 layers) and 7B (28 layers)**, loading pretrained weights, LoRA r=16, 1MB data, 2000 steps:

| Setting | plain best | gated best | Layers used | Cost |
|---|---|---|---|---|
| Qwen2.5-3B target 33 | 12.61 | 14.94 | 32.79/36 (91%) | +18% |
| Qwen2.5-7B target 26 | 7.01 | 9.71 | 25.70/28 (92%) | +38% |
| Qwen2.5-7B target 24 | 7.01 | 12.93 | 24.01/28 (86%) | +85% |
| Qwen2.5-7B target 22 | 7.01 | 12.79 | 22.27/28 (80%) | +82% |

The 7B target-26 group also suffered gate collapse late in training (PPL rose to 1243, layers fell to 20).

**Observation**: pretrained weights + light post-training + small data: layers cannot be compressed and quality rises in cost. This is not a claim that "large models cannot be compressed"; it only shows "this post-training scheme does not work."

### 3.5 GPT-2 gated model + inference-side MoD (capacity routing)

On the GPT-2 gated model from 3.2 (7.48/12 layers, PPL 12.03), test inference schemes:

| Scheme | PPL | vs dense | Avg active | Note |
|---|---|---|---|---|
| dense gated (reference) | 12.033 | — | — | all compute |
| open_only (open tokens only, keep K/V) | **12.032** | **equivalent** | 0.622 | dynamic shapes |
| open_cap (open-first + capacity cap) | 12.176 | +1.2% | 0.592 | dynamic shapes |
| global top-k | 12.182 | +1.2% | 0.624 | dynamic shapes |
| static padded (K_max + mask) | 12.046–12.107 | +0.1%–+0.6% | 0.62–0.77 | static shapes |

**K_max margin sweep** (dense reference 12.034; K_max = average open count × factor):

| factor | PPL | Avg active | Nominal compute saving |
|---|---|---|---|
| 1.35 | 12.046 | 0.767 | 23.3% |
| 1.25 | 12.054 | 0.730 | 27.0% |
| 1.15 | 12.051 | 0.691 | 30.9% |
| 1.05 | 12.098 | 0.649 | 35.1% |
| **1.00** | **12.107** | **0.621** | **37.9%** |
| 0.95 | 14.458 | 0.592 | 40.8% |

**Observation**: the quality knee is at factor 1.0–1.05; the quality-first point is factor = 1.0, nominal 37.9% saving, PPL +0.6%.

**Real wall-clock (important negative result)**:

| Implementation | batch | dense | sparse | speedup |
|---|---|---|---|---|
| early Q-side sparse | 1 | 18.9 ms | 20.5 ms | 0.93× |
| same | 8 | 19.7 ms | 20.8 ms | 0.95× |
| same | 32 | 43.4 ms | 35.5 ms | 1.22× |
| static padded | 32 | 38.9 ms | 41.7–43.4 ms | 0.89–0.93× |
| static padded | 64 | 73.9 ms | 73.5 ms | 1.01× |

Our own implementation is Python-level gather + custom attention, far slower than PyTorch fused kernels. The difference between the early 1.22× and the later 0.89× shows: **wall-clock results are highly implementation-dependent and cannot be a stable conclusion.**

### 3.6 Attention subsetting: failure

**(a) Switching subsetting semantics on an already-trained model** (skipped tokens produce no K/V):

| Capacity | PPL | vs dense |
|---|---|---|
| quantized (nominal 37.5% saving) | 12.855 | +6.8% |
| half (45.8%) | 14.030 | +16.6% |
| quarter (68.75%) | 18.692 | +55% |

**(b) From-scratch subsetting (two attempts)**:

| Attempt | plain PPL | subset PPL | Active ratio |
|---|---|---|---|
| gate + threshold dynamic subset | 19.20 | 350.99 | collapsed to 8.3% |
| gate as router + fixed-capacity top-k + curriculum | 19.03 | 393.71 | 0.496 (capacity not collapsed) |

**(c) Short fine-tune recovery**: 400 steps, lr 5e-5, PPL collapsed to 136 (bad hyperparameters; cannot be used as evidence that "fine-tuning does not help").

**Observation**: attention subsetting on our gating route costs clearly; from-scratch training is worse. But this is not a conclusion that "subsetting itself is infeasible" — MoD's original method uses an independent router + capacity routing and validated the semantics at larger scale.

### 3.7 Branch-independent gating: failure

Two gates per layer (attention gate, MLP gate separated), from scratch, 12000 steps: final PPL 14.484 (attention gate 0.61, MLP gate 0.47); in contrast, joint gating (one gate for both branches) reaches 12.033 at 4000 steps. Branch-independent gating is clearly worse even after 3× steps.

**Branch sparsity split evaluation** (on the branch-independent model, forcing single-side sparsity via top-k):

| Test | PPL |
|---|---|
| baseline | 14.486 |
| MLP compressed to 25% | 558.95 |
| attention compressed to 25% | 69.45 |
| both compressed to 25% | 2195.20 |

**Observation**: on this model, "attention updates" tolerate sparsity better than "MLP updates." Together with "keeping K/V is lossless, subsetting hurts quality," the preliminary picture is: **MLP (weight-carried transforms) and K/V (memory) are load-bearing; Q-side updates are relatively skippable.** But this is a single-model observation, not a conclusion.

## 4. Discussion

### 4.1 Why "keeping K/V" is clearly better

**[Explanation]** Attention is the cross-token information pathway. If skipped tokens disappear from attention, later tokens see less context, and language modeling cannot compensate. Gating only decides "whether to update this token's representation"; keeping K/V means the decision does not affect information accessible to other tokens. This is the direct reason we see "keeping K/V lossless, subsetting +6.8%."

### 4.2 Why from-scratch training and post-training differ so much

**[Explanation]** From scratch, the model learns under the constraint "layers may be skipped" from the beginning and can concentrate computation into a few layers (the last 9 layers of the 1.5B model being almost closed is evidence). A pretrained model has no such opportunity: every layer was "used" during pretraining, and low-rank LoRA updates cannot change this structure.

### 4.3 Nominal compute saving vs real speedup

**[Fact]** What we measured is nominal compute (layers × token ratio). Real wall-clock depends on kernel implementation, batch size, and memory access; our own implementation gives 0.89–1.22× at batch 32/64 and cannot be a stable conclusion. Real speedup is an independent engineering problem beyond this experiment's conditions.

## 5. Limitations

- Mostly single seed; limited data (1MB–100MB); plain not converged in some experiments;
- From-scratch groups' absolute PPL does not represent real model capability (undertrained);
- PPL only, no downstream tasks;
- Wall-clock measurements are highly implementation-dependent;
- No same-setting comparison with the original MoD paper;
- From-scratch training above 1B and cross-domain generalization not verified.

## 6. Conclusion

1. **Gate training is usable**, and the gate is "one W_l per layer, one decision per token per layer, following the token's representation" — a content gate.
2. **"Sparse execution keeping K/V" is exactly equivalent to dense gating** — gating itself does not hurt quality; quality differences come from the execution scheme.
3. **Inference-side capacity routing (open-first + static K_max) achieves nominal 37.9% compute saving, PPL +0.6%**; the quality knee is K_max ≈ average open count.
4. **Attention subsetting on our gating route costs clearly** (+6.8%; from-scratch collapses), not generalized to "subsetting itself is infeasible."
5. **The key variable is the training scheme, not parameter count**: from-scratch 1.2M–1.5B can all use about half the layers; pretrained + LoRA post-training cannot compress.
6. **Real speedup is an independent engineering problem**; this paper draws no conclusion on it.

---

## Appendix: tags

- **[Fact]** all PPL, layer counts, activation rates, wall-clock in Section 3 (from results JSON).
- **[Explanation]** the analysis in Section 4.
- **[Conjecture]** "from-scratch training concentrates computation into a few layers" — supported by the 1.5B activation rates, not verified at larger scale.
- **[Not claimed]** no new method; no real speedup; no comparability with the original MoD paper.
- **Relation to old papers**: this paper consolidates former Papers 39, 40, 41, 42 and the unpublished 43; the old papers keep their DOIs and are considered superseded by this paper.

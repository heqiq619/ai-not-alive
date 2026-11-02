# Paper 45 · Frozen Submodels: Interfaces, Coordination and Hierarchy — Two Minimal Experiments (Pending Review)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Experiments (internal No. 45)
> Date: 2026-11-01
> Status: minimal-experiment observations — single seed, small scale; no method claims.
> English translation of the Chinese paper (the Chinese text is authoritative).

---

## Abstract

This paper answers one question: **can submodels that have already been trained and frozen be combined through interfaces to form a new structure?**

We ran two complementary minimal experiments.

**Experiment 1 (parallel composition)**: two independently trained 6-layer character-level models — A learns "next character of normal text," B learns "next character of Caesar-shifted (+1) text." Freeze A and B, add trainable controller interfaces between them, supporting four modes: A alone, B alone, A→B (normal input, shifted output), B→A (shifted input, normal output).

Results:
- Direct end-to-end concatenation (identity interface): PPL 62.84 (collapses);
- With a trainable controller: A→B 5.94, B→A 5.67;
- Native 12-layer model (upper bound on the same task): 5.41;
- A alone 6.03, B alone 6.31.

**Experiment 2 (hierarchical composition)**: a minimal chemotaxis environment (one-dimensional circular track, food consumption and regrowth, energy and death). The perception module M1 (supervised) and adaptation module M2 (supervised) are frozen; the decision layer D is trained with reinforcement learning in the environment.

Results:
- Random policy: return −1.34, average survival 66 steps, death rate 97%;
- Raw sensors only + D: return −1.40, survival 45 steps, death rate 98% (cannot learn);
- M1 + D: return 0.494, survival 183 steps, death rate 10%;
- M1 + M2 + D: return 0.505, survival 184 steps, death rate 9%.

**Conclusions (observations, not settled claims):**
1. Frozen submodels cannot be concatenated directly; a trainable interface/controller is needed.
2. With a controller, parallel composition approaches the native model (5.94/5.67 vs 5.41).
3. In hierarchical composition, frozen lower-level features are decisive for the upper decision layer (M1 cuts death rate from 98% to 10%).
4. The adaptation module M2 brings only a small improvement here (0.494 → 0.505); its value has not yet been forced out by the environment.

## 1. Problem and background

### 1.1 Why "frozen submodel composition"

Training a model is expensive; if capabilities can be compressed into small, freezable submodels and then combined, we can:
- reuse existing capabilities (no retraining);
- replace a single module without touching the rest;
- build more complex structures incrementally (hierarchy/modularity).

But freezing also means **no compensation by continued training**: the interface must do the coordination itself. That is what this paper tests.

### 1.2 Relation to existing work

We claim no new method. Adjacent work includes:
- Model stitching: freeze two halves of a network and connect them with a small stitch layer, used to study representation similarity;
- Task vectors / function vectors: transferable representations of capabilities in weight or activation space;
- Frozen-expert combination: multiple frozen modules + trainable interfaces/routing (e.g. the Bicameral Model couples two frozen language models through a trainable interface).

Our experiments are minimal-scale validations of these ideas: **is the interface necessary, how much can it recover, and is hierarchical freezing feasible?**

### 1.3 Terminology

- **Frozen submodel**: a model whose parameters are no longer updated after training.
- **Controller/interface**: a small trainable module inserted between two frozen submodels, responsible for representation-space alignment (in our experiments, a two-layer MLP per direction).
- **Parallel composition**: two submodels with different capabilities connected by interfaces (Experiment 1).
- **Hierarchical composition**: frozen lower modules provide features; a trainable upper module makes decisions (Experiment 2).

## 2. Experiment 1: parallel composition (two frozen language models + controller)

### 2.1 Setup

- Models: two tiny GPT-2-style character-level models (6 layers each, hidden 256, 8 heads, character vocabulary of 65).
- Data: tinyshakespeare character level, sequence length 128.
- Tasks:
  - A: next character of normal text;
  - B: next character of Caesar-shifted (+1) text.
- Training: A and B each trained from scratch for 1200 steps (batch 16, lr 3e-4), then frozen.
- Controller: one two-layer MLP per direction (256→256→256, GELU), initialized near identity; only the controller is trained; A and B frozen.
- Controls:
  - identity interface (untrained);
  - native 12-layer model (same task, 1500 steps) as an "upper bound";
  - A-alone and B-alone PPL.

### 2.2 Mode definitions

```
A-only: input → A's embedding → A's 6 layers → A's ln_f + lm_head
B-only: input → B's embedding → B's 6 layers → B's ln_f + lm_head
A→B:    input → A's embedding → A's 6 layers → C_AB → B's 6 layers → B's ln_f + lm_head
B→A:    input → B's embedding → B's 6 layers → C_BA → A's 6 layers → A's ln_f + lm_head
```

### 2.3 Results

| Setting | Validation PPL |
|---|---|
| A alone (normal text) | 6.03 |
| B alone (shifted text) | 6.31 |
| Native 12-layer (upper bound on translation task) | 5.41 |
| A→B direct concatenation (identity interface) | **62.84** |
| A→B + trained controller | **5.94** |
| B→A + trained controller | **5.67** |

### 2.4 Observations

1. **The identity interface fails completely** (62.84): two independently trained models have different hidden representation spaces; connecting them head-to-tail is like feeding one "language" into layers that only understand another.
2. **The trainable controller recovers it**: A→B 5.94, B→A 5.67, close to the native 12-layer upper bound 5.41 and to each submodel's own level (6.0–6.3).
3. **The controller is very small**: about 260k parameters for both directions, about 2.6% of the two submodels (about 5M each).
4. **Directions are roughly symmetric**: A→B vs B→A differ little (5.94 vs 5.67); no strong asymmetry appeared in this experiment.

### 2.5 Limitations

- Character-level tiny models; Caesar shift is an extremely simple task;
- The native 12-layer upper bound was trained for only 1500 steps and may not be fully converged;
- Modes are discrete switches (four independent modes), not "simultaneous bidirectional coupling";
- Single seed.

## 3. Experiment 2: hierarchical composition (frozen perception/adaptation + trainable decision in a chemotaxis environment)

### 3.1 Environment

Minimal chemotaxis environment (pure-function simulator, runs on CPU):

- One-dimensional circular track, 64 cells;
- Food field f[i] ∈ [0,1]: 2–3 Gaussian hotspots initially; decreases when eaten; regrows at 0.0015 per step;
- Agent: position p, energy e (initial 0.5, cap 0.8);
  - Each step costs 0.035 energy;
  - Eating the current cell's food: at most 0.15×0.6 replenishment;
  - e ≤ 0 → death, episode ends;
- Observation: average food in two cells ahead and behind (Gaussian noise 0.02);
- Actions: move left / move right / stay;
- At most 200 steps per episode;
- Reward: energy change + 0.002 (alive); death adds −1.

### 3.2 Modules

```
M1 perception (supervised, frozen):
  · Input: left/right sensor readings (2 dims)
  · Output: which side has more food (2 classes)
  · Label: the true left/right food comparison in the simulator (exactly computable)
  · Training: 4000 random-position samples

M2 adaptation (supervised, frozen):
  · Input: the last 6 steps' sensor means (6 dims)
  · Output: background food level (scalar)
  · Label: the simulator's global mean food level
  · Training: 3000 sequences

D decision (trainable):
  · Input: raw sensors (2) + M1 output (2) + M2 output (1)
  · Output: logits over 3 actions
  · Training: reinforcement learning (REINFORCE + return normalization), 2500 episodes
  · M1, M2 frozen; only D updated
```

### 3.3 Results

| Policy | Return | Average survival steps | Death rate |
|---|---|---|---|
| Random policy | −1.34 | 66 | 0.97 |
| Raw sensors only + D | −1.40 | 45 | 0.98 |
| M1 + D | 0.494 | 183 | 0.10 |
| M1 + M2 + D | 0.505 | 184 | 0.09 |

### 3.4 Observations

1. **The environment has real pressure**: the random policy starves 97% of the time, surviving only 66 steps on average.
2. **With raw sensors only, the decision layer cannot learn**: return −1.40, death rate 98%, comparable to random. Noisy single-step observations are insufficient for a small MLP to learn chemotaxis by policy gradient.
3. **The frozen perception module is decisive**: with M1, return turns positive (0.494), survival is 183 steps, death rate falls to 10%.
4. **The adaptation module M2 brings only a small improvement**: 0.494 → 0.505. Possible reasons: background changes are slow in this environment, so M2's information gain is limited; or M2's supervised target (global mean) is not exactly what the decision needs.
5. **Engineering is feasible**: all small MLPs + CPU; training and evaluation complete in minutes.

### 3.5 Limitations

- One-dimensional, discrete grid, simplified food dynamics;
- M1 and M2 overlap functionally in the 1D setting; their independent contributions are not fully separated;
- The RL policy is trained for only 2500 episodes and may not be converged;
- Single seed.

## 4. Discussion

### 4.1 Why the identity interface fails

**[Explanation]** Two independently trained models each form their own hidden representation coordinates (scale, direction, feature basis). A's last-layer output is "for A's output layer," not what B's input layer expects. Direct connection is cross-language communication without translation; failure is expected.

### 4.2 Why a small controller can recover it

**[Explanation]** The controller only needs to map between representation spaces, not relearn the task. The mapping is a low-dimensional linear/nonlinear transform, far smaller than the submodels but sufficient to move A's representation near B's input distribution. In the experiment, 2.6% of parameters recovered about 90% of the gap (62.84 → 5.94, upper bound 5.41).

### 4.3 Why frozen lower layers are decisive in hierarchical composition

**[Explanation]** The decision layer only sees observations and lower-level features. If the observations themselves are insufficient (noisy single-step sensors), policy gradient struggles to learn effective behavior from sparse rewards; the frozen perception module directly provides the discriminative feature "which side has more food," equivalent to giving a good state representation. This matches the common experience of "pretrained features + linear probing/fine-tuning heads."

### 4.4 On whether "perception and adaptation are redundant"

**[Fact]** In the 1D setting, M1 and M2 do overlap (both process sensor history/difference). This experiment did not separate the contributions of "history information" from "perception features." Answering this requires two additional controls: "raw_hist" (raw history but no M1/M2) and a "recurrent decision layer."

## 5. Limitations (overall)

- Both experiments are single-seed and extremely small-scale (character-level tiny models / one-dimensional environment);
- Experiment 1's "upper bound" model was trained with fewer steps than the submodels, so the comparison is not strict;
- Experiment 2's RL training is limited; M2's benefit may be underestimated;
- No "simultaneous bidirectional coupling" (lockstep) or "layer-by-layer frozen growth" experiments;
- Transferability at real scale not verified.

## 6. Conclusion

1. **Frozen submodels cannot be concatenated directly**; a trainable interface/controller is needed for representation alignment (Experiment 1: 62.84 → 5.94).
2. **A small controller (about 2.6% of parameters) recovers most of the loss**, bringing parallel composition close to the native model (5.94/5.67 vs 5.41).
3. **Hierarchical composition works**: frozen perception + trainable decision layer cuts the death rate from 98% to 10% and turns the return positive in the chemotaxis environment.
4. **The adaptation module's value has not appeared** (0.494 → 0.505); a more "adaptation-demanding" environment is needed to test it.
5. Engineering has no special barrier: small MLPs + CPU suffice; interfaces and modules can all be frozen/replaced.

---

## Appendix: tags

- **[Fact]** all PPL, returns, survival steps, and death rates in Sections 2 and 3 (from run results).
- **[Explanation]** the analysis in Section 4.
- **[Conjecture]** "the adaptation module will have value in a harder environment" — not verified.
- **[Not claimed]** no new method; not claimed to outperform native models; not claimed to scale to real size.
- Adjacent work: model stitching, task/function vectors, frozen-expert combination (e.g. the Bicameral Model).

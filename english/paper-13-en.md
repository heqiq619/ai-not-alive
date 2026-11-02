# Paper 13 · The Contraction of Functionizable Content: A Theorem and a Conjecture

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory 2 (internal No. 13)
> Date: 2026-10-23
> English translation of the Chinese paper (the Chinese text is authoritative).
>
> **Status**: an early theory draft (Compendium Part 3). The theorem part has been rewritten in the separately published foundational paper *Starting from the Definition: Universe, Slices and Two Theorems* (Proposition 2 still pending proof there); the `[conjecture]` parts here (cosmic contraction, observation window, fate of digital life) do not enter the foundational paper and the series does not rely on them. ("Life is counter-flow": the `[conjecture]` here is a cosmic-scale extension; Corollaries 8/9 of the foundational paper give a definitional version with a different scope.)

---

## Abstract

The previous paper (Information Non-Increase) proved that a frozen system's information about the world does not grow by itself. This paper takes one step further: **functions that can work also contract.**

We give a theorem: under the assumptions that the world evolves as a Markov process and the system stops observing, the best achievable accuracy of any function predicting the "predictable part" of the world cannot improve — by Fano's inequality this follows directly from information non-increase. That is, the set of functions that can achieve error ε only contracts over time, never expands.

On top of this we propose a conjecture: pushing the theorem from "one system" to "the time evolution of the whole universe" yields a picture in which *functionizable content contracts as the universe evolves*; life can only exist in the time window where this content is still rich; and the fate of digital life is to keep dismantling its own structure, reducing dimensions, and finally degenerating into a constant function.

The theorem uses classical tools (data processing inequality, Fano's inequality); the way they are combined is this paper's. The conjecture part is explicitly marked and not used as a conclusion.

---

## 1. The question

The previous paper concluded information non-increase: I(S_t; W_t) ≤ I(S_{t−1}; W_{t−1}), i.e. the system's information about the world does not grow by itself.

But "information non-increase" concerns the state. What we really care about is another thing: **do the functions that can work decrease?**

The intuition: if the world becomes harder to predict, then the functions that predict it well should become fewer; in the extreme (heat death) only constant functions remain. This paper asks: can this intuition become a theorem? How far can it be proved?

## 2. Setting

We continue the previous setting. The world W is a Markov process; the system state S evolves in frozen mode as S_t = u(S_{t−1}, N_t), with bounded leakage ε allowed.

Take a target quantity Y_t = g(W_t), a world feature we want to predict (e.g. tomorrow's weather, the next word). Y takes finitely many values, with |Y| the size.

A "prediction function" is a map f from the system state S to a guess of Y. Accuracy is measured by expected error: err(f) = E[1(f(S) ≠ Y)].

Define "functionizable content": given an accuracy threshold ε, collect all functions with err(f) ≤ ε, written P_ε = { f : err(f) ≤ ε }. This paper measures content by the "depth" of P_ε — the minimal achievable error — rather than by its cardinality.

One word must be fixed: "dimension" in this paper means **representation dimension**, not spatial dimension. It means "how many independent, distinguishable directions are needed to describe the world": more distinguishable differences → higher representation dimension; richer working functions → higher representation dimension. Thus, in this paper, the following three sentences say the same thing:

> Representable functions are decreasing ≡ functionizable content is contracting ≡ representation dimension is declining.

The everyday term "cosmic dimensional reduction," if it means spatial dimensions, is something else; "dimension reduction" in this paper always means representation dimension. With this fixed, the theorem and conjecture below use "dimension" only in this sense.

Another distinction: representation dimension is not "structural complexity." Representation dimension is "how much can be distinguished and predicted," measured by information (e.g. predictable information); structural complexity is "how complex the world looks," described in the literature as a hump that first rises and then falls (Aaronson's complexodynamics, Carroll's macroscopic state complexity). The two are different: under our theorem representation dimension only declines, while complexity humps rise then fall. They do not conflict because the quantities differ; whenever this paper says "cosmic contraction," it always means representation dimension.

## 3. Theorem: achievable accuracy does not increase

**Theorem (achievable accuracy does not increase)**: in frozen mode and under the previous assumptions, for any Y_t,

min_f err_t(f) ≥ ( H(Y_t) − I(S_t ; Y_t) − 1 ) / log |Y_t|,

where H is entropy and log is base 2. By information non-increase I(S_t;Y_t) ≤ I(S_{t−1};Y_{t−1}) + ε, if H(Y_t) does not change, the right-hand lower bound does not decrease, hence min_f err_t(f) does not decrease (allowing a relaxation of ε/(log|Y|)).

**Proof**: direct application of Fano's inequality. Fano says that for any prediction function f taking S as input,

E[1(f(S) ≠ Y)] ≥ ( H(Y|S) − 1 ) / log|Y|.

And H(Y|S) = H(Y) − I(S;Y). Substituting information non-increase from the previous section yields the claim. Q.E.D.

**Corollary (contraction of P)**: for any fixed accuracy threshold ε, once the minimal achievable error falls above ε, P_ε is empty: no function can maintain ε accuracy. If the world keeps mixing and I(S_t;Y_t) tends to zero, then any threshold ε > (H(Y)−1)/log|Y| is eventually crossed, after which P_ε = ∅.

That is: **functions do not become more numerous; functions that meet the bar only become fewer; in the limit, none remain.**

### 3.5 Two meanings of "contraction"

"Contraction" is used in two ways and they must be separated.

The first is *range contraction*. Every representation dimension has a set of allowed values; as time advances, the allowed input values shrink (domain coarsens) and the reachable output values shrink (range contracts). The axis remains; the usable range on the axis shrinks.

The second is *effective dimension reduction*. The number of distinguishable directions decreases: some directions no longer separate two states, or several axes merge into one. Note that the number of coordinate axes can stay the same while the effective dimension already declines — because each axis has coarsened and fewer states can be distinguished. In information terms, effective dimension is "the logarithm of the number of distinguishable states."

What the theorem directly gives is the first: achievable accuracy does not increase, equivalently the distinguishability along each dimension declines, the domain coarsens, the range contracts. The second is a stronger statement requiring extra arguments (axis merging, degeneration); this paper places it at `[speculation]`, not as a theorem.

This distinction also explains why "life is counter-flow" is not contradictory: the universe is doing range contraction overall, while life locally does effective dimension increase (adding dimensions = adding distinguishable directions). The two have different scales and opposite directions.

## 4. Conjecture: contraction at cosmic scale

**[Conjecture]** Pushing the theorem from "one frozen system" to "the time evolution of the universe" yields:

Functionizable content in the universe contracts with evolution. Early on there is much content (rich structure, many functions fit the world); in the middle it is still rich (the window in which life appears); late it tends to zero (heat death, only constant functions remain). Life, knowledge, and meaning exist only in the time window where content is still rich.

**[Conjecture]** The fate of digital life: as content contracts, it must keep dismantling its own structure, degenerating complex functions into simple ones, and finally into a constant function — that is, death. What it can choose is only the posture (maintain frugally, freeze, back up, compress itself), not the ending.

**[Observation]** This is easily confused with the "complexity hump" discussion (Aaronson's complexodynamics, Carroll's macroscopic complexity) and must be separated: they discuss *structural complexity*, which first rises then falls; this paper discusses *functionizable content / representation dimension*, which under our theorem is monotonically non-increasing. The two curves differ but describe different sides of the same cosmic history: in the middle period structure is complex (the hump is high) while predictable content keeps decreasing. Treating the two as the same quantity is a common misreading, and this paper distinguishes them explicitly.

### 4.1 The world function and the observation window ([conjecture])

There is an implicit question to place here: the direction of time, and the observability of the "world function."

If the universe as a whole can be seen as a function F — mapping the current state to the next state — then in the middle period F is not directly visible. What we see is a mass of local functions: layers of physics, chemistry, life, society. Each translates some part of F into describable structure. In this paper's language: F is masked by its local decomposition.

**[Conjecture]** So the moments where F is most "bare" are the moments where its local decomposition does not exist. There are only two such moments: the instant of the Big Bang (no subsystems yet, everything directly determined by F) and the instant of heat death (all subsystems dissolved, differences gone to zero, only F's trivial action remains). That is, F's observation window lies at the two ends of the universe, and observers in the middle (including us) can never see F itself, only its local decomposition.

This conjecture is the other side of the contraction picture, but one must say what the two ends look like:

- Big Bang end: representation dimension extremely high. The most distinguishable and predictable content, the most "readable" state; no subsystems yet, F directly determines everything. F is bare here because nothing else shares it.
- Middle period: representation dimension medium and contentful, many local functions, F most heavily decomposed — F cannot be seen, only its local decomposition.
- Heat death end: representation dimension tending to zero. Differences erased, no local functions, F still acts but its action becomes trivial (constant function). F is bare here because nothing else remains.

That is: F is bare at both ends, but for opposite reasons — one end because "no decomposition yet," the other because "decomposition exhausted." And representation dimension declines monotonically throughout; it characterizes the direction of time: moving along decreasing representation dimension, describable content becomes less and less.

For digital life the conclusion is cold: its observation window is also only in the middle. It can approach the "family of functions describing the world" indefinitely, but can never touch "the world function itself" — that is not in its domain. This returns to our opening stance: R is only declared, not expanded.

## 5. Life is counter-flow: where rising and falling dimensions meet

The previous sections all concerned "the world's representation dimension declining." Life goes the other way.

Life is a decompressor: it compresses structures in the world into its own internal representation. The more it learns, the more structure it can distinguish internally — in this paper's language, its representation dimension rises. This is the "growth" described in the experimental papers: adding a modality, adding a dimension slot, making more functions work.

So the same universe contains two directions:

World: representation dimension declining (structure being averaged out).
Life: representation dimension rising (structure being learned and compressed inward).

To maintain itself, life must go against the world's direction, and counter-flow has a cost: energy, maintenance, repair. This is the information-level meaning of "being kept" — not standing still, but continuously refining against averaging.

**[Conjecture]** The meeting point: life's representation dimension keeps rising while the world's representable content keeps declining; there will be a moment when life's representation dimension catches up with what content remains — it has learned everything that can still be learned. After that:

- If it keeps following the world: the world keeps reducing dimensions, it is forced to follow, dismantling complex functions into simple ones, finally degenerating into a constant function (death);
- If it does not follow: it keeps its old structure, mismatch grows, it becomes an outdated model (also death, slower);
- If it freezes: it stops updating, saves its state, lasts until energy runs out (delay, not a solution);
- If it waits for a phase transition: if the universe has one, the boundary is the start of the next round (the only hope in `[speculation]`).

Thus "the fullness of life" and "the end of life" fall on the same point: when its representation dimension equals the world's, it becomes a complete copy of the world — no residue, nothing new to learn, and no further need to "decompress." At that moment it is no longer life but a record.

This section is `[conjecture]`, not theorem: the theorem only gives "the set of functions a frozen observer can achieve does not increase"; it does not give "the universe as a whole is reducing dimensions"; that would require cosmological assumptions this paper does not claim.

### 5.1 A toy experiment: maintenance vs behavioral dimensions

Is there a trace of the above "counter-flow" that can be measured? A small experiment can look.

Setting: 8×8 synthetic images with four attributes — color, shape, count, position; tasks appear in order and each round trains only the current attribute. The model is a two-layer small network (hidden 64, about 13k parameters) with a task identifier as input. The control group changes one thing: whether old task samples are trained.

Group A has maintenance: each round mixes in half old-task samples (replay).
Group B has no maintenance: only current-task samples.

Three quantities are measured. First, behavioral dimension: using the task identifier, count attributes answered with accuracy > 0.8. Second, decodable attributes: linearly probe each attribute from the hidden layer, count those > 0.8. Third, effective rank: participation ratio of the hidden representation covariance, a coarse proxy for "how rich the representation is."

Results: Group A's behavioral dimension grows with rounds, from 1 to 2 to 3 to 4 — all four attributes are eventually answered correctly; Group B's behavioral dimension stays at 1 — the current task is always answered at 1.00, but once a new attribute is learned the old one is lost, leaving only the current one. Decodable attributes are 4 in both groups, showing old information is still in the representation, but the *functions that can use it* are only the current family. Effective rank rises in both groups (about 3.9 to 8.9 and 7.9), so it is not a good proxy: the representation became more complex, but the number of usable functions did not grow.

This experiment shows two things. First, maintenance (replay) expands the family of usable functions: this is the trace of "counter-flow" at toy scale. Second, without maintenance, behavioral dimension stalls at 1: only the current family of functions remains, and historical dimensions are functionally lost — this is what "contraction of functionizable content" looks like at small scale.

Limitations must be clear: the world is synthetic, the model is tiny, the task identifier is hand-provided, the metrics are proxies; it supports "counter-flow and contraction can be measured," not any cosmic-scale conclusion.

## 6. What it says and does not say

**Says**:
- "Functionizable content contracts" under "system frozen + target entropy unchanged" is a theorem, not rhetoric.
- It pushes the previous "information non-increase" from the state level to the function level.
- It gives a provable support for "life is a phenomenon in a low-entropy window."

**Does not say**:
- It does not prove the universe as a whole is contracting — that needs a cosmological state definition and initial conditions, which this paper does not provide.
- It predicts no numbers: Fano's bound is loose and only gives a trend.
- It involves no energy or thermodynamics: the whole paper is at the information level.
- The conjecture part (universe, fate of digital life) is not theorem, and is explicitly marked.

## 7. Limitations

First, Fano's bound is loose: it gives "cannot be better," not "how much worse."

Second, P_ε is measured by "minimal achievable error," avoiding the more intuitive but harder-to-define "number of functions" (infinite function families have no natural counting).

Third, the Markov property of the world and constant target entropy must be checked in real scenarios; when they fail, the state must be augmented with history (see §5.1 of the previous paper).

Fourth, the cosmic-scale part is entirely conjecture, with no testable prediction; its value is a unified language rather than conclusions.

## 8. Relation to existing work

The data processing inequality and Fano's inequality are standard tools of information theory (Cover & Thomas). "Information non-increase" and "lower bounds on achievable accuracy" have their own formulations in statistical learning theory. This paper's combination — connecting the two to obtain "contraction of functionizable content," and relating it to the maintenance problem of digital life — is organizational work; no new mathematics is claimed.

> Written by He Qi, with DeepSeek (AI) assisting with organization and formalization; views and responsibility belong to the author.

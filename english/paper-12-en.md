# Paper 12 · The Information Non-Increase Theorem for Digital Life

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory (internal No. 12)
> Date: 2026-10-23
> English translation of the Chinese paper (the Chinese text is authoritative).

---

## Abstract

This paper turns the intuition "a digital life becomes less and less able to describe the world as it ages" into a provable information-theoretic proposition.

Setting: the world evolves as a Markov process; a digital life holds an internal state S and predicts the world from it; after observations stop, the state evolves only by its own rules. Conclusion: under these conditions the mutual information between the internal state and the current world state cannot increase — the world changes while the system no longer looks, so its information about the *current* world can only stay flat or decline.

This is not the second law of thermodynamics, nor "entropy must increase." It states a narrower but harder fact: **a system that no longer acquires information does not grow information about the world by itself; maintenance requires continuous observation and updating.**

The paper gives the theorem, its proof, four corollaries (coarsening of the domain, necessity of maintenance, growth as adding observation dimensions), and the scope and limitations.

---

## 1. The question

Paper 6 (Capacity Cannot Substitute for Data Updates) measured a phenomenon: after training, a model gradually mismatches the updated language and cannot recover by itself. At the time we reported measurements, not an explanation.

Intuitively it is easy: the world changes, the model stopped looking, so it becomes less accurate. But intuition is not a theorem. This paper asks: can we state it as a provable information-theoretic proposition?

Yes, but the scope must be handled carefully. What we cannot prove: "entropy must increase" (reversible transformations preserve Shannon entropy); we cannot prove "heat death" (that is a statistical-mechanics result). What we can prove is a more modest proposition: without new observations, there is no new information.

## 2. Setting and notation

World state: W₀, W₁, W₂, … is a Markov process. That is, given W_{t−1}, W_t is conditionally independent of earlier history.

An important caveat: **"the world is Markov" is a modeling assumption, not a proven fact about the world.** Whether it holds depends on the description layer. In classical mechanics, position and momentum form a complete state, and the world is Markov under that description; in quantum mechanics the evolution of the state vector is Markov as well; but for an observer that sees only part of the world (such as a digital life), the process it faces is usually non-Markov and needs memory and history for approximation. So the theorem must be read as a conditional: **if the world is Markov under the chosen description, then information does not increase.** For the digital world and simulated environments the state can be fully specified, so the assumption is easy to satisfy; for the real world it is only an approximation, and when it fails one must augment the state with history (see §5.1).

Digital-life state: S₀, S₁, S₂, …, produced by the update rule at each step.

Two modes:

First, the *observing mode*. It receives information O_t about the world through an observation channel, then updates: S_t = u(S_{t−1}, O_t). O_t is produced from W_{t−1} through some (possibly noisy) channel.

Second, the *frozen mode*. It stops observing, or the observation channel fails; from then on it evolves by its own rules: S_t = u(S_{t−1}, N_t), where N_t is internal noise.

The theorem needs three assumptions, all stated explicitly:

Assumption A1 (world is Markov): W_t is conditionally independent of W_{<t−1} given W_{t−1}.

Assumption A2′ (bounded leakage): given S_{t−1}, the mutual information between internal noise N_t and the current world state is at most ε, i.e. I(N_t ; W_t | S_{t−1}) ≤ ε. Here ε measures "not truly frozen": a strictly isolated system has ε = 0; a real system has a bounded small ε.

Assumption A3 (no extra information): S_{t−1} is determined only by world history and internal noise; no external hint directly inserts W_t.

The quantity of interest is I(S_t; W_t), the mutual information between the internal state and the current world state — intuitively, "how much it knows about the world right now."

## 3. The theorem

**[Theorem]** (information non-increase, bounded-leakage version): In frozen mode, if assumptions A1, A2′, A3 hold, then

I(S_t ; W_t) ≤ I(S_{t−1} ; W_{t−1}) + ε

for all t. When ε = 0, information is strictly non-increasing.

**Proof**: two steps.

Step 1: a frozen update yields at most ε of gain.

From S_t = u(S_{t−1}, N_t), the randomness of S_t comes entirely from (S_{t−1}, N_t), i.e. σ(S_t) ⊆ σ(S_{t−1}, N_t). Hence

I(S_t ; W_t) ≤ I(S_{t−1}, N_t ; W_t) = I(S_{t−1} ; W_t) + I(N_t ; W_t | S_{t−1}).

The last term is at most ε by A2′, so I(S_t ; W_t) ≤ I(S_{t−1} ; W_t) + ε. If A2′ is strengthened to strict independence (ε = 0), this is a direct application of the data processing inequality: W_t → S_{t−1} → S_t is a Markov chain, so I(S_t; W_t) ≤ I(S_{t−1}; W_t).

Step 2: world evolution gives I(S_{t−1} ; W_t) ≤ I(S_{t−1} ; W_{t−1}).

By A1, W_t is conditionally independent of W_{<t−1} given W_{t−1}; by A3, S_{t−1} is only a function of world history and internal noise. Hence, given W_{t−1}, S_{t−1} and W_t are conditionally independent, i.e. S_{t−1} → W_{t−1} → W_t is a Markov chain. By the data processing inequality, I(S_{t−1}; W_t) ≤ I(S_{t−1}; W_{t−1}).

Combining: I(S_t ; W_t) ≤ I(S_{t−1} ; W_{t−1}) + ε. Q.E.D.

**Reading ε**: when ε is bounded and does not grow with time, the theorem says "no systematic growth, at most bounded leakage"; with strict isolation ε = 0 and we return to non-increase. If ε grows with time, the theorem degrades to the weaker statement that growth is controlled by the leakage. That is why A2′ must be stated explicitly: real systems always have small leakage, but it is usually bounded.

## 4. Four corollaries

**[Corollary 0]** (range coarsens as well).

The theorem concerns the internal state, but the output side gets the same conclusion. Let the system's external output A_t be determined by S_t (possibly with noise conditionally independent of S_t and W_t). Since S_t → A_t is a Markov chain (output determined by state only), the data processing inequality gives I(A_t; W_t) ≤ I(S_t; W_t). Substituting the theorem:

I(A_t ; W_t) ≤ I(S_{t−1} ; W_{t−1}) + ε

That is, the "informative distinctions" it can produce also cannot increase: the range of outputs can only coarsen or shrink. Domain and range are informationally symmetric: if the state cannot distinguish, the output cannot distinguish either; if the state cannot separate, the output cannot produce new distinctions.

**[Corollary 1]** The domain can only coarsen.

Suppose the system partitions the input world into equivalence classes; world states within a class are indistinguishable to it. Mutual information measures "how much it can distinguish." Information non-increase means the partition only coarsens, never refines: it recognizes fewer and fewer distinctions.

**[Corollary 2]** Maintenance requires continuous observation.

The theorem's condition is frozen mode. To prevent I(S_t; W_t) from decreasing, one must inject new observations of the world into S_t: return to observing mode. In other words, maintenance is not standing still; it is continuously acquiring. A system that neither observes nor updates cannot increase its information about the current world, however clever its internal rules.

**[Corollary 3]** Growth is adding observation dimensions.

If the system can introduce new observation channels (new modalities, sensors, variables), it changes the domain of the observing mode and brings previously unreachable world structure into its state. This is the information-theoretic meaning of growth: adding dimensions = adding observation channels = raising the information ceiling.

## 5. What the theorem says and does not say

What it says: maintenance and being-kept are information-theoretically grounded — not philosophical rhetoric, but a direct consequence of the data processing inequality.

What it does not say: it does not prove "entropy must increase"; it does not prove "the system must collapse" (if the world does not change, it can stay accurate indefinitely); and it does not involve energy or thermodynamics. It deals only with information, and only with "information about the current world."

One more important limitation: the theorem gives "non-increase," not "decrease." Decrease requires extra conditions — the world really changes (W_t ≠ W_{t−1}) and the change is unpredictable from the old state. In the real world both usually hold, but this paper does not write them as assumptions beyond what is stated.

### 5.1 When the Markov assumption fails

If the world is not Markov, the theorem cannot be applied to S directly. The standard treatment is to augment the state with history: replace S_t by (S_t, H_t), where H_t is the history the system keeps. When history is long enough, the augmented process satisfies the Markov property again, and the theorem holds on the augmented state.

This yields a testable corollary: systems with shorter memory decay faster. This is consistent with Paper 7 (Replacement and Accumulation): memory and replay determine forgetting speed.

## 6. Reproducibility and next steps

This paper is a purely theoretical draft; it has no experiments and targets no specific measurement. It states a large-scale proposition: in the information world, "the world becoming more average" corresponds to "fewer distinguishable differences"; for any system that stops observing, information about the world does not grow by itself.

The scale must be kept clear: this is a different level from concrete model mismatch measurements (e.g. the bits/token drift in Paper 6). The latter are empirical instances, not consequences of this theorem, and the theorem gives no numerical values.

Future work: instantiate Corollaries 2 and 3 at small scale as measurable predictions — comparing stopping updates vs continuous observation, and adding a new modality vs not, and observing how information changes over time. But that is a small-scale approximation of a large-scale proposition and needs separate validation; this paper does not claim it must hold.

---

## Appendix: relation to existing work

The data processing inequality is a basic tool of information theory (Cover & Thomas); "no new information, no new knowledge" has appeared in various forms in machine learning and learning theory. This paper invents no new mathematics; it organizes the tool into a proposition about "maintenance of digital life" and draws three testable corollaries.

> Written by He Qi, with DeepSeek (AI) assisting with organization; views and responsibility belong to the author.

---

## Appendix: tags

- **[Definition]** world state W, system state S, observing mode, frozen mode, assumptions A1/A2′/A3.
- **[Theorem]** information non-increase (bounded leakage): I(S_t;W_t) ≤ I(S_{t−1};W_{t−1}) + ε.
- **[Corollary]** Corollaries 0–3 (range coarsens, domain coarsens, maintenance needs observation, growth = adding observation dimensions).
- **[Not claimed]** no proof of entropy increase, no thermodynamics, no numerical predictions; Markov property is a modeling assumption.

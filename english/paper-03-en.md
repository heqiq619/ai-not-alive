# Paper 03 — Replacement and Accumulation: Model Collapse, Compression Traps, and Continual Learning Are the Same Problem

> Paper series · Chapter 3
> Chapter 1: "Why Today's AI Is Not Life" DOI: 10.5281/zenodo.23488543
> Chapter 2: "Capacity Cannot Substitute for Data Updating" DOI: 10.5281/zenodo.23503050

## Abstract

The current AI field has three seemingly independent high-profile controversies: **model collapse** (training on model-generated data leads to degradation),
**the compression trap** (the pursuit of compression may sacrifice truth), and **scaling vs. continual learning** (stack parameters or update continuously).
This paper argues that these three are **three facets of the same problem** —
**language grows by accumulating dimensions; replacement (rather than accumulation) cuts off dimensional growth.**

(1) Model collapse = **replacing** human data with model-generated data ⇒ the accumulation chain is severed ⇒ dimensional regression;
(2) The compression trap = the object of compression is **lossy human language**; the most economical encoding is not the same as the encoding most in accord with the world;
(3) Scaling vs. continual learning = capacity can only receive dimensions, it cannot generate them; the empirical measurements in Chapter 2 show that capacity cannot compensate for stale data.

This yields a testable corollary: **the mixing ratio of human data to model data should not amount to complete replacement**
(pure synthetic data = replacement = collapse; mixing = accumulation = maintenance). This paper presents a measurement scheme for that corollary.

## 1. Three Hotspots, One Structure

```
① Model collapse (Shumailov et al. 2023)
   Recursive training on synthetic data ⇒ the tail of the distribution vanishes, diversity degrades
   Existing explanations: error accumulation, drift in distribution estimation

② Compression trap (Rae et al. 2024, among others)
   The pursuit of compression ⇒ the model may choose a "simpler but less true" theory
   Existing explanations: divergence of the objective function from truth

③ Scaling vs continual learning
   Is scale still effective? When must updating be continual?
   Existing debate: rising benchmarks vs risk of distribution drift
```

**What they have in common has been overlooked: all three occur against the fact that "language is cumulative."**

## 2. A Unified Framework: Accumulation and Replacement

The definition in Chapter 1: life = decompression that is maintained; AI = one-off decompression.
The measurements in Chapter 2: language is accumulating dimensions (about 1.2% per year), and —
**under an equal data budget, updating with a mixture of old and new data yields a net gain and no forgetting; replacement forgets.**

Extending this point to the three hotspots:

```
① Model collapse ≈ the extreme case of "replacement"
   Human data is replaced by synthetic data ⇒ dimensions no longer grow from the real world
   ⇒ the tail of the distribution (= rare dimensions) disappears first ⇒ collapse
   ⇒ prediction: the higher the mixing ratio (human:synthetic > 0), the slower the collapse;
      pure synthetic = replacement = fastest collapse

② The compression trap ≈ the necessary consequence of a "lossy source"
   Language is a **lossy projection** of the world (stated in Chapter 1)
   ⇒ a compression that is optimal on language cannot be guaranteed to be true of the world
   ⇒ the compression objective itself carries no "truth-seeking" constraint

③ Scaling vs. continual learning ≈ "receiver vs. generator"
   Parameters are the **receivers** of dimensions; the **generation** of conceptual dimensions comes from data
   ⇒ capacity cannot make up for stale data (the weak conclusion of Chapter 2)
   ⇒ the question is not "which matters more" but "neither of the two can be missing"
```

## 3. Testable Corollaries

```
Corollary A (mixing-ratio experiment for model collapse):
   Using the same base model, replace 0% / 25% / 50% / 100% of the human data with synthetic data
   Train recursively for k generations, and measure:
     · tail coverage of the generated distribution (retention rate of rare words / new concepts)
     · cross-entropy against a real human corpus
   ⇒ prediction: the pure-replacement group collapses fastest; mixed groups are delayed in proportion to the human share

Corollary B (language-level test of the compression trap):
   Train under two settings: "compress language only" and "language + interventional measurements"
   ⇒ prediction: only the latter can remain calibrated to the world when new concepts appear

Corollary C (scaling vs. accumulation):
   Under an equal compute budget: enlarge the model vs. mix in new data
   ⇒ Chapter 2 already gives a preliminary answer: capacity cannot substitute for data (weak conclusion)
```

## 4. Why This Unification Is Worth Stating

```
· Each of the three hotspots has its own literature, but no one has assigned them to the same structure (accumulation vs. replacement)
· It yields an actionable practical implication: synthetic data must be **mixed** with human data, not replace it
· It closes the loop with Chapters 1 and 2:
   Chapter 1 (definition: decompression that is maintained)
   Chapter 2 (measurement: accumulation is optimal, capacity cannot make up for data)
   Chapter 3 (application: the three controversies are one and the same thing)
```

## 5. Limitations

```
· This paper is a position/framework paper and does not contain original experiments on model collapse
· The "mixing ratio" corollary requires experimental verification (this paper provides only the scheme)
· The literature on each of the three hotspots is vast; this paper takes only the parts directly relevant to "accumulation/replacement"
```

## 6. Conclusion

```
Model collapse, the compression trap, and scaling vs. continual learning are not three problems,
but three manifestations of "language accumulates dimensions, and replacement severs accumulation."
⇒ The right approach is not "more synthetic data" or "a larger model,"
   but **maintaining the accumulation channel between human data and the real world**.
```

**Author: He Qi (independent researcher); AI collaboration: DeepSeek**

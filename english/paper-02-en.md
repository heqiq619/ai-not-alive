# Paper 02 — The First Measurement: Capacity Cannot Substitute for Data Updates

## Measuring Mismatch under the Dimensional Growth of Language (Scaling vs. Continual Learning: A Weak Conclusion)

> Paper series · Chapter 2
> **DOI: https://doi.org/10.5281/zenodo.23503050**
> Chapter 1: "Why Today's AI Is Not Life" (DOI: https://doi.org/10.5281/zenodo.23488543)

## Abstract

Chapter 1 proposed that life is "maintained decompression" and AI is "one-shot decompression", and predicted that a frozen model would exhibit a **relative mismatch** as language grows in dimensionality.
This chapter provides the measurement, and **self-corrects two methodological errors in the process**:

(1) We first measured with "old model vs. purely new model" and found the magnitudes in the two directions to be close (+0.108 vs. +0.128) ⇒ a symmetric difference, which cannot detect "falling behind";
(2) We then switched to a **cumulative reference frame** (old model vs. a model that knows all years); the mismatch decreases monotonically as the cutoff year becomes later
      (+1.026 → +0.721 → +0.322 bits/token), but the control is also significantly positive ⇒ a confounding "data volume" effect is mixed in;
(3) Finally we used an **equal-data-budget control** (the three models are trained on the same amount of data and differ only in how old the data is) to isolate the independent effect of concept freshness:
      the model trained only on the most recent data is better than the model trained only on the earliest data by **0.405 bits/token** on the 2024 test set (same data volume),
      while the model mixing old and new data loses almost nothing on the old test set (13.655 vs. 13.659).

We further ran a **capacity-compensation experiment**: raising model capacity from order 2 to order 6 (interpolated n-gram),
the gap between old data and mixed data stays stable at **+0.86–0.94 bits/token**, with no narrowing observed
⇒ **no capacity-compensation effect is observed** under this setting (a weak conclusion: it does not constitute a refutation of scaling, and requires transformer-based replication).

Conclusion: **language grows in dimensionality cumulatively — adding new concepts does not lose old concepts. The correct update is therefore "cumulative/mixed" rather than "replacement":
replacement forgets (13.800 vs. 13.659 on the old corpus when only new data is used), while freezing stops at the training moment.
The optimal strategy for continual updating = mix in new data, retain old capabilities.** All scripts are reproducible.

## 1. The Question

```
If language adds new "dimensions" (new concepts, new usages) over time
⇒ a model frozen at its training moment has no behavioral spectrum for these new dimensions
Questions:
  ① How large is this gap?
  ② Does it come from "concept oldness" or "amount of data"?
  ③ Can added model capacity (parameters) compensate for it?
  ④ What is the correct form of update: replacement or accumulation?
```

## 2. Data and Methods

**Data**: arXiv cs.AI, 3000 papers each from 2018 / 2020 / 2022 / 2024 (title + abstract), 12000 papers in total.
Fetched with: `502_fetch_arxiv.py`.

**Two self-corrections (method)**
```
Initial (504): old model vs. purely new model — symmetric in both directions ⇒ wrong, cannot detect falling behind
Correction 1 (505): cumulative reference frame — direction is right, but data volume is confounded
Correction 2 (506): equal-data budget — three models with identical data volume, differing only in oldness
```

**Capacity experiment (507/508)**
```
Fixed data volume N=1800 papers; n-gram order 2→6 as the capacity proxy
508 uses Jelinek-Mercer interpolation to make higher orders more stable
Compare bits/token of the three groups OLD / MIX / REC on the 2024 held-out set
```

## 3. Results

### 3.1 A Word-Level Proxy for the Rate of Dimensional Growth (`501_vl_newterm.py`)

2018 vs. 2024 (6 years): new words account for **7.30%** (≈ **1.2%/year**), and there are 7787 new concepts.

Top new concepts: large language, llms, prompting, rag, generative ai, vision-language models, retrieval-augmented, gpt-4o, etc.

### 3.2 The Equal-Data-Budget Control (Core Result, `506`)

bits/token (the three are exactly identical in data volume):

| Model (same data volume) | 2024 test set | 2018 test set |
|---|---|---|
| A: only the earliest year (2018) | 14.026 | 13.659 |
| B: mixed all years | 13.742 | 13.655 |
| C: only the most recent year (2024) | **13.621** | 13.800 |

```
① C beats A by 0.405 bits/token on the 2024 test set (same data volume)
   ⇒ concept freshness has **independent value**
② B (mixed): 13.742 on the new test set, 13.655 on the old test set ≈ A's 13.659
   ⇒ mixing in new data: new data improves, old capability is not lost ⇒ **updating has a net benefit**
③ C gets worse on the old test set (13.800)
   ⇒ using only new data forgets old concepts ⇒ **replacement has a cost**
```

### 3.3 Capacity-Compensation Experiment (`508`, with interpolation)

```
Max order   OLD      MIX      REC      OLD−MIX
2           10.712   9.774    9.505    +0.938
3           10.946   10.059   9.808    +0.888
4           11.011   10.143   9.901    +0.868
5           11.029   10.169   9.931    +0.860
6           11.035   10.178   9.942    +0.857
```

```
① The OLD−MIX gap is almost unchanged (0.938 → 0.857)
   ⇒ adding capacity **does not compensate** for "data being too old"
   ⇒ weak conclusion: no capacity compensation is observed under this experimental setting (it does not constitute a refutation of scaling)
② REC is best on the new corpus (9.94), but gets worse on the old corpus (see 3.2)
```

### 3.4 The Cumulative Reference Frame (`505`, as a Method Demonstration)

| Cutoff year | M (new test) | M_ctl (old test) |
|---|---|---|
| 2018 | +1.026 | +0.808 |
| 2020 | +0.721 | +0.459 |
| 2022 | +0.322 | +0.151 |

M decreases monotonically (the more it knows, the less it falls behind);
but M_ctl is also positive ⇒ data-volume confounding ⇒ the equal-budget control of 3.2 is required to isolate it.

## 4. Conclusion

```
① Dimensional growth of language really exists: over a 6-year span, the independent value of concept freshness is about 0.4 bits/token
② But it is slow (about 1.2%/year at the word level); the mismatch of a frozen model accumulates slowly, it is not a cliff
③ Added capacity cannot compensate for old data (**weakly established**, see the three tiers below)
④ Language grows in dimensionality **cumulatively**: adding new concepts does not lose old concepts
   ⇒ the correct update is "cumulative/mixed", not "replacement"
   ⇒ freezing = one-shot decompression; replacement = single-dimension decompression; accumulation = maintained decompression
      — this last point corresponds exactly to Chapter 1's condition that "life = maintained decompression"
```

**Three tiers of conclusion strength (this paper claims only the second tier):**

```
Strong: parameters cannot substitute for new data — requires transformer-level evidence, which this paper does not reach
Weak: no capacity compensation is observed under this experimental setting — this is the tier this paper claims
Zero: scaling is ineffective — this paper has no evidence to support it and does not claim it
```
### What "Weak Conclusion" Signifies (not wordplay — it must be stated clearly)

```
It signifies: data updating and model scaling are two **different levers** that, under this setting, cannot substitute for each other.
· It does not signify "scaling is ineffective" — scaling remains effective within a fixed data distribution
· It does not signify "the more parameters the worse" — it only indicates that the extra parameters cannot buy a remedy for stale data
· It signifies: the mismatch is a problem on the "data side", not on the "parameter side"
  ⇒ if language continues to grow in dimensionality cumulatively, the correct countermeasure is **updating the data (mixing)**,
    not merely making the model bigger

Practical implication:
  a strategy that only enlarges the model without updating the data will fall behind by about 0.4–0.9 bits/token on new corpora

Scientific implication:
  "continual learning" cannot be reduced to "adding enough parameters" —
  the growth of dimensions (concepts) needs new data to carry it; parameters are only the receiver.

Boundary (stated once more):
  the above is a **weak conclusion** under an n-gram capacity proxy; before transformer-level verification,
  it cannot be generalized to "the bigger, the more useless".
```
## 5. Limitations (Must Be Read Together with the Conclusion)

```
· Only one domain (cs.AI) and one source (arXiv abstracts)
· n-gram is a minimal language model: it measures word-level concept mismatch, and does not represent mismatch at the semantic/reasoning level of large models
· The capacity proxy = n-gram order, not the true parameter count; high-order CE is still rather large (interpolation λ fixed)
  ⇒ the capacity conclusion can only count as preliminary evidence, and requires replication with a small transformer
· The equal budget controls the number of training documents (not the number of tokens); sampling uses only one random seed
```

## 6. Reproducibility

```
python 502_fetch_arxiv.py cs.AI 2018 2024          # and 2020/2022
python 501_vl_newterm.py <corpus root> 6           # new-concept rate
python 504_series.py <2018> <2020> <2022> <2024>   # symmetry test (demonstrates the error)
python 505_cumulative_mismatch.py <four-year dir>  # cumulative reference frame
python 506_equal_budget.py <four-year dir>         # equal-budget control (core)
python 507_capacity_vs_data.py <four-year dir>     # first capacity probe (no backoff)
python 508_backoff_capacity.py <four-year dir>     # capacity compensation (with interpolation)
```

**Author: He Qi (independent researcher); AI collaboration: DeepSeek**

# Paper 04 — Alignment Is a Constraint on Decompression: Why Alignment Drifts, and Why "Replacement" Destroys It

> Paper Series · Chapter 4
> Chapter 1: Why Today's AI Is Not Life (DOI: 10.5281/zenodo.23488543)
> Chapter 2: Capacity Cannot Substitute for Data Updating (DOI: 10.5281/zenodo.23503050)
> Chapter 3: Replacement and Accumulation (DOI: 10.5281/zenodo.23503559)

## Abstract

Mainstream alignment research (RLHF, constitutional AI, scalable oversight) takes one premise for granted: **models can be shaped stably**.
Using the framework of the first three chapters, this paper argues: **AI is a re-decompression of human language; alignment = a constraint on that decompression.**
From this follow three testable corollaries:

(1) **Alignment drift**: language is rising in dimensionality (Chapter 2 measures roughly 1.2%/year), and the alignment objectives of a frozen model also fall behind—
      they are aligned to **the language of the training moment**, not to the world at this moment;
(2) **Ambiguity concentration**: the root of the compression trap is that language is lossy (Chapter 3); the more ambiguous the language,
      the more the model tends to choose the "least-encoding" interpretation ⇒ **alignment failures should concentrate at the points where human language is ambiguous**;
(3) **Replacement erosion**: alignment signals are hidden in human data; **replacing** rather than accumulating—with synthetic data or new data—
      severs the accumulation chain of value signals ⇒ **alignment degrades as the accumulation channel is severed.**

This paper gives testable experimental designs corresponding to this framework, and points out one practical implication:
**alignment is not a one-off training problem, but a continuous engineering problem of "maintaining the accumulation channel."**

## 1. The Implicit Premises of Mainstream Alignment Frameworks

　　RLHF: human feedback → reward model → optimized policy

　　Constitutional AI: constrain outputs with a text of principles

　　Scalable oversight: use AI to assist in supervising AI

　　⇒ All three assume: model behavior can be stably shaped and maintained


**But none of them answers:**
　　① When the language/values of the world change, do alignment objectives "expire"?

　　② Do alignment failures have a structural distribution (rather than being random noise)?

　　③ When a model is updated, does alignment bleed away because "only new data is fed in"?


## 2. Framework: Alignment = a Constraint on Decompression

　　AI = re-decompression of human language L(W) (Chapter 1)

　　Alignment = constraining this decompression process: at ambiguous points, at value-relevant points, decompress according to human intent

　　⇒ alignment is carried by **the value signals in human language**

　　⇒ the failure mode of alignment is determined by "the nature of language"


## 3. Three Corollaries

**Corollary A: Alignment drift (from Chapter 2)**
　　Language rises in dimensionality ⇒ a frozen model is aligned to the linguistic norms of the training moment

　　⇒ after new concepts/new values emerge, the model still decompresses according to the old compression

　　⇒ alignment drift is not a bug, it is the necessary consequence of "one-off decompression"

　　Testable: the same model's alignment score on "new norms that appeared after training" declines over time


**Corollary B: Ambiguity concentration (from Chapter 3)**
　　Compressed language is lossy ⇒ at ambiguous points there exist multiple equally short decompressions

　　⇒ the model tends to choose the "most common / least-encoding" interpretation

　　⇒ alignment failures should **concentrate at the points where human language is ambiguous**, rather than be uniformly distributed

　　Testable: stratify alignment-failure samples by "degree of human judgment disagreement",

　　and predict that the failure rate rises monotonically with the degree of disagreement


**Corollary C: Replacement erosion (from Chapter 3)**
　　Alignment signals (human preferences, value judgments) are hidden in human data

　　Replacement-style updating (new data only / replacing with synthetic data) ⇒ severs the value accumulation chain

　　⇒ alignment degrades as the replacement ratio rises

　　Testable: during fine-tuning, with human data share 0/25/50/100%,

　　look at alignment scores on public safety/value test sets


## 4. Testable Experimental Designs

　　Experiment 1 (drift):

　　Take two open-source models of different generations, score alignment on "new norms that appeared after the training cutoff"

　　⇒ Prediction: the older model scores lower, and the gap widens with the difference in cutoff times

　　Experiment 2 (ambiguity concentration):

　　Select a public alignment dataset, mark out "human disagreement" strata by hand/script

　　⇒ Prediction: the alignment failure rate rises with the degree of disagreement

　　Experiment 3 (replacement erosion):

　　Fine-tune a small model: mix in human safety data at proportions 0/25/50/100%, with the rest being new-task data

　　⇒ Prediction: the alignment score rises monotonically with the share of human data


## 5. Practical Implications

　　① Alignment cannot "be trained once and then hold for years"—it is continuous engineering

　　② Updates must accumulate (preserve the human-data channel), not replace

　　③ Alignment resources should be directed at "the points where language is ambiguous" (that is where failures concentrate), rather than spread uniformly


## 6. Limitations

　　· This is a framework paper; none of the three corollaries has had its experiment completed (the designs are given)

　　· The operational definition of "degree of ambiguity" requires care (inter-annotator disagreement vs. linguistic ambiguity)

　　· Alignment evaluation is itself contested (a benchmark is not equal to human values)


## Conclusion

　　The difficulty of alignment lies not only in "making the model obey," but also in:

　　· it is aligned to language that expires (drift)

　　· at ambiguous points it must choose an interpretation itself (ambiguity concentration)

　　· its value signals are washed away by replacement-style updating (replacement erosion)

　　⇒ Therefore: alignment = maintaining an accumulating decompression channel, not a one-off training task.


**Author: He Qi (independent researcher); AI collaboration: DeepSeek**

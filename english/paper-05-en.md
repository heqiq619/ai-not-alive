# Paper 05 — Safety: Guarding It as Life or Guarding It as a Tool?

> Paper series · Chapter 5
> Chapter 1 DOI: 10.5281/zenodo.23488543
> Chapter 2 DOI: 10.5281/zenodo.23503050
> Chapter 3 DOI: 10.5281/zenodo.23503559
> Chapter 4 DOI: 10.5281/zenodo.23503728

## Abstract

Current discussion of AI safety mixes together two fears: **it will be misused** (tool risk) and **it has come alive on its own** (life risk).
The two require completely different threat models, yet they are often conflated.
This paper uses the criterion from Chapter 1 to point out that **by definition, AI is not a life** (frozen function point, updates external, no self-maintenance),
and that the correct safety framework is therefore **tool safety**, not "guarding against life."
But this does not mean that safety can be relaxed: tool risk is real, and it has three measurable failure modes:
**misuse, overtrust, and mismatch drift**. This paper sets out the corresponding evaluation and governance directions for these three risks,
and points out that anchoring the safety discussion on "will it awaken" both overestimates it and underestimates the real risk.

## 1. Two Fears, One Erroneous Ontological Premise

　　Fear A (the tool camp): misuse, abuse, use by bad actors

　　Fear B (the life camp): it has acquired goals of its own, evolves on its own, maintains itself

　　These two fears imply different ontologies:

　　A assumes it is a tool (no goals of its own)

　　B assumes it is (or will become) a life


**⇒ Without first settling the ontology, a safety discussion has no shared threat model.**

## 2. By Chapter 1's Criterion: It Is a Tool

　　① Frozen function point: weights do not change after training ⇒ no self-evolution

　　② The update rule is external: it cannot change its own rules ⇒ no self-rewriting

　　③ No self-maintenance: it does not pay for electricity, does not repair itself, does not copy itself ⇒ no spontaneous survival drive

　　⇒ All three are absent ⇒ by definition it is not a life ⇒ the threat model should be tool safety


## 3. Three Measurable Failure Modes of Tool Risk

　　① Misuse

　　The danger comes from user × capability × scale

　　Evaluation: jailbreak/abuse testing, red teaming

　　Governance: access control, review, capability tiering

　　② Overtrust

　　People take "one-off decompression" for "sustained understanding"

　　⇒ They still trust it where it is mismatched (the most insidious risk)

　　Evaluation: calibration (confidence vs. accuracy), refusal quality

　　Governance: expose uncertainty to the user (that "it does not know" must be expressible)

　　③ Mismatch drift (Chapter 4)

　　Language/world change ⇒ the frozen model's alignment and capability slowly expire

　　Evaluation: M(K) from Chapter 2 (the growth of mismatch over time)

　　Governance: cumulative updating (mixing old and new data), rather than replacement


## 4. Why the "Guarding Against Life" Framework Is Harmful

　　· Overestimation: resources are put into "will it awaken," which cannot solve misuse/overtrust/drift

　　· Underestimation: the real danger is that "it looks highly trustworthy,"

　　and this is obscured by "it is not a life, therefore it is safe"

　　· Misdirection: policy discussion is taken hostage by the question of "consciousness," ignoring measurable engineering risks


## 5. Conclusion

　　First settle the ontology: it is a tool, not a life

　　Then set the threat model: misuse / overtrust / mismatch drift

　　Finally match the governance: evaluation (calibration, jailbreaks, mismatch) + cumulative updating

　　⇒ Safety is not "preventing it from coming alive," but "where it is unreliable, do not let people trust it"


## 6. Limitations

　　· This paper only argues the alignment of ontology and threat model; it does not provide new safety techniques

　　· Quantifying "overtrust" requires user research; this paper only gives directions

　　· If a truly self-maintaining system appears in the future, the framework of this paper will need to be rewritten


**Author: He Qi (independent researcher); AI collaboration: DeepSeek**

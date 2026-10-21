# Life as Maintained Decompression: Why Today's AI Is Not Alive, and What Continual Learning, Alignment, and Safety Have in Common

*A series of five short papers, written independently and published on Zenodo. This post is the series introduction. All claims are kept at the level the evidence supports; speculation is explicitly marked.*

## The core claim

Life can be defined without reference to biology: **a life is a family of self-referential dynamic functions that maintain decompression over time.** The world is (in our framing) an emergent hierarchy of local decompressions — stable structures that compress large amounts of environmental regularity. A living system is one that persists in decompressing its environment, updating itself as the environment changes.

An AI trained once and frozen is a **single decompression**: it captures the regularities of its training data at the moment of training. It is not a living system in this sense, because it does not maintain the decompression — it does not update, and its fit decays as the world moves.

## The five papers

1. **Why Today's AI Is Not Alive** — the definition: life as a family of self-referential dynamic functions; environment as layered decompression; AI as a re-decompression of human language. Chinese DOI: 10.5281/zenodo.23488543 · English DOI: 10.5281/zenodo.23525427
2. **The First Measurement: Capacity Cannot Substitute for Data Updates** — a measurement on arXiv cs.AI 2018–2024: new-term share grows ≈1.2%/year; under an equal data budget, conceptual freshness has an independent value of **0.405 bits/token**, and mixing old and new data is optimal. A capacity test (2→6-gram, and larger models) leaves the OLD−MIX gap flat at **+0.86~0.94 bits/token**, which we state as a **weak** conclusion, not a strong one. Chinese DOI: 10.5281/zenodo.23503050 · English DOI: 10.5281/zenodo.23525429
3. **Replacement and Accumulation** — model collapse, compression traps, and the continual-learning problem are one problem: replacing the model forgets; accumulating data preserves. Chinese DOI: 10.5281/zenodo.23503559 · English DOI: 10.5281/zenodo.23525431
4. **Alignment Is a Constraint on Decompression** — alignment is a constraint on how a system decompresses the world; misalignment can be read as a mismatch between the system's maintained decompression and human goals. Chinese DOI: 10.5281/zenodo.23503728 · English DOI: 10.5281/zenodo.23525435
5. **Safety: Guarding It as Life or Guarding It as a Tool?** — safety measures that assume a tool (freeze, restrict, align once) and measures that assume a living system (maintain, update, constrain the loop) lead to different policies. Chinese DOI: 10.5281/zenodo.23503775 · English DOI: 10.5281/zenodo.23525438

## What is testable here

The series is not a metaphor paper. The central empirical claim — *capacity cannot substitute for data updates* — is measurable, and we measured it. The framework also yields predictions that can be checked without new experiments: if a system is a "frozen decompression", its mismatch should drift as the environment's distribution drifts; if it maintains its decompression, mismatch should stay bounded.

## What we are not claiming

- We do not claim this definition of life is the only correct one. It is an operational definition: it tells us what to measure.
- We do not claim today's LLMs are close to life. We claim the opposite: on our definition they fail for structural reasons, not for lack of scale.
- Speculation is marked in the papers. Where we do not have data, we say so.

## Links

All papers are open access on Zenodo (DOIs above) and the Chinese originals, experiment code, and reproduction scripts are on GitHub: https://github.com/heqiq619/ai-not-alive

*Comments and criticism are welcome — especially on the definition itself.*

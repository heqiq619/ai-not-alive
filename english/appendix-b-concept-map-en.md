# Concept Map · Glossary (v3, English translation)

> Digital Life Series · Compendium Appendix B (working version)
> Original date: 2026-10-27 (v3); English translation: 2026-11-02
> Usage: update this table whenever a paper is added; each term gets one sentence + source.
> Source labels use the volume structure of this English edition (Intro, Theory I–IV, Experiments, Gating & Frozen Modules, Constraints, Appendices). The Chinese text is authoritative.

---

## I. Core definitions

| Concept | One-sentence definition | Source |
|---|---|---|
| Universe | P + R; P is functionizable, R is not (declared only, not expanded) | Intro |
| Functionizable | Can be written in our function language to arbitrarily small error | Intro |
| p_life | The part of life that falls in P; the object of definition and discussion | Intro / Paper 1 |
| R_life | The part of life that falls in R; declared only | Intro |
| Life | p_life + R_life; p_life = a family of dynamic functions that is kept (official definition D1–D5, foundational paper Def. 14) | Intro / Paper 1 / Foundational |
| Relative R (notation) | Trailing marker on explicit function forms: the part our function language cannot reach; declared only, not expanded; absolute R is not judged | Theory I / III / IV |
| Absolute R | The part of the universe itself that is not functionizable; whether it exists is not judged | Intro supplement |
| Relative R | Non-empty for any finite observer (fluctuations, finite resources, self-reference, undecidability, etc.) | Intro supplement |
| Digital world | A formal object: state is a finite string, rule is an algorithm; absolute R = ∅ by construction | Intro / Paper 1 |
| Residue | A measurable lower bound of error on the P side (the boundary shape of P); **not** an effect or projection of R | Intro notation |
| Functionizable ≠ computable ≠ measurable | Three separate things: a mapping exists / can be computed / can be observed and reproduced | Intro |

## II. Function language (Theory I)

| Concept | One-sentence definition | Source |
|---|---|---|
| Slice | A function f: X → Y with (d_in, d_out, Δ) | Theory I |
| Representation dimension | d_in = dim(X), d_out = dim(Y); the number of axes of a slice | Theory I |
| Effective dimension | Log of the number of distinguishable states; can decline even when the number of axes is unchanged (each axis coarsens) | Theory II |
| Spatial composition | Chain of composed functions F = f_N ∘ … ∘ f_1; the composition law requires type compatibility | Theory I |
| Temporal composition | Operator sequence s_{t+1} = I_{σ(t)}(s_t); three cases: constant / varying / mixed | Theory I |
| Step count k (computational thickness) | How many steps a temporal composition takes along the path | Theory I |
| Judgment J | One-pass, not iteration: J_choose (choose operator) + J_stop (decide to stop) | Theory I |
| Three levels of self-reference | Representation / parameter / structure self-reference, weak to strong | Theory I |
| Fixed core Φ | The set of unchangeable constraints; all three self-reference levels are constrained by it | Theory I |
| Composition law | How slices may interact (order / shared state / parallel / routing / shared parameters) | Theory I |
| Domain of the composition law | The input set that makes the whole slice chain "run" = the compatible intersection of the slices' domains | Theory I |
| Kept (function version) | The composition law is defined throughout the time interval | Theory I |
| Structure | Structure = decomposition D + composition C; it is also a compression scheme (Paper 1 §3.3's "structure" refers to the universe's local presentation, an environmental view) | Theory I |
| Decomposition D / composition C | Map a function onto a set of slices / assemble a set of slices back into a function | Theory I |
| Time-driver source | Internal (clock lives in the system's own substrate, biological) / external (external timer + interpreter, digital world) | Theory I |
| Types A/B/C/D | Continuous flow / sampled dynamics / automaton / mixed | Theory I |
| Five axes | Space continuous/discrete, time continuous/discrete, time internal/external, degrees of freedom of the composition law, levels of self-reference | Theory I |

## III. Three identities: universe / environment / life (Theory I)

| Concept | One-sentence definition | Source |
|---|---|---|
| Universe slice | U_t = (S_t, C_s, d_t); temporal composition is between slices (T_comb: U_t → U_{t+1}) | Theory I |
| Spatial composition (universe) | Within one instant, how parts compose into a whole (C_s) | Theory I |
| Temporal composition (universe) | How slices connect; a single instant has only spatial structure | Theory I |
| Environment | A sub-slice of the universe: d^E ⊆ d, C_s^E ⊆ C_s, state is the projection π_E(S_t); no judgment, no self-reference | Theory I |
| Environment's time | Restriction of T_comb + boundary input u_t | Theory I |
| Life (four conditions) | Kept (trajectory stays in V) / boundary open / self-referential regulation / plastic (bounded by Φ) | Theory I |
| Frozen instant | Life and environment are isomorphic at one instant and cannot be distinguished; life must be identified over time | Theory I |
| Life = kept trajectory | Not a state; a property of "a segment of trajectory" | Theory I |

## IV. Representation and dimension (Theory I/II)

| Concept | One-sentence definition | Source |
|---|---|---|
| Representation space | The space of all possible representations/states | Theory I |
| State | A point in representation space (a tuple of coordinates along representation dimensions), not a dimension | Theory I |
| Domain / range | The allowed/reachable ranges along some representation dimensions (subsets), not axes | Theory I |
| Width | Number of representation dimensions in one layer | Theory I |
| Depth | Step count / layer count, another axis different from representation dimension | Theory I |
| Dimension raising | Adding distinguishable representation dimensions | Experiments |
| Three spaces | Representation space (activations) / parameter space (weights) / input-output space (data) | Theory I |
| Thickness (general term) | Distribution thickness (vertical) and computational thickness (horizontal), orthogonal | Theory I |
| Distribution thickness | How wide a family of outputs corresponds to one input (entropy/ambiguity); flattened by representation dimensions | Theory I |
| Computational thickness | How many steps from input to target along the composition law (path length); spread out by steps/time | Theory I |
| Flattenable / non-flattenable | Dimension raising can flatten thickness / cannot; structural thickness = dimensions coupled so they cannot be separated | Theory I |
| Relative residue | Thickness / distinguishable scale; relative residue rises as dimensions decrease | Theory I |
| Range contraction | The input/output range on each representation dimension shrinks | Theory II |
| Three resources | Representation dimensions in space / representation dimensions in the composition law / steps in time | Experiments |

## V. Compression and decompression (Theory I)

| Concept | One-sentence definition | Source |
|---|---|---|
| Compression | Dimension-reducing map f: X → Y, dim(Y) < dim(X) | Theory I |
| Decompression | Re-expanding from a compressed representation (not unique; need not equal the original) | Theory I |
| "Good enough" decompression | Decompression need not be strictly invertible; it must be good enough for maintenance; the environment selects which dimensions must be invertible | Theory I |
| Narrow in, wide out | Input is constrained and coarse-grained; output expands by structure, and the extra dimensions come from structure (past compression) | Theory I |
| Body-perimeter | The environment an individual sees = the projection π_L(E) of the compression map | Theory I |
| Compression scheme | The rules "which distinctions to keep, which to merge, which past to compress into structure," written into structure | Theory I |
| One-shot decompression | A frozen model is fixed after training; it no longer updates or maintains | Intro / Paper 1 |
| Language = public compression scheme | Sensation→language is compression; language→description/understanding/reasoning is decompression; logic = language's composition law | Theory I |
| Closed loop | At step t: (s_t, in_t) → (s_{t+1}, out_t); in_{t+1} = W(out_t, world) | Theory I |
| Semi-closed loop | Large model: output only continues text; it does not change the environment | Theory I |
| Interface layer / mechanism layer | Input-output behavior / how it computes internally, maintains, changes itself | Theory I |
| Semantic residue | The semantic gap language cannot carry (minimum achievable error under a given modality combination) | Experiments |
| Grounding | Filling the semantic residue with multimodality/action | Experiments |

## VI. Capability, convergence and efficiency (Theory I/IV + experiments)

| Concept | One-sentence definition | Source |
|---|---|---|
| On-demand convergence | Try → judge whether converged → if not, loop with memory → consolidate after convergence | Split out to note *The Executor's Uniform Computation*; not a series conclusion |
| Halting judge | Checks "is it enough?" at each layer and decides exit/continue/which path | Experiments |
| Fast/slow structure | Fast structure (facts, converged in one or two layers, frozen into premises) + slow structure (trade-offs, loops in time) | Discussion draft (not a paper; related experiments in the Experiments part) |
| Three uniformities | Uniform depth / uniform width / no on-demand loop | Split out to note *The Executor's Uniform Computation*; not a series conclusion |
| Uniform-depth waste | Different structures need very different depths; on-demand allocation is cheaper (routing 47%) | Theory IV (former Paper 28) |
| Over-computation | Error rises after exceeding the task's thickness (on-demand mobilization 0.434 vs uniform 1.756) | Theory IV (former Paper 28) |
| Layer ≈ step | A frozen model's depth acts as time steps (pseudo-time) | Theory IV |
| Time-for-dimension | Giving loop steps (time) can greatly reduce required representation dimensions | Paper 1 / experiments |
| Loop saves parameters | The same iterative effect: looping saves about 27× the parameters of adding layers | Theory IV (former Paper 28) |
| Layer thickness placement | With the same parameters, narrow front + wide back is cheaper | Experiments |
| Minimal slice | The minimal (width, depth) configuration in which a structure appears | Experiments |
| Capability boundary | The configuration region that achieves accuracy; a "trainability boundary," not a pure representation boundary | Experiments |
| Emergence | Capability/structure appears after crossing a dimension threshold (a phase transition, i.e. a piecewise discontinuity) | Intro / experiments |
| Fixed core Φ | Unchangeable constraints; plasticity only within Φ | Theory I |

## VII. Language function and language structure (Theory IV · Language and the Brain)

| Concept | One-sentence definition | Source |
|---|---|---|
| Language | Symbol system + composition rules + shared conventions: compress internal representations into transmissible symbol sequences and allow decompression | Theory IV |
| Public compression interface | Language's role: speaker encodes, listener decodes, group shares | Theory IV |
| Human-brain function B | Individual brain: world → representation → behavior (organ, maintenance, internal loop, judgment) | Theory IV |
| Language function L | The public structure externalized from many brains' outputs: symbol → meaning (not owned by a single brain) | Theory IV |
| Large model (executor) | A system that learns and executes L; not an implementation of B | Theory IV |
| Symbol slice | Language's slice: input is a symbol, output is a meaning representation | Theory IV |
| Word = slice | A word is a "symbol→meaning" mapping | Theory IV |
| Syntax = spatial composition | Words compose into larger structures (composition-law compatibility) | Theory IV |
| Semantics = representation and grounding | What symbols point to, whether they connect to the world | Theory IV |
| Discourse = temporal composition | Context, reference, order dependence unfold in time | Theory IV |
| Logic = rules of the composition law | Which combinations are legal, how to infer | Theory IV |
| Pragmatics = judgment | Occasion, appropriateness, truth (one-pass) | Theory IV |
| p_language / relative R_language | The functionizable part of language / the part unreachable for a given function class (not absolute R) | Theory IV |
| Implicature (unsaid meaning) | The part supplied during decompression: mostly p_language (conversational implicature/pragmatic rules), a small part relative R_language (tacit understanding/experience/tone) | Theory IV |
| Language's time (three kinds) | Structure has no time; use is a time sequence; evolution is slow change of structure | Theory IV |
| Time encoded by language | Tense, time words, narrative order: language's representation *about* time, not language's own time | Theory IV |

## VIII. Layer paths, judgment and early exit (Experiments)

| Concept | One-sentence definition | Source |
|---|---|---|
| Layer redundancy | The same structure has replaceable copies across layers: skipping one layer has little effect, skipping a group collapses | Experiments |
| Single-layer skip | A layer's output = input (identity pass), removing only that layer's contribution | Experiments |
| Redundancy amount | Flip rate of skipping a group − the larger of the two single-layer rates (positive = compensation/redundancy) | Experiments |
| Late-layer reconstruction/correction | After damaging the current state, the final prediction can still recover: later layers recompute from context | Experiments |
| Language predictability | Entropy predicted by the full model as a proxy: low entropy = strong, predictable language structure | Experiments |
| Language structure as independent variable | Grouping by predictability instead of "arbitrary token categories" | Experiments |
| Judge A (confidence) | Decide exit using the confidence/entropy of the current layer's prediction | Experiments |
| Judge B (path) | Decide exit using cross-layer consistency (adjacent-layer agreement, KL, trend) | Experiments |
| Judge L (language) | Decide exit using language-structure features (word class, position, repetition, first-layer entropy) | Experiments |
| Oracle early exit | Assume knowing which layer's prediction is correct and exit there: the upper bound of early exit | Experiments |
| Early exit + write-back | Write the early-exit result into context and continue: a single time can be absorbed, repeatedly it accumulates error | Experiments |
| Over-computation is harmful | Early exit can be more accurate than the full model: later layers can damage correct predictions | Experiments |

## IX. Experimental readings (GPT-2 / toys)

| Concept | One-sentence definition | Source |
|---|---|---|
| Inter-layer Δ_l | Relative change of hidden states between adjacent layers; on GPT-2 not monotone, larger at the end | Real-model experiments |
| Calibration probe | Map h_l to h_final with a linear/MLP map and decode, to test whether early exit is feasible | Real-model experiments |
| Halt judge | Train a classifier to predict "does this layer's probe equal the final prediction," realizing early exit | Real-model experiments |
| Early-exit ceiling | Average depth 2.31/12 under oracle judgment (81% saved) | Real-model experiments |
| Realizable early exit | After training halt: 72–80% depth saved, accuracy about −1.6 to −1.8 points | Real-model experiments |
| Fast/slow toy | Fast encoding + slow loop vs flat MLP: comparable accuracy, about 2.2× fewer parameters | Discussion draft (not a paper; related experiments in the Experiments part) |

## X. To define / to unify (next steps)

- **Maintenance (quantifiable)**: lifetime, recovery time, critical perturbation, maintenance cost — not expanded yet
- **"Good enough" criterion**: decompression invertibility requirements depend on the environment; not operationalized
- **Feasible region V and fixed core Φ**: measuring protocols for "is it kept" and "what is unchangeable" are missing
- **Training signal for the judge**: what labels to use for halt (consistency/impact/cost) is undecided
- **Correspondence between language structure and brain structure**: the B–L mapping is only conceptual, with no measurable correspondence
- **Boundary of implicature**: which parts rely on p_language rules and which on relative R_language is not operationalized
- **Position of R**: R does not enter continuous/discrete or domain/range discussions (a category issue), but readers must be prevented from misreading

---

## Dependency graph (what defines what)

```
P / R → functionizable → p_life → five conditions D1–D5
   (in P / a family / changes / self-refers / is kept)
                        ↓
                digital world (R=∅) → frozen model → one-shot decompression → mismatch
                        ↓
              structure (D, C) → slice → composition law → domain of composition law = maintainable set
                        ↓
        representation space → representation dimension → state / domain / range
                        ↓
     thickness → flattenable/structural thickness → dimension raising → relative residue
                        ↓
     time (internal/external) → A/B/C/D → layer ≈ step → time for dimension
                        ↓
     capability boundary (minimal slice) → emergence (threshold/phase transition)
                        ↓
【language branch】public compression scheme → language function L → large model (executor)
            → strength of language structure (predictability) → layer redundancy / early exit / judgment
            → implicature (p_language / relative R_language)
                        ↓
【main line of Theory I】function language → three identities (universe/environment/life) → compression/decompression
            → narrow in, wide out → body-perimeter → closed-loop rhythm → language (public compression scheme)
            → judge/on-demand convergence → three uniformities → loop saves parameters
```

## Appendix: gating observations (Gating & Frozen Modules)

> Naming convention: **gate open (p > 0.5) = compute this layer and write back; gate closed = skip, residual passes through.** (Earlier drafts used the opposite wording; this table uses the unified convention.)

| Term | One sentence | Source |
|---|---|---|
| Bypass gate | Gate open = compute the layer's transform and write back; gate closed = pass the residual through | Gating paper |
| Hard budget | Each token computes at most k layers; the optimum degenerates to the first k fixed layers | Gating paper |
| Soft cost | Loss += λ · average number of computed layers; directly adding its gradient collapses | Gating paper |
| Lagrange gating | λ adaptively pushes the average layer count; controllable and differentiated per token | Gating paper |
| Depth redundancy | A 6-layer task needs 2–3 layers; a 24-layer task needs about 5.3 layers to break even (within noise) | Gating paper |
| Frozen submodel | A trained submodel whose parameters are no longer updated | Frozen-submodel paper |
| Trainable interface/controller | A small trainable module between frozen submodels that aligns representation spaces | Frozen-submodel paper |
| Parallel composition | Two different submodels connected by an interface (e.g. A→B and B→A) | Frozen-submodel paper |
| Hierarchical composition | Frozen lower modules provide features; a trainable upper decision layer acts on them | Frozen-submodel paper |

---

> This concept map is a working document; it changes whenever the papers change. The Chinese version is authoritative.

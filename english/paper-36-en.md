# Paper 36 · Language and the Brain: Two Function Forms

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory 14 (internal No. 36)
> Date: 2026-10-27
> Note: this paper merges the former Paper 21 "The Functionizable Form of the Human Brain" and former Paper 35 "The Functionizable Form of Language Structure."
> English translation of the Chinese paper (the Chinese text is authoritative).

---

## Abstract

This paper places two objects side by side: the human-brain function B, the language function L, and the executor (a large model) that learns L.

First B. The brain is a functionizable organ: slices (input→representation), spatial composition (chains of composed functions), temporal composition (sequences of operators, with step count k), judgment (choosing an operator / deciding to stop), and three levels of self-reference (representation / parameters / structure, constrained by a fixed core Φ). The human brain is one instance: heterogeneous, low-dimensional and efficient, with internal time, judgment, and three active levels of self-reference; but it is not self-sufficient — oxygen, glucose, and homeostasis depend on the body, and what is kept is the whole "body + brain + environment."

Then L. Language grows out of the compression chain "organ→sensation→symbol"; it is a public compression interface (speaker encodes, listener decodes, the group shares). Function decomposition: word = slice (symbol→meaning), syntax = spatial composition law, semantics = representation mapping and grounding, discourse = temporal composition, logic = the rules of the composition law (pragmatics = judgment). Language has no physical substance, but a slice does not need physical substance — its slice is a "symbol slice," and physics appears only at the grounding end. Language's time has three layers: structure has no time, use is a sequence, evolution is slow change. Language = p_language + relative R_language; most of the "unsaid meaning" lies in p_language (conversational implicature, pragmatic rules), a small part in relative R_language (tacit understanding, shared experience, tone).

The relation of the three layers is a generation chain: **B produces L; the large model executes L.** This fixes the division of research objects: study large models with L's variables (predictability, composition depth, compression/decompression, grounding residue); study life with B's mechanisms (maintenance, self-reference, judgment, internal loops). Brain mechanisms have projections onto L (convergence→predictability, redundancy→multiple encoding, judgment→linguistic convention), but a projection is not the original — treating the projection as the original makes conclusions "slide."

Testable corollaries and boundaries are given.

## Tables of definitions

| Term | One-sentence definition |
|---|---|
| Human-brain function B | Individual brain: world → representation → behavior (organ, maintenance, internal loop, judgment); explicit forms end with + R_relative |
| Language function L | The public structure externalized from many brains' outputs: symbol → meaning (transmissible, accumulable, not owned by a single brain) |
| Executor | A system that learns and executes L (a large model): has a symbol layer and composition rules, without B's organ/maintenance/internal loop |
| Slice | A function f: X → Y with representation dimensions (d_in, d_out) |
| Spatial composition | Chain of composed functions F = f_N ∘ … ∘ f_1 |
| Temporal composition | Operator sequence s_{t+1} = I_{σ(t)}(s_t); step count k |
| Judgment J | One-pass: choose an operator, decide to stop (derived definition; foundational paper Def. 4a) |
| Three levels of self-reference | Representation self-reference / parameter self-reference / structure self-reference |
| Fixed core Φ | The set of unchangeable constraints |
| Language | Symbol system + composition rules + shared conventions: compress representations into transmissible symbol sequences and allow decompression |
| Public compression interface | Language's role: speaker encodes, listener decodes, group shares |
| Symbol slice | Language's slice: input is a symbol, output is a meaning representation |
| Word = slice | A word is a "symbol→meaning" mapping |
| Syntax / semantics / discourse / logic | Spatial composition / representation and grounding / temporal composition / rules of the composition law |
| p_language / relative R_language | The functionizable part of language / the part unreachable for a given function class (not absolute R) |
| Unsaid meaning (implicature) | The part supplied during decompression: mostly p_language, a small part relative R_language |

---

## 1. The question

We have two objects, both worth writing in function form:

1. **The human brain**: a concrete, living organ with organ constraints, maintenance needs, and internal time;
2. **Language**: the public structure externalized from human groups' brain outputs, transmissible and accumulable, with no physical substance of its own.

And one product: **the large model**. It learns language (L), not the human brain (B). The three are often conflated, producing two kinds of errors: treating a large model as a brain (probing it with B's mechanism vocabulary, so conclusions "slide"), or treating language as an entity (demanding its own time and maintenance). This paper separates the three layers, then states their connections and what cannot substitute for what.

## 2. The human-brain function B: explicit form

All explicit function forms in this paper are written as: **form + R_relative**.

(Notation: every explicit function form here writes only the p side, i.e. the part our function language can express; the trailing + R_relative marks "the part our function language cannot reach" — limited by our current function class and observation position, declared but not expanded; whether absolute R exists is not judged.)

### 2.1 The brain as a functionizable organ (qualitative)

- The brain has a finite representation space: finitely many distinguishable directions, constrained by body and energy;
- The brain has compositional structure: wiring, projections, shared states between regions;
- The brain has internal time: oscillations, firing, metabolism run without an external clock;
- The brain has judgment and self-reference: choose, stop, change itself.

⇒ The brain falls on the "functionizable" side (B), but it is an organ maintained by the body, not a self-sufficient system.

### 2.2 Slices and representation dimensions

A slice is a function f: X → Y with (d_in, d_out, Δ): representation dimension is "the number of distinguishable directions"; Δ is how it composes with neighboring slices. Each processing stage of the brain can be seen as a slice (sensation→representation, representation→decision, …).

### 2.3 Spatial composition: chains of composed functions

F_space = f_N ∘ … ∘ f_1

The composition law requires type compatibility: Y(f_i) ⊆ X(f_{i+1}). The brain's spatial composition is not a fixed chain but a variable composition (projections, routing, shared states) — one reason it is low-dimensional and efficient.

### 2.4 Temporal composition: operator sequences and step count

s_{t+1} = I_{σ(t)}(s_t), t = 0, 1, …, k−1

{I_{σ(t)}} are the available operators, σ(t) chooses which at step t, k is the step count. Three cases: constant (same operator repeatedly), varying (different functions in sequence), mixed. The brain is mixed: both repetition (oscillations, iteration) and switching (different circuits in sequence).

### 2.5 Judgment: choosing and stopping

J: S → D (finite judgment space)

Judgment decides two things: which operator σ(t) = J_choose(s_t); when to stop k = J_stop(s_t). The brain's judgment is internal, fast, and one-pass.

### 2.6 Self-reference: changing itself

Three levels, weak to strong: representation self-reference (input contains its own representation), parameter self-reference (θ_{t+1} = U(θ_t, s_t)), structure self-reference (C_{t+1} = V(C_t, s_t)). All three are constrained by a fixed core Φ: θ ∈ Θ_Φ, C ∈ 𝒞_Φ. The human brain: synapses and local circuits can change; neuron types, large-scale anatomy, and metabolic constraints cannot.

### 2.7 Instance: the human brain

- Slices: heterogeneous, low-dimensional and efficient;
- Spatial composition: variable (projections/routing/shared states);
- Temporal composition: operator sequences, mixture of k=0 and k≥1;
- Judgment: has J (choose operator/stop/consolidate);
- Self-reference: all three levels active;
- Maintenance: body + environment.

### 2.8 Why it is not self-sufficient; the unit of life is the whole

The brain is about 2% of body weight but consumes about 20% of energy; it depends on continuous oxygen and glucose supply, and on the body maintaining temperature and internal environment; a few minutes of hypoxia is irreversible. So the carrier unit of "being kept" is not the isolated brain but the loop "body + brain + environment" (the maintenance unit). Consistent with Paper 1: the criterion of life is still "which family of functions is kept"; the environment itself is not part of life; what is said here is the carrier unit of maintenance, not the definition boundary; the life criterion is still p_life in D1–D5 of the foundational paper.

## 3. The language function L: functionizable form

(The foundational paper's Def. 15 gives only the symbol–meaning slice part L₀ of L; this paper gives the full composition: L₀ + syntactic composition + discourse temporal composition + logical rules.)

### 3.1 Origin: from organ to symbol

Organs are compressors: the eye compresses light into visual representation, the ear compresses sound into auditory representation. The earliest language was most likely "specific sounds for specific phenomena": sound is cheap, transmissible over distance, shareable. Two sounds combined produce new meaning, and the composition law appears; repeated use consolidates into grammar; categories and relations are extracted from concrete reference — the embryo of logic. In form: initial language L₀ = {(s_i, r_i)} (pairs of symbol and representation) + composition operation C ⇒ L is the closure generated by L₀ and C; public conventions stabilize mappings and rules within a group.

### 3.2 What language is: a public compression interface

- For the speaker: compress internal representation into a symbol sequence (encoding);
- For the listener: decompress the symbols back into internal representation using their own structure (decoding);
- For the group: the encode/decode rules are shared, transmitted, accumulated (a public scheme).

So language is neither the world itself nor thought itself; it is "a transmissible compression package."

### 3.3 Five-part function decomposition

- Word = slice: symbol → meaning;
- Syntax = spatial composition law: words combine into larger structures;
- Semantics = representation mapping and grounding: what symbols point to, whether they connect to the world;
- Discourse = temporal composition: context, reference, order dependence;
- Logic = rules of the composition law: which combinations are legal, how to infer;
- (Pragmatics = judgment: occasion, appropriateness, truth.)

### 3.4 Language has no physical substance; how are slices used?

A slice is a function, not a physical object; language's slice simply replaces the input space with "symbol space." Two layers:

Layer 1: symbols (discrete, countable) — slices act at the symbol layer.
Layer 2: meaning (representation) — slice outputs land in representation space.
The physical world lies outside layer 2 and connects only through the "grounding" end.

So: language's functionizable form = symbol-layer slices + composition law + temporal sequence; physical substance appears only at the grounding end — for symbols to point at the world, a "symbol–world" correspondence is needed, which is the source of semantic residue (relative R).

### 3.5 Language's time

- Language structure: a static compression scheme; it does not run by itself, and has no internal clock (a dictionary has no time);
- Language use: a sequence unfolded in time (s_{t+1}=I(s_t)); discourse/reference/order dependence are temporal composition; this is externally supplied time;
- Language evolution: word-meaning drift, grammar change, new concepts — slow change of structure C in historical time.

Tense, time words, narrative order are the time *encoded by* language, not language's own time.

### 3.6 Language as a public compression scheme

Vocabulary = categories (cutting continuous sensation into discrete classes); grammar = composition law; logic = rules of the composition law; shared conventions = stability. Language's power to describe the world = the completeness of this scheme; the scheme can accumulate (culture, science, written language — compressing time into structure).

### 3.7 Levels of functionizability: p_language / relative R_language

- Form (symbol strings): functionizable;
- Syntax (composition): functionizable;
- Semantics (representation): partially functionizable relative to a function class/observer (grounding depends on modality; see the supplement of Paper 0);
- Pragmatic judgment (occasion, appropriateness): mostly not functionizable; the rule-like part (conversational implicature patterns, irony patterns) belongs to p_language.

The corresponding division is p_language + relative R_language (relative to our function language and finite observers; absolute R is not judged).

A frequently asked term: **unsaid meaning (implicature)**. It is "the part supplied during decompression": the speaker compresses the whole feeling into literal wording, and the listener uses their own structure to supply what is not written. Most lies in p_language (conversational implicature, pragmatic rules, irony patterns), a small part in relative R_language (shared experience, tacit understanding, tone).

### 3.8 Language can self-reference

Language can describe language (grammar books, dictionaries, this paper). Self-reference has two consequences: language can expand itself (new words, new grammar); language can describe "description" itself (metalanguage). But self-reference reaches only finitely many layers: every description is partial.

## 4. Object layers: B → L → executor

The three layers are not parallel; they form a generation chain:

- **B (brain function)**: world → representation → behavior;
- **L (language function)**: the public structure externalized from many B outputs;
- **Executor (large model)**: learns and executes L.

Hence the division of research objects:

- Studying large models: use L's variables (predictability, composition depth, compression/decompression, grounding residue);
- Studying life: use B's mechanisms (maintenance, self-reference, judgment, internal loops).

Brain mechanisms have projections onto L: convergence → language predictability; redundancy → multiple encoding in the public structure; judgment → linguistic convention. But a projection is not the original — treating the projection as the original makes conclusions "slide."

(The executor's uniform computation and the "brain vs executor" comparison involve subjective understanding of the brain and are not in this paper; see the note *The Executor's Uniform Computation*.)

## 5. The language layer and the executor

The executor learns exactly the product of L: the public compression scheme.

- It gets the symbol layer and its composition rules (p_language), so it speaks language and reasons (logic = composition law);
- It lacks the "organ→sensation→symbol" grounding process — no body, no organs, no sound–phenomenon correspondence;
- Therefore its semantics is symbol-to-symbol correspondence, not symbol-to-world correspondence.

This explains three things:

1. **Speaking language ≠ having language ability**: it reproduces the scheme, not the process that grew the scheme;
2. **Semantic residue**: the unconnected part is not a bug but the necessity of having only the symbol side;
3. **Hallucination**: without correction from the world side, symbol combinations can be self-consistent and wrong.

The same for implicature: the rule-like part (conversational implicature, irony) is learnable; the part relying on tacit understanding and experience (relative R_language) is not.

## 6. Testable corollaries

1. A frozen instant cannot identify life: a single-time check cannot decide life; observation across time is required.
2. The brain's on-demand convergence should correlate with energy constraints: the tighter the constraint, the more on-demand needed. (Note: the free gating in Paper 23 still used only 5.39 layers on average at λ=0, opposite to this direction; the mechanism is to be examined; this corollary is marked as to be tested.)
3. For an executor to adapt depth per token, "composition law (inter-layer routing / intra-layer sparsity) + judgment + cost" must all be present; adding only cost makes it uniformly shallower (testable by controlled training).
4. Syntactic complexity should map to computation steps: deeper dependencies require more layers/steps.
5. Semantic residue should be determined by grounding dimensions: adding a missing dimension reduces residue; redundant modalities do not.
6. The rule-like part of implicature (p_language) should be learnable by models; the tacit part (relative R_language) should not — testable with irony/insinuation tasks.

## 7. Limitations

First, R is only declared, not expanded: only the P side is written; the boundary of R_language/relative R is not operationalized.

Second, language structure is not strictly defined: the common-sense division "word/syntax/semantics/discourse/logic" is used, without formal grammar or a strict semantic framework.

Third, the B–L correspondence is only conceptual: which brain structure corresponds to which language function has no measurable mapping.

Fourth, the origin part is speculative: the evolution from organ to symbol cannot be directly verified.

Fifth, the executor comparison (uniform computation, on-demand convergence) has been split out of this paper into a separate note; this paper does not include those inferences.

Sixth, this paper is formal organization, not new mathematics; understanding of the human brain and language is limited, and no claim is made beyond existing neurolinguistics and linguistics.

---

## Appendix: tags

- **[Definition]** function forms of B and L, five-part decomposition, p_language/relative R_language, implicature, object layers (generation chain).
- **[Organization]** merging former Paper 21 (five forms, Φ, three self-reference levels, unit of life is the whole; the "uniform computation" content has been split into the note *The Executor's Uniform Computation* and marked as subjective understanding of the brain) and former Paper 35 (origin, public compression interface, five parts, symbol slice, language's time, functionizability levels, self-reference).
- **[Speculation]** the origin narrative of language; the executor's "cost + composition law + judgment" being inseparable — a directional speculation.
- **[Not claimed]** no formal grammar; no explanation of consciousness or experience; R not expanded.

> Written by He Qi, with DeepSeek (AI) assisting with organization and writing; views and responsibility belong to the author.

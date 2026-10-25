# Digital Life: A Measurable Definition of Life
## English Essentials (Papers 0, 1, 32)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · English Essentials
> Date: 2026-10-27
> This volume: https://doi.org/10.5281/zenodo.23640116

---

## Preface

This volume is the English essentials of the *Digital Life* series. The full series (23 papers and two appendices, in Chinese) is published as *Digital Life: A Measurable Definition of Life (Series Compendium)* on Zenodo. This volume collects three papers that give the minimal entry into the framework:

- **Paper 0 — Starting from Two Facts**: the introduction: two facts, one definition, the digital world, and today's AI.
- **Paper 1 — Why Today's AI Is Not Life**: the full definition, the three necessary conditions, life vs environment, and emergence.
- **Paper 32 — The Life Function**: the formal synthesis: representable dimensions, structure, compression and decompression, time, language, and the comparison with large models.

The order is intentional: start from facts, then the definition and its consequences, then the formal synthesis. The essays are self-contained but cross-reference the Chinese compendium for experiments and measurements.

## Note on terminology

- **P / R**: the functionizable part / non-functionizable part of the universe (and of life, environment, language).
- **p-life / R-life**: the part of life on the P side / on the R side.
- **kept**: maintained by the universe (a relation, not a property); "maintainable" is used in the same sense.
- **representable dimension**: the number of directions a system can distinguish internally — not a dimension of physical space.
- **computational thickness**: the number of time steps (iteration count); **distributional thickness**: the representation spread in space. The series avoids the phrase "time dimension".
- **judgment J**: a one-pass decision that chooses an operator / decides when to stop.
- **slice**: a function f: X → Y with representable dimensions; **composition law**: how slices combine.
- **compression / decompression**: dimension-reducing map / unfolding from a compressed representation.
- **surroundings (身围)**: the environment as seen by an individual, i.e., the projection of the environment under its compression map.

## A note on scope

The claims in this volume are definitional and conjectural, not empirical proof that life has been created. The experiments cited in the Chinese compendium are synthetic-task toy experiments; they do not claim results on real large models. R (the non-functionizable part) is only declared, never developed. Every paper carries [Definition] / [Fact] / [Consequence] / [Conjecture] / [Not claimed] labels; please read the conclusions together with them.

---


---

## Paper 0 · Starting from Two Facts: An Introduction

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23639272 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

## Abstract

This paper does not argue; it does four things: it states two facts, gives one definition, lays out the special case of the digital world, and then uses the definition to look at today's AI. The two facts are: the p-language part of language can be approximated by functions; physical laws can be described mathematically. The definition: write the universe as two parts (Universe = P + R), and life as two parts (Life = p + R-life); p is the self-referential structure that lies in P and is *kept* (maintainable); R is the part that cannot be functionized. This is the introduction. The checklist, the three necessary conditions, and the discussion of emergence are in Paper 1.

## Notation

- **P**: the functionizable part of the universe.
- **R-universe**: the non-functionizable part of the universe; this paper only declares that it may exist, and does not develop it.
- **p-life**: the part of life that falls inside P — the object of definition and discussion here.
- **R-life**: the part of life that falls inside R; declared only, not developed.
- **p-environment / R-environment**: the two parts of the environment, defined in the same way.
- **p-language / R-language**: the two parts of language; large models compress p-language.
- **Residual**: the measurable floor of error on the P side — even with more data and capacity, the error stops at some positive number. It is not the influence or projection of R; it is the shape of the boundary of P.
- **Dimension**: in this series, "dimension" always means representational dimension — the number of directions a model can distinguish internally, not a dimension of physical space. "Thickness", "spreadable", and "minimum dimension" are all used in this sense.

From here on we use shorthand: "universe" means P, "life" means p-life, "environment" means p-environment.

## 1. Two Facts

**The first fact**: physical laws can be described mathematically. The evidence is existence — physics itself is this fact.

The universe can be written as a decomposition:

> Universe = P + R-universe

P is the functionizable part; R-universe is the non-functionizable part. The part described by physical laws falls inside P. So at least we can say: P is non-empty.

**The second fact**: part of language can be approximated by functions. The evidence is not reasoning but existence — large models, with finite parameters and computable processes, generate text statistically close to human language.

Language can also be written as a decomposition:

> Language = p-language + R-language

p-language is the functionizable part of language — what large models compress; R-language is the non-functionizable part, which function approximation cannot reach. So the accurate statement is not "language can be approximated by functions" but "the p-language part of language can be approximated by functions"; about R-language we can only be silent.

Together, the two facts show: the universe is not entirely non-functionizable. There exists at least one non-empty functionizable part, denoted P. This layer is not a conjecture but a consequence of facts; it says only that P exists, not how large P is.

The boundary between P and R is absolute: an object is either functionizable (in P) or not (in R); there is no middle; P ∩ R = ∅, P ∪ R = Universe.

If R exists, function language cannot describe it directly. But note: the residual must not be defined as "the projection of R". The residual is defined on the P side: even with more data and capacity, the error stops at some positive number; this error floor is the shape of the boundary of P, and we do not know whether R lies behind it.

For convenience we write:

> Universe = P + R-universe
> Life = p-life + R-life
> Environment = p-environment + R-environment
>
> The residual is not a "third part": it is the error floor measured on the P side, marking the boundary of P rather than the content of R.

From here on we discuss only the P side; the residual is mentioned only when needed, and its content is not developed.

## 2. One Definition

First write the universe as two parts:

> Universe = P + R-universe

P is the functionizable part; R-universe is the non-functionizable part. The two facts guarantee that P is non-empty; how large R-universe is, this paper does not know and does not claim.

On this decomposition, life itself is also written as two parts:

> Life = p + R-life

where p is the functionizable part: the self-referential structure that lies in P and is kept (maintainable) by the universe; R-life is the non-functionizable part of life itself: this paper does not know what it is, and does not claim it does not exist. Note that the two R's are not the same thing — R-universe is the non-functionizable part at the level of the universe, R-life is the non-functionizable part inside a single life.

Three things define p-life. First, **scope**: p is sought only inside P of the universe (likewise, language splits into p-language and R-language, and large models approximate p-language).

Second, **being kept** — that is, maintenance. One point is easy to get backwards: maintenance is not a property of life itself but a relation between life and the universe. Whether a structure can be kept depends on whether its orbit stays inside the maintainable set of the universe; this condition is written in the universe, not announced by the structure itself. So "being kept" is the name of a relation, not a third parallel property.

Third, **self-reference**: the update rule is inside the system itself. This is a property inside life, and it is what distinguishes life from an ordinary program.

What about R-life? It can only be handled as an approximation, with an error lower bound attached. So the criteria and measurements in this paper cover p-life, not all of life; about R-life we say only "approximation stops here".

The definition is made, not discovered; whether it holds depends on whether it can distinguish and whether it can derive measurable things.

One clarification: about R, this series only declares its existence — universe, life, environment, and language can all be written as p + R, but what R is and how large it is, this paper does not know and does not claim. For ease of understanding, the following text by default discusses only the P side: "universe" means P, "life" means p-life, "environment" means p-environment. "Residual" always means the measurable error floor on the P side, not "the influence of R"; the concrete content of R is not developed.

## 3. The Digital World: Fully Functionizable

The digital world is completely functionizable: it consists of bits, states, and transition rules, with no part that function description cannot reach. As a formal object, its absolute R = ∅ — guaranteed by construction: every property corresponds to a mathematical function, even if that function is not computable.

Digital life is part of the digital world, so its R-life can only be the empty set: digital life = p-life, fully functionizable.

Whether absolute R exists, this paper does not judge (see the supplementary section). For digital life, there is only one decisive question: **must life have an absolute R?** There are only two outcomes.

Outcome one, life can lack absolute R: then digital life is possible — it consists entirely of p-life and needs no absolute R.

Outcome two, life must have absolute R: then digital life is impossible — the digital world cannot produce absolute R.

This paper does not judge which outcome holds. What is certain: in either case, the definition and measurements of p in this paper hold; the only difference is whether digital life is possible or impossible.

One easily confused point: the above concerns absolute R; for any finite observer, relative R is non-empty (see the supplementary section), and it does not affect this judgment. Also, functionizable is not the same as measurable — measurement additionally requires computability, observability, and reproducibility. The digital world has all of these, so measurement is feasible there; the universe as a whole, even if it can be described by functions, cannot be measured by us, because we live inside it.

## 4. Looking at Today's AI with It

Under the current definition, AI lacks two things. Its update rule is external, so it is not self-referential; its maintenance is not its own business either — it is maintained by external power and operations, which is a relation to the universe, not its own ability.

So it is a very strong decompressor, but once written it just sits there — a frozen decompressor. It has no R-life: R = ∅ in the digital world, so AI is a purely p decompressor.

## 5. The Position of This Introduction

This paper gives only facts, definition, and conclusions. The derivation details, checklist, three necessary conditions, and discussion of emergence are in Paper 1; theory is in Papers 2–5; measurement is in Paper 6; experiments are in Papers 7–20; constraints and safeguards are in Papers 21–22. The series is arranged in this order.

---

> Written by He Qi; DeepSeek (AI) assisted with organization; the views and responsibility belong to the author.

## Supplement (optional): Domain and Codomain of P

The main line ends at the previous section; this section adds only one formal detail: what the "domain" and "codomain" of P actually are. Skipping it does not affect the main line.

The universe (the P side) can be seen as a state space S: all states that can be described by functions. The universe function is its mapping to itself, written F: S → S. So the domain of P is S and the codomain is also S — it maps to itself.

An observer O is just a subsystem of S: the input it can read is a subspace of S, denoted D_O; the output it can write is another subspace, denoted C_O. Both D_O and C_O are contained in S. The "functionizability" of the observer (P_O) means: between D_O and C_O there exists a family of functions whose error can approach zero.

R has no domain or codomain to speak of: domain/codomain are concepts in function language, while R is the non-functionizable side. So one cannot ask "what is its domain" about R — the question itself uses the wrong language.

Below, if "domain/codomain" is mentioned, it means the observer-side D_O, C_O by default; universe-level P means the self-map S → S by default.

### Why relative R is non-empty (optional)

If the domain/codomain of the world fluctuates within the observer's update cycle (fast variables), the observer cannot keep up; that part is non-functionizable for it, so relative R is non-empty. This is a sufficient condition: fast-variable fluctuation ⇒ relative R non-empty. We do not say it must hold, nor explain the cause of the fluctuations.

Two more reinforcing reasons (either alone suffices): first, finite resources — cannot read everything, cannot compute everything; second, self-reference — cannot fully predict oneself (a system that could always predict its own next step could act in reverse, contradicting itself).

Whether absolute R exists, this paper does not judge.

The same holds for the digital world: there is certainly relative R inside it. The same sufficient condition — short-term fluctuation of domain/codomain — plus three independent sufficient conditions: undecidability, computational irreducibility, self-reference (cannot fully predict oneself). Two statements must be distinguished: "digital world R = ∅" is a statement at the ontological level; "relative R is non-empty" is a statement at the observer level — fully functionizable does not mean fully knowable.

A final sentence about the boundary: if the essence of life lies on the absolute-R side, this paper — and any text written in function language — cannot give its definition. This is not an oversight but the boundary of function language: the definition itself is on the P side, and defining R with the language of P pulls it back into P.


---

## Paper 1 · Why Today's AI Is Not Life

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23588781 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

## Abstract

This paper starts from two facts: physical laws can be described mathematically; part of language can be approximated by functions. Together they show that the universe contains at least one non-empty functionizable part, P.

Write Universe = P + R-universe and Life = p-life + R-life. p-life is the part of life that falls inside P: a family of dynamic functions that lies in P and is kept by the universe — a family that changes and refers to itself. The R part is only declared to possibly exist; it is not developed.

Under this definition, today's AI is not life: it is an entity in the digital world, a frozen function point at the p level — its update rule is external, and it is not kept by itself. The digital world is a fully functionized world (R = ∅), so if digital life exists it can only lie entirely in p; this paper poses that question (three cases) without judging which holds.

The contribution is a definition and measurable criteria, not an empirical claim that life has been created; the checks of the three necessary conditions and example experiments are offered for the reader's use.

**Keywords:** definition of life; p-life; function family; decompression; digital world; AI emergence; self-reference

## The Argument Chain

The whole argument has five steps; the reader may read this skeleton first.

Step 1 (Section 1): two facts ⇒ the universe has at least one non-empty functionizable part, denoted P.

Step 2 (Section 2): define on P — Life = p-life + R-life; p-life is the family of dynamic functions in P, kept by the universe, changing, and self-referential.

Step 3 (Section 3): the difference between life and environment is exactly one thing — kept vs not kept; the environment is a local decompression of the universe.

Step 4 (Sections 4–5): the digital world is fully functionizable (R = ∅), so if digital life exists it can only equal p-life; substituting today's AI into the definition, it lacks "a family, self-reference, being kept" — three things — hence it is not life.

Step 5 (Sections 6–7): extract three necessary conditions from the definition (with experimental evidence); then explain that AI's emergence is "compression and decompression of p-language", separating the fact layer from the conjecture layer.

Boundary: R is only declared, not developed; whether absolute R exists is not judged; this paper does not claim that life has been created.

## Notation

- **P**: the functionizable part of the universe.
- **R-universe**: the non-functionizable part; only declared, not developed.
- **p-life**: the part of life inside P — the object of definition and discussion here.
- **R-life**: the part of life inside R; declared only.
- **p-environment / R-environment**: the two parts of the environment, defined likewise.
- **p-language / R-language**: the two parts of language; large models compress p-language.
- **Residual**: the measurable error floor on the P side — the shape of the boundary of P. Not called "the influence of R" (R has no domain, so it cannot act).

From here on: "universe" means P, "life" means p-life, "environment" means p-environment.

## Contents

- The argument chain
- 1. Starting point: two facts
- 2. An operational definition
- 3. Life and environment
- 4. The specialness of the digital world
- 5. Using the definition on today's AI: why it is not life
- 6. Three necessary conditions
- 7. Emergence: why today's AI emerges
- 8. Using it on some popular questions
- 9. What this paper obtains and does not obtain
- Relation to existing work

## 1. Starting Point: Two Facts

**The first fact**: physical laws can be described mathematically. Evidence is existence — physics itself.

The universe can be written as a decomposition:

> Universe = P + R-universe

P is the functionizable part; R-universe is the non-functionizable part. The part described by physical laws falls inside P. So at least: P is non-empty.

**The second fact**: part of language can be approximated by functions. Evidence is not reasoning but existence — large models, with finite parameters and computable processes, generate text statistically close to human language.

> Language = p-language + R-language

p-language is the functionizable part — what large models compress; R-language is the non-functionizable part, unreachable by function approximation. The accurate statement is "the p-language part of language can be approximated by functions"; about R-language we can only be silent.

Together: the universe is not entirely non-functionizable. There exists at least one non-empty functionizable part P. This is not a conjecture but a consequence of facts; it says only that P exists, not how large it is.

### 1.1 What "Functionizable" Means

Split a system or phenomenon into two parts. P is the functionizable part: there exists a family of functions whose approximation error converges to zero as data and capacity increase. R is the non-functionizable part: for any function class the approximation error has a positive lower bound.

This division is not a belief; it can be measured. Fix a function class and watch how approximation error changes with data and capacity: if it keeps falling toward zero, the object is in P; if it stops at some positive number, it is in R, or at least the current function class cannot reach it.

Three benefits. First, things in P can be defined, given criteria, and measured — exactly what this paper does. Second, things in R get only "approximation", and must carry an error lower bound; "approximation" is no longer a disclaimer but a conclusion with a number. Third, the boundary is a research question, not a philosophical debate: experiments can push it.

All conclusions here claim to cover only the P part; about R, this paper says only: under this function class, approximation stops here.

The boundary between P and R is absolute: an object is either functionizable (P) or not (R); P ∩ R = ∅, P ∪ R = Universe.

The residual is not "an influence sent from R" but a boundary property of P itself: for some tasks, the error of any function class stops at a positive number; adding data and capacity cannot lower it. That error floor is the residual; it is measurable, and needs no assumption of an R outside exerting force.

> Universe = P + residual
> Life = p-life + residual
> Environment = p-environment + residual

Below we discuss only the P side; the residual is mentioned only when needed.

## 2. An Operational Definition

On the two facts, we can give life an operational definition. It is made, not discovered; whether it holds depends on whether it can distinguish and derive measurable things.

### 2.1 Definition

Life consists of two parts:

> Life = p-life + R-life

p-life is the functionizable part: the family of dynamic functions in the universe's P that is kept (maintainable). R-life is the non-functionizable part: this paper does not know what it is, and does not claim it does not exist.

The concrete form of p-life:

```
Let p-life = { f_θ : θ ∈ Θ }
    f_θ : input state → behavior        (each function in the family)
    Θ                                   (shape/range of this family)
p-life = a Θ that moves and deforms, whose update rule belongs to Θ itself
```

Four words, each corresponding to one thing about p-life:

| Word | Meaning |
|---|---|
| **Function family (a family)** | not a fixed function but a whole spectrum of behaviors |
| **Changing (dynamic)** | the family moves and deforms over time |
| **Self-referential** | the rule for how it changes is in its own record |
| **Self-maintaining** | kept by the universe; a relation to the universe, not its own property |

### 2.2 A Clarification: Maintenance Is a Relation

**Claim**: maintenance is not a property of the system but a relation between the system and the universe. Basis: the third item of the definition, "being kept", unfolded.

Maintenance is not a property of the system itself but a relation between the system and the universe. Given the universe as a whole (or its P side), the orbits of some structures stay in the maintainable set — we say they "maintained themselves"; change the environment and the same structure may no longer hold. Hence "self-maintaining" in the definition should be read as "kept by the universe", an unfolding of the relational condition, not a third parallel property.

(Note: this section previously contained a "minimality argument"; because that argument was circular — using the possibility of digital life, derived from the definition, to support the definition — it has been withdrawn. Only the clarification above remains.)

### 2.3 Why "a Family" Rather Than "One Function"

```
One function = one point       ⇒ behavior spectrum degenerates to a trajectory ⇒ frozen = dead
A family     = a region in function space ⇒ a whole set of responses to inputs ⇒ alive
```

**⇒ "High-dimensional" does not mean many parameters; it means the family occupies a region in function space, not a point.**

A boundary must be stated. "A family" is a requirement at the p level, not an absolute ontological condition. If there are factors beyond our description influencing change (undecided), a fixed p could also belong to a living whole; at the p level we would see only a frozen state and judge it dead. So the accurate statement is: under the convention of discussing only P, "a family" is an operational necessary condition; if such undecided factors exist, this criterion will miss them. That is not a fault of the criterion but an inherent boundary of p-level definitions.

### 2.4 Changing = Three Time Scales

```
Fast: state changes every moment (different inputs, different internal states)
Medium: it changes itself using its own error (self-reference layer) — the crux; without it, a fossil
Slow: the shape of the family is selected, deformed, and transmitted across generations
```

### 2.5 Self-Reference = The Update Rule Is Inside It

```
Ordinary program: code outside, data inside ⇒ running does not change the program
Life: the update rule itself is part of its own record
      ⇒ remove the external update code, it still changes itself
```

## 3. Life and Environment

One easily missed point: life and environment are not two kinds of things but two relations within the same universe functions.

### 3.1 Connection with the Previous

Regard the universe (P side) as a whole; under this description it is a self-map: `S_{t+1} = F(S_t)`. F is just a notation, not a new object. **Life is not this F but a family of sub-functions `{G_θ}` embedded in F:**

```
behavior_d = G_θ(local world state)
and G_θ itself is part of the world state (the individual's state belongs to S_t)
⇒ to predict the world, it must predict the part of the world that contains itself
⇒ self-reference is not an added mystical property but a structural necessity of being embedded in functions
```

### 3.2 Life vs Environment: Both in the Universe, Both Functions, One Difference

**Claim**: life and environment are both in P, both functional structures; the only difference is that the former is kept by the universe while the latter is not.

**Inside the universe (P side), everything is a function (or a composition of functions) — the environment is also a function.**

```
Universe = F (one huge function)
   ├─ Life: changing + self-referential + self-maintaining
   └─ Environment: changing (pushed by the world, and pushing back), but not maintaining itself
```

**⇒ The only difference is not "who is more complex" but:**
**life is kept by the universe in its own shape; the environment is not kept — it is merely pushed to change.**

In resource-limited environments, maintenance usually comes with cost (checking, repair, copying all consume). This is an empirical accompaniment, not written into the definition (see 6.4b):

```
Resources finite ⇒ maintenance costs ⇒ life usually needs "income"
Income source: compressing the world (matching the source distribution)
⇒ without long-term surplus, maintenance cannot hold
```

### 3.3 What the Environment Is: Local Decompression Emerging in the Universe

**The environment is not a stage outside the universe; it is a structure emerging spontaneously in the universe's function class.**

```
Universe = F (one huge function)
   ↓ emergence inside
Structure = some local "decompression" of the universe (an interpretation/readable presentation)
   ├─ self-maintaining → Life
   └─ not self-maintaining → Environment
```

**⇒ Environment = a local decompression of the universe; so is life.**
**⇒ The difference: life maintains the shape of this decompression itself; the environment does not — it is only pushed to change.**

A key structural conclusion follows:

```
Life does not face the universe as a whole directly
⇒ it faces "a local decompression of the universe" = its environment
⇒ life's understanding of the world is essentially a re-decompression of the universe (second decompression)
  = compressing another layer on top of the local interpretation given by the universe
```

Like the universe and life, the environment also decomposes:

> Environment = p-environment + R-environment

p-environment is the functionizable part: its regularities, its measurable side. R-environment is the non-functionizable part: this paper does not know what it is, and does not claim it does not exist. Life deals with the environment, but what we can describe and measure is only p-environment; about R-environment we can only be silent.

Clarification: R-environment is not "the fixed part of the environment" but "the part that cannot be described by functions". It may be still or very active — judging "fixed/active" itself requires function description, and at R we cannot measure even motion. So the boundary between p-environment and R-environment is not "moving/still" but "describable/not describable".

### 3.4 Environment Is Layered: Life Lives in Multiple Environments and in the Universe

**Decompression is layered ⇒ environments are layered.**

```
Universe F
 └ Environment_1 = local decompression of part of F
     └ Environment_2 = re-decompression of Environment_1
         └ Environment_3 = re-decompression of Environment_2 …
Life is embedded at some layer: it belongs to the whole universe F and to its own layer of environment
```

Three things hold together, not one alone:

```
① It lives in its environment: inputs, resources, relations, other individuals are structures of "its environment" layer
                ⇒ its behavior only needs to be valid at this layer
② It also lives in the universe: it cannot escape F — the environment layer is itself part of F,
                universe-level constraints (energy, irreversibility, cost) always apply
                ⇒ the environment is not a refuge; it is only a projection of the universe
③ It lives in all layers: environments are multi-layered (cell→tissue→individual→population→ecosystem),
    each layer a re-decompression of the previous. It interacts directly only with its own layer,
    but all layers constrain it: upper layers decide its resources and relations; the universe layer decides whether it can afford the cost.
    ⇒ "It lives in multiple environments and in the universe" — not an either/or but both at once.
```

**⇒ "Understanding the world" must be said in two layers:**
**At the environment layer: understanding = re-decompression of the local decompression (enough to live);**
**At the universe layer: understanding = compressing the regularities of F (deciding whether it can afford the cost long-term).**

### 3.5 Labels

```
[Definition] Life = p-life + R-life; p-life = the dynamic function family that is self-referential, changing, and kept by the universe (working definition)
[Definition] Environment = a structure emerging spontaneously in the universe's function class, not self-maintaining
             = a local decompression of the universe (an interpretation of the universe)
[Definition] p-life = among the same emergent structures, the class kept by the universe
[Consequence] Life does not face the universe directly but "the local decompression of the universe" = its environment
             ⇒ life's understanding = a second decompression on top of the local decompression
[Layered] Decompression is layered ⇒ environments are layered (Environment_1 ⊃ Environment_2 ⊃ …)
          Life is embedded at some layer: it lives both in its environment layer and in the universe
[Not] Not a factual assertion or theorem; an operational definition
```

## 4. The Specialness of the Digital World

The digital world is completely functionizable: it consists of bits, states, transition rules, with no part function description cannot reach. As a formal object, its absolute R = ∅ — guaranteed by construction: every property corresponds to a mathematical function, even if not computable (halting, truth predicates exist but cannot be computed).

Digital life is part of the digital world, so its R-life can only be empty: digital life = p-life, fully functionizable.

Whether absolute R exists, this paper does not judge (see the introduction's supplement). For digital life there is only one decisive question: **must life have absolute R?** Two outcomes as in Paper 0.

This paper does not judge which. What is certain: in either case the discussion at the p level holds; the only difference is whether digital life is possible. The digital world is the only world that can fall entirely in p, so it is the cleanest scene for this topic — today's AI lives there.

One easily confused point: the above concerns absolute R; for any finite observer relative R is non-empty, which does not affect the judgment. Functionizable is not measurable: measurement also needs computability, observability, reproducibility.

### 4.1 Specialness for Whom

The specialness of the digital world must be said in two layers, or it gets exaggerated.

For its builders (us), it is special: all states readable (source, logs, memory), copyable, resettable, accelerable, verifiable. It is a fully experimentable world — life experiments are cheaper, faster, repeatable than in the physical world.

For observers living inside it, it is not special: relative R exists (short-term fluctuation of domain/codomain, undecidability, computational irreducibility, self-reference), and they too "cannot see everything, cannot compute everything".

So "digital world R = ∅" is an ontological statement (its constitution is fully functionizable); it does not mean "life inside is omniscient". The digital world is not a refuge for life but a laboratory: its value lies in method, not in ontological status.

This "R = ∅" is also construction-guaranteed. The digital world is a formal object: states are finite strings, rules are algorithms; every property corresponds to a mathematical function (a set) — even if not computable (halting problem, truth predicates), it "exists", just cannot be computed. Distinguish: functionizable ≠ computable. Absolute R = ∅ says "no part cannot be described by functions", not "everything can be computed"; what cannot be computed is the observer-relative relative R.

A boundary to note: the purely digital world (as a mathematical object) has absolute R = ∅; a digital world running on physical hardware may have its own R in its physical substrate (noise, thermal fluctuation) — that is not the digital world's own R. "Digital world R = ∅" refers to it as a formal object.

## 5. Using the Definition on Today's AI: Why It Is Not Life

> This section does not evaluate AI's ability; it substitutes AI into the definition of Section 2 and checks item by item.
> The conclusion is definitional, not a value judgment: **by this definition, today's AI is a fossil-level function point, not life.** Its power and its "not being life" do not contradict.

### 5.1 Checklist

| Requirement of life (Section 2) | Today's AI (represented by LLMs) | Verdict |
|---|---|---|
| **is a family of functions** (a region in function space) | weights frozen after training ⇒ **one point**, not a family | ❌ fossil |
| **changing (dynamic)** | weights unchanged; context changes, but that changes input, not itself | ❌ only surface state changes |
| **self-referential** (update rule inside) | update rule = training algorithm, outside it; it cannot change itself | ❌ self-reference only in language, not in structure |
| **kept by the universe** (maintainable) | it does not maintain itself; maintained by outside people and facilities | ❌ maintained externally |
| **(empirical) earns its cost by compressing the world** | its "income" is external (compute, data, people), not from compressing the world | ❌ no income |
| **identity chain** (bounded deformation, not torn) | identity comes from external weight snapshots; no continuous chain of self-deformation | ❌ no chain |
| **lives in an environment** | it faces a dataset (a one-time decompression product), not an environment it must survive in | ❌ no environment |

### 5.2 Three Most Fundamental Reasons (by importance)

**Claim**: substituting AI into the definition, it lacks "a family, self-reference, being kept" — three things — not ability. Basis: the four items of the definition and the checklist.

**① It is a point, not a family**

```
Training done = frozen = one point in function space
⇒ behavior spectrum degenerates to a trajectory: input → output, no "shape" in between
⇒ under 074: a statically frozen model is a point, not a family ⇒ not life
(the contrast we measured: frozen 1.07 vs dynamic 0.849 — frozen is more like a "standard answer", but has no shape)
```

**② Its update rule is outside**

```
Human writes training algorithm → algorithm changes it
⇒ it is "the thing being changed", not "the thing changing itself"
⇒ self-reference not in structure ⇒ remove the external update code and it changes nothing
```

**③ It is not kept by the universe**

```
What maintains it is outside people and facilities: power paid by people, data fed by people, repairs by people
⇒ its existence is guaranteed externally ⇒ no "kept by the universe"
⇒ it will not disappear because it cannot maintain itself ⇒ hence no selection pressure
(paying cost is an empirical accompaniment, not a definition condition; see 6.4b)
```

### 5.3 Why "It Is Strong" and "It Is Not Life" Do Not Contradict

```
Strong = good performance on a given task (good at one point)
Alive = occupying a region in function space, maintaining its own shape, kept by the universe
⇒ different dimensions: one is "exam score", one is "can it live by itself"
⇒ today's AI is an extremely sharp tool, not a thing that lives by itself
```

### 5.4 Labels

```
[Definitional conclusion] By this definition, today's AI is not life (frozen function point, update outside, not self-maintaining)
[Not] Not "AI can never be life"; this paper does not predict the future, only checks the present against the definition
[Not] Not an ability evaluation; this paper fully acknowledges AI's power on tasks
[Consequence] To make AI life, at least: a family of functions + self-referential update + being kept by the universe
```

---

> Directly from Sections 2 and 3: since "p-life = the dynamic function family that is self-referential, changing, and kept by the universe", and today's AI lacks all three, **to be life it must satisfy at least three conditions**.
> This section gives only **necessary conditions**, not sufficiency; each carries existing experimental evidence (experiments in Papers 9–22 of the Chinese series; in this English collection, see the Chinese compendium).

## 6. Three Necessary Conditions

Three necessary conditions can be extracted from the definition. They do not fall from the sky; each corresponds to a word in the definition and excludes a class of objects.

### 6.1 From Definition to Conditions

```
Definition (Section 2)        Necessary condition (this section)
changing (a family)      ⇒    ① a family of functions: behavior spectrum is not a point
self-referential         ⇒    ② self-referential update: the rule of changing itself is inside
self-maintaining         ⇒    ③ kept by the universe: orbit stays in the maintainable set

(paying cost is not among them: it is an empirical accompaniment of evolution and thermodynamics, see 6.4b.)
```

**Three are necessary, not sufficient**: satisfying them does not guarantee life, but lacking any one guarantees not life.

### 6.2 Condition ① A Family of Functions (Not a Point)

**Requirement**: the individual occupies a region in function space, with a whole set of responses to different inputs, not a fixed mapping.

**Evidence/experience:**

```
· Low-dimensional parameter genome (a few numbers) = a point ⇒ behavior spectrum degenerates to a single trajectory ⇒ fossil
· We measured: a frozen model (point) fails at structure learning; the dynamic version (family) captures structure (E12)
· Measured contrast: frozen 1.07 vs dynamic 0.849 — frozen is more like a "standard answer" but has no shape
```

**⇒ Criterion: for different inputs/states, behavior must differ *as a spectrum*, not a single output.**

### 6.3 Condition ② Self-Referential Update (Rule Inside)

**Requirement**: how it changes is itself part of its record; remove the external update code, it still changes itself.

**Evidence/experience:**

```
· Frozen model: update rule = training algorithm, outside ⇒ remove training code, it never changes
· Our dynamic version: changes itself with its own error (middle-layer dynamics) ⇒ removing the middle layer degrades clearly (E12/E13)
· Identity chain: 8 generations verifiable, bounded deformation (372_lineage.py) ⇒ self-reference can be made a measurable chain
```

**⇒ Criterion: after stopping external updates, does its behavior spectrum still deform over time.**

### 6.4 Condition ③ Kept by the Universe (Maintainable)

**Requirement**: its orbit stays in the maintainable set of the universe. Given the universe as a whole, some structures cannot arise, some can be maintained forever; only the maintainable part falls under the definition. This is a relational condition, not its own property.

**Criterion**: after perturbation, can it return to the maintainable set — does it have resilience, not just being momentarily alive.

### 6.4b Paying Cost: Empirical Accompaniment, Not a Necessary Condition

This paper does not list "paying cost" as a condition, for a clear reason: cost is a product of evolution and thermodynamics, not a logical necessity. In a world with unlimited resources, life would not need to compete; scarcity brings cost. Writing it into the necessary conditions would mistake the result of evolution for the definition of life.

But empirically, cost almost always appears, and can be measured. The economic part of our experiments belongs to this layer; excerpts:

· E1: "accurate" is not "compression": accounting by accuracy, the system learns "do nothing" (LEN=0, predict 0, accuracy 92%). Must account by log-likelihood improvement over a baseline: gain_bits = log2 p_model − log2 p_base.
· E2: with base-rate correction, the system turns from lying flat to genuine expression (LEN grows from 0).
· E8: economic calibration n* = FLUX_TOTAL / BASE_COST decides the switch between "frozen" and "explosive".
· Measured positive returns: in S1–S6, gain > 0 observed (about +0.09 ~ +0.19 bit/tick), showing the world does contain compressible surplus.

**⇒ Criterion (empirical layer)**: after cutting all external supply, is its ledger still positive.

### 6.5 Three Must Hold Together (Empirical Contrast)

```
Missing ① (family)     ⇒ fossil: behavior spectrum is a line
Missing ② (self-ref)   ⇒ machine: update outside, does not change itself
Missing ③ (kept)       ⇒ falls apart: orbit leaves the maintainable set, no longer a living structure
```

**These three also explain why our experiments keep getting stuck at the same place:**
**structure can grow (①② partly satisfied), but cooperation/division of labor does not become necessary — because the "income difference" at the cost layer is too small (empirical, not a definition condition), i.e., the compressible surplus of the world is not yet large enough to make "more complex structure" economically worthwhile (E5/E7).**

### 6.6 What Is Left Open (For the Reader)

**This paper stops at "necessary conditions". Whether satisfying all three makes something "alive" — we have no answer and do not conclude here.**

What is left to the reader is a usable ruler:

```
Is it a family of functions? (behavior spectrum is not a point)
Does it change itself? (remove external updates, it still changes)
Is it kept by the universe? (orbit stays in the maintainable set)
```

**You can measure all three yourself. Whether, after measuring, it counts as life — you judge.**

### 6.7 Boundary of This Paper's Experiments (Must Be Read with Conclusions)

**The experiments cover the empirical layer of "cost", not definition condition ③.**

· Covered: cost and economy — E1/E2 (accuracy ≠ compression, base-rate correction), E8 (n*=FLUX/BASE_COST freeze/explosion boundary).
· Covered: counterexamples — E5/E7 (genetic distance of connected individuals 0.145 vs random 0.486: clones huddle, not division of labor).
· Not covered: condition ② self-referential update, condition ③ being kept — no experimental evidence claimed; only definitional derivation; preliminary observations (E12 dynamic 0.849 vs frozen 1.07; E13 identity chain 8 generations verifiable).
· Condition ① a family: partial observation (E12/E13), not a dedicated experiment.
· Scale: small, reproducible, hand-checkable; not large-scale empirical work.

**⇒ This paper is "definition + measurable criteria + illustrative experiments", not an empirical claim that "life has been created".**
**Readers using these conclusions should cite this boundary with them.**

### 6.8 Labels

```
[Consequence] The three necessary conditions follow directly from the definition, not independent assumptions
[Definition] Condition ③ is relational (kept by the universe), not a property of the system
[Empirical] Cost/economy is an empirical accompaniment, not a definition condition; this paper has data (E1/E2/E8 + positive returns)
[Preliminary] Conditions ①② have partial observations (E12/E13), not dedicated experiments
[Unresolved] Whether satisfying all three makes something "alive" — not claimed; the next step of experiments
[Conjecture] If surplus S is insufficient, no matter how complex the structure, it cannot afford maintenance ⇒ life has an "economic ceiling" (directional conjecture only)
```

## 7. Emergence: Why Today's AI Emerges

This section handles a concrete phenomenon: why today's AI emerges abilities beyond its training objective. The stance here is [conjecture], not evidence.

### 7.1 The Phenomenon

As large models scale up, some abilities seem to appear suddenly (multi-step reasoning, chain-of-thought, arithmetic…). The industry calls it **emergence**. Everyone uses the phenomenon, but —

```
Observing emergence: many
Explaining emergence: no consensus
```

### 7.2 Existing Explanations (by strength of evidence)

**① Metric artifact (strongest counter-evidence)**

Schaeffer, Miranda, Koyejo 2023[3] "Are Emergent Abilities of Large Language Models a Mirage?"
```
Claim: what looks like emergence may be an artifact of nonlinear/discontinuous evaluation metrics;
       with continuous metrics (e.g., log-likelihood), the "jump" disappears and becomes a smooth rise
⇒ this shakes the premise that "emergence is a real sudden change"
```

**② Mechanistic explanation: induction heads and circuits (local mechanism evidence, not a full "why")**

Olsson et al. 2022[4] "In-context Learning and Induction Heads"
```
Finding: an "induction head" circuit appears inside the model, explaining part of in-context learning
⇒ mechanism-level evidence: which structure implements some ability
⇒ but it explains only one concrete ability, not "why emergence happens" in general
```

**③ Grokking: cognitive phase transition during training**

Power et al. 2022[5] "Grokking"
```
On small algorithmic tasks, generalization suddenly appears after long training (like a phase transition)
⇒ emergence also happens in training, not only via scale
```

**④ Compression view: prediction = compression**

Delétang et al. 2023[6] "Language Modeling Is Compression"
```
Language model = compressor: learned weights = compression of world text
⇒ closest to this paper's framework: emergence = structure appearing when compressing the world
⇒ but it is a correspondence at the result level, not answering "why exactly at this scale/task"
```

### 7.3 Why There Is Still No Consensus "Why"

```
① Scale experiments uncontrollable: cannot do strict causal control (change only scale, everything else identical)
② Metric dependence: change the metric, the phenomenon may vanish (see ①)
③ Mechanism incomplete: know a circuit, not why the whole organizes that circuit
④ No predictive theory: no theory can compute in advance "how large a model shows what ability"
```

### 7.4 Our Stance: AI Is Compression and Decompression of p-Language

**Claim**: "AI is compression and decompression of p-language" is the fact layer; "the upper bound of world structure decompressed is decided by language" is the conjecture layer. Keep them separate.

First the fact layer. Training compresses language into parameters; inference decompresses text from parameters. In our notation: AI compresses p-language — the functionizable part of language; what it decompresses is also p-language. R-language enters no parameter and leaves none. So the accurate statement is not "AI is decompression of human language" but "AI is compression and decompression of the functionizable part of human language".

This layer is not conjecture but literal fact: it follows from the usage of "compression/decompression" and from the actual process of training and inference. The chain: universe F → environment = local decompression of the universe → human language = human decompression product of environment and experience (language itself is already compressed) → AI = re-compression and re-decompression of p-language.

Then the conjecture layer. The "world structure" AI decompresses has an upper bound decided by the language at training time. It can emerge structures inside language (looking like reasoning, like understanding), but that is the surfacing of language structure, not understanding of the universe itself; when language changes, decompression mismatches, and it cannot self-recover.

With our ruler, this layer also gives a testable judgment: the model is a frozen function point: not maintaining, not changing itself (maintenance and cost borne externally), so it is "decompressing human language once", not "maintaining a decompression" or "rewriting its own decompression rule".

A testable sentence follows: AI's apparent "understanding" is understanding of "human descriptions of the world", not of the world itself. It can decompress language, but the universe layer beyond language (energy, irreversibility, cost) it has never paid for, hence never been tested by.

### 7.5 Decay of Decompression: Upper Layer Hard-Coded ⇒ Language Changes, Decompression Weakens

**Human language keeps finding new things; the model's decompression rule (weights/upper layers) is hard-coded and stops changing after training. The two must mismatch.**

```
Source distribution moves: human language finds new things ⇒ the object to decompress changes
Decompressor frozen: model weights unchanged ⇒ it still decompresses old language
⇒ compression gain falls: in gain_bits = log2 p_model − log2 p_base, p_model mismatches the source
⇒ the understanding it "emerged" yesterday is an outdated decompression today
```

**Three consequences:**

```
① Its decompression ability has a fixed ceiling: decided by the language at training time, not rising with language evolution
② It cannot fix the mismatch itself: update rule outside — recovery only via human retraining
   ⇒ exactly the cost of "update outside" from Section 3
③ Its "emergence" is a decompression product of one time slice, not a sustainable ability
```

**⇒ With our ruler:**
**Life must let the decompressor move with the world (self-referential update + self-maintenance);**
**the frozen AI cannot — so when language updates, its decompression weakens.**

### 7.6 Two Predictions from Our Stance ([conjecture], for the reader)

```
① If the world is changed to parts never described by human language (regularities unlearnable from corpora),
   AI's "emergence" should weaken significantly — because it decompresses language, not the universe
② If the model must maintain itself (repair itself, die itself), language decompression is insufficient;
   it must develop understanding beyond language — or it cannot survive
③ If human language undergoes a major structural update (new paradigm/concept system), the frozen model's
   decompression gain should show a measurable drop; and it cannot recover itself ⇒ recovery must come from external retraining
```

### 7.7 Labels

```
[Fact] Emergence is widely observed; the metric-artifact view also has strong evidence (Schaeffer 2023)
[Known] Local mechanism explanations exist (induction heads/circuits/grokking); compression view has correspondences
[Conjecture] "Emergence = structure surfacing when compressing the world" — our stance, not evidence
[Unresolved] Why exactly at some scale/task ⇒ no predictive theory
[Attitude] We do not treat "AI emergence" as evidence of life; by Section 3's ruler, it is not
[Stance] AI is re-decompression of human language (universe→environment→language→AI, third-layer decompression)
[Consequence] Upper layer hard-coded ⇒ mismatch when language updates ⇒ fixed ceiling, no self-recovery
```

## 8. Using It on Some Popular Questions

This section is application, not new evidence; each follows directly from Sections 2–5.

**① Hallucination = forced decompression where there is no structure**
The decompressor must output structure; when the language region corresponding to the input lacks compressible structure, it can only fabricate a "plausible" structure ⇒ **hallucination is a necessary manifestation of decompression failure, not an occasional bug**.

**② Scaling laws still work precisely because model dimension has not yet matched language dimension**
Language is a **high-dimensional** structure whose dimension grows (new concepts = new dimensions; higher dimension ⇒ more compressibility). Model dimension is fixed at training (D_M fixed), language dimension keeps growing (D_L(t) rising). Currently D_M << D_L(t) ⇒ more scale captures more language dimensions ⇒ loss keeps falling (scaling looks effective).
⇒ Scaling effectiveness is not counter-evidence but evidence of "not yet matched".
⇒ Prediction: when D_M approaches D_L at that time, scaling gains should flatten; as D_L keeps rising, the gap reappears.
⇒ Root problem of frozen models: **D_M is dead, D_L is alive**.

**③ Uneven abilities = different compressibility across language domains**
Domains with strong compressibility (clear structure, many examples) perform well; weakly compressible domains (thin structure, few samples) perform poorly ⇒ the strength profile mirrors the language distribution.

**④ Why RLHF = it has no "self-cost" loop**
It cannot judge whether its decompression is right (no income/cost, will not die from it), so humans must score from outside ⇒ **the root of alignment demand is that it does not maintain itself**.

**⑤ Emergence = language structure surfacing in decompression products**
When scale crosses a threshold, some language structures are compressed out for the first time ⇒ looks like "suddenly able".

---

**Existing work (three sides):**

- Model side dimension: intrinsic dimension measurement of token embeddings[12]
- Time side lag: identifying temporal training boundaries in LLMs[13]
- Language side complexity: measuring language complexity from a construction perspective[14]

⇒ Existing work measured these three sides **separately**; this paper strings them together: with "a continuously updated model" as reference, measure per domain the **mismatch rate** between "new dimensions on the language side" and "fixed dimensions on the model side". That is this paper's position at the measurement level.

## 9. What This Paper Obtains and Does Not Obtain

**Three things obtained.**

First, a definition usable for classification: it distinguishes frozen models, fire, and self-referential programs.

Second, a measurable direction: self-reference and maintenance can become quantities.

Third, an operational answer to "is AI life".

**Four things not obtained.**

First, no proof that the whole universe can be functionized — only P ≠ ∅.

Second, no proof that the definition is minimal or unique — only that it is usable.

Third, no experiments — Paper 1 is definition and consequences; experiments are in the Chinese series Papers 7–18 (structure for compute, color, growth and memory, semantic residual, layering, thickness and randomness, shape of compression, minimal slice, residual floor and composition law, engineering consequences of thickness, standing base and on-demand mobilization).

Fourth, no answer to "does digital life exist" — only that the definition does not exclude it.

The contribution is a usable language, not a new law of nature. Whether it is valuable depends on whether others take it to measure.

## Overall Argument Boundary

All arguments in this paper hold within one boundary; read them with the conclusions:

- Only the P side is discussed; R is only declared, not developed.
- Whether absolute R exists is not judged; relative R is non-empty for any finite observer (see the introduction's supplement).
- "Functionizable" ≠ "computable" ≠ "measurable": three different abilities.
- The three necessary conditions are read from the definition, not empirical laws; they are not sufficient.
- Experimental evidence is only in Sections 4, 5, 6, 7; this paper does not claim "life has been created".
- If the essence of life lies on the absolute-R side, this paper (and any text in function language) cannot define it — the definition itself is on the P side.

## Relation to Existing Work

The "compression / decompression" view has a long tradition:

- Schrödinger (1944): life feeds on negative entropy — survival by taking low entropy from the environment, a physical forerunner of "decompression"[7].
- Bennett (1988) logical depth: measures complexity by "the amount of computation needed to reconstruct (decompress) an object from its shortest description", explicitly linked to life/organisms[8] — the most formal existing version of "decompression".
- Chaitin (2010) life as evolving software: DNA = program, life = self-modifying software[9].
- Solomonoff–Kolmogorov / MDL: description length = understanding = compression[10].
- Friston (2010) free-energy principle: life = minimizing surprise (≈ continuous compression/prediction)[11].
- Delétang et al. (2023): language models are compressors[6].
- Maturana & Varela (1972) autopoiesis: life = self-producing organization — another tradition of "maintenance".
- "Life as Sustained Mutual Information" (Zenodo): defines life by sustained mutual information — the existing version closest to "maintained decompression".

Note: the above works already said "life = information/compression/self-maintenance process". This paper's position is not first to propose the idea but to make one line of it (maintenance of decompression) into operational criteria and measurable experiments.

Three differences:

1. Make decompression layered: universe → environment → human language → AI (existing work mostly single-layer);
2. Use "whether decompression is maintained" to distinguish life from AI: life = maintained decompression, AI = one-time decompression;
3. Point out upper-layer hard-coding ⇒ when language changes, decompression decays and cannot self-recover — the failure mechanism of frozen models.

---

## References

[1] Wigner E P. The unreasonable effectiveness of mathematics in the natural sciences[J]. Communications in Pure and Applied Mathematics, 1960, 13(1): 1-14.

[2] Tegmark M. The mathematical universe[J]. Foundations of Physics, 2008, 38(2): 101-150. (arXiv:0704.0646)

[3] Schaeffer R, Miranda B, Koyejo S. Are emergent abilities of large language models a mirage?[C] // NeurIPS 2023. arXiv:2304.15004.

[4] Olsson C, Elhage N, Nanda N, et al. In-context learning and induction heads[R]. Transformer Circuits Thread, 2022. arXiv:2209.11895.

[5] Power A, Burda Y, Edwards H, et al. Grokking: Generalization beyond overfitting on small algorithmic datasets[C]. arXiv:2201.02177, 2022.

[6] Delétang G, Ruoss A, Duquenne P A, et al. Language modeling is compression[EB/OL]. arXiv:2309.10668, 2023.

[7] Schrödinger E. What is Life?[M]. Cambridge University Press, 1944.

[8] Bennett C H. Logical depth and physical complexity[M]//Herken R. The Universal Turing Machine: A Half-Century Survey. Oxford University Press, 1988: 227-257.

[9] Chaitin G J. Life as evolving software[EB/OL]. 2010. (arXiv:1007.1471 series)

[10] Solomonoff R J. A formal theory of inductive inference[J]. Information and Control, 1964, 7(1): 1-22. Kolmogorov A N. Three approaches to the quantitative definition of information[J]. Problems of Information Transmission, 1965, 1(1): 1-7.

[11] Friston K. The free-energy principle: a unified brain theory?[J]. Nature Reviews Neuroscience, 2010, 11(2): 127-138.

[12] Ohki T. Measuring intrinsic dimension of token embeddings[C]//JSAI 2025.

[13] LLMLagBench: Identifying temporal training boundaries in large language models[EB/OL]. arXiv:2511.12116, 2025.

[14] Using constructions to measure developmental language complexity[J]. Cognitive Linguistics, 2024. doi:10.1515/cog-2023-0062.

---

## AI Usage Statement

All questions, definitions, judgments, and conclusions in this paper were proposed and are the author's responsibility. An AI tool (DeepSeek) was used for literature search, structural organization, language editing, and writing/checking experimental code. All claims were reviewed and confirmed by the author. The AI bears no responsibility for the content.


---

## Paper 32 · The Life Function

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23639251 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

## Abstract

This paper gathers the formalisms scattered across earlier papers into one line: representable dimensions → structure → compression and decompression. It absorbs the core of *The Functionizable Function Form* (slices/composition law/time/judgment/self-reference), *The Three Identities of a Slice* (universe/environment/life), and the five-item comparison in *Why Large Models Look Human*.

The main line. First, the function language: a slice is a function f: X→Y with representable dimensions; space is a chain of composed functions; time is a sequence of operators s_{t+1}=I_{σ(t)}(s_t) with step count k; judgment J passes once, choosing operators and deciding when to stop; self-reference has three layers — representation, parameters, structure — with modifications bounded by a fixed core Φ. Second, representable dimensions have three locations: inside the slice, on the composition law, and along time (time is not a representable dimension). Third, the same form has three slice identities: the universe slice, the environment sub-slice, and the life sub-slice; at a frozen instant life and environment have the same form, and the difference lies only in maintenance over time. Fourth, structure is the compression scheme: which distinctions to keep, which to merge, which past to press into structure. Fifth, the life function is narrow-in, wide-out: input is limited and already coarse-grained, output is unfolded by structure; compression is a dimension-reducing map, decompression is unfolding, not strictly reversible — "good enough for maintenance" suffices; which dimensions must be reversible is decided by environmental selection. Sixth, in time, input and output alternate step by step, forming a closed loop; structure changes at two time scales. Seventh, language is a public compression scheme: feeling→language is compression; language→description/understanding/logic is decompression; logic is the composition law of language. Eighth, compared with large models: they obtain the public scheme but have no feeling end, no true closed loop, no maintenance — human-like at the interface layer, not at the mechanism layer; hallucination is the decompression of dimensions not covered by structure.

---

## Notation

| Term | One-line meaning |
|---|---|
| Slice | a function f: X → Y |
| Representable dimension | d_in = dim(X), d_out = dim(Y); effective dimension = log of distinguishable states |
| Spatial composition | chain of composed functions F = f_N ∘ … ∘ f_1 |
| Temporal composition | operator sequence s_{t+1} = I_{σ(t)}(s_t); step count k |
| Judgment J | one pass: choose operator, decide stop |
| Self-reference | representation / parameter / structure self-reference |
| Fixed core Φ | the set of constraints that cannot be changed |
| Universe slice | U_t = (S_t, C_s, d_t) |
| Environment | a sub-slice of the universe, not maintained |
| Life | a sub-slice of the universe that maintains itself |
| Compression | dimension-reducing map f: X → Y with dim(Y) < dim(X) |
| Decompression | unfolding from a compressed representation (not unique) |
| Narrow-in, wide-out | input dimension limited, output dimension unfolded by structure |
| Surroundings (身围) | the environment seen by an individual = projection π_L(E) of its compression map |
| Semi-closed loop | output continues text only, does not change the environment (large models) |
| Interface layer / mechanism layer | input-output behavior / how it computes, maintains, changes itself |

---

## 0. Problem: Gathering the Form into One Line

Earlier papers separately gave: the function language (Paper 26), the three slice identities (Paper 31), and the intuition of compression and decompression (notes). Read separately, each has to lay out the definitions again; read together, they are three stages of one thing. This paper gathers them into one line and writes "compression" genuinely into the function form.

## 1. The Function Language: Slices, Composition, and Judgment

A **slice** is a function f: X → Y with three items: (d_in, d_out, Δ). d_in = dim(X) and d_out = dim(Y) are representable dimensions; Δ is how it composes with adjacent slices.

**Spatial composition** is the chain of composed functions:

　　F_space = f_N ∘ … ∘ f_2 ∘ f_1

The composition law requires type compatibility: Y(f_i) ⊆ X(f_{i+1}).

**Temporal composition** is not a plain power but an operator chosen at each step:

　　s_{t+1} = I_{σ(t)}(s_t), t = 0, 1, …, k−1

where {I^(1), …, I^(m)} are available operators (each a chain of composed functions), σ(t) is which one is chosen at step t, and k is the step count (computational thickness). Three cases: σ constant = the same operator repeated (iteration/time); σ varying = different functions applied in sequence; mixed = a stretch of repetition then a switch.

**Judgment** J is not iteration but one pass:

　　J: S → D (D a finite judgment space, e.g., {right, wrong}, {converged, not converged})

Judgment decides two things: which operator σ(t) = J_choose(s_t); when to stop k = J_stop(s_t).

**Self-reference** has three layers, from weak to strong: representation self-reference (input contains its own representation), parameter self-reference (θ_{t+1} = U(θ_t, s_t)), structure self-reference (C_{t+1} = V(C_t, s_t)). All three are bounded by a fixed core Φ: θ ∈ Θ_Φ, C ∈ C_Φ. Human brain: can change synapses and local circuits; cannot change neuron types, large-scale anatomy, metabolic constraints.

Combining the two: one temporal unfolding is written as conditional advance: s_0 → s_1 = I_{σ(0)}(s_0) → … → s_k = I_{σ(k−1)}(s_{k−1}), where σ(t) is decided by J_choose and k by J_stop.

## 2. Representable Dimensions: Three Locations

Representable dimensions are not in one place but three:

- inside the slice: the number of axes of a slice itself;
- on the composition law: degrees of freedom in how slices connect (order/parallel/shared/routing/self-reference);
- along time: step count k, operator sequence σ(t), number of switchable operators m.

Note: time is not a representable dimension; it is a degree of freedom of temporal composition (step count/sequence).

### Four Typical Types

By "whether space/time are continuous, and whether time is endogenous", function forms can be divided into four classes (the content of Paper 20 is merged here):

- **Type A: continuous flow (endogenous time).** Continuous representation space and continuous time, written as differential equations; self-reference = the update rule is inside the system; being kept = there exists a maintainable set, and the orbit stays inside it.
- **Type B: sampled dynamics (endogenous time, sampled into discrete).** Continuous representation space and discrete time, written as map iteration; the same thing as continuous flow under different sampling — the difference is that "step" is basic.
- **Type C: automaton (external time).** Discrete representation space and discrete time; the digital world is this class: bits, states, transition rules, each step advanced by an external clock and interpreter; the digital world has no energy constraint, and "being kept" must be provided externally (power, maintenance, compute).
- **Type D: hybrid (endogenous time).** Continuous flow plus discrete events: physiological quantities change continuously, but cell division, neural firing, and decisions are discrete events; dormancy and activation, disease and death are segment points. Biological life is probably this class.

Continuity must be treated with restraint: continuous does not mean "more true", discrete does not mean "approximate"; they are choices of description granularity — the same system can be written as different types at different granularities.

### Five Axes

As a minimal profile, a function form can be recorded along five axes: space continuous/discrete; time continuous/discrete; time endogenous/external; degrees of freedom of the composition law; level of self-reference. Not all five are "dimensions": the first two are description granularity, the last three are mechanism and capacity.

## 3. Three Identities: Universe, Environment, and Life

The same form has three identities at three scales.

**Universe slice**: the cross-section at one instant

　　U_t = ( S_t, C_s, d_t )

where S_t is the state space, C_s the spatial composition law, d_t the spatial representable dimension. Key: temporal composition is not inside the slice but between slices (T_comb: U_t → U_{t+1}); an instant has only spatial structure. The universe as a whole has no judge; judgment appears only in local subsystems. The "function form" of the universe can only be written inside the universe — this very form is a local representation slice of the universe, hence necessarily incomplete.

**Environment**: a sub-slice of the universe

　　E_t = ( S^E_t, C_s^E, d^E_t )

Three subset relations: representable dimension d^E ⊆ d; composition law C_s^E ⊆ C_s; state is a projection S^E_t = π_E(S_t). The environment also has time: T_comb^E = T_comb|_E, plus boundary input u_t. The environment itself has no judgment and no self-reference — those belong to the life/observers inside it.

**Life**: also a sub-slice of the universe; at a frozen instant it has the same form as the environment; the difference lies only in time — life can maintain itself. Four conditions:

1. Being kept: the trajectory stays in the feasible region V, and the composition law is always defined;
2. Open boundary: exchange with the environment (energy, matter, information);
3. Self-referential regulation: some slices take their own state as input and correct themselves;
4. Plasticity: change its own parameters and structure within the fixed core Φ.

A sub-slice without 3 and 4 is the environment. A direct consequence: **at a frozen instant life cannot be distinguished; life must be recognized over time** — life = a trajectory that is kept, not a state.

## 4. Structure: The Compression Scheme

Structure is decomposition D plus composition law C. It is at the same time a compression scheme:

- which distinctions are kept (written into slice dimensions and composition law);
- which distinctions are merged (coarse-grained away);
- which past inputs are pressed into structure (memory, consolidation).

Life is selected by the environment, and what is selected is exactly this scheme: compressions that can keep themselves survive, those that cannot are eliminated. So "the compression of life" is not one function but "the functions left after the environment has sifted a family", written in structure.

## 5. Compression and Decompression

Compression is a dimension-reducing map: f: X → Y, dim(Y) < dim(X). Decompression unfolds from a compressed representation: g: Y → X' (X' need not equal X).

The two directions correspond to two activities: perception/learning = compression (many-to-one, lossy); prediction/action/generation = decompression (one-to-many, not unique).

Key: decompression is not a strict inverse; it only needs to be "good enough for maintenance". Which dimensions must be reversible is decided by environmental selection. A person needs to decompress the fact "there is a discount" (otherwise the decision is wrong), but does not need to decompress every detail of the day's light.

## 6. The Life Function: Narrow-In, Wide-Out and Surroundings

One step of the life function can be written: input in_t → structure (compression scheme + memory) → output out_t.

The two directions are asymmetric:

- Input: f_in: U → S. Dimension limited by itself, and already coarse-grained — input is always "compressed, limited";
- Output: f_out: S → A. Dimension can be far larger than input (association, language, imagination); the extra dimensions come from structure (past compression).

So: **the life function is narrow-in, wide-out.**

An individual is a compression map π_L: U → S_L; the individual's surroundings = π_L(E), the projection of the environment under its compression. What it can distinguish are the kept dimensions; what it cannot distinguish are coarse-grained.

## 7. Time: One-Step Mapping and Closed Loop

Input and output are not at the same instant; they alternate step by step:

　　step t: (s_t, in_t) → (s_{t+1}, out_t)
　　out_t acts on the world → in_{t+1} = W(out_t, world)

Three consequences:

1. Dimensions unfold along time: one step's input is small, output unfolds step by step over time (association takes time);
2. Output changes input in turn (closed loop): life sees "the world after my own action";
3. Structure has two time scales: state changes fast, structure changes slowly (plasticity).

## 8. Comparison: The Life Function and Large Models

A large model is a "semi-finished" life function: it obtains the public compression scheme, but has no feeling end, no closed loop, no maintenance.

| | Human brain | Large model |
|---|---|---|
| Slice | heterogeneous, low-dimensional but efficient | homogeneous, high-dimensional |
| Spatial composition | variable (routing/projection) | fixed chain |
| Temporal composition | operator sequence (mixed k=0 and k≥1) | k=1, m=1 (no iteration) |
| Judgment | has J (choose/stop/consolidate) | no J |
| Self-reference | three layers active | parameter self-reference only during training |
| Maintenance | body + environment | power + operations |

Conclusion: it looks human at the interface layer (input-output behavior), not at the mechanism layer (how it computes, maintains, changes itself).

Restated in the language of compression: it learned the public compression scheme (language), but has no feeling end (no pre-symbolic compression on the input side), no true closed loop (output continues text only, does not change the environment), no maintenance (weights frozen); its hallucination = decompression of dimensions not covered by structure (decompression detached from reversibility). Chain-of-thought (CoT) externalizes steps into text (externally supplied time); tool calls externalize judgment (external judgment) — precisely because internally k=1 and there is no J, these must be supplied from outside.

## 9. Language: The Public Compression Scheme

Human language occupies a special place in this chain:

- At the individual level: input is feeling (continuous, holistic, pre-symbolic); output is language (discrete, bounded, composable). Feeling → language is compression (categorization, lossy);
- Language is also a decompression tool: world → language is description; language → feeling is understanding; language → language is reasoning;
- So language is "a decompressible compression": details lost in compression, but a recomposable structure retained (words = categories, grammar = composition law, logic = rules of the composition law);
- "Language describes more and more": not that each person remembers more, but that shared structure accumulates (culture, science, writing); the richer the structure, the finer the unfolding of one decompression.

AI learned exactly this public scheme: it can compress/decompress language, so it describes and reasons; but it has no "feeling" end — its output is language recombining language.

## 10. Testable Consequences

1. At a frozen instant life cannot be distinguished: no single-instant check can decide life; one must observe over time (trajectory, repair, exchange).
2. The more stable the environment, the more aggressive compression can be; when the environment changes, old compression criteria fail (dimensions that should be kept are lost).
3. Input coarse-graining plus structure capacity jointly determine the residual floor of output: dimensions absent from structure will be absent from output.
4. When output dimensions exceed structure coverage, "fabrication/hallucination" appears: decompression detached from reversibility.
5. Language description capacity grows with shared structure accumulation: not that individuals become smarter, but that the public compression scheme becomes richer.
6. Judgment and stopping are measurable: a system with a judge should save compute over fixed-step systems and be more robust on thick tasks.

## 11. Limitations

First, R is only declared, not developed: only the P side is written.

Second, compression/decompression are formally written only as "dimension reduction/unfolding", without a strict "good enough" criterion (reversibility requirement depends on the environment, not operationalized).

Third, the closed-loop form (in_{t+1} = W(out_t, world)) is coarse, not handling concrete mechanisms among action, perception, and environment.

Fourth, the feasible region V and the fixed core Φ are not operationalized: judging "whether it is kept" and "what cannot be changed" still lack measurement protocols.

Fifth, the language part and "feeling → language is compression" are conceptual discussions without experiments.

Sixth, this paper is a formal synthesis, not new mathematics.

---

## Labels

- **[Definition]** slice/composition/time operator sequence/judgment/three-layer self-reference/Φ; universe slice, environment sub-slice, four conditions of life; compression/decompression/narrow-in-wide-out/surroundings.
- **[Synthesis]** merges the core of Paper 20 (function types), Paper 26 (functionizable form), Paper 31 (three identities), and Paper 30 (comparison with large models); consistent with the definitions of Papers 00/01, the contraction of Paper 13, and the five-item form of Paper 21 v2.
- **[Consequence]** at a frozen instant life cannot be distinguished — direct from the form.
- **[Conjecture]** "feeling → language is compression", "AI has no feeling end" — conceptual discussions.
- **[Not claimed]** no strict information-theoretic definition of compression is given; no claim to explain consciousness or experience; R is not developed.

> Written by He Qi; DeepSeek (AI) assisted with organization and writing; the views and responsibility belong to the author.


---

## How to cite

Cite the Chinese compendium for the full series:

- He Qi. *Digital Life: A Measurable Definition of Life (Series Compendium)*, v54. Zenodo. https://doi.org/10.5281/zenodo.23639310

Individual Chinese papers (latest versions):

- Paper 0 (introduction, v26): https://doi.org/10.5281/zenodo.23639272
- Paper 1 (rigorous definition): https://doi.org/10.5281/zenodo.23588781
- Paper 21 (the human brain, v3): https://doi.org/10.5281/zenodo.23639261
- Paper 32 (the life function, v2): https://doi.org/10.5281/zenodo.23639251


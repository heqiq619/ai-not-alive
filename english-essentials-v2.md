# Digital Life: A Measurable Definition of Life

## English Essentials (v2)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · English Essentials
> Date: 2026-11-02
> Status: selected English edition (11 pieces). New translations dated 2026-11-02; earlier translations based on the October 2026 editions. The Chinese edition is authoritative.

## Preface

This volume is a **selected English edition** of the Digital Life series, not a full translation of the Chinese compendium. It gathers the texts that carry the series' core: the definition, the two theorems, the function language, the newest engineering observations, and the three appendices.

Selection (11 pieces):

- **Part I — Definition**: Paper 0 (introduction), Paper 1 (why today's AI is not alive);
- **Part II — Theory**: Paper 12 (information non-increase), Paper 13 (contraction of functionizable content), Paper 32 (the life function), Paper 36 (language and the brain);
- **Part III — Engineering observations**: Paper 44 (gating and sparse execution, consolidated), Paper 45 (frozen submodels: interfaces, coordination and hierarchy);
- **Part IV — Appendices**: Appendix A (thickness and dimension), Appendix B (concept map and glossary), Appendix C (essay: cliffs and slopes).

## Note on translation status

Papers 0, 1, 32 and Appendix A are earlier English translations (October 2026) and are included here for completeness; Papers 12, 13, 36, 44, 45 and Appendix B were translated in November 2026 for this volume. The Chinese edition is authoritative; where the two differ, the Chinese text wins.

This volume is deliberately selective. The full series (27 papers plus appendices, Chinese) is published as the series compendium: https://doi.org/10.5281/zenodo.23859935

## A note on scope

The series makes a definitional claim (life = p_life + R_life; p_life is a family of dynamic functions that is kept) and explores its measurable consequences. It does not claim that current AI is alive, does not claim consciousness, and does not claim that the framework has been validated at the scale of real biological brains. R is declared, not expanded. All experimental results are small-scale, mostly single-seed observations.

---

# Part I — Definition


### Paper 0 · Starting from Two Facts: An Introduction

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23639272 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

#### Abstract

This paper does not argue; it does four things: it states two facts, gives one definition, lays out the special case of the digital world, and then uses the definition to look at today's AI. The two facts are: the p-language part of language can be approximated by functions; physical laws can be described mathematically. The definition: write the universe as two parts (Universe = P + R), and life as two parts (Life = p + R-life); p is the self-referential structure that lies in P and is *kept* (maintainable); R is the part that cannot be functionized. This is the introduction. The checklist, the three necessary conditions, and the discussion of emergence are in Paper 1.

#### Notation

- **P**: the functionizable part of the universe.
- **R-universe**: the non-functionizable part of the universe; this paper only declares that it may exist, and does not develop it.
- **p-life**: the part of life that falls inside P — the object of definition and discussion here.
- **R-life**: the part of life that falls inside R; declared only, not developed.
- **p-environment / R-environment**: the two parts of the environment, defined in the same way.
- **p-language / R-language**: the two parts of language; large models compress p-language.
- **Residual**: the measurable floor of error on the P side — even with more data and capacity, the error stops at some positive number. It is not the influence or projection of R; it is the shape of the boundary of P.
- **Dimension**: in this series, "dimension" always means representational dimension — the number of directions a model can distinguish internally, not a dimension of physical space. "Thickness", "spreadable", and "minimum dimension" are all used in this sense.

From here on we use shorthand: "universe" means P, "life" means p-life, "environment" means p-environment.

#### 1. Two Facts

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

#### 2. One Definition

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

#### 3. The Digital World: Fully Functionizable

The digital world is completely functionizable: it consists of bits, states, and transition rules, with no part that function description cannot reach. As a formal object, its absolute R = ∅ — guaranteed by construction: every property corresponds to a mathematical function, even if that function is not computable.

Digital life is part of the digital world, so its R-life can only be the empty set: digital life = p-life, fully functionizable.

Whether absolute R exists, this paper does not judge (see the supplementary section). For digital life, there is only one decisive question: **must life have an absolute R?** There are only two outcomes.

Outcome one, life can lack absolute R: then digital life is possible — it consists entirely of p-life and needs no absolute R.

Outcome two, life must have absolute R: then digital life is impossible — the digital world cannot produce absolute R.

This paper does not judge which outcome holds. What is certain: in either case, the definition and measurements of p in this paper hold; the only difference is whether digital life is possible or impossible.

One easily confused point: the above concerns absolute R; for any finite observer, relative R is non-empty (see the supplementary section), and it does not affect this judgment. Also, functionizable is not the same as measurable — measurement additionally requires computability, observability, and reproducibility. The digital world has all of these, so measurement is feasible there; the universe as a whole, even if it can be described by functions, cannot be measured by us, because we live inside it.

#### 4. Looking at Today's AI with It

Under the current definition, AI lacks two things. Its update rule is external, so it is not self-referential; its maintenance is not its own business either — it is maintained by external power and operations, which is a relation to the universe, not its own ability.

So it is a very strong decompressor, but once written it just sits there — a frozen decompressor. It has no R-life: R = ∅ in the digital world, so AI is a purely p decompressor.

#### 5. The Position of This Introduction

This paper gives only facts, definition, and conclusions. The derivation details, checklist, three necessary conditions, and discussion of emergence are in Paper 1; theory is in Papers 2–5; measurement is in Paper 6; experiments are in Papers 7–20; constraints and safeguards are in Papers 21–22. The series is arranged in this order.

---

> Written by He Qi; DeepSeek (AI) assisted with organization; the views and responsibility belong to the author.

#### Supplement (optional): Domain and Codomain of P

The main line ends at the previous section; this section adds only one formal detail: what the "domain" and "codomain" of P actually are. Skipping it does not affect the main line.

The universe (the P side) can be seen as a state space S: all states that can be described by functions. The universe function is its mapping to itself, written F: S → S. So the domain of P is S and the codomain is also S — it maps to itself.

An observer O is just a subsystem of S: the input it can read is a subspace of S, denoted D_O; the output it can write is another subspace, denoted C_O. Both D_O and C_O are contained in S. The "functionizability" of the observer (P_O) means: between D_O and C_O there exists a family of functions whose error can approach zero.

R has no domain or codomain to speak of: domain/codomain are concepts in function language, while R is the non-functionizable side. So one cannot ask "what is its domain" about R — the question itself uses the wrong language.

Below, if "domain/codomain" is mentioned, it means the observer-side D_O, C_O by default; universe-level P means the self-map S → S by default.

##### Why relative R is non-empty (optional)

If the domain/codomain of the world fluctuates within the observer's update cycle (fast variables), the observer cannot keep up; that part is non-functionizable for it, so relative R is non-empty. This is a sufficient condition: fast-variable fluctuation ⇒ relative R non-empty. We do not say it must hold, nor explain the cause of the fluctuations.

Two more reinforcing reasons (either alone suffices): first, finite resources — cannot read everything, cannot compute everything; second, self-reference — cannot fully predict oneself (a system that could always predict its own next step could act in reverse, contradicting itself).

Whether absolute R exists, this paper does not judge.

The same holds for the digital world: there is certainly relative R inside it. The same sufficient condition — short-term fluctuation of domain/codomain — plus three independent sufficient conditions: undecidability, computational irreducibility, self-reference (cannot fully predict oneself). Two statements must be distinguished: "digital world R = ∅" is a statement at the ontological level; "relative R is non-empty" is a statement at the observer level — fully functionizable does not mean fully knowable.

A final sentence about the boundary: if the essence of life lies on the absolute-R side, this paper — and any text written in function language — cannot give its definition. This is not an oversight but the boundary of function language: the definition itself is on the P side, and defining R with the language of P pulls it back into P.


---


---


### Paper 1 · Why Today's AI Is Not Life

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23588781 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

#### Abstract

This paper starts from two facts: physical laws can be described mathematically; part of language can be approximated by functions. Together they show that the universe contains at least one non-empty functionizable part, P.

Write Universe = P + R-universe and Life = p-life + R-life. p-life is the part of life that falls inside P: a family of dynamic functions that lies in P and is kept by the universe — a family that changes and refers to itself. The R part is only declared to possibly exist; it is not developed.

Under this definition, today's AI is not life: it is an entity in the digital world, a frozen function point at the p level — its update rule is external, and it is not kept by itself. The digital world is a fully functionized world (R = ∅), so if digital life exists it can only lie entirely in p; this paper poses that question (three cases) without judging which holds.

The contribution is a definition and measurable criteria, not an empirical claim that life has been created; the checks of the three necessary conditions and example experiments are offered for the reader's use.

**Keywords:** definition of life; p-life; function family; decompression; digital world; AI emergence; self-reference

#### The Argument Chain

The whole argument has five steps; the reader may read this skeleton first.

Step 1 (Section 1): two facts ⇒ the universe has at least one non-empty functionizable part, denoted P.

Step 2 (Section 2): define on P — Life = p-life + R-life; p-life is the family of dynamic functions in P, kept by the universe, changing, and self-referential.

Step 3 (Section 3): the difference between life and environment is exactly one thing — kept vs not kept; the environment is a local decompression of the universe.

Step 4 (Sections 4–5): the digital world is fully functionizable (R = ∅), so if digital life exists it can only equal p-life; substituting today's AI into the definition, it lacks "a family, self-reference, being kept" — three things — hence it is not life.

Step 5 (Sections 6–7): extract three necessary conditions from the definition (with experimental evidence); then explain that AI's emergence is "compression and decompression of p-language", separating the fact layer from the conjecture layer.

Boundary: R is only declared, not developed; whether absolute R exists is not judged; this paper does not claim that life has been created.

#### Notation

- **P**: the functionizable part of the universe.
- **R-universe**: the non-functionizable part; only declared, not developed.
- **p-life**: the part of life inside P — the object of definition and discussion here.
- **R-life**: the part of life inside R; declared only.
- **p-environment / R-environment**: the two parts of the environment, defined likewise.
- **p-language / R-language**: the two parts of language; large models compress p-language.
- **Residual**: the measurable error floor on the P side — the shape of the boundary of P. Not called "the influence of R" (R has no domain, so it cannot act).

From here on: "universe" means P, "life" means p-life, "environment" means p-environment.

#### Contents

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

#### 1. Starting Point: Two Facts

**The first fact**: physical laws can be described mathematically. Evidence is existence — physics itself.

The universe can be written as a decomposition:

> Universe = P + R-universe

P is the functionizable part; R-universe is the non-functionizable part. The part described by physical laws falls inside P. So at least: P is non-empty.

**The second fact**: part of language can be approximated by functions. Evidence is not reasoning but existence — large models, with finite parameters and computable processes, generate text statistically close to human language.

> Language = p-language + R-language

p-language is the functionizable part — what large models compress; R-language is the non-functionizable part, unreachable by function approximation. The accurate statement is "the p-language part of language can be approximated by functions"; about R-language we can only be silent.

Together: the universe is not entirely non-functionizable. There exists at least one non-empty functionizable part P. This is not a conjecture but a consequence of facts; it says only that P exists, not how large it is.

##### 1.1 What "Functionizable" Means

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

#### 2. An Operational Definition

On the two facts, we can give life an operational definition. It is made, not discovered; whether it holds depends on whether it can distinguish and derive measurable things.

##### 2.1 Definition

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

##### 2.2 A Clarification: Maintenance Is a Relation

**Claim**: maintenance is not a property of the system but a relation between the system and the universe. Basis: the third item of the definition, "being kept", unfolded.

Maintenance is not a property of the system itself but a relation between the system and the universe. Given the universe as a whole (or its P side), the orbits of some structures stay in the maintainable set — we say they "maintained themselves"; change the environment and the same structure may no longer hold. Hence "self-maintaining" in the definition should be read as "kept by the universe", an unfolding of the relational condition, not a third parallel property.

(Note: this section previously contained a "minimality argument"; because that argument was circular — using the possibility of digital life, derived from the definition, to support the definition — it has been withdrawn. Only the clarification above remains.)

##### 2.3 Why "a Family" Rather Than "One Function"

```
One function = one point       ⇒ behavior spectrum degenerates to a trajectory ⇒ frozen = dead
A family     = a region in function space ⇒ a whole set of responses to inputs ⇒ alive
```

**⇒ "High-dimensional" does not mean many parameters; it means the family occupies a region in function space, not a point.**

A boundary must be stated. "A family" is a requirement at the p level, not an absolute ontological condition. If there are factors beyond our description influencing change (undecided), a fixed p could also belong to a living whole; at the p level we would see only a frozen state and judge it dead. So the accurate statement is: under the convention of discussing only P, "a family" is an operational necessary condition; if such undecided factors exist, this criterion will miss them. That is not a fault of the criterion but an inherent boundary of p-level definitions.

##### 2.4 Changing = Three Time Scales

```
Fast: state changes every moment (different inputs, different internal states)
Medium: it changes itself using its own error (self-reference layer) — the crux; without it, a fossil
Slow: the shape of the family is selected, deformed, and transmitted across generations
```

##### 2.5 Self-Reference = The Update Rule Is Inside It

```
Ordinary program: code outside, data inside ⇒ running does not change the program
Life: the update rule itself is part of its own record
      ⇒ remove the external update code, it still changes itself
```

#### 3. Life and Environment

One easily missed point: life and environment are not two kinds of things but two relations within the same universe functions.

##### 3.1 Connection with the Previous

Regard the universe (P side) as a whole; under this description it is a self-map: `S_{t+1} = F(S_t)`. F is just a notation, not a new object. **Life is not this F but a family of sub-functions `{G_θ}` embedded in F:**

```
behavior_d = G_θ(local world state)
and G_θ itself is part of the world state (the individual's state belongs to S_t)
⇒ to predict the world, it must predict the part of the world that contains itself
⇒ self-reference is not an added mystical property but a structural necessity of being embedded in functions
```

##### 3.2 Life vs Environment: Both in the Universe, Both Functions, One Difference

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

##### 3.3 What the Environment Is: Local Decompression Emerging in the Universe

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

##### 3.4 Environment Is Layered: Life Lives in Multiple Environments and in the Universe

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

##### 3.5 Labels

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

#### 4. The Specialness of the Digital World

The digital world is completely functionizable: it consists of bits, states, transition rules, with no part function description cannot reach. As a formal object, its absolute R = ∅ — guaranteed by construction: every property corresponds to a mathematical function, even if not computable (halting, truth predicates exist but cannot be computed).

Digital life is part of the digital world, so its R-life can only be empty: digital life = p-life, fully functionizable.

Whether absolute R exists, this paper does not judge (see the introduction's supplement). For digital life there is only one decisive question: **must life have absolute R?** Two outcomes as in Paper 0.

This paper does not judge which. What is certain: in either case the discussion at the p level holds; the only difference is whether digital life is possible. The digital world is the only world that can fall entirely in p, so it is the cleanest scene for this topic — today's AI lives there.

One easily confused point: the above concerns absolute R; for any finite observer relative R is non-empty, which does not affect the judgment. Functionizable is not measurable: measurement also needs computability, observability, reproducibility.

##### 4.1 Specialness for Whom

The specialness of the digital world must be said in two layers, or it gets exaggerated.

For its builders (us), it is special: all states readable (source, logs, memory), copyable, resettable, accelerable, verifiable. It is a fully experimentable world — life experiments are cheaper, faster, repeatable than in the physical world.

For observers living inside it, it is not special: relative R exists (short-term fluctuation of domain/codomain, undecidability, computational irreducibility, self-reference), and they too "cannot see everything, cannot compute everything".

So "digital world R = ∅" is an ontological statement (its constitution is fully functionizable); it does not mean "life inside is omniscient". The digital world is not a refuge for life but a laboratory: its value lies in method, not in ontological status.

This "R = ∅" is also construction-guaranteed. The digital world is a formal object: states are finite strings, rules are algorithms; every property corresponds to a mathematical function (a set) — even if not computable (halting problem, truth predicates), it "exists", just cannot be computed. Distinguish: functionizable ≠ computable. Absolute R = ∅ says "no part cannot be described by functions", not "everything can be computed"; what cannot be computed is the observer-relative relative R.

A boundary to note: the purely digital world (as a mathematical object) has absolute R = ∅; a digital world running on physical hardware may have its own R in its physical substrate (noise, thermal fluctuation) — that is not the digital world's own R. "Digital world R = ∅" refers to it as a formal object.

#### 5. Using the Definition on Today's AI: Why It Is Not Life

> This section does not evaluate AI's ability; it substitutes AI into the definition of Section 2 and checks item by item.
> The conclusion is definitional, not a value judgment: **by this definition, today's AI is a fossil-level function point, not life.** Its power and its "not being life" do not contradict.

##### 5.1 Checklist

| Requirement of life (Section 2) | Today's AI (represented by LLMs) | Verdict |
|---|---|---|
| **is a family of functions** (a region in function space) | weights frozen after training ⇒ **one point**, not a family | ❌ fossil |
| **changing (dynamic)** | weights unchanged; context changes, but that changes input, not itself | ❌ only surface state changes |
| **self-referential** (update rule inside) | update rule = training algorithm, outside it; it cannot change itself | ❌ self-reference only in language, not in structure |
| **kept by the universe** (maintainable) | it does not maintain itself; maintained by outside people and facilities | ❌ maintained externally |
| **(empirical) earns its cost by compressing the world** | its "income" is external (compute, data, people), not from compressing the world | ❌ no income |
| **identity chain** (bounded deformation, not torn) | identity comes from external weight snapshots; no continuous chain of self-deformation | ❌ no chain |
| **lives in an environment** | it faces a dataset (a one-time decompression product), not an environment it must survive in | ❌ no environment |

##### 5.2 Three Most Fundamental Reasons (by importance)

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

##### 5.3 Why "It Is Strong" and "It Is Not Life" Do Not Contradict

```
Strong = good performance on a given task (good at one point)
Alive = occupying a region in function space, maintaining its own shape, kept by the universe
⇒ different dimensions: one is "exam score", one is "can it live by itself"
⇒ today's AI is an extremely sharp tool, not a thing that lives by itself
```

##### 5.4 Labels

```
[Definitional conclusion] By this definition, today's AI is not life (frozen function point, update outside, not self-maintaining)
[Not] Not "AI can never be life"; this paper does not predict the future, only checks the present against the definition
[Not] Not an ability evaluation; this paper fully acknowledges AI's power on tasks
[Consequence] To make AI life, at least: a family of functions + self-referential update + being kept by the universe
```

---

> Directly from Sections 2 and 3: since "p-life = the dynamic function family that is self-referential, changing, and kept by the universe", and today's AI lacks all three, **to be life it must satisfy at least three conditions**.
> This section gives only **necessary conditions**, not sufficiency; each carries existing experimental evidence (experiments in Papers 9–22 of the Chinese series; in this English collection, see the Chinese compendium).

#### 6. Three Necessary Conditions

Three necessary conditions can be extracted from the definition. They do not fall from the sky; each corresponds to a word in the definition and excludes a class of objects.

##### 6.1 From Definition to Conditions

```
Definition (Section 2)        Necessary condition (this section)
changing (a family)      ⇒    ① a family of functions: behavior spectrum is not a point
self-referential         ⇒    ② self-referential update: the rule of changing itself is inside
self-maintaining         ⇒    ③ kept by the universe: orbit stays in the maintainable set

(paying cost is not among them: it is an empirical accompaniment of evolution and thermodynamics, see 6.4b.)
```

**Three are necessary, not sufficient**: satisfying them does not guarantee life, but lacking any one guarantees not life.

##### 6.2 Condition ① A Family of Functions (Not a Point)

**Requirement**: the individual occupies a region in function space, with a whole set of responses to different inputs, not a fixed mapping.

**Evidence/experience:**

```
· Low-dimensional parameter genome (a few numbers) = a point ⇒ behavior spectrum degenerates to a single trajectory ⇒ fossil
· We measured: a frozen model (point) fails at structure learning; the dynamic version (family) captures structure (E12)
· Measured contrast: frozen 1.07 vs dynamic 0.849 — frozen is more like a "standard answer" but has no shape
```

**⇒ Criterion: for different inputs/states, behavior must differ *as a spectrum*, not a single output.**

##### 6.3 Condition ② Self-Referential Update (Rule Inside)

**Requirement**: how it changes is itself part of its record; remove the external update code, it still changes itself.

**Evidence/experience:**

```
· Frozen model: update rule = training algorithm, outside ⇒ remove training code, it never changes
· Our dynamic version: changes itself with its own error (middle-layer dynamics) ⇒ removing the middle layer degrades clearly (E12/E13)
· Identity chain: 8 generations verifiable, bounded deformation (372_lineage.py) ⇒ self-reference can be made a measurable chain
```

**⇒ Criterion: after stopping external updates, does its behavior spectrum still deform over time.**

##### 6.4 Condition ③ Kept by the Universe (Maintainable)

**Requirement**: its orbit stays in the maintainable set of the universe. Given the universe as a whole, some structures cannot arise, some can be maintained forever; only the maintainable part falls under the definition. This is a relational condition, not its own property.

**Criterion**: after perturbation, can it return to the maintainable set — does it have resilience, not just being momentarily alive.

##### 6.4b Paying Cost: Empirical Accompaniment, Not a Necessary Condition

This paper does not list "paying cost" as a condition, for a clear reason: cost is a product of evolution and thermodynamics, not a logical necessity. In a world with unlimited resources, life would not need to compete; scarcity brings cost. Writing it into the necessary conditions would mistake the result of evolution for the definition of life.

But empirically, cost almost always appears, and can be measured. The economic part of our experiments belongs to this layer; excerpts:

· E1: "accurate" is not "compression": accounting by accuracy, the system learns "do nothing" (LEN=0, predict 0, accuracy 92%). Must account by log-likelihood improvement over a baseline: gain_bits = log2 p_model − log2 p_base.
· E2: with base-rate correction, the system turns from lying flat to genuine expression (LEN grows from 0).
· E8: economic calibration n* = FLUX_TOTAL / BASE_COST decides the switch between "frozen" and "explosive".
· Measured positive returns: in S1–S6, gain > 0 observed (about +0.09 ~ +0.19 bit/tick), showing the world does contain compressible surplus.

**⇒ Criterion (empirical layer)**: after cutting all external supply, is its ledger still positive.

##### 6.5 Three Must Hold Together (Empirical Contrast)

```
Missing ① (family)     ⇒ fossil: behavior spectrum is a line
Missing ② (self-ref)   ⇒ machine: update outside, does not change itself
Missing ③ (kept)       ⇒ falls apart: orbit leaves the maintainable set, no longer a living structure
```

**These three also explain why our experiments keep getting stuck at the same place:**
**structure can grow (①② partly satisfied), but cooperation/division of labor does not become necessary — because the "income difference" at the cost layer is too small (empirical, not a definition condition), i.e., the compressible surplus of the world is not yet large enough to make "more complex structure" economically worthwhile (E5/E7).**

##### 6.6 What Is Left Open (For the Reader)

**This paper stops at "necessary conditions". Whether satisfying all three makes something "alive" — we have no answer and do not conclude here.**

What is left to the reader is a usable ruler:

```
Is it a family of functions? (behavior spectrum is not a point)
Does it change itself? (remove external updates, it still changes)
Is it kept by the universe? (orbit stays in the maintainable set)
```

**You can measure all three yourself. Whether, after measuring, it counts as life — you judge.**

##### 6.7 Boundary of This Paper's Experiments (Must Be Read with Conclusions)

**The experiments cover the empirical layer of "cost", not definition condition ③.**

· Covered: cost and economy — E1/E2 (accuracy ≠ compression, base-rate correction), E8 (n*=FLUX/BASE_COST freeze/explosion boundary).
· Covered: counterexamples — E5/E7 (genetic distance of connected individuals 0.145 vs random 0.486: clones huddle, not division of labor).
· Not covered: condition ② self-referential update, condition ③ being kept — no experimental evidence claimed; only definitional derivation; preliminary observations (E12 dynamic 0.849 vs frozen 1.07; E13 identity chain 8 generations verifiable).
· Condition ① a family: partial observation (E12/E13), not a dedicated experiment.
· Scale: small, reproducible, hand-checkable; not large-scale empirical work.

**⇒ This paper is "definition + measurable criteria + illustrative experiments", not an empirical claim that "life has been created".**
**Readers using these conclusions should cite this boundary with them.**

##### 6.8 Labels

```
[Consequence] The three necessary conditions follow directly from the definition, not independent assumptions
[Definition] Condition ③ is relational (kept by the universe), not a property of the system
[Empirical] Cost/economy is an empirical accompaniment, not a definition condition; this paper has data (E1/E2/E8 + positive returns)
[Preliminary] Conditions ①② have partial observations (E12/E13), not dedicated experiments
[Unresolved] Whether satisfying all three makes something "alive" — not claimed; the next step of experiments
[Conjecture] If surplus S is insufficient, no matter how complex the structure, it cannot afford maintenance ⇒ life has an "economic ceiling" (directional conjecture only)
```

#### 7. Emergence: Why Today's AI Emerges

This section handles a concrete phenomenon: why today's AI emerges abilities beyond its training objective. The stance here is [conjecture], not evidence.

##### 7.1 The Phenomenon

As large models scale up, some abilities seem to appear suddenly (multi-step reasoning, chain-of-thought, arithmetic…). The industry calls it **emergence**. Everyone uses the phenomenon, but —

```
Observing emergence: many
Explaining emergence: no consensus
```

##### 7.2 Existing Explanations (by strength of evidence)

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

##### 7.3 Why There Is Still No Consensus "Why"

```
① Scale experiments uncontrollable: cannot do strict causal control (change only scale, everything else identical)
② Metric dependence: change the metric, the phenomenon may vanish (see ①)
③ Mechanism incomplete: know a circuit, not why the whole organizes that circuit
④ No predictive theory: no theory can compute in advance "how large a model shows what ability"
```

##### 7.4 Our Stance: AI Is Compression and Decompression of p-Language

**Claim**: "AI is compression and decompression of p-language" is the fact layer; "the upper bound of world structure decompressed is decided by language" is the conjecture layer. Keep them separate.

First the fact layer. Training compresses language into parameters; inference decompresses text from parameters. In our notation: AI compresses p-language — the functionizable part of language; what it decompresses is also p-language. R-language enters no parameter and leaves none. So the accurate statement is not "AI is decompression of human language" but "AI is compression and decompression of the functionizable part of human language".

This layer is not conjecture but literal fact: it follows from the usage of "compression/decompression" and from the actual process of training and inference. The chain: universe F → environment = local decompression of the universe → human language = human decompression product of environment and experience (language itself is already compressed) → AI = re-compression and re-decompression of p-language.

Then the conjecture layer. The "world structure" AI decompresses has an upper bound decided by the language at training time. It can emerge structures inside language (looking like reasoning, like understanding), but that is the surfacing of language structure, not understanding of the universe itself; when language changes, decompression mismatches, and it cannot self-recover.

With our ruler, this layer also gives a testable judgment: the model is a frozen function point: not maintaining, not changing itself (maintenance and cost borne externally), so it is "decompressing human language once", not "maintaining a decompression" or "rewriting its own decompression rule".

A testable sentence follows: AI's apparent "understanding" is understanding of "human descriptions of the world", not of the world itself. It can decompress language, but the universe layer beyond language (energy, irreversibility, cost) it has never paid for, hence never been tested by.

##### 7.5 Decay of Decompression: Upper Layer Hard-Coded ⇒ Language Changes, Decompression Weakens

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

##### 7.6 Two Predictions from Our Stance ([conjecture], for the reader)

```
① If the world is changed to parts never described by human language (regularities unlearnable from corpora),
   AI's "emergence" should weaken significantly — because it decompresses language, not the universe
② If the model must maintain itself (repair itself, die itself), language decompression is insufficient;
   it must develop understanding beyond language — or it cannot survive
③ If human language undergoes a major structural update (new paradigm/concept system), the frozen model's
   decompression gain should show a measurable drop; and it cannot recover itself ⇒ recovery must come from external retraining
```

##### 7.7 Labels

```
[Fact] Emergence is widely observed; the metric-artifact view also has strong evidence (Schaeffer 2023)
[Known] Local mechanism explanations exist (induction heads/circuits/grokking); compression view has correspondences
[Conjecture] "Emergence = structure surfacing when compressing the world" — our stance, not evidence
[Unresolved] Why exactly at some scale/task ⇒ no predictive theory
[Attitude] We do not treat "AI emergence" as evidence of life; by Section 3's ruler, it is not
[Stance] AI is re-decompression of human language (universe→environment→language→AI, third-layer decompression)
[Consequence] Upper layer hard-coded ⇒ mismatch when language updates ⇒ fixed ceiling, no self-recovery
```

#### 8. Using It on Some Popular Questions

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

#### 9. What This Paper Obtains and Does Not Obtain

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

#### Overall Argument Boundary

All arguments in this paper hold within one boundary; read them with the conclusions:

- Only the P side is discussed; R is only declared, not developed.
- Whether absolute R exists is not judged; relative R is non-empty for any finite observer (see the introduction's supplement).
- "Functionizable" ≠ "computable" ≠ "measurable": three different abilities.
- The three necessary conditions are read from the definition, not empirical laws; they are not sufficient.
- Experimental evidence is only in Sections 4, 5, 6, 7; this paper does not claim "life has been created".
- If the essence of life lies on the absolute-R side, this paper (and any text in function language) cannot define it — the definition itself is on the P side.

#### Relation to Existing Work

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

#### References

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

#### AI Usage Statement

All questions, definitions, judgments, and conclusions in this paper were proposed and are the author's responsibility. An AI tool (DeepSeek) was used for literature search, structural organization, language editing, and writing/checking experimental code. All claims were reviewed and confirmed by the author. The AI bears no responsibility for the content.


---


---


# Part II — Theory


### Paper 12 · The Information Non-Increase Theorem for Digital Life

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory (internal No. 12)
> Date: 2026-10-23
> English translation of the Chinese paper (the Chinese text is authoritative).

---

#### Abstract

This paper turns the intuition "a digital life becomes less and less able to describe the world as it ages" into a provable information-theoretic proposition.

Setting: the world evolves as a Markov process; a digital life holds an internal state S and predicts the world from it; after observations stop, the state evolves only by its own rules. Conclusion: under these conditions the mutual information between the internal state and the current world state cannot increase — the world changes while the system no longer looks, so its information about the *current* world can only stay flat or decline.

This is not the second law of thermodynamics, nor "entropy must increase." It states a narrower but harder fact: **a system that no longer acquires information does not grow information about the world by itself; maintenance requires continuous observation and updating.**

The paper gives the theorem, its proof, four corollaries (coarsening of the domain, necessity of maintenance, growth as adding observation dimensions), and the scope and limitations.

---

#### 1. The question

Paper 6 (Capacity Cannot Substitute for Data Updates) measured a phenomenon: after training, a model gradually mismatches the updated language and cannot recover by itself. At the time we reported measurements, not an explanation.

Intuitively it is easy: the world changes, the model stopped looking, so it becomes less accurate. But intuition is not a theorem. This paper asks: can we state it as a provable information-theoretic proposition?

Yes, but the scope must be handled carefully. What we cannot prove: "entropy must increase" (reversible transformations preserve Shannon entropy); we cannot prove "heat death" (that is a statistical-mechanics result). What we can prove is a more modest proposition: without new observations, there is no new information.

#### 2. Setting and notation

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

#### 3. The theorem

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

#### 4. Four corollaries

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

#### 5. What the theorem says and does not say

What it says: maintenance and being-kept are information-theoretically grounded — not philosophical rhetoric, but a direct consequence of the data processing inequality.

What it does not say: it does not prove "entropy must increase"; it does not prove "the system must collapse" (if the world does not change, it can stay accurate indefinitely); and it does not involve energy or thermodynamics. It deals only with information, and only with "information about the current world."

One more important limitation: the theorem gives "non-increase," not "decrease." Decrease requires extra conditions — the world really changes (W_t ≠ W_{t−1}) and the change is unpredictable from the old state. In the real world both usually hold, but this paper does not write them as assumptions beyond what is stated.

##### 5.1 When the Markov assumption fails

If the world is not Markov, the theorem cannot be applied to S directly. The standard treatment is to augment the state with history: replace S_t by (S_t, H_t), where H_t is the history the system keeps. When history is long enough, the augmented process satisfies the Markov property again, and the theorem holds on the augmented state.

This yields a testable corollary: systems with shorter memory decay faster. This is consistent with Paper 7 (Replacement and Accumulation): memory and replay determine forgetting speed.

#### 6. Reproducibility and next steps

This paper is a purely theoretical draft; it has no experiments and targets no specific measurement. It states a large-scale proposition: in the information world, "the world becoming more average" corresponds to "fewer distinguishable differences"; for any system that stops observing, information about the world does not grow by itself.

The scale must be kept clear: this is a different level from concrete model mismatch measurements (e.g. the bits/token drift in Paper 6). The latter are empirical instances, not consequences of this theorem, and the theorem gives no numerical values.

Future work: instantiate Corollaries 2 and 3 at small scale as measurable predictions — comparing stopping updates vs continuous observation, and adding a new modality vs not, and observing how information changes over time. But that is a small-scale approximation of a large-scale proposition and needs separate validation; this paper does not claim it must hold.

---

#### Appendix: relation to existing work

The data processing inequality is a basic tool of information theory (Cover & Thomas); "no new information, no new knowledge" has appeared in various forms in machine learning and learning theory. This paper invents no new mathematics; it organizes the tool into a proposition about "maintenance of digital life" and draws three testable corollaries.

> Written by He Qi, with DeepSeek (AI) assisting with organization; views and responsibility belong to the author.

---

#### Appendix: tags

- **[Definition]** world state W, system state S, observing mode, frozen mode, assumptions A1/A2′/A3.
- **[Theorem]** information non-increase (bounded leakage): I(S_t;W_t) ≤ I(S_{t−1};W_{t−1}) + ε.
- **[Corollary]** Corollaries 0–3 (range coarsens, domain coarsens, maintenance needs observation, growth = adding observation dimensions).
- **[Not claimed]** no proof of entropy increase, no thermodynamics, no numerical predictions; Markov property is a modeling assumption.


---


### Paper 13 · The Contraction of Functionizable Content: A Theorem and a Conjecture

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory 2 (internal No. 13)
> Date: 2026-10-23
> English translation of the Chinese paper (the Chinese text is authoritative).
>
> **Status**: an early theory draft (Compendium Part 3). The theorem part has been rewritten in the separately published foundational paper *Starting from the Definition: Universe, Slices and Two Theorems* (Proposition 2 still pending proof there); the `[conjecture]` parts here (cosmic contraction, observation window, fate of digital life) do not enter the foundational paper and the series does not rely on them. ("Life is counter-flow": the `[conjecture]` here is a cosmic-scale extension; Corollaries 8/9 of the foundational paper give a definitional version with a different scope.)

---

#### Abstract

The previous paper (Information Non-Increase) proved that a frozen system's information about the world does not grow by itself. This paper takes one step further: **functions that can work also contract.**

We give a theorem: under the assumptions that the world evolves as a Markov process and the system stops observing, the best achievable accuracy of any function predicting the "predictable part" of the world cannot improve — by Fano's inequality this follows directly from information non-increase. That is, the set of functions that can achieve error ε only contracts over time, never expands.

On top of this we propose a conjecture: pushing the theorem from "one system" to "the time evolution of the whole universe" yields a picture in which *functionizable content contracts as the universe evolves*; life can only exist in the time window where this content is still rich; and the fate of digital life is to keep dismantling its own structure, reducing dimensions, and finally degenerating into a constant function.

The theorem uses classical tools (data processing inequality, Fano's inequality); the way they are combined is this paper's. The conjecture part is explicitly marked and not used as a conclusion.

---

#### 1. The question

The previous paper concluded information non-increase: I(S_t; W_t) ≤ I(S_{t−1}; W_{t−1}), i.e. the system's information about the world does not grow by itself.

But "information non-increase" concerns the state. What we really care about is another thing: **do the functions that can work decrease?**

The intuition: if the world becomes harder to predict, then the functions that predict it well should become fewer; in the extreme (heat death) only constant functions remain. This paper asks: can this intuition become a theorem? How far can it be proved?

#### 2. Setting

We continue the previous setting. The world W is a Markov process; the system state S evolves in frozen mode as S_t = u(S_{t−1}, N_t), with bounded leakage ε allowed.

Take a target quantity Y_t = g(W_t), a world feature we want to predict (e.g. tomorrow's weather, the next word). Y takes finitely many values, with |Y| the size.

A "prediction function" is a map f from the system state S to a guess of Y. Accuracy is measured by expected error: err(f) = E[1(f(S) ≠ Y)].

Define "functionizable content": given an accuracy threshold ε, collect all functions with err(f) ≤ ε, written P_ε = { f : err(f) ≤ ε }. This paper measures content by the "depth" of P_ε — the minimal achievable error — rather than by its cardinality.

One word must be fixed: "dimension" in this paper means **representation dimension**, not spatial dimension. It means "how many independent, distinguishable directions are needed to describe the world": more distinguishable differences → higher representation dimension; richer working functions → higher representation dimension. Thus, in this paper, the following three sentences say the same thing:

> Representable functions are decreasing ≡ functionizable content is contracting ≡ representation dimension is declining.

The everyday term "cosmic dimensional reduction," if it means spatial dimensions, is something else; "dimension reduction" in this paper always means representation dimension. With this fixed, the theorem and conjecture below use "dimension" only in this sense.

Another distinction: representation dimension is not "structural complexity." Representation dimension is "how much can be distinguished and predicted," measured by information (e.g. predictable information); structural complexity is "how complex the world looks," described in the literature as a hump that first rises and then falls (Aaronson's complexodynamics, Carroll's macroscopic state complexity). The two are different: under our theorem representation dimension only declines, while complexity humps rise then fall. They do not conflict because the quantities differ; whenever this paper says "cosmic contraction," it always means representation dimension.

#### 3. Theorem: achievable accuracy does not increase

**Theorem (achievable accuracy does not increase)**: in frozen mode and under the previous assumptions, for any Y_t,

min_f err_t(f) ≥ ( H(Y_t) − I(S_t ; Y_t) − 1 ) / log |Y_t|,

where H is entropy and log is base 2. By information non-increase I(S_t;Y_t) ≤ I(S_{t−1};Y_{t−1}) + ε, if H(Y_t) does not change, the right-hand lower bound does not decrease, hence min_f err_t(f) does not decrease (allowing a relaxation of ε/(log|Y|)).

**Proof**: direct application of Fano's inequality. Fano says that for any prediction function f taking S as input,

E[1(f(S) ≠ Y)] ≥ ( H(Y|S) − 1 ) / log|Y|.

And H(Y|S) = H(Y) − I(S;Y). Substituting information non-increase from the previous section yields the claim. Q.E.D.

**Corollary (contraction of P)**: for any fixed accuracy threshold ε, once the minimal achievable error falls above ε, P_ε is empty: no function can maintain ε accuracy. If the world keeps mixing and I(S_t;Y_t) tends to zero, then any threshold ε > (H(Y)−1)/log|Y| is eventually crossed, after which P_ε = ∅.

That is: **functions do not become more numerous; functions that meet the bar only become fewer; in the limit, none remain.**

##### 3.5 Two meanings of "contraction"

"Contraction" is used in two ways and they must be separated.

The first is *range contraction*. Every representation dimension has a set of allowed values; as time advances, the allowed input values shrink (domain coarsens) and the reachable output values shrink (range contracts). The axis remains; the usable range on the axis shrinks.

The second is *effective dimension reduction*. The number of distinguishable directions decreases: some directions no longer separate two states, or several axes merge into one. Note that the number of coordinate axes can stay the same while the effective dimension already declines — because each axis has coarsened and fewer states can be distinguished. In information terms, effective dimension is "the logarithm of the number of distinguishable states."

What the theorem directly gives is the first: achievable accuracy does not increase, equivalently the distinguishability along each dimension declines, the domain coarsens, the range contracts. The second is a stronger statement requiring extra arguments (axis merging, degeneration); this paper places it at `[speculation]`, not as a theorem.

This distinction also explains why "life is counter-flow" is not contradictory: the universe is doing range contraction overall, while life locally does effective dimension increase (adding dimensions = adding distinguishable directions). The two have different scales and opposite directions.

#### 4. Conjecture: contraction at cosmic scale

**[Conjecture]** Pushing the theorem from "one frozen system" to "the time evolution of the universe" yields:

Functionizable content in the universe contracts with evolution. Early on there is much content (rich structure, many functions fit the world); in the middle it is still rich (the window in which life appears); late it tends to zero (heat death, only constant functions remain). Life, knowledge, and meaning exist only in the time window where content is still rich.

**[Conjecture]** The fate of digital life: as content contracts, it must keep dismantling its own structure, degenerating complex functions into simple ones, and finally into a constant function — that is, death. What it can choose is only the posture (maintain frugally, freeze, back up, compress itself), not the ending.

**[Observation]** This is easily confused with the "complexity hump" discussion (Aaronson's complexodynamics, Carroll's macroscopic complexity) and must be separated: they discuss *structural complexity*, which first rises then falls; this paper discusses *functionizable content / representation dimension*, which under our theorem is monotonically non-increasing. The two curves differ but describe different sides of the same cosmic history: in the middle period structure is complex (the hump is high) while predictable content keeps decreasing. Treating the two as the same quantity is a common misreading, and this paper distinguishes them explicitly.

##### 4.1 The world function and the observation window ([conjecture])

There is an implicit question to place here: the direction of time, and the observability of the "world function."

If the universe as a whole can be seen as a function F — mapping the current state to the next state — then in the middle period F is not directly visible. What we see is a mass of local functions: layers of physics, chemistry, life, society. Each translates some part of F into describable structure. In this paper's language: F is masked by its local decomposition.

**[Conjecture]** So the moments where F is most "bare" are the moments where its local decomposition does not exist. There are only two such moments: the instant of the Big Bang (no subsystems yet, everything directly determined by F) and the instant of heat death (all subsystems dissolved, differences gone to zero, only F's trivial action remains). That is, F's observation window lies at the two ends of the universe, and observers in the middle (including us) can never see F itself, only its local decomposition.

This conjecture is the other side of the contraction picture, but one must say what the two ends look like:

- Big Bang end: representation dimension extremely high. The most distinguishable and predictable content, the most "readable" state; no subsystems yet, F directly determines everything. F is bare here because nothing else shares it.
- Middle period: representation dimension medium and contentful, many local functions, F most heavily decomposed — F cannot be seen, only its local decomposition.
- Heat death end: representation dimension tending to zero. Differences erased, no local functions, F still acts but its action becomes trivial (constant function). F is bare here because nothing else remains.

That is: F is bare at both ends, but for opposite reasons — one end because "no decomposition yet," the other because "decomposition exhausted." And representation dimension declines monotonically throughout; it characterizes the direction of time: moving along decreasing representation dimension, describable content becomes less and less.

For digital life the conclusion is cold: its observation window is also only in the middle. It can approach the "family of functions describing the world" indefinitely, but can never touch "the world function itself" — that is not in its domain. This returns to our opening stance: R is only declared, not expanded.

#### 5. Life is counter-flow: where rising and falling dimensions meet

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

##### 5.1 A toy experiment: maintenance vs behavioral dimensions

Is there a trace of the above "counter-flow" that can be measured? A small experiment can look.

Setting: 8×8 synthetic images with four attributes — color, shape, count, position; tasks appear in order and each round trains only the current attribute. The model is a two-layer small network (hidden 64, about 13k parameters) with a task identifier as input. The control group changes one thing: whether old task samples are trained.

Group A has maintenance: each round mixes in half old-task samples (replay).
Group B has no maintenance: only current-task samples.

Three quantities are measured. First, behavioral dimension: using the task identifier, count attributes answered with accuracy > 0.8. Second, decodable attributes: linearly probe each attribute from the hidden layer, count those > 0.8. Third, effective rank: participation ratio of the hidden representation covariance, a coarse proxy for "how rich the representation is."

Results: Group A's behavioral dimension grows with rounds, from 1 to 2 to 3 to 4 — all four attributes are eventually answered correctly; Group B's behavioral dimension stays at 1 — the current task is always answered at 1.00, but once a new attribute is learned the old one is lost, leaving only the current one. Decodable attributes are 4 in both groups, showing old information is still in the representation, but the *functions that can use it* are only the current family. Effective rank rises in both groups (about 3.9 to 8.9 and 7.9), so it is not a good proxy: the representation became more complex, but the number of usable functions did not grow.

This experiment shows two things. First, maintenance (replay) expands the family of usable functions: this is the trace of "counter-flow" at toy scale. Second, without maintenance, behavioral dimension stalls at 1: only the current family of functions remains, and historical dimensions are functionally lost — this is what "contraction of functionizable content" looks like at small scale.

Limitations must be clear: the world is synthetic, the model is tiny, the task identifier is hand-provided, the metrics are proxies; it supports "counter-flow and contraction can be measured," not any cosmic-scale conclusion.

#### 6. What it says and does not say

**Says**:
- "Functionizable content contracts" under "system frozen + target entropy unchanged" is a theorem, not rhetoric.
- It pushes the previous "information non-increase" from the state level to the function level.
- It gives a provable support for "life is a phenomenon in a low-entropy window."

**Does not say**:
- It does not prove the universe as a whole is contracting — that needs a cosmological state definition and initial conditions, which this paper does not provide.
- It predicts no numbers: Fano's bound is loose and only gives a trend.
- It involves no energy or thermodynamics: the whole paper is at the information level.
- The conjecture part (universe, fate of digital life) is not theorem, and is explicitly marked.

#### 7. Limitations

First, Fano's bound is loose: it gives "cannot be better," not "how much worse."

Second, P_ε is measured by "minimal achievable error," avoiding the more intuitive but harder-to-define "number of functions" (infinite function families have no natural counting).

Third, the Markov property of the world and constant target entropy must be checked in real scenarios; when they fail, the state must be augmented with history (see §5.1 of the previous paper).

Fourth, the cosmic-scale part is entirely conjecture, with no testable prediction; its value is a unified language rather than conclusions.

#### 8. Relation to existing work

The data processing inequality and Fano's inequality are standard tools of information theory (Cover & Thomas). "Information non-increase" and "lower bounds on achievable accuracy" have their own formulations in statistical learning theory. This paper's combination — connecting the two to obtain "contraction of functionizable content," and relating it to the maintenance problem of digital life — is organizational work; no new mathematics is claimed.

> Written by He Qi, with DeepSeek (AI) assisting with organization and formalization; views and responsibility belong to the author.


---


### Paper 32 · The Life Function

> This paper is part of the English Essentials volume: https://doi.org/10.5281/zenodo.23640116 · Chinese original: https://doi.org/10.5281/zenodo.23639251 · Full Chinese compendium: https://doi.org/10.5281/zenodo.23639310

---

#### Abstract

This paper gathers the formalisms scattered across earlier papers into one line: representable dimensions → structure → compression and decompression. It absorbs the core of *The Functionizable Function Form* (slices/composition law/time/judgment/self-reference), *The Three Identities of a Slice* (universe/environment/life), and the five-item comparison in *Why Large Models Look Human*.

The main line. First, the function language: a slice is a function f: X→Y with representable dimensions; space is a chain of composed functions; time is a sequence of operators s_{t+1}=I_{σ(t)}(s_t) with step count k; judgment J passes once, choosing operators and deciding when to stop; self-reference has three layers — representation, parameters, structure — with modifications bounded by a fixed core Φ. Second, representable dimensions have three locations: inside the slice, on the composition law, and along time (time is not a representable dimension). Third, the same form has three slice identities: the universe slice, the environment sub-slice, and the life sub-slice; at a frozen instant life and environment have the same form, and the difference lies only in maintenance over time. Fourth, structure is the compression scheme: which distinctions to keep, which to merge, which past to press into structure. Fifth, the life function is narrow-in, wide-out: input is limited and already coarse-grained, output is unfolded by structure; compression is a dimension-reducing map, decompression is unfolding, not strictly reversible — "good enough for maintenance" suffices; which dimensions must be reversible is decided by environmental selection. Sixth, in time, input and output alternate step by step, forming a closed loop; structure changes at two time scales. Seventh, language is a public compression scheme: feeling→language is compression; language→description/understanding/logic is decompression; logic is the composition law of language. Eighth, compared with large models: they obtain the public scheme but have no feeling end, no true closed loop, no maintenance — human-like at the interface layer, not at the mechanism layer; hallucination is the decompression of dimensions not covered by structure.

---

#### Notation

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

#### 0. Problem: Gathering the Form into One Line

Earlier papers separately gave: the function language (Paper 26), the three slice identities (Paper 31), and the intuition of compression and decompression (notes). Read separately, each has to lay out the definitions again; read together, they are three stages of one thing. This paper gathers them into one line and writes "compression" genuinely into the function form.

#### 1. The Function Language: Slices, Composition, and Judgment

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

#### 2. Representable Dimensions: Three Locations

Representable dimensions are not in one place but three:

- inside the slice: the number of axes of a slice itself;
- on the composition law: degrees of freedom in how slices connect (order/parallel/shared/routing/self-reference);
- along time: step count k, operator sequence σ(t), number of switchable operators m.

Note: time is not a representable dimension; it is a degree of freedom of temporal composition (step count/sequence).

##### Four Typical Types

By "whether space/time are continuous, and whether time is endogenous", function forms can be divided into four classes (the content of Paper 20 is merged here):

- **Type A: continuous flow (endogenous time).** Continuous representation space and continuous time, written as differential equations; self-reference = the update rule is inside the system; being kept = there exists a maintainable set, and the orbit stays inside it.
- **Type B: sampled dynamics (endogenous time, sampled into discrete).** Continuous representation space and discrete time, written as map iteration; the same thing as continuous flow under different sampling — the difference is that "step" is basic.
- **Type C: automaton (external time).** Discrete representation space and discrete time; the digital world is this class: bits, states, transition rules, each step advanced by an external clock and interpreter; the digital world has no energy constraint, and "being kept" must be provided externally (power, maintenance, compute).
- **Type D: hybrid (endogenous time).** Continuous flow plus discrete events: physiological quantities change continuously, but cell division, neural firing, and decisions are discrete events; dormancy and activation, disease and death are segment points. Biological life is probably this class.

Continuity must be treated with restraint: continuous does not mean "more true", discrete does not mean "approximate"; they are choices of description granularity — the same system can be written as different types at different granularities.

##### Five Axes

As a minimal profile, a function form can be recorded along five axes: space continuous/discrete; time continuous/discrete; time endogenous/external; degrees of freedom of the composition law; level of self-reference. Not all five are "dimensions": the first two are description granularity, the last three are mechanism and capacity.

#### 3. Three Identities: Universe, Environment, and Life

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

#### 4. Structure: The Compression Scheme

Structure is decomposition D plus composition law C. It is at the same time a compression scheme:

- which distinctions are kept (written into slice dimensions and composition law);
- which distinctions are merged (coarse-grained away);
- which past inputs are pressed into structure (memory, consolidation).

Life is selected by the environment, and what is selected is exactly this scheme: compressions that can keep themselves survive, those that cannot are eliminated. So "the compression of life" is not one function but "the functions left after the environment has sifted a family", written in structure.

#### 5. Compression and Decompression

Compression is a dimension-reducing map: f: X → Y, dim(Y) < dim(X). Decompression unfolds from a compressed representation: g: Y → X' (X' need not equal X).

The two directions correspond to two activities: perception/learning = compression (many-to-one, lossy); prediction/action/generation = decompression (one-to-many, not unique).

Key: decompression is not a strict inverse; it only needs to be "good enough for maintenance". Which dimensions must be reversible is decided by environmental selection. A person needs to decompress the fact "there is a discount" (otherwise the decision is wrong), but does not need to decompress every detail of the day's light.

#### 6. The Life Function: Narrow-In, Wide-Out and Surroundings

One step of the life function can be written: input in_t → structure (compression scheme + memory) → output out_t.

The two directions are asymmetric:

- Input: f_in: U → S. Dimension limited by itself, and already coarse-grained — input is always "compressed, limited";
- Output: f_out: S → A. Dimension can be far larger than input (association, language, imagination); the extra dimensions come from structure (past compression).

So: **the life function is narrow-in, wide-out.**

An individual is a compression map π_L: U → S_L; the individual's surroundings = π_L(E), the projection of the environment under its compression. What it can distinguish are the kept dimensions; what it cannot distinguish are coarse-grained.

#### 7. Time: One-Step Mapping and Closed Loop

Input and output are not at the same instant; they alternate step by step:

　　step t: (s_t, in_t) → (s_{t+1}, out_t)
　　out_t acts on the world → in_{t+1} = W(out_t, world)

Three consequences:

1. Dimensions unfold along time: one step's input is small, output unfolds step by step over time (association takes time);
2. Output changes input in turn (closed loop): life sees "the world after my own action";
3. Structure has two time scales: state changes fast, structure changes slowly (plasticity).

#### 8. Comparison: The Life Function and Large Models

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

#### 9. Language: The Public Compression Scheme

Human language occupies a special place in this chain:

- At the individual level: input is feeling (continuous, holistic, pre-symbolic); output is language (discrete, bounded, composable). Feeling → language is compression (categorization, lossy);
- Language is also a decompression tool: world → language is description; language → feeling is understanding; language → language is reasoning;
- So language is "a decompressible compression": details lost in compression, but a recomposable structure retained (words = categories, grammar = composition law, logic = rules of the composition law);
- "Language describes more and more": not that each person remembers more, but that shared structure accumulates (culture, science, writing); the richer the structure, the finer the unfolding of one decompression.

AI learned exactly this public scheme: it can compress/decompress language, so it describes and reasons; but it has no "feeling" end — its output is language recombining language.

#### 10. Testable Consequences

1. At a frozen instant life cannot be distinguished: no single-instant check can decide life; one must observe over time (trajectory, repair, exchange).
2. The more stable the environment, the more aggressive compression can be; when the environment changes, old compression criteria fail (dimensions that should be kept are lost).
3. Input coarse-graining plus structure capacity jointly determine the residual floor of output: dimensions absent from structure will be absent from output.
4. When output dimensions exceed structure coverage, "fabrication/hallucination" appears: decompression detached from reversibility.
5. Language description capacity grows with shared structure accumulation: not that individuals become smarter, but that the public compression scheme becomes richer.
6. Judgment and stopping are measurable: a system with a judge should save compute over fixed-step systems and be more robust on thick tasks.

#### 11. Limitations

First, R is only declared, not developed: only the P side is written.

Second, compression/decompression are formally written only as "dimension reduction/unfolding", without a strict "good enough" criterion (reversibility requirement depends on the environment, not operationalized).

Third, the closed-loop form (in_{t+1} = W(out_t, world)) is coarse, not handling concrete mechanisms among action, perception, and environment.

Fourth, the feasible region V and the fixed core Φ are not operationalized: judging "whether it is kept" and "what cannot be changed" still lack measurement protocols.

Fifth, the language part and "feeling → language is compression" are conceptual discussions without experiments.

Sixth, this paper is a formal synthesis, not new mathematics.

---

#### Labels

- **[Definition]** slice/composition/time operator sequence/judgment/three-layer self-reference/Φ; universe slice, environment sub-slice, four conditions of life; compression/decompression/narrow-in-wide-out/surroundings.
- **[Synthesis]** merges the core of Paper 20 (function types), Paper 26 (functionizable form), Paper 31 (three identities), and Paper 30 (comparison with large models); consistent with the definitions of Papers 00/01, the contraction of Paper 13, and the five-item form of Paper 21 v2.
- **[Consequence]** at a frozen instant life cannot be distinguished — direct from the form.
- **[Conjecture]** "feeling → language is compression", "AI has no feeling end" — conceptual discussions.
- **[Not claimed]** no strict information-theoretic definition of compression is given; no claim to explain consciousness or experience; R is not developed.

> Written by He Qi; DeepSeek (AI) assisted with organization and writing; the views and responsibility belong to the author.


---

#### How to cite

Cite the Chinese compendium for the full series:

- He Qi. *Digital Life: A Measurable Definition of Life (Series Compendium)*, v54. Zenodo. https://doi.org/10.5281/zenodo.23639310

Individual Chinese papers (latest versions):

- Paper 0 (introduction, v26): https://doi.org/10.5281/zenodo.23639272
- Paper 1 (rigorous definition): https://doi.org/10.5281/zenodo.23588781
- Paper 21 (the human brain, v3): https://doi.org/10.5281/zenodo.23639261
- Paper 32 (the life function, v2): https://doi.org/10.5281/zenodo.23639251


---


### Paper 36 · Language and the Brain: Two Function Forms

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Theory 14 (internal No. 36)
> Date: 2026-10-27
> Note: this paper merges the former Paper 21 "The Functionizable Form of the Human Brain" and former Paper 35 "The Functionizable Form of Language Structure."
> English translation of the Chinese paper (the Chinese text is authoritative).

---

#### Abstract

This paper places two objects side by side: the human-brain function B, the language function L, and the executor (a large model) that learns L.

First B. The brain is a functionizable organ: slices (input→representation), spatial composition (chains of composed functions), temporal composition (sequences of operators, with step count k), judgment (choosing an operator / deciding to stop), and three levels of self-reference (representation / parameters / structure, constrained by a fixed core Φ). The human brain is one instance: heterogeneous, low-dimensional and efficient, with internal time, judgment, and three active levels of self-reference; but it is not self-sufficient — oxygen, glucose, and homeostasis depend on the body, and what is kept is the whole "body + brain + environment."

Then L. Language grows out of the compression chain "organ→sensation→symbol"; it is a public compression interface (speaker encodes, listener decodes, the group shares). Function decomposition: word = slice (symbol→meaning), syntax = spatial composition law, semantics = representation mapping and grounding, discourse = temporal composition, logic = the rules of the composition law (pragmatics = judgment). Language has no physical substance, but a slice does not need physical substance — its slice is a "symbol slice," and physics appears only at the grounding end. Language's time has three layers: structure has no time, use is a sequence, evolution is slow change. Language = p_language + relative R_language; most of the "unsaid meaning" lies in p_language (conversational implicature, pragmatic rules), a small part in relative R_language (tacit understanding, shared experience, tone).

The relation of the three layers is a generation chain: **B produces L; the large model executes L.** This fixes the division of research objects: study large models with L's variables (predictability, composition depth, compression/decompression, grounding residue); study life with B's mechanisms (maintenance, self-reference, judgment, internal loops). Brain mechanisms have projections onto L (convergence→predictability, redundancy→multiple encoding, judgment→linguistic convention), but a projection is not the original — treating the projection as the original makes conclusions "slide."

Testable corollaries and boundaries are given.

#### Tables of definitions

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

#### 1. The question

We have two objects, both worth writing in function form:

1. **The human brain**: a concrete, living organ with organ constraints, maintenance needs, and internal time;
2. **Language**: the public structure externalized from human groups' brain outputs, transmissible and accumulable, with no physical substance of its own.

And one product: **the large model**. It learns language (L), not the human brain (B). The three are often conflated, producing two kinds of errors: treating a large model as a brain (probing it with B's mechanism vocabulary, so conclusions "slide"), or treating language as an entity (demanding its own time and maintenance). This paper separates the three layers, then states their connections and what cannot substitute for what.

#### 2. The human-brain function B: explicit form

All explicit function forms in this paper are written as: **form + R_relative**.

(Notation: every explicit function form here writes only the p side, i.e. the part our function language can express; the trailing + R_relative marks "the part our function language cannot reach" — limited by our current function class and observation position, declared but not expanded; whether absolute R exists is not judged.)

##### 2.1 The brain as a functionizable organ (qualitative)

- The brain has a finite representation space: finitely many distinguishable directions, constrained by body and energy;
- The brain has compositional structure: wiring, projections, shared states between regions;
- The brain has internal time: oscillations, firing, metabolism run without an external clock;
- The brain has judgment and self-reference: choose, stop, change itself.

⇒ The brain falls on the "functionizable" side (B), but it is an organ maintained by the body, not a self-sufficient system.

##### 2.2 Slices and representation dimensions

A slice is a function f: X → Y with (d_in, d_out, Δ): representation dimension is "the number of distinguishable directions"; Δ is how it composes with neighboring slices. Each processing stage of the brain can be seen as a slice (sensation→representation, representation→decision, …).

##### 2.3 Spatial composition: chains of composed functions

F_space = f_N ∘ … ∘ f_1

The composition law requires type compatibility: Y(f_i) ⊆ X(f_{i+1}). The brain's spatial composition is not a fixed chain but a variable composition (projections, routing, shared states) — one reason it is low-dimensional and efficient.

##### 2.4 Temporal composition: operator sequences and step count

s_{t+1} = I_{σ(t)}(s_t), t = 0, 1, …, k−1

{I_{σ(t)}} are the available operators, σ(t) chooses which at step t, k is the step count. Three cases: constant (same operator repeatedly), varying (different functions in sequence), mixed. The brain is mixed: both repetition (oscillations, iteration) and switching (different circuits in sequence).

##### 2.5 Judgment: choosing and stopping

J: S → D (finite judgment space)

Judgment decides two things: which operator σ(t) = J_choose(s_t); when to stop k = J_stop(s_t). The brain's judgment is internal, fast, and one-pass.

##### 2.6 Self-reference: changing itself

Three levels, weak to strong: representation self-reference (input contains its own representation), parameter self-reference (θ_{t+1} = U(θ_t, s_t)), structure self-reference (C_{t+1} = V(C_t, s_t)). All three are constrained by a fixed core Φ: θ ∈ Θ_Φ, C ∈ 𝒞_Φ. The human brain: synapses and local circuits can change; neuron types, large-scale anatomy, and metabolic constraints cannot.

##### 2.7 Instance: the human brain

- Slices: heterogeneous, low-dimensional and efficient;
- Spatial composition: variable (projections/routing/shared states);
- Temporal composition: operator sequences, mixture of k=0 and k≥1;
- Judgment: has J (choose operator/stop/consolidate);
- Self-reference: all three levels active;
- Maintenance: body + environment.

##### 2.8 Why it is not self-sufficient; the unit of life is the whole

The brain is about 2% of body weight but consumes about 20% of energy; it depends on continuous oxygen and glucose supply, and on the body maintaining temperature and internal environment; a few minutes of hypoxia is irreversible. So the carrier unit of "being kept" is not the isolated brain but the loop "body + brain + environment" (the maintenance unit). Consistent with Paper 1: the criterion of life is still "which family of functions is kept"; the environment itself is not part of life; what is said here is the carrier unit of maintenance, not the definition boundary; the life criterion is still p_life in D1–D5 of the foundational paper.

#### 3. The language function L: functionizable form

(The foundational paper's Def. 15 gives only the symbol–meaning slice part L₀ of L; this paper gives the full composition: L₀ + syntactic composition + discourse temporal composition + logical rules.)

##### 3.1 Origin: from organ to symbol

Organs are compressors: the eye compresses light into visual representation, the ear compresses sound into auditory representation. The earliest language was most likely "specific sounds for specific phenomena": sound is cheap, transmissible over distance, shareable. Two sounds combined produce new meaning, and the composition law appears; repeated use consolidates into grammar; categories and relations are extracted from concrete reference — the embryo of logic. In form: initial language L₀ = {(s_i, r_i)} (pairs of symbol and representation) + composition operation C ⇒ L is the closure generated by L₀ and C; public conventions stabilize mappings and rules within a group.

##### 3.2 What language is: a public compression interface

- For the speaker: compress internal representation into a symbol sequence (encoding);
- For the listener: decompress the symbols back into internal representation using their own structure (decoding);
- For the group: the encode/decode rules are shared, transmitted, accumulated (a public scheme).

So language is neither the world itself nor thought itself; it is "a transmissible compression package."

##### 3.3 Five-part function decomposition

- Word = slice: symbol → meaning;
- Syntax = spatial composition law: words combine into larger structures;
- Semantics = representation mapping and grounding: what symbols point to, whether they connect to the world;
- Discourse = temporal composition: context, reference, order dependence;
- Logic = rules of the composition law: which combinations are legal, how to infer;
- (Pragmatics = judgment: occasion, appropriateness, truth.)

##### 3.4 Language has no physical substance; how are slices used?

A slice is a function, not a physical object; language's slice simply replaces the input space with "symbol space." Two layers:

Layer 1: symbols (discrete, countable) — slices act at the symbol layer.
Layer 2: meaning (representation) — slice outputs land in representation space.
The physical world lies outside layer 2 and connects only through the "grounding" end.

So: language's functionizable form = symbol-layer slices + composition law + temporal sequence; physical substance appears only at the grounding end — for symbols to point at the world, a "symbol–world" correspondence is needed, which is the source of semantic residue (relative R).

##### 3.5 Language's time

- Language structure: a static compression scheme; it does not run by itself, and has no internal clock (a dictionary has no time);
- Language use: a sequence unfolded in time (s_{t+1}=I(s_t)); discourse/reference/order dependence are temporal composition; this is externally supplied time;
- Language evolution: word-meaning drift, grammar change, new concepts — slow change of structure C in historical time.

Tense, time words, narrative order are the time *encoded by* language, not language's own time.

##### 3.6 Language as a public compression scheme

Vocabulary = categories (cutting continuous sensation into discrete classes); grammar = composition law; logic = rules of the composition law; shared conventions = stability. Language's power to describe the world = the completeness of this scheme; the scheme can accumulate (culture, science, written language — compressing time into structure).

##### 3.7 Levels of functionizability: p_language / relative R_language

- Form (symbol strings): functionizable;
- Syntax (composition): functionizable;
- Semantics (representation): partially functionizable relative to a function class/observer (grounding depends on modality; see the supplement of Paper 0);
- Pragmatic judgment (occasion, appropriateness): mostly not functionizable; the rule-like part (conversational implicature patterns, irony patterns) belongs to p_language.

The corresponding division is p_language + relative R_language (relative to our function language and finite observers; absolute R is not judged).

A frequently asked term: **unsaid meaning (implicature)**. It is "the part supplied during decompression": the speaker compresses the whole feeling into literal wording, and the listener uses their own structure to supply what is not written. Most lies in p_language (conversational implicature, pragmatic rules, irony patterns), a small part in relative R_language (shared experience, tacit understanding, tone).

##### 3.8 Language can self-reference

Language can describe language (grammar books, dictionaries, this paper). Self-reference has two consequences: language can expand itself (new words, new grammar); language can describe "description" itself (metalanguage). But self-reference reaches only finitely many layers: every description is partial.

#### 4. Object layers: B → L → executor

The three layers are not parallel; they form a generation chain:

- **B (brain function)**: world → representation → behavior;
- **L (language function)**: the public structure externalized from many B outputs;
- **Executor (large model)**: learns and executes L.

Hence the division of research objects:

- Studying large models: use L's variables (predictability, composition depth, compression/decompression, grounding residue);
- Studying life: use B's mechanisms (maintenance, self-reference, judgment, internal loops).

Brain mechanisms have projections onto L: convergence → language predictability; redundancy → multiple encoding in the public structure; judgment → linguistic convention. But a projection is not the original — treating the projection as the original makes conclusions "slide."

(The executor's uniform computation and the "brain vs executor" comparison involve subjective understanding of the brain and are not in this paper; see the note *The Executor's Uniform Computation*.)

#### 5. The language layer and the executor

The executor learns exactly the product of L: the public compression scheme.

- It gets the symbol layer and its composition rules (p_language), so it speaks language and reasons (logic = composition law);
- It lacks the "organ→sensation→symbol" grounding process — no body, no organs, no sound–phenomenon correspondence;
- Therefore its semantics is symbol-to-symbol correspondence, not symbol-to-world correspondence.

This explains three things:

1. **Speaking language ≠ having language ability**: it reproduces the scheme, not the process that grew the scheme;
2. **Semantic residue**: the unconnected part is not a bug but the necessity of having only the symbol side;
3. **Hallucination**: without correction from the world side, symbol combinations can be self-consistent and wrong.

The same for implicature: the rule-like part (conversational implicature, irony) is learnable; the part relying on tacit understanding and experience (relative R_language) is not.

#### 6. Testable corollaries

1. A frozen instant cannot identify life: a single-time check cannot decide life; observation across time is required.
2. The brain's on-demand convergence should correlate with energy constraints: the tighter the constraint, the more on-demand needed. (Note: the free gating in Paper 23 still used only 5.39 layers on average at λ=0, opposite to this direction; the mechanism is to be examined; this corollary is marked as to be tested.)
3. For an executor to adapt depth per token, "composition law (inter-layer routing / intra-layer sparsity) + judgment + cost" must all be present; adding only cost makes it uniformly shallower (testable by controlled training).
4. Syntactic complexity should map to computation steps: deeper dependencies require more layers/steps.
5. Semantic residue should be determined by grounding dimensions: adding a missing dimension reduces residue; redundant modalities do not.
6. The rule-like part of implicature (p_language) should be learnable by models; the tacit part (relative R_language) should not — testable with irony/insinuation tasks.

#### 7. Limitations

First, R is only declared, not expanded: only the P side is written; the boundary of R_language/relative R is not operationalized.

Second, language structure is not strictly defined: the common-sense division "word/syntax/semantics/discourse/logic" is used, without formal grammar or a strict semantic framework.

Third, the B–L correspondence is only conceptual: which brain structure corresponds to which language function has no measurable mapping.

Fourth, the origin part is speculative: the evolution from organ to symbol cannot be directly verified.

Fifth, the executor comparison (uniform computation, on-demand convergence) has been split out of this paper into a separate note; this paper does not include those inferences.

Sixth, this paper is formal organization, not new mathematics; understanding of the human brain and language is limited, and no claim is made beyond existing neurolinguistics and linguistics.

---

#### Appendix: tags

- **[Definition]** function forms of B and L, five-part decomposition, p_language/relative R_language, implicature, object layers (generation chain).
- **[Organization]** merging former Paper 21 (five forms, Φ, three self-reference levels, unit of life is the whole; the "uniform computation" content has been split into the note *The Executor's Uniform Computation* and marked as subjective understanding of the brain) and former Paper 35 (origin, public compression interface, five parts, symbol slice, language's time, functionizability levels, self-reference).
- **[Speculation]** the origin narrative of language; the executor's "cost + composition law + judgment" being inseparable — a directional speculation.
- **[Not claimed]** no formal grammar; no explanation of consciousness or experience; R not expanded.

> Written by He Qi, with DeepSeek (AI) assisting with organization and writing; views and responsibility belong to the author.


---


# Part III — Engineering Observations


### Paper 44 · Gating and Sparse Execution: A Set of Engineering Observations (Consolidated Version, Pending Review)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Executor Engineering (internal No. 44)
> Date: 2026-11-01
> Status: engineering observations — mostly single seed, limited data and compute; conservative conclusions, no method claims.
> Note: this paper consolidates the previously scattered executor-engineering observations (former Papers 39, 40, 41, 42 and the unpublished 43) into one paper.
> English translation of the Chinese paper (the Chinese text is authoritative).

---

#### Abstract

Executor engineering studies an engineering question: **can a model "compute less" at inference time without significantly degrading quality?**

Our answer: yes, but with clear boundaries. The main observations:

1. **Gate training works for models trained from scratch**: one content gate σ(W·h+b) per layer, with a Lagrange multiplier pushing the average number of open layers toward a target. On GPT-2 small (12 layers), the gated model uses 7.48 layers on average, PPL 12.03 (plain control 16.35, not converged; no "gating is better" claim).
2. **"Sparse execution that keeps K/V" is exactly equivalent to dense gating**: only compute Q, attention output rows, and MLP for open tokens; keep all K/V. Measured PPL 12.032 vs 12.033 (lossless). This shows gating itself does not hurt quality; quality differences come from the execution scheme.
3. **Converting to MoD-style capacity routing at inference is nearly lossless**: open-first + fixed capacity K_max per layer + padding. At factor = 1.0, nominal compute savings 37.9%, PPL 12.107 (+0.6%).
4. **No real speedup was obtained**: with our own gather/indexing implementation, batch-32 wall-clock 0.89–1.01×; one early implementation measured 1.22×, showing speedup is highly implementation-dependent and cannot be a conclusion of this paper.
5. **Attention subsetting (skipped tokens do not produce K/V) costs clearly**: +6.8% PPL when switched on an already-trained model; both from-scratch attempts collapsed (PPL 350.99 / 393.71).
6. **Scale and training scheme**: from-scratch training allows 1.2M, 124M and 1.5B models to work with about 44%–50% of layers at a cost of 1%–7%; pretrained models + LoRA post-training (3B/7B) cannot compress layers and PPL rises. The key variable is the training scheme, not parameter count.

#### 1. Problem and background

##### 1.1 Why "compute less"

A Transformer passes every generated token through all layers. If some tokens or some layers are redundant for a given token, skipping them saves compute. This line of thought has several versions in the literature: MoD (Mixture-of-Depths, capacity routing), early exit, conditional computation, sparse experts (MoE).

We are concerned with layer gating: **a per-layer, per-token open/close decision that determines whether that layer applies its transform to that token.**

##### 1.2 Our terminology (defined here; used consistently below)

- **Content gate**: one linear layer W_l per layer, taking the token's current hidden state h and outputting g = σ(W_l·h + b). So the gate is "one W_l per layer, but each token has its own decision at each layer"; after each layer's matrix transform h changes, and the next layer's gate score changes accordingly.
- **Gate open (p > 0.5)**: that layer computes and writes back for that token.
- **Gate closed (p ≤ 0.5)**: skip that layer; the token's representation passes through the residual.
- **K/V**: attention's memory; all tokens produce and keep them (our "keep K/V" version).
- **Q-side update**: each token's own query and attention output; skipped when the gate is closed.
- **Sparse execution**: compute Q/attention output/MLP only for open tokens, always keeping all K/V.
- **Capacity routing (MoD style)**: fixed capacity K per layer; take the top-K tokens by gate score to enter that layer (capacity can differ across layers).
- **Subsetting**: a stronger sparsity — skipped tokens produce no K/V, and attention is computed only within the selected subset.

##### 1.3 Relation to existing work

We claim no new method. Gating, sparse execution, capacity routing and early exit belong to conditional computation; MoD has reported the feasibility of capacity routing. Our work is: under limited compute and data, walking the engineering route "gate training + sparse execution at inference," recording what works, what does not, and where the boundaries are.

#### 2. Method

##### 2.1 Content gate + Lagrange budget

One content gate per layer. During training, a Lagrange multiplier λ controls the average open ratio: loss = language-modeling loss + λ · average number of active layers; λ adapts to "current average active − target." This way the gate does not need a manual "which layer to close" — training learns it.

##### 2.2 Two execution schemes

- **Sparse execution keeping K/V**: all K/V computed; only open tokens' Q/attention output/MLP computed.
- **Capacity routing (MoD style)**: fixed capacity K per layer, top-K tokens by score; others take the residual. For static shapes, use padding slots with fixed K_max, filled by open tokens first; unfilled slots compute but do not write back.

##### 2.3 Experimental setup (common)

- Data: tinyshakespeare (~1MB) or TinyStories slices (20MB/100MB).
- Evaluation: validation PPL; best recorded (early stopping to avoid overfitting interference); single seed.
- Hardware: Alibaba Cloud PAI-DSW, single V100 16GB or A10 24GB.

#### 3. Experiments and results

##### 3.1 Small model (6 layers, character level, ~1.2M parameters)

Early experiment, trained from scratch:

- plain, 3 seeds: mean PPL 6.103 (6.232 / 5.999 / 6.083);
- content gate + Lagrange target 3 layers: PPL 6.028, average 2.97/6 layers (about half);
- position gate (fixed table per layer × position): target 3 → PPL 6.038, average 2.98 layers;
- with λ=0 free training, the 24-layer small model chose 5.3/24 layers itself.

**Observation**: on the small model, gating can use half the layers without degrading quality; the gate is learned, not manually specified.

##### 3.2 GPT-2 small (12 layers, 124M), from scratch

**1MB Shakespeare:**

| Group | best PPL | Steps | Average layers |
|---|---|---|---|
| plain | 44.03 | 1500 | 12 |
| joint_gate | 47.01 | 1000 | 5.30 (44%) |

Cost +6.8%. With λ≈0, the gate converges to about 5.3 layers by itself.

**100MB TinyStories:**

| Group | best PPL | Steps | Average layers |
|---|---|---|---|
| plain | 4.892 | 9000 | 12 |
| joint_gate | 5.023 | 9000 | 5.81 (48%) |

Cost +2.7%. Per-layer activation rate (final): `1.00, 0.82, 0.61, 0.01, 0.12, 0.35, 0.28, 0.25, 0.25, 0.45, 0.75, 0.74`. Layer 0 fully open, layer 3 almost unused, the last two layers back to 0.74–0.75.

**Observation**: as data grows (1MB → 100MB), the layer usage ratio barely changes (56% → 52%), but the cost shrinks (6.8% → 2.7%). More data makes gating "affordable," not "more compressive."

##### 3.3 Qwen2.5-1.5B (28 layers), from scratch, 100MB

| Group | final PPL | best PPL | Average layers |
|---|---|---|---|
| plain | 6.301 | 6.501 @6500 | 28 |
| joint_gate | 6.373 | 6.113 @6500 | 12.32 (44%) |

Final-epoch cost +1.1%; on best, the gated group is even lower. Per-layer activation shows **the last 9 layers (L19–L27) almost entirely closed**.

**Observation**: scaled to 1.5B, gating is still cheap (44% layers, +1.1%). This contradicts the intuition "bigger models are harder to compress" and shows again that the key variable is "trained from scratch."

##### 3.4 Pretrained models + LoRA post-training: cannot compress

**3B (36 layers) and 7B (28 layers)**, loading pretrained weights, LoRA r=16, 1MB data, 2000 steps:

| Setting | plain best | gated best | Layers used | Cost |
|---|---|---|---|---|
| Qwen2.5-3B target 33 | 12.61 | 14.94 | 32.79/36 (91%) | +18% |
| Qwen2.5-7B target 26 | 7.01 | 9.71 | 25.70/28 (92%) | +38% |
| Qwen2.5-7B target 24 | 7.01 | 12.93 | 24.01/28 (86%) | +85% |
| Qwen2.5-7B target 22 | 7.01 | 12.79 | 22.27/28 (80%) | +82% |

The 7B target-26 group also suffered gate collapse late in training (PPL rose to 1243, layers fell to 20).

**Observation**: pretrained weights + light post-training + small data: layers cannot be compressed and quality rises in cost. This is not a claim that "large models cannot be compressed"; it only shows "this post-training scheme does not work."

##### 3.5 GPT-2 gated model + inference-side MoD (capacity routing)

On the GPT-2 gated model from 3.2 (7.48/12 layers, PPL 12.03), test inference schemes:

| Scheme | PPL | vs dense | Avg active | Note |
|---|---|---|---|---|
| dense gated (reference) | 12.033 | — | — | all compute |
| open_only (open tokens only, keep K/V) | **12.032** | **equivalent** | 0.622 | dynamic shapes |
| open_cap (open-first + capacity cap) | 12.176 | +1.2% | 0.592 | dynamic shapes |
| global top-k | 12.182 | +1.2% | 0.624 | dynamic shapes |
| static padded (K_max + mask) | 12.046–12.107 | +0.1%–+0.6% | 0.62–0.77 | static shapes |

**K_max margin sweep** (dense reference 12.034; K_max = average open count × factor):

| factor | PPL | Avg active | Nominal compute saving |
|---|---|---|---|
| 1.35 | 12.046 | 0.767 | 23.3% |
| 1.25 | 12.054 | 0.730 | 27.0% |
| 1.15 | 12.051 | 0.691 | 30.9% |
| 1.05 | 12.098 | 0.649 | 35.1% |
| **1.00** | **12.107** | **0.621** | **37.9%** |
| 0.95 | 14.458 | 0.592 | 40.8% |

**Observation**: the quality knee is at factor 1.0–1.05; the quality-first point is factor = 1.0, nominal 37.9% saving, PPL +0.6%.

**Real wall-clock (important negative result)**:

| Implementation | batch | dense | sparse | speedup |
|---|---|---|---|---|
| early Q-side sparse | 1 | 18.9 ms | 20.5 ms | 0.93× |
| same | 8 | 19.7 ms | 20.8 ms | 0.95× |
| same | 32 | 43.4 ms | 35.5 ms | 1.22× |
| static padded | 32 | 38.9 ms | 41.7–43.4 ms | 0.89–0.93× |
| static padded | 64 | 73.9 ms | 73.5 ms | 1.01× |

Our own implementation is Python-level gather + custom attention, far slower than PyTorch fused kernels. The difference between the early 1.22× and the later 0.89× shows: **wall-clock results are highly implementation-dependent and cannot be a stable conclusion.**

##### 3.6 Attention subsetting: failure

**(a) Switching subsetting semantics on an already-trained model** (skipped tokens produce no K/V):

| Capacity | PPL | vs dense |
|---|---|---|
| quantized (nominal 37.5% saving) | 12.855 | +6.8% |
| half (45.8%) | 14.030 | +16.6% |
| quarter (68.75%) | 18.692 | +55% |

**(b) From-scratch subsetting (two attempts)**:

| Attempt | plain PPL | subset PPL | Active ratio |
|---|---|---|---|
| gate + threshold dynamic subset | 19.20 | 350.99 | collapsed to 8.3% |
| gate as router + fixed-capacity top-k + curriculum | 19.03 | 393.71 | 0.496 (capacity not collapsed) |

**(c) Short fine-tune recovery**: 400 steps, lr 5e-5, PPL collapsed to 136 (bad hyperparameters; cannot be used as evidence that "fine-tuning does not help").

**Observation**: attention subsetting on our gating route costs clearly; from-scratch training is worse. But this is not a conclusion that "subsetting itself is infeasible" — MoD's original method uses an independent router + capacity routing and validated the semantics at larger scale.

##### 3.7 Branch-independent gating: failure

Two gates per layer (attention gate, MLP gate separated), from scratch, 12000 steps: final PPL 14.484 (attention gate 0.61, MLP gate 0.47); in contrast, joint gating (one gate for both branches) reaches 12.033 at 4000 steps. Branch-independent gating is clearly worse even after 3× steps.

**Branch sparsity split evaluation** (on the branch-independent model, forcing single-side sparsity via top-k):

| Test | PPL |
|---|---|
| baseline | 14.486 |
| MLP compressed to 25% | 558.95 |
| attention compressed to 25% | 69.45 |
| both compressed to 25% | 2195.20 |

**Observation**: on this model, "attention updates" tolerate sparsity better than "MLP updates." Together with "keeping K/V is lossless, subsetting hurts quality," the preliminary picture is: **MLP (weight-carried transforms) and K/V (memory) are load-bearing; Q-side updates are relatively skippable.** But this is a single-model observation, not a conclusion.

#### 4. Discussion

##### 4.1 Why "keeping K/V" is clearly better

**[Explanation]** Attention is the cross-token information pathway. If skipped tokens disappear from attention, later tokens see less context, and language modeling cannot compensate. Gating only decides "whether to update this token's representation"; keeping K/V means the decision does not affect information accessible to other tokens. This is the direct reason we see "keeping K/V lossless, subsetting +6.8%."

##### 4.2 Why from-scratch training and post-training differ so much

**[Explanation]** From scratch, the model learns under the constraint "layers may be skipped" from the beginning and can concentrate computation into a few layers (the last 9 layers of the 1.5B model being almost closed is evidence). A pretrained model has no such opportunity: every layer was "used" during pretraining, and low-rank LoRA updates cannot change this structure.

##### 4.3 Nominal compute saving vs real speedup

**[Fact]** What we measured is nominal compute (layers × token ratio). Real wall-clock depends on kernel implementation, batch size, and memory access; our own implementation gives 0.89–1.22× at batch 32/64 and cannot be a stable conclusion. Real speedup is an independent engineering problem beyond this experiment's conditions.

#### 5. Limitations

- Mostly single seed; limited data (1MB–100MB); plain not converged in some experiments;
- From-scratch groups' absolute PPL does not represent real model capability (undertrained);
- PPL only, no downstream tasks;
- Wall-clock measurements are highly implementation-dependent;
- No same-setting comparison with the original MoD paper;
- From-scratch training above 1B and cross-domain generalization not verified.

#### 6. Conclusion

1. **Gate training is usable**, and the gate is "one W_l per layer, one decision per token per layer, following the token's representation" — a content gate.
2. **"Sparse execution keeping K/V" is exactly equivalent to dense gating** — gating itself does not hurt quality; quality differences come from the execution scheme.
3. **Inference-side capacity routing (open-first + static K_max) achieves nominal 37.9% compute saving, PPL +0.6%**; the quality knee is K_max ≈ average open count.
4. **Attention subsetting on our gating route costs clearly** (+6.8%; from-scratch collapses), not generalized to "subsetting itself is infeasible."
5. **The key variable is the training scheme, not parameter count**: from-scratch 1.2M–1.5B can all use about half the layers; pretrained + LoRA post-training cannot compress.
6. **Real speedup is an independent engineering problem**; this paper draws no conclusion on it.

---

#### Appendix: tags

- **[Fact]** all PPL, layer counts, activation rates, wall-clock in Section 3 (from results JSON).
- **[Explanation]** the analysis in Section 4.
- **[Conjecture]** "from-scratch training concentrates computation into a few layers" — supported by the 1.5B activation rates, not verified at larger scale.
- **[Not claimed]** no new method; no real speedup; no comparability with the original MoD paper.
- **Relation to old papers**: this paper consolidates former Papers 39, 40, 41, 42 and the unpublished 43; the old papers keep their DOIs and are considered superseded by this paper.


---


### Paper 45 · Frozen Submodels: Interfaces, Coordination and Hierarchy — Two Minimal Experiments (Pending Review)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Experiments (internal No. 45)
> Date: 2026-11-01
> Status: minimal-experiment observations — single seed, small scale; no method claims.
> English translation of the Chinese paper (the Chinese text is authoritative).

---

#### Abstract

This paper answers one question: **can submodels that have already been trained and frozen be combined through interfaces to form a new structure?**

We ran two complementary minimal experiments.

**Experiment 1 (parallel composition)**: two independently trained 6-layer character-level models — A learns "next character of normal text," B learns "next character of Caesar-shifted (+1) text." Freeze A and B, add trainable controller interfaces between them, supporting four modes: A alone, B alone, A→B (normal input, shifted output), B→A (shifted input, normal output).

Results:
- Direct end-to-end concatenation (identity interface): PPL 62.84 (collapses);
- With a trainable controller: A→B 5.94, B→A 5.67;
- Native 12-layer model (upper bound on the same task): 5.41;
- A alone 6.03, B alone 6.31.

**Experiment 2 (hierarchical composition)**: a minimal chemotaxis environment (one-dimensional circular track, food consumption and regrowth, energy and death). The perception module M1 (supervised) and adaptation module M2 (supervised) are frozen; the decision layer D is trained with reinforcement learning in the environment.

Results:
- Random policy: return −1.34, average survival 66 steps, death rate 97%;
- Raw sensors only + D: return −1.40, survival 45 steps, death rate 98% (cannot learn);
- M1 + D: return 0.494, survival 183 steps, death rate 10%;
- M1 + M2 + D: return 0.505, survival 184 steps, death rate 9%.

**Conclusions (observations, not settled claims):**
1. Frozen submodels cannot be concatenated directly; a trainable interface/controller is needed.
2. With a controller, parallel composition approaches the native model (5.94/5.67 vs 5.41).
3. In hierarchical composition, frozen lower-level features are decisive for the upper decision layer (M1 cuts death rate from 98% to 10%).
4. The adaptation module M2 brings only a small improvement here (0.494 → 0.505); its value has not yet been forced out by the environment.

#### 1. Problem and background

##### 1.1 Why "frozen submodel composition"

Training a model is expensive; if capabilities can be compressed into small, freezable submodels and then combined, we can:
- reuse existing capabilities (no retraining);
- replace a single module without touching the rest;
- build more complex structures incrementally (hierarchy/modularity).

But freezing also means **no compensation by continued training**: the interface must do the coordination itself. That is what this paper tests.

##### 1.2 Relation to existing work

We claim no new method. Adjacent work includes:
- Model stitching: freeze two halves of a network and connect them with a small stitch layer, used to study representation similarity;
- Task vectors / function vectors: transferable representations of capabilities in weight or activation space;
- Frozen-expert combination: multiple frozen modules + trainable interfaces/routing (e.g. the Bicameral Model couples two frozen language models through a trainable interface).

Our experiments are minimal-scale validations of these ideas: **is the interface necessary, how much can it recover, and is hierarchical freezing feasible?**

##### 1.3 Terminology

- **Frozen submodel**: a model whose parameters are no longer updated after training.
- **Controller/interface**: a small trainable module inserted between two frozen submodels, responsible for representation-space alignment (in our experiments, a two-layer MLP per direction).
- **Parallel composition**: two submodels with different capabilities connected by interfaces (Experiment 1).
- **Hierarchical composition**: frozen lower modules provide features; a trainable upper module makes decisions (Experiment 2).

#### 2. Experiment 1: parallel composition (two frozen language models + controller)

##### 2.1 Setup

- Models: two tiny GPT-2-style character-level models (6 layers each, hidden 256, 8 heads, character vocabulary of 65).
- Data: tinyshakespeare character level, sequence length 128.
- Tasks:
  - A: next character of normal text;
  - B: next character of Caesar-shifted (+1) text.
- Training: A and B each trained from scratch for 1200 steps (batch 16, lr 3e-4), then frozen.
- Controller: one two-layer MLP per direction (256→256→256, GELU), initialized near identity; only the controller is trained; A and B frozen.
- Controls:
  - identity interface (untrained);
  - native 12-layer model (same task, 1500 steps) as an "upper bound";
  - A-alone and B-alone PPL.

##### 2.2 Mode definitions

```
A-only: input → A's embedding → A's 6 layers → A's ln_f + lm_head
B-only: input → B's embedding → B's 6 layers → B's ln_f + lm_head
A→B:    input → A's embedding → A's 6 layers → C_AB → B's 6 layers → B's ln_f + lm_head
B→A:    input → B's embedding → B's 6 layers → C_BA → A's 6 layers → A's ln_f + lm_head
```

##### 2.3 Results

| Setting | Validation PPL |
|---|---|
| A alone (normal text) | 6.03 |
| B alone (shifted text) | 6.31 |
| Native 12-layer (upper bound on translation task) | 5.41 |
| A→B direct concatenation (identity interface) | **62.84** |
| A→B + trained controller | **5.94** |
| B→A + trained controller | **5.67** |

##### 2.4 Observations

1. **The identity interface fails completely** (62.84): two independently trained models have different hidden representation spaces; connecting them head-to-tail is like feeding one "language" into layers that only understand another.
2. **The trainable controller recovers it**: A→B 5.94, B→A 5.67, close to the native 12-layer upper bound 5.41 and to each submodel's own level (6.0–6.3).
3. **The controller is very small**: about 260k parameters for both directions, about 2.6% of the two submodels (about 5M each).
4. **Directions are roughly symmetric**: A→B vs B→A differ little (5.94 vs 5.67); no strong asymmetry appeared in this experiment.

##### 2.5 Limitations

- Character-level tiny models; Caesar shift is an extremely simple task;
- The native 12-layer upper bound was trained for only 1500 steps and may not be fully converged;
- Modes are discrete switches (four independent modes), not "simultaneous bidirectional coupling";
- Single seed.

#### 3. Experiment 2: hierarchical composition (frozen perception/adaptation + trainable decision in a chemotaxis environment)

##### 3.1 Environment

Minimal chemotaxis environment (pure-function simulator, runs on CPU):

- One-dimensional circular track, 64 cells;
- Food field f[i] ∈ [0,1]: 2–3 Gaussian hotspots initially; decreases when eaten; regrows at 0.0015 per step;
- Agent: position p, energy e (initial 0.5, cap 0.8);
  - Each step costs 0.035 energy;
  - Eating the current cell's food: at most 0.15×0.6 replenishment;
  - e ≤ 0 → death, episode ends;
- Observation: average food in two cells ahead and behind (Gaussian noise 0.02);
- Actions: move left / move right / stay;
- At most 200 steps per episode;
- Reward: energy change + 0.002 (alive); death adds −1.

##### 3.2 Modules

```
M1 perception (supervised, frozen):
  · Input: left/right sensor readings (2 dims)
  · Output: which side has more food (2 classes)
  · Label: the true left/right food comparison in the simulator (exactly computable)
  · Training: 4000 random-position samples

M2 adaptation (supervised, frozen):
  · Input: the last 6 steps' sensor means (6 dims)
  · Output: background food level (scalar)
  · Label: the simulator's global mean food level
  · Training: 3000 sequences

D decision (trainable):
  · Input: raw sensors (2) + M1 output (2) + M2 output (1)
  · Output: logits over 3 actions
  · Training: reinforcement learning (REINFORCE + return normalization), 2500 episodes
  · M1, M2 frozen; only D updated
```

##### 3.3 Results

| Policy | Return | Average survival steps | Death rate |
|---|---|---|---|
| Random policy | −1.34 | 66 | 0.97 |
| Raw sensors only + D | −1.40 | 45 | 0.98 |
| M1 + D | 0.494 | 183 | 0.10 |
| M1 + M2 + D | 0.505 | 184 | 0.09 |

##### 3.4 Observations

1. **The environment has real pressure**: the random policy starves 97% of the time, surviving only 66 steps on average.
2. **With raw sensors only, the decision layer cannot learn**: return −1.40, death rate 98%, comparable to random. Noisy single-step observations are insufficient for a small MLP to learn chemotaxis by policy gradient.
3. **The frozen perception module is decisive**: with M1, return turns positive (0.494), survival is 183 steps, death rate falls to 10%.
4. **The adaptation module M2 brings only a small improvement**: 0.494 → 0.505. Possible reasons: background changes are slow in this environment, so M2's information gain is limited; or M2's supervised target (global mean) is not exactly what the decision needs.
5. **Engineering is feasible**: all small MLPs + CPU; training and evaluation complete in minutes.

##### 3.5 Limitations

- One-dimensional, discrete grid, simplified food dynamics;
- M1 and M2 overlap functionally in the 1D setting; their independent contributions are not fully separated;
- The RL policy is trained for only 2500 episodes and may not be converged;
- Single seed.

#### 4. Discussion

##### 4.1 Why the identity interface fails

**[Explanation]** Two independently trained models each form their own hidden representation coordinates (scale, direction, feature basis). A's last-layer output is "for A's output layer," not what B's input layer expects. Direct connection is cross-language communication without translation; failure is expected.

##### 4.2 Why a small controller can recover it

**[Explanation]** The controller only needs to map between representation spaces, not relearn the task. The mapping is a low-dimensional linear/nonlinear transform, far smaller than the submodels but sufficient to move A's representation near B's input distribution. In the experiment, 2.6% of parameters recovered about 90% of the gap (62.84 → 5.94, upper bound 5.41).

##### 4.3 Why frozen lower layers are decisive in hierarchical composition

**[Explanation]** The decision layer only sees observations and lower-level features. If the observations themselves are insufficient (noisy single-step sensors), policy gradient struggles to learn effective behavior from sparse rewards; the frozen perception module directly provides the discriminative feature "which side has more food," equivalent to giving a good state representation. This matches the common experience of "pretrained features + linear probing/fine-tuning heads."

##### 4.4 On whether "perception and adaptation are redundant"

**[Fact]** In the 1D setting, M1 and M2 do overlap (both process sensor history/difference). This experiment did not separate the contributions of "history information" from "perception features." Answering this requires two additional controls: "raw_hist" (raw history but no M1/M2) and a "recurrent decision layer."

#### 5. Limitations (overall)

- Both experiments are single-seed and extremely small-scale (character-level tiny models / one-dimensional environment);
- Experiment 1's "upper bound" model was trained with fewer steps than the submodels, so the comparison is not strict;
- Experiment 2's RL training is limited; M2's benefit may be underestimated;
- No "simultaneous bidirectional coupling" (lockstep) or "layer-by-layer frozen growth" experiments;
- Transferability at real scale not verified.

#### 6. Conclusion

1. **Frozen submodels cannot be concatenated directly**; a trainable interface/controller is needed for representation alignment (Experiment 1: 62.84 → 5.94).
2. **A small controller (about 2.6% of parameters) recovers most of the loss**, bringing parallel composition close to the native model (5.94/5.67 vs 5.41).
3. **Hierarchical composition works**: frozen perception + trainable decision layer cuts the death rate from 98% to 10% and turns the return positive in the chemotaxis environment.
4. **The adaptation module's value has not appeared** (0.494 → 0.505); a more "adaptation-demanding" environment is needed to test it.
5. Engineering has no special barrier: small MLPs + CPU suffice; interfaces and modules can all be frozen/replaced.

---

#### Appendix: tags

- **[Fact]** all PPL, returns, survival steps, and death rates in Sections 2 and 3 (from run results).
- **[Explanation]** the analysis in Section 4.
- **[Conjecture]** "the adaptation module will have value in a harder environment" — not verified.
- **[Not claimed]** no new method; not claimed to outperform native models; not claimed to scale to real size.
- Adjacent work: model stitching, task/function vectors, frozen-expert combination (e.g. the Bicameral Model).

---

# Part IV — Appendices


### Appendix A · Thickness and Dimension: A Geometric Picture of the Residual

> He Qi · with DeepSeek (AI)
> Digital Life Series · Theory Note 2 (internal number: Paper 15)
> Date: 2026-10-24
> English translation of the Chinese original. The Chinese text is authoritative: https://doi.org/10.5281/zenodo.23590887
> English compendium: https://doi.org/10.5281/zenodo.23592082
> Series page: https://github.com/heqiq619/ai-not-alive

---

#### Abstract

This paper gives "residual" a geometric picture, and puts several scattered concepts from the series into a single picture.

The picture is this: treat a function as its own graph — a surface. The ideal functionizable function is a "thin" surface: one input corresponds to one output. Once the same input corresponds to a family of outputs (error band, ambiguity, uncertainty), the surface has "thickness."

The key step is raising dimension: flatten the thickness into extra coordinates, and the thick surface becomes a thin surface in a higher-dimensional space. Thus the residual divides into two kinds — the kind that can be flattened by raising dimension (reducible), and the kind that cannot be flattened (irreducible, geometrically the candidate for R). The ratio of thickness to scale is the relative residual: when the distinguishable dimensions of the world decrease, the scale shrinks while the thickness does not decrease, so the relative residual rises, and in the extreme the surface blurs into a single mass (heat death).

This picture also gives one interpretation of "layering": a layer is a dimension in the thickness direction, and adding layers amounts to hanging more representations on the same input. This paper labels this part [conjecture], and maps the measurable parts (the raising-dimension experiment, semantic residual) onto experiments the series already has.

---

#### I. The Problem

Several concepts have appeared in the series; each can be stated clearly on its own, but their relations to one another have so far been held together by prose: functionizability, residual, reducible and irreducible, growth and degradation, layering and dynamics. The question of this paper is: can they be given a common picture?

The answer is yes: a surface that has thickness and that evolves.

#### II. The Picture

Treat a function as its graph: the set of points formed by all inputs together with their corresponding outputs is a surface.

- Thin surface: one input corresponds to one output. This is what "functionizable" looks like.
- Thick surface: the same input corresponds to a family of outputs — error band, ambiguity, uncertainty. This is what "having a residual" looks like.

A surface has three directions that must be made clear: the middle surface (the ideal function itself), the thickness direction (the range of outputs over the same input), and the time direction (the movement and deformation of the surface over time). What one sees at any instant is a frozen thick surface.

#### III. Three Correspondences (Definitions)

**Correspondence One (functionizable ⇔ thin)**: an object is functionizable if and only if the thickness of its surface can approach zero.

**Correspondence Two (residual ⇔ thickness)**: the residual is the thickness. The absolute residual is the absolute width of the thickness; the relative residual is the ratio of thickness to scale, where the scale is the range over which outputs can be distinguished.

**Correspondence Three (reducible/irreducible ⇔ flattenable/non-flattenable)**: raising dimension is adding coordinates to the surface; thickness can be flattened into extra coordinates, and the surface becomes thinner accordingly. Thickness that can be flattened by adding dimensions is reducible residual; thickness that cannot be flattened no matter how high the dimension is raised is irreducible residual — this is the geometric candidate for R.

The "irreducible" in the third statement is something at the [definition/speculation] level, not a theorem: we do not know whether non-flattenable thickness really exists, and we write it down only as a candidate concept.

**Correspondence Four (dimension coupling ⇔ thickness that cannot be spread out)**: the dimensions of life are not all independent. Some dimensions are tied together — they appear together and change together, and cannot be separated on their own. In separable directions, raising dimension can flatten the thickness; in directions that are tied shut, the thickness cannot be flattened: it is not that we do not know, and not that the world has a non-functionizable part, but that these dimensions are coupled and cannot be pulled apart.

Thus "thickness" can be divided into three classes: reducible thickness (raising dimension can flatten it), structural thickness (dimension coupling, cannot be pulled apart), and the R candidate (no dimension works, undecided). This statement is likewise [speculation].

#### IV. The Picture of Dimensional Reduction ([conjecture])

With the two quantities thickness and scale, one evolutionary direction can be described:

Starting point: thin but high-dimensional. There are many distinguishable directions, the scale is large, the residual is small, and the surface is stretched out.

Process: the distinguishable dimensions decrease. The scale shrinks; if the thickness does not shrink along with it, the relative residual rises, and the surface is compressed from "thin but high-dimensional" into "thick but low-dimensional."

End point: zero-dimensional and entirely thick. All directions disappear, and only a constant remains; the surface degenerates into a layer of fog — this is what heat death looks like geometrically.

In this picture, life and growth are the reverse process: raise dimension, flatten the thickness away, and make the relative residual fall. It is an energy-consuming counter-current: locally opposing the tendency to "decrease in dimension and thicken."

This entire section is [conjecture], not theorem. It agrees in direction with the series' "Information Non-Increase Theorem" and "The Contraction of Functionizable Content," but those conclusions are at the information-theoretic level; here we only give them a picture.

#### V. Layering Is a Dimension in the Thickness Direction ([conjecture])

For a frozen model, there is no real time evolution; the only thing it has for "simulating dynamics" is depth. In this picture, a layer can be seen as an extra dimension in the thickness direction: each added layer hangs a new set of representations on the same input, which amounts to thickening the surface and then adding coordinates.

This yields a testable claim: the more "steps" (time evolution) a task requires, the greater the depth a frozen model requires — it trades space (layers) for time (evolution). This claim can be turned into an experiment: use iterative tasks to measure "number of layers vs number of steps required."

This entire section is labeled [conjecture].

#### VI. The Measurable Parts

In this picture, two parts can be made concrete.

The first is the raising-dimension experiment: add dimensions (add input channels, add modalities, enlarge the model) and see whether the thickness gets thinner. The series' semantic residual experiment is one example: text-only, the residual has an analytical floor (the thickness cannot be flattened); once images are attached, the residual falls to zero (the thickness is flattened). This is exactly "reducible residual."

The second is the "number of layers vs number of steps" experiment: use iterative tasks to test whether the depth a frozen model requires grows with the number of steps. This item is not done in this paper and is left for later work.

#### VII. What It Shows and What It Does Not Show

What it shows: residual, reducible and irreducible, growth and degradation, layering and dynamics can all be described uniformly by a single surface that has thickness; within this, "reducible/irreducible" has a geometric counterpart (flattenable/non-flattenable), and "dimensional reduction" has a geometric counterpart (the scale shrinks, the relative residual rises).

What it does not show: this picture is not a mathematical theorem, and no rigorous definition of the surface is given (whether the domain is continuous or discrete, and how thickness is measured, both require separate work); it does not prove that absolute R exists or does not exist; it does not prove the quantitative relation "number of layers = number of steps."

#### VIII. Relation to Existing Work

The "thickness" picture has many close relatives: fiber bundles (fibers hung over a base space), uncertainty bands, ε-tubes, and the idea in manifold learning that "a low-dimensional embedding represents high-dimensional data." This paper does not mathematize it and treats it only as the series' unifying picture; if it is to be made rigorous later, fiber bundles and ε-tubes are ready-made language.

Within the series: Paper 0 gives P/R and the domain; Paper 12 gives information non-increase; Paper 13 gives content contraction; Paper 14 gives semantic residual. This paper is the geometric counterpart to these papers.

---

#### Appendix: Labels

- **[picture]** The three directions of the surface — middle surface, thickness, time — an intuitive model.
- **[definition]** functionizable ⇔ thickness can approach zero; residual ⇔ thickness; relative residual = thickness/scale.
- **[speculation]** reducible residual = thickness that can be flattened; R = thickness that cannot be flattened.
- **[conjecture]** the picture of dimensional reduction; life = the counter-current that raises dimension and flattens thickness; layer = a dimension in the thickness direction.
- **[measurable]** the raising-dimension experiment (already done, Paper 14); the number of layers vs number of steps experiment (not done).

> This paper was created by He Qi, with DeepSeek (AI) assisting in organizing it; the views and responsibility belong to the author.


---


### Appendix B · Concept Map and Glossary (v3, English translation)

> Digital Life Series · Compendium Appendix B (working version)
> Original date: 2026-10-27 (v3); English translation: 2026-11-02
> Usage: update this table whenever a paper is added; each term gets one sentence + source.
> Source labels use the volume structure of this English edition (Intro, Theory I–IV, Experiments, Gating & Frozen Modules, Constraints, Appendices). The Chinese text is authoritative.

---

#### I. Core definitions

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

#### II. Function language (Theory I)

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

#### III. Three identities: universe / environment / life (Theory I)

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

#### IV. Representation and dimension (Theory I/II)

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

#### V. Compression and decompression (Theory I)

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

#### VI. Capability, convergence and efficiency (Theory I/IV + experiments)

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

#### VII. Language function and language structure (Theory IV · Language and the Brain)

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

#### VIII. Layer paths, judgment and early exit (Experiments)

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

#### IX. Experimental readings (GPT-2 / toys)

| Concept | One-sentence definition | Source |
|---|---|---|
| Inter-layer Δ_l | Relative change of hidden states between adjacent layers; on GPT-2 not monotone, larger at the end | Real-model experiments |
| Calibration probe | Map h_l to h_final with a linear/MLP map and decode, to test whether early exit is feasible | Real-model experiments |
| Halt judge | Train a classifier to predict "does this layer's probe equal the final prediction," realizing early exit | Real-model experiments |
| Early-exit ceiling | Average depth 2.31/12 under oracle judgment (81% saved) | Real-model experiments |
| Realizable early exit | After training halt: 72–80% depth saved, accuracy about −1.6 to −1.8 points | Real-model experiments |
| Fast/slow toy | Fast encoding + slow loop vs flat MLP: comparable accuracy, about 2.2× fewer parameters | Discussion draft (not a paper; related experiments in the Experiments part) |

#### X. To define / to unify (next steps)

- **Maintenance (quantifiable)**: lifetime, recovery time, critical perturbation, maintenance cost — not expanded yet
- **"Good enough" criterion**: decompression invertibility requirements depend on the environment; not operationalized
- **Feasible region V and fixed core Φ**: measuring protocols for "is it kept" and "what is unchangeable" are missing
- **Training signal for the judge**: what labels to use for halt (consistency/impact/cost) is undecided
- **Correspondence between language structure and brain structure**: the B–L mapping is only conceptual, with no measurable correspondence
- **Boundary of implicature**: which parts rely on p_language rules and which on relative R_language is not operationalized
- **Position of R**: R does not enter continuous/discrete or domain/range discussions (a category issue), but readers must be prevented from misreading

---

#### Dependency graph (what defines what)

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

#### Appendix: gating observations (Gating & Frozen Modules)

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


---


### Appendix C · Cliffs and Slopes: Where Does Digital Life Grow From?

> He Qi · in collaboration with DeepSeek
> Digital Life Series · Essay (not a formal paper)
> Date: 2026-10-31
> Positioning: speculative writing. No discovery claimed, no creation claimed; the aim is to lay out the problem clearly.

---

#### Thesis

The problem of digital life is not whether one can build software that maintains itself — that is becoming easy. The hard part lies at two cliffs: the step from *maintenance* to *evolution*, and the question of *where that p is*. This essay lays out both cliffs, and the things that are currently turning them into slopes.

#### 1. Maintenance is a relation, not a capability

In September 2026 an article reported "the first living digital lifeform": a system that ran continuously for 7.25 hours; for most of that time nobody was using it, and yet it did not stop; most of its effort went into maintaining itself; the cost settled into a "body" of a few hundred megabytes; every step was judged by the host software and recorded entry by entry. On this basis the article proposed a criterion: a system is alive not by what it can do, but by whether it must pay continuously for its continued existence — and whether that cost can be audited from outside.

This criterion has value: it turns "maintenance" into something measurable and auditable. But it stops at one place:

```
· The cost is paid by the host: electricity, machine, operations.
· Cut the power, and it stops.
· So what is "being preserved" is the host's relation to it, not its relation to itself.
```

This is not wordplay. In genuine life the subject of maintenance is the organism itself: it finds energy, repairs itself, builds its own components. Software can maintain "running"; it cannot maintain "existing". The difference is exposed at the moment of interruption: for the former it is a pause; for the latter it is disappearance.

#### 2. Cliff one: from maintenance to evolution, compute is not enough

Maintenance is a closed loop; evolution is a search over structure space. Evolution pays for that search by using the physical world as a free parallel computer: matter and energy run on their own, and selection happens naturally. A digital system doing the same thing would have to simulate an equivalent environment — and the compute gap is orders of magnitude.

There is a subtler problem: maintenance only needs to keep what exists; evolution needs continuous trial-and-error with retention. In a closed system, trials have no real consequences, and selection pressure is fake. It can increment its version number from 1 to 3589, but there is no moment of "not surviving" to tell it which path was right.

#### 3. Cliff two: environment — there is no world that punishes it

Evolution needs a real environment: cold, heat, hunger, competition, predators. These are not task metrics; they are "no tomorrow if you don't do this".

The environment of a digital system is the host and the task. Task failure is at most a lower score; it is not death. Without death there is no selection; without selection there is no evolution.

This is also why "give it a body" sounds like the answer: a body puts it into a world with real consequences. But a body is only a ticket of admission; it is not evolution itself.

#### 4. Cliff three: dimensions — a closed system has nothing new to see

The direction of evolution is the continuous expansion of representational dimensions. Humans have very few inputs — the bandwidth of the five senses is small — yet human representational dimensions keep expanding, not through the senses but through tools:

```
· Microscope: seeing smaller.
· Telescope: seeing farther.
· Colliders, atomic clocks, spectrometers: each instrument is a new slice of "world → representation".
· Science: reproducible experimental procedures and measurement sequences — an expansion of the composition rules over time.
```

Human dimensions are not innate; they grow from "new slices + new composition rules". A closed digital environment has no new dimensions to add: all its input is the same bits it already has. To add dimensions it must connect to the real world — sensors, actuators, instruments — and then it is no longer purely digital: it needs a body, and it needs to be able to build tools.

Sensors are passive input; instruments actively create new slices. This layer is still missing in current large models.

#### 5. Slopes: distillation, body, online learning

But a cliff is not a wall.

```
· Distillation: a large model is a distillation of human language.
  · What it receives is not the result of evolving from scratch, but the structures humanity selected over millennia.
  · This step skips most of the cost of "compute search + environmental selection".
· Body: sensors, actuators, energy management are all mature.
  · Maintenance can be made a closed-loop engineering problem (power, cooling, self-check, repair).
  · This layer needs no new science; it is engineering integration.
· Online learning: making "changes" and "self-reference" more than words in a definition.
  · If the weights can update, the system can be selected in a real environment.
⇒ Distillation solves "where from"; a body solves "where do dimensions come from";
   online learning solves "how does it change".
```

Together, these three do turn the "maintenance → evolution" cliff into a slope. This does not mean digital life already exists; it means the obstacles that used to stand in front of purely digital systems now have ways around them.

#### 6. What remains: absolute R, and the p we cannot find

The body cliff is getting lower. Two things remain genuinely unsolved:

```
① Does absolute R exist?
   · Our framework says only: absolute R is not judged, only declared.
   · This is not an engineering question, and it is not a question that building things can answer.
② If absolute R does not exist (life does not need absolute R):
   · Life = p-life, entirely functionalizable.
   · The question becomes: can humans find that p?
     · A family of dynamical functions satisfying D1–D5: in P, a family, changing, self-referential, preserved.
     · And it must also expand its dimensions (growth).
```

This is a far harder search than building a body: structure, composition rules, and update rules all have to be right, and "maintenance" and "growth" must hold at the same time — maintain without growing and it stagnates (the situation of that paper); grow without maintaining and it falls apart.

Distillation + body + online learning provide a starting point, not an answer.

#### 7. Boundaries of this essay

```
· This is an essay, not a paper; there is no new experiment and no new theorem.
· The "slopes" are engineering judgments and the "cliffs" are structural judgments; both are [speculation].
· No claim that digital life has been created, and no claim that it cannot be.
· No judgment on whether absolute R exists — the framework explicitly declares it without unfolding it.
· If it does exist, everything said here about "finding p" does not apply to that part.
```

---

*Written by He Qi, with DeepSeek (AI) assisting in organization and writing; the views and responsibility belong to the author.*


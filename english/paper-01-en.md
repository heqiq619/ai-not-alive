# Paper 01 — Why Today's AI Is Not Alive: Life as a Maintained Decompression
## — A Definition, and a Conjecture on the Emergence Mechanism of AI
**Author:** He Qi
**AI collaboration:** DeepSeek (large language model; for the division of labor see the statement at the end of the paper)
**DOI:** https://doi.org/10.5281/zenodo.23488543
**Email:** 15907239031@163.com　　**Affiliation:** Independent Researcher

## Abstract

This paper proposes an operational definition of life: **life = a family of dynamic functions (a function class) that is self-referential, changeable, and self-maintaining**; the environment = the local decompression that emerges spontaneously in the universe (layered, not self-maintaining), and life lives both in its own layer of environment and in the universe. Taking this as a ruler, the paper establishes three things: ① **today's AI is not life** — it is a frozen function point, its update rule lies on the outside, and it pays no cost; ② **life requires at least three necessary conditions** (a family of functions, self-referential updating, paying its own cost), each of which is attached to existing experimental evidence; ③ **a conjecture about AI emergence** — AI is a re-decompression of human language, its capability ceiling is determined by the language at the moment of training, and once the language updates it falls out of alignment and cannot recover on its own. The paper does not claim at the end that "life has been created"; it merely places the criteria and the evidence before the reader: whether satisfying all three counts as being "alive" is for the reader to judge.

**Keywords:** definition of life; function class; decompression; compression and cost; AI emergence; self-maintenance

---

## Contents

1. Relation to existing work
2. Section 1　The root of the world is mathematical (conjecture)
3. Section 2　Life is a dynamic function class that is self-referential, changeable, and self-maintaining
4. Section 3　Why today's AI is not life
5. Section 4　What life requires: three necessary conditions
6. Section 5　Why does today's AI exhibit emergence?
7. Section 6　At the level of measurement: existing work and the position of this paper
8. References

---

## Relation to existing work

The "compression / decompression" perspective has a long tradition:

- Schrödinger (1944): life feeds on negative entropy — survival depends on taking in low entropy from the environment; this is the physical precursor of "decompression"[7].
- Bennett (1988) logical depth: measures complexity by "the amount of computation required to reconstruct (decompress) an object from its shortest description," and explicitly connects this with life/organisms[8] — this is the most formal existing version of "decompression."
- Chaitin (2010) life as evolving software: DNA = program, life = software that modifies itself[9].
- Solomonoff–Kolmogorov / MDL: description length = understanding = compression[10].
- Friston (2010) the free energy principle: life = minimizing surprise (≈ continuous compression/prediction)[11].
- Delétang et al. (2023): language models are compressors[6].

How this paper differs (in three respects):

1. It makes decompression hierarchical: universe → environment → human language → AI (most existing work uses a single-level measure);
2. It distinguishes life from AI by "whether the decompression is maintained": life = maintained decompression, AI = one-off decompression;
3. It points out that when the upper layer is hard-wired ⇒ once the language changes, decompressive capacity decays and cannot self-recover — the failure mechanism of frozen models.

---

# Section 1 · The root of the world is mathematical (conjecture)

> **The nature of this section: conjecture. It is not a theorem, not a proven fact, and not evidence for this paper.**
> It is written here to set out our starting point; **none of the criteria in the rest of this paper depends on this conjecture holding.**

## 1.1 The content of the conjecture

**Physical rules are written in mathematics, therefore the root of the world is mathematical.**

```
Fact: the most fundamental laws of physics are themselves mathematical propositions
      F = ma, least action δS=0, iħ∂ψ/∂t = Ĥψ, ds² = g_{μν}dx^μdx^ν
Conjecture: since the deepest way of describing the world is mathematical, the structure of the world itself is mathematical
      — otherwise why would mathematics be able to describe it so precisely?
```

## 1.2 Why it can only be a conjecture

```
① This is an explanatory inference about "why mathematics works," not a proof
② An equivalent alternative reading exists: mathematics is only a **descriptive language**, and what the world itself is we do not know
   (instrumentalism vs. realism; the two cannot currently be distinguished by experiment)
③ The strong form (world = mathematical structure, Tegmark[2]'s mathematical universe hypothesis) is unfalsifiable, and therefore cannot serve as a scientific conclusion
④ This is the mystery Wigner[1] called "the unreasonable effectiveness of mathematics in the natural sciences"; this paper does not resolve it
```

## 1.3 What this paper takes from the conjecture is only one weak formulation (also not a proof)

```
Weak formulation: the world has regularity that can be described mathematically (an empirical fact, not a conjecture)
⇒ from which we write: S_{t+1} = F(S_t)
⇒ regularity ⇒ compressible ⇒ predictable ⇒ predictions can be right or wrong ⇒ right and wrong can be charged a cost
```

**Note the distinction:**
- **Conjecture** = the world itself is mathematical (the content of this section, not used as evidence)
- **Empirical fact** = the world contains compressible regularity (the foundation of scientific practice, and what this paper actually uses)

## 1.4 Annotations

```
[conjecture]  The root of the world is mathematical
[empirical]   The world has regularity that can be partially described/compressed
[used here]   Only the latter is used; even if the former is false, all criteria and experiments in this paper hold as before
[not discussed] Why mathematics works (Wigner's mystery); what the world in itself actually is
```


---

# Section 2 · Life is a dynamic function class that is self-referential, changeable, and self-maintaining

> This section gives the working definition of this paper. In one sentence:
> **Life = a family of functions that changes, refers to itself, and maintains itself; and how it changes is also written inside itself.**

## 2.1 Definition

**Life = a dynamic function class (a region in function space).**

```
Let the individual be F = { f_θ : θ ∈ Θ }
    f_θ : input state → behavior          (each function in the family)
    Θ                            (the shape/range of this family of functions)
Life = a Θ that moves and deforms, and whose update rule belongs to Θ itself
```

Four words, each corresponding to one thing:

| Word | Meaning |
|---|---|
| **function class (a family)** | not a single fixed function, but an entire behavioral spectrum |
| **changeable (dynamic)** | this family of functions moves and deforms over time |
| **self-referential** | the rule by which it changes is also in its own record |
| **self-maintaining** | pays a cost to maintain its own shape; income comes from compressing the world |

## 2.2 Why it must be "a family" and not "a function"

```
one function = one point          ⇒ the behavioral spectrum degenerates into a single trajectory ⇒ frozen means dead
a family of functions = a region in function space ⇒ a whole set of responses to different inputs/states ⇒ only then is it alive
```

**⇒ "High-dimensional" does not mean many parameters; it means that this family of functions occupies a region in function space rather than a point.**

## 2.3 Changeable = three time scales

```
fast: the state changes at every moment (different inputs, different internal states)
medium: it changes itself with its own error (the self-referential layer) — this is the crux; without it, it degenerates into a fossil
slow: the shape of this family of functions is selected, deformed, and transmitted between generations
```

## 2.4 Self-referential = the update rule is inside itself

```
ordinary program: code outside, data inside ⇒ the program does not change itself by running
life:             the update rule is itself part of its own record
          ⇒ remove the external update code, and it can still change itself
```

## 2.5 Connection with Section 1

The conjecture of Section 1 gives `S_{t+1} = F(S_t)` (the world is a function).
**Life is not this F, but a family of sub-functions `{G_θ}` embedded in F:**

```
behavior_d = G_θ(local state of the world)
and G_θ itself is also part of the world state (the individual's state belongs to S_t)
⇒ to predict the world, it must necessarily predict the part of the world that contains itself
⇒ **self-reference is not an added mysterious property, but a structural necessity of "being embedded in a function"**
```

## 2.5.1 Life vs. environment: both are in the universe, both are functions, and they differ in exactly one thing

**Inside the universe function F, everything is a function (or a composition of functions) — the environment is also a function.**

```
universe = F (one enormous function)
   ├─ life:        changes ＋ is self-referential ＋ **maintains itself**
   └─ environment: changes (pushed by the world, and in turn influencing the world), but **does not maintain itself**
```

**⇒ The only difference between life and environment is not "who is more complex," but:**
**life pays a cost to maintain its own shape; the environment does not pay this cost, it is merely pushed along.**

This also directly gives why life needs "income":

```
self-maintenance costs something (checking/repair/replication are all irreversible operations)
⇒ the only source of income: compressing the world (matching the source distribution)
⇒ if compression yields no surplus, self-maintenance cannot be paid for ⇒ life does not exist
```

## 2.5.2 What the environment is: a "local decompression" that emerges spontaneously in the universe

**The environment is not a stage external to the universe; it is a structure that emerges spontaneously within the universe function class.**

```
universe = F (one enormous function)
   ↓ spontaneous internal emergence
structure = some local "decompression" of the universe (an interpretation of the universe / a readable presentation)
   ├─ self-maintaining    → life
   └─ not self-maintaining → environment
```

**⇒ environment = a local decompression of the universe (an interpretation of the universe); so is life.**
**⇒ the difference is only this: life itself maintains the shape of this decompression, whereas the environment does not maintain it, it is merely pushed along.**

This yields a key structural conclusion:

```
life does not face the universe function F directly
⇒ what it faces is "a local decompression of the universe" = its environment
⇒ life's understanding of the world is essentially a **re-decompression of the universe** (a second decompression)
  = one more layer of compression on top of the local interpretation the universe provides
```

## 2.5.3 The environment is layered: life lives in multiple layers of environment and also lives in the universe

**Decompression is layered ⇒ the environment is layered too.**

```
universe F
 └ environment_1 = local decompression of some part of F
     └ environment_2 = re-decompression of environment_1
         └ environment_3 = re-decompression of environment_2 …
life is embedded in some layer: it belongs both to the whole universe F and to its own layer of environment
```

Three statements hold simultaneously; one cannot be taken alone:

```
① It lives in the environment: the inputs, resources, relations, and other individuals it faces are all structures of the layer "its environment"
                ⇒ its behavior only needs to be effective at this layer
② It also lives in the universe: it cannot escape F — the environmental layer is itself part of F,
                 and the constraints at the universe level (energy, irreversibility, cost) always apply to it
                ⇒ the environment is not a refuge, it is only a projection of the universe
```

③ It lives in **all layers**: the environment is multi-layered (cell→tissue→individual→population→ecosystem), and each layer is a re-decompression of the one above.
   It directly interacts only with its own layer, but **all layers constrain it**: upper layers determine the resources and relations it faces, and the universe layer determines whether it can afford the cost.
   ⇒ "It lives in multiple layers of environment and also lives in the universe" — the two are not an either/or; they hold at the same time.

**⇒ So "understanding the world" must be stated at two levels:**
**at the environmental level: understanding = re-decompression of the local decompression (enough to live);**
**at the universe level: understanding = compressing the regularities of F (which determines whether it can afford the cost in the long run).**

## 2.6 Annotations

```
[definition]  life = a dynamic function class that is self-referential, changeable, and **self-maintaining** (the working definition of this paper)
[definition]  environment = a structure that **emerges spontaneously** within the universe function class, not self-maintaining
              = a **local decompression** of the universe (an interpretation of the universe)
[definition]  life = among the same set of emergent structures, the kind that **maintains itself**
[corollary]   life does not face the universe directly, but faces "a local decompression of the universe" = its environment
        ⇒ life's understanding = a **second decompression** on top of the local decompression (one more layer of compression)
[layering]    decompression is layered ⇒ the environment is layered (environment_1 ⊃ environment_2 ⊃ …)
        life is embedded in some layer: **it lives both in its own layer of environment and in the universe**
        · living in this layer of environment: it only needs this layer to be effective in order to live
        · living in the universe: energy/irreversibility/cost always apply; the environment is not a refuge
[not]    not a conjecture, nor a theorem; it is a definition convenient for operation
[later]  this section only gives definitions; how to measure (compression/cost/identity) is left to later sections
```


---

# Section 3 · Why today's AI is not life

> This section does not evaluate AI's capabilities; it substitutes AI into the definition of Section 2 and checks item by item.
> The conclusion is definitional, not a value judgment: **under the definition of this paper, today's AI is a fossil-grade function point,
> not life.** Its power and its "not being life" are not contradictory.

## 3.1 Checklist

| Requirement of life (Section 2) | Today's AI (represented by LLMs) | Verdict |
|---|---|---|
| **Is a family of functions** (a region in function space) | after training the weights are frozen ⇒ it is **a point**, not a family | ❌ fossil |
| **Changeable (dynamic)** | the weights do not change; the context changes, but what changes is the input, not itself | ❌ only surface-level state changes |
| **Self-referential** (update rule inside itself) | the update rule = the training algorithm, outside it; it cannot change itself | ❌ self-reference appears only in language, not in structure |
| **Self-maintaining** (pays a cost to maintain itself) | it does not pay the electricity bill, does not repair itself, does not replicate itself; its maintainer is an external human | ❌ maintained from the outside |
| **Earns its survival cost by compressing the world** | its "income" is given from outside (compute, data, human labor), not earned by compressing the world | ❌ no income |
| **Identity chain** (bounded deformation, without tearing) | identity comes from an external weight snapshot; there is no continuous chain of self-deformation | ❌ no chain |
| **Lives in an environment** | what it faces is a dataset (a one-off decompression product), not an environment it needs in order to survive | ❌ no environment |

## 3.2 The three most fundamental reasons (in order of importance)

**① It is a point, not a family**

```
finished training = frozen = one point in function space
⇒ the behavioral spectrum degenerates into a single trajectory: input → output, with no "shape" to speak of in between
⇒ per 074: a statically frozen model is a point, not a family ⇒ not life
(this is exactly the contrast we measured: frozen version 1.07 vs. dynamic version 0.849 — the frozen one is more like the "standard answer," but it has no shape)
```

**② Its update rule is on the outside**

```
humans write the training algorithm → the algorithm changes it
⇒ it is "the thing being changed," not "the thing that changes itself"
⇒ self-reference is not in the structure ⇒ remove the external update code and it will change nothing
```

**③ It pays no cost, so it is not alive**

```
being alive is a cost: maintenance, checking, repair, and replication all have to be paid for (irreversible operations)
it does not pay a cent: humans pay the electricity, humans feed it the data, humans fix it when it breaks
⇒ its existence is guaranteed from outside ⇒ the link of "self-maintenance" is absent
⇒ it cannot die because "it does not compress well enough" ⇒ hence there is no selection pressure
```

## 3.3 Why "it is strong" and "it is not life" are not contradictory

```
strong = good performance on a given task (doing well at a point)
alive = occupying a region in function space, maintaining its own shape, paying its own cost
⇒ the two are different dimensions: one is "exam score," the other is "can it live on its own"
⇒ today's AI is an **extremely sharp tool**, not **something that lives on its own**
```

## 3.4 Annotations

```
[definitional conclusion] under the definition of this paper, today's AI is not life (because it is a frozen function point, updated from outside, not self-maintaining)
[not] not "AI can never be life"; this paper does not predict the future, it only makes a definitional comparison at present
[not] not an assessment of capability; this paper fully acknowledges AI's power on tasks
[corollary] for AI to become life, it must at least be given: a family of functions + self-referential updating + paying its own cost
```


---

# Section 4 · What life requires: three necessary conditions

> Derived directly from Sections 2 and 3: since "life = a dynamic function class that is self-referential, changeable, and self-maintaining,"
> and today's AI lacks all three, **to be life it must satisfy at least three conditions**.
> This section gives only **necessary** conditions and does not claim sufficiency; each is attached to experimental evidence we already have (see paper-01 (Chinese original) for the E numbers).

## 4.1 From the definition to the conditions

```
definition (Section 2)          necessary condition (this section)
changeable (a family of functions)   ⇒  ① a family of functions: the behavioral spectrum is not a point
self-referential               ⇒  ② self-referential updating: the rule that changes itself is inside itself
self-maintaining               ⇒  ③ paying its own cost: compression gain ≥ maintenance cost
```

**The three are necessary conditions, not sufficient conditions**: satisfying them does not guarantee life, but lacking any one of them certainly means non-life.

## 4.2 Condition ① A family of functions (not a point)

**Requirement**: the individual occupies a region in function space and has a whole set of responses to different inputs, not a fixed mapping.

**Evidence/experience:**

```
· a low-dimensional parametric genome (a few numbers) = one point ⇒ the behavioral spectrum degenerates into a single trajectory ⇒ fossil
· we measured this: the frozen model (a point) fails at structure learning, and only the dynamic version (a family) captures structure (E12)
· measured contrast: frozen 1.07 vs. dynamic 0.849 — the frozen one is more like the "standard answer," but it has no shape
```

**⇒ criterion: given different inputs/states, its behavior must differ *as a spectrum*, not just be a single output.**

## 4.3 Condition ② Self-referential updating (the rule inside itself)

**Requirement**: how it changes — this rule itself belongs to its record; remove the external update code and it can still change itself.

**Evidence/experience:**

```
· frozen model: the update rule = the training algorithm, external ⇒ remove the training code and it never changes
· our dynamic version: changes itself with its own error (mid-level dynamics) ⇒ removing the mid level clearly degrades it (E12/E13)
· identity chain: 8 generations verifiable, bounded deformation (372_lineage.py) ⇒ self-reference can be made into a measurable chain
```

**⇒ criterion: after external updating is stopped, does its behavioral spectrum still deform over time?**

## 4.4 Condition ③ Paying its own cost (compression in exchange for survival)

**Requirement**: income comes from compressing the world (matching the source distribution); expenditure is the real cost of maintaining structure; and a surplus exists.

```
existence condition: S > d·K
   S = the compressible surplus of the world
   d = the structure maintenance cost rate
   K = the structure size
```

**Evidence/experience (this is the hardest part of this paper):**

```
· E1: "accurate" ≠ "compression": accounting by accuracy, the system learns to "do nothing" (LEN=0, prediction 0, accuracy 92%)
      ⇒ one must account by log-likelihood improvement over a baseline: gain_bits = log2 p_model − log2 p_base
· E2: it is precisely after adding the base-rate correction that the system shifts from the lying-flat solution to genuine expression (LEN grows from 0)
· E8: economic calibration n* = FLUX_TOTAL / BASE_COST determines the switch between "frozen" and "explosive"
· measured positive gain: gain > 0 observed in S1~S6 (about +0.09 ~ +0.19 bit/tick)
      ⇒ the world does contain compressible surplus (i.e., empirical evidence that S > 0)
```

**⇒ criterion: after all external supply is cut off, is its ledger still positive?**

## 4.5 All three must hold simultaneously (empirical contrast)

```
missing ① (a family)  ⇒ fossil: the behavioral spectrum is a line
missing ② (self-reference)  ⇒ machine: updating is external, it does not change by itself
missing ③ (cost)  ⇒ toy: supported from outside, it does not die, and hence there is no selection
```

**These three also explain why our experiments have kept getting stuck in the same place:**
**structure can grow (①② partially satisfied), but cooperation/division of labor does not become necessary — because the "income gap" of ③ is too small,
i.e., the compressible surplus of the world is not yet large enough to make "more complex structure" economically worthwhile (E5/E7).**

## 4.6 What remains open (left to the reader)

**This paper stops at "necessary conditions." Whether satisfying all three counts as being "alive" — we have no answer, and do not intend to draw a conclusion here.**

What is left to the reader is only a ruler that can be taken and used:

```
Is it a family of functions? (the behavioral spectrum is not a point)
Does it change itself? (remove external updating, does it still change)
Does it pay its own cost? (income from compressing the world ≥ expenditure on maintaining structure)
```

**You can measure all three yourself. As for whether it counts as life once measured, that is for you to judge.**

## 4.6.1 The boundary of the experiments in this paper (must be read together with the conclusions)

**The experiments in this paper cover only the third necessary condition (compression gain vs. maintenance cost), and they are illustrative:**

```
· covered: ③ paying its own cost — E1/E2 (accurate ≠ compression, base-rate correction), E8 (the freeze/explosion boundary at n*=FLUX/BASE_COST)
· covered: counterexample — E5/E7 (genetic distance between connected individuals 0.145 vs. random 0.486 ⇒ clonal clustering, not division of labor)
· not covered: ① a family of functions, ② self-referential updating — this paper does not claim experimental evidence, and derives them only definitionally;
           there are only preliminary observations (E12 dynamic 0.849 vs. frozen 1.07; E13 identity chain verifiable for 8 generations)
· scale: small, reproducible, hand-checkable; not large-scale empirical work
```

**⇒ The positioning of this paper is "a definition + measurable criteria + illustrative experiments," not an empirical paper claiming that "life has been created."**
**Readers who wish to use these conclusions should cite them together with this boundary.**

## 4.7 Annotations

```
[corollary] the three necessary conditions follow directly from Sections 2 and 3; they are not independent assumptions
[evidence] condition ③ has experimental data (E1/E2/E8 + positive gain); conditions ①② have partial data (E12/E13)
[unresolved] whether satisfying all three counts as being "alive" — this paper does not claim so; this is what the next round of experiments must answer
[speculation] if the surplus S is insufficient, then no matter how complex the structure, it cannot be maintained ⇒ life has an "economic ceiling" (a directional speculation only)
```


---

# Section 5 · Why does today's AI exhibit emergence?

> Judgment of the current state (the core of this section): **many have observed emergence; no one has explained "why."**
> Existing explanations each cover a corner, and most are speculation; even "whether emergence really exists" is itself still disputed.

## 5.1 The phenomenon

After large models scale up, certain abilities seem to appear suddenly (multi-step reasoning, chain of thought, arithmetic…),
and the industry calls this **emergence**. Everyone uses this phenomenon, but—

```
observing emergence: many
explaining emergence: no accepted answer
```

## 5.2 Existing explanations (ordered by strength of evidence)

**① The metric-artifact account (the strongest counter-evidence)**

Schaeffer, Miranda, Koyejo 2023[3] "Are Emergent Abilities of Large Language Models a Mirage?"
```
claim: so-called emergence may be an artifact caused by the **nonlinearity/discontinuity of the evaluation metric**;
      switch to a continuous metric (such as log-likelihood) and the "jump" disappears, becoming a smooth rise
⇒ this shakes the very premise that "emergence is a real discontinuity"
```

**② Mechanistic explanation: induction heads and circuits (local mechanistic evidence, not a complete "why")**

Olsson et al. 2022[4] "In-context Learning and Induction Heads"
```
finding: an "induction head" circuit appears inside the model, explaining part of the in-context learning ability
⇒ this is **mechanism-level** evidence: it shows what structure implements a certain ability
⇒ but it only explains one specific ability, not the general question "why emergence occurs"
```

**③ Grokking: a cognitive phase transition during training**

Power et al. 2022[5] "Grokking"
```
on small algorithmic tasks, after long training generalization appears suddenly (like a phase transition)
⇒ shows that "emergence" also happens during training, and does not necessarily depend only on scale
```

**④ The compression account: prediction = compression**

Delétang et al. 2023[6] "Language Modeling Is Compression"
```
language model = compressor: the learned weights = a compression of the world's text
⇒ this is closest to the framework of this paper: emergence = structure that appears when compressing the world
⇒ but it is still a "correspondence at the level of results," and does not answer "why exactly at this scale/on this task"
```

## 5.3 Why there is still no accepted "why"

```
① scale experiments are uncontrollable: strict causal controls (changing only scale, everything else identical) cannot be performed
② metric dependence: change the metric and the phenomenon may disappear (see ①)
③ the mechanism level is incomplete: one knows a certain circuit, but not why the whole organizes that circuit
④ lack of a predictive theory: no theory can compute in advance "at what size a model will show what ability"
```

## 5.4 Our position ([speculation], not evidence for this paper): **AI is a decompression of human language**

**First look at this chain:**

```
universe F
 └ environment = a local decompression of the universe
    └ human language = the product of humans decompressing the environment (and their own experience)  ← language itself is already compressed
       └ AI = a **re-decompression** of human language (one more layer of compression on top of the human decompression)
```

**⇒ So AI's "emergence" is not understanding the universe, but structure surfacing when decompressing human language.**

**Seen with the ruler of Sections 2 and 3:**

```
· the model is a frozen function point (one point, not a family)
· its "emergence" appears on the **behavioral spectrum**: different inputs, different performance ⇒ it looks like it reasons
· but the model does not maintain this spectrum, does not change itself, does not pay a cost
⇒ it "has decompressed human language once," rather than "maintaining a decompression" or "rewriting the decompression rule itself"
```

**⇒ This yields a testable statement:**
**the "understanding" AI exhibits is essentially understanding of "human descriptions of the world," not understanding of the world itself.**
**It can decompress language, but the universe layer beyond language (energy, irreversibility, cost) it has never paid for, and hence has never been tested by it.**

## 5.4.1 The decay of decompressive capacity: a hard-wired upper layer ⇒ once the language changes, decompression weakens

**Human language keeps discovering new things; yet the model's decompression rule (the weights/upper layer) is hard-wired and stops changing once training ends. The two must fall out of alignment.**

```
source distribution moves: human language discovers new things ⇒ the object to be decompressed has changed
decompressor frozen: model weights unchanged     ⇒ what it decompresses is still **the old language**
⇒ compression gain falls: in gain_bits = log2 p_model − log2 p_base, p_model is out of alignment with the source
⇒ the understanding it "emerged" yesterday is an outdated decompression today
```

**Three consequences:**

```
① its decompressive capacity has a **fixed ceiling**: the ceiling is determined by the language at the moment of training, and does not rise as the language evolves
② it cannot make up the misalignment itself: the update rule is external — to recover, humans must retrain it once more
   ⇒ this is exactly the cost of "updating is external" described in Section 3
③ its "emergence" is **a decompression product at one time slice**, not a sustainable ability
```

**⇒ Put with the ruler of this paper:**
**life must let the decompressor move together with the world (self-referential updating + self-maintenance);**
**a frozen AI cannot do this — so once the language updates, its decompression weakens.**

## 5.5 Two predictions derived from the position ([speculation], for the reader to judge)

```
① if the world is replaced by the part not yet described by human language (regularities that cannot be learned from a corpus),
   AI's "emergence" should weaken markedly — because what it decompresses is language, not the universe
② if the model is made to pay its own cost (maintain itself, repair itself, die itself), language decompression will not be enough to support it,
    and it must develop a mode of understanding beyond language — otherwise it cannot survive
③ if human language undergoes a major structural update (a new paradigm/new conceptual system), the decompression gain of a frozen model
    should show a measurable decline; and it cannot recover by itself ⇒ recovery must come from external retraining
```

## 5.6 Annotations

```
[fact] the emergence phenomenon is widely observed; the metric-artifact account also has strong evidence (Schaeffer 2023)
[known] there are local explanations at the mechanism level (induction heads/circuits/grokking), and the compression view has a correspondence
[speculation] "emergence = the presentation of structure when compressing the world" — the position of this paper, not evidence
[unresolved] why it appears exactly at a certain scale/task ⇒ no one has given a predictive theory
[attitude of this paper] "AI emergence" is not taken as evidence that life exists; by the ruler of Section 3, it is not
[position of this paper] AI is a re-decompression of **human language** (the third layer of decompression: universe→environment→language→AI)
[corollary] a hard-wired upper layer ⇒ misalignment as soon as the language updates ⇒ decompressive capacity has a fixed ceiling and cannot self-recover
```

---

## Using it to look at a few popular questions

This section is application, not new evidence; each item follows directly from Sections 2–5.

**① Hallucination = forced decompression where there is no structure**
The decompressor must output structure; when the region of language corresponding to the input itself lacks compressible structure, it can only fabricate a "plausible-looking" structure ⇒ **hallucination is a necessary manifestation of decompression failure, not an occasional bug**.

**② Scaling laws still hold, precisely because the model dimension has not yet matched the language dimension**
Language is a **high-dimensional** structure, and its dimension is growing (new concepts = new dimensions; raising the dimension ⇒ compressibility rises). The model dimension is fixed at training time (D_M fixed), while the language dimension keeps growing (D_L(t) rising). The current observation is D_M << D_L(t) ⇒ continuing to add scale can capture more language dimensions ⇒ loss keeps falling (scaling appears still valid).
⇒ So the validity of scaling is not a counterexample to this paper's thesis, but evidence of "not yet matched."
⇒ Prediction: when D_M approaches the then-current D_L, the returns to scaling should flatten noticeably; while D_L keeps raising dimension ⇒ the gap reappears.
⇒ The fundamental problem of a frozen model: **its D_M is dead, while D_L is alive**.


**③ Uneven capabilities = different compressibility across language domains**
Domains with strong compressibility (clear structure, many examples) perform well; domains with weak compressibility (thin structure, few samples) perform poorly ⇒ the pattern of strengths and weaknesses is a mirror of the language distribution.

**④ Why RLHF is needed = it has no "self-cost" loop**
It cannot judge whether it decompresses correctly (no income/expenditure, it does not die from it), so humans must score it from outside ⇒ **the root of the alignment requirement is that it does not maintain itself**.

**⑤ Emergence = the presentation of language structure on the decompression product**
When scale crosses a threshold, certain language structures are squeezed out for the first time ⇒ it looks like "suddenly it can."

---
# Section 6 · At the level of measurement: existing work and the position of this paper

**Existing work (three aspects):**

- model-side dimension: measurement of the intrinsic dimension of token embeddings[12]
- temporal lag: identification of the temporal training boundary of large models[13]
- language-side complexity: measurement of language complexity from the constructionist perspective[14]

⇒ existing work has measured these three aspects **separately**; this paper strings them together: taking a "continuously updated model" as the reference frame, measure by domain the **rate of misalignment** between "new dimensions added on the language side" and "fixed dimensions on the model side." This is the position of this paper at the level of measurement.
## References

[1] Wigner E P. The unreasonable effectiveness of mathematics in the natural sciences[J].
    Communications in Pure and Applied Mathematics, 1960, 13(1): 1-14.

[2] Tegmark M. The mathematical universe[J]. Foundations of Physics, 2008, 38(2): 101-150.
    (arXiv:0704.0646)

[3] Schaeffer R, Miranda B, Koyejo S. Are emergent abilities of large language models a mirage?[C]
    // Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2304.15004.

[4] Olsson C, Elhage N, Nanda N, et al. In-context learning and induction heads[R].
    Transformer Circuits Thread, 2022. arXiv:2209.11895.

[5] Power A, Burda Y, Edwards H, et al. Grokking: Generalization beyond overfitting on small
    algorithmic datasets[C]. arXiv:2201.02177, 2022.

[6] Delétang G, Ruoss A, Duquenne P A, et al. Language modeling is compression[EB/OL].
    arXiv:2309.10668, 2023.

[7] Schrödinger E. What is Life?[M]. Cambridge: Cambridge University Press, 1944.

[8] Bennett C H. Logical depth and physical complexity[M]//Herken R. The Universal Turing Machine:
    A Half-Century Survey. Oxford: Oxford University Press, 1988: 227-257.

[9] Chaitin G J. Life as evolving software[EB/OL]. 2010. (the arXiv:1007.1471 series of work)

[10] Solomonoff R J. A formal theory of inductive inference[J]. Information and Control, 1964, 7(1): 1-22.
     Kolmogorov A N. Three approaches to the quantitative definition of information[J].
     Problems of Information Transmission, 1965, 1(1): 1-7.

[11] Friston K. The free-energy principle: a unified brain theory?[J].
     Nature Reviews Neuroscience, 2010, 11(2): 127-138.
---

## Author Statement (AI Usage Statement)

All questions, definitions, judgments, and conclusions in this paper were proposed by and are the responsibility of the author.
AI tools (DeepSeek) were used for: literature search, structural organization, language editing, and the writing and checking of experimental code.
All claims in the text were confirmed by the author; the AI bears no responsibility for the content of this paper.

*AI Usage Statement: The author is solely responsible for the ideas, arguments, and conclusions of this paper. An AI tool (DeepSeek) was used for literature search, structural organization, language editing, and writing/checking experimental code. All claims were reviewed and confirmed by the author. The AI bears no responsibility for the content.*

[12] Ohki T. Measuring intrinsic dimension of token embeddings[C]//The 39th Annual Conference of the Japanese Society for Artificial Intelligence (JSAI 2025), 2025.

[13] LLMLagBench: Identifying temporal training boundaries in large language models[EB/OL]. arXiv:2511.12116, 2025.

[14] Using constructions to measure developmental language complexity[J]. Cognitive Linguistics, 2024. doi:10.1515/cog-2023-0062.

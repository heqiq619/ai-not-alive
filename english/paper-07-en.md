# Paper 07 — The Limits of Large Models: The Engineering Wall, the Observation Wall, and the World-in-Itself Wall (Draft)

> He Qi · in collaboration with DeepSeek
> Series: Digital Life · Paper 07 (Draft, pending review)
> Date: 2026-10-22

---

## Abstract

This paper breaks the question "do large models have limits?" into three walls:

1. **The engineering wall**: the energy/compute efficiency of a single training run. This wall really exists and will be hit, but it is not "insufficient information capacity."
2. **The observation wall**: the data humans can collect comes mainly from the observable environmental layer (the everyday scale, essentially the classical-physics layer). A model can only decompress the world that has been observed.
3. **The world-in-itself wall**: the world function contains unobserved variables, counterfactuals, and causal mechanisms; finite data cannot determine it uniquely.

Conclusion: **"Limits" are the upper bounds of engineering and observation, not the upper bound of the world.** The world has not yet been fully measured, so capability has no endpoint; but the path of "scaling up a single body" will hit the engineering wall first, and the directions after that are modularization (cerebellum + coordinator) and new data layers (interaction, instruments, scientific experiments).

---

## 1. The Form of the Problem

Let the world function be `F(X)`, and let the model be an approximation of it, `f_θ`. The question is: to what degree can `f_θ` approximate `F`?

The three constraints are independent:

```
① Engineering constraint: how much energy/compute is needed to train f_θ
② Observation constraint: how much of F the data {X} can cover
③ Ontological constraint: whether F itself can be uniquely determined by finite data
```

---

## 2. The First Wall: The Engineering Wall (Energy)

Let us do an order-of-magnitude calculation (an approximate calculation, not exact values):

```
Landauer limit (room temperature): minimum energy to write 1 bit ≈ kT ln2 ≈ 3×10^-21 J
Global annual electricity generation: about 10^20 J
⇒ Information theoretically writable ≈ 3×10^40 bit
A 1-trillion-parameter model: about 10^12 bit
⇒ A gap of about 28 orders of magnitude
```

This shows that: **the energy wall is not a problem of "information does not fit", but a problem of engineering efficiency being extremely far from the theoretical limit.** Real training efficiency (the bits that can be written per joule) is far below the Landauer limit, so "take all the energy and use it for training" hits a wall in engineering first, not in information theory.

An important distinction: what energy determines is "how fast and how expensively the writing is done"; it **does not determine the source of information**. The information in the parameters comes from data, not from energy.

## 3. The Second Wall: The Observation Wall

The environment humans can observe directly is mainly the everyday scale — essentially the classical-physics layer: objects, organisms, society, language. The data collected by ordinary people lies almost entirely in this layer.

Deeper environmental layers (quantum, cosmic scale, microstructure) can only be observed indirectly through instruments: the data are sparse, and they carry measurement assumptions and theoretical mediation.

Thus:

```
· What the model decompresses is "the human-observable layer + human records"
· This layer it can learn in great detail (because there is a great deal of data)
· For deeper layers, it can only retell what humans have already decompressed
⇒ The model's understanding of the world is inherently layered and incomplete
```

## 4. The Third Wall: The World-in-Itself Wall

What the model learns is `P(data)`, not `F`. The world function contains:

- variables that have not been observed;
- counterfactuals (what would happen if ...);
- causal mechanisms (rather than correlations).

Finite observational data cannot uniquely determine these. **Where there is no data, no amount of parameters is anything more than a prior.**

Therefore, even if engineering and observation were both unconstrained, the goal of "containing the real world" would not hold in itself: what the parameters contain is the observed regularities, not the world-in-itself.

## 5. The Position of the World Model

From the layering above, we can give "world model" a precise position:

```
· World model = the interaction decompressor of the classical observable layer (physics, causality, consequences of action)
· Language model = the decompressor of the human semantic layer
```

The two do not compete, but they share the same upper bound: both can only compress the layer that "humans are able to observe/record".

On efficiency: language is data that humans have already compressed; a world model needs to collect raw interaction data anew, and the cost for the same amount of information is several orders of magnitude higher. Therefore:

- **A death sentence for "a world model covers general intelligence"** — it can only cover the classical interaction layer, and its cost structure is worse;
- **A statement of necessity for "a world model supplements the interaction layer"** — language contains almost no knowledge of motion, contact, or manipulation.

## 6. After Hitting the Wall: Cerebellarization

Continuing to increase the dimensions of a monolithic model will hit the engineering wall first (compute, memory, electricity, training stability, data supply). At that point the viable direction is not "a larger monolith", but:

```
Many specialized small models (cerebella) + one coordinator
· Each cerebellum covers a narrow domain deeply (high fit)
· The coordinator handles scheduling, verification, and composition
⇒ Composition is used to obtain a larger "effective dimension"
```

The cost must be stated explicitly: the **effective dimension of composition grows more slowly than parameter stacking** (interfaces, communication, coordination losses), but it is the only direction that can still grow after the engineering ceiling. This is consistent with biological systems: the brain is not an infinitely scaled monolithic network, but modularization + coordination.

## 7. Dimension and Fit (Connection to Paper 02 v3)

Paper 02 v3 proposed the distinction:

```
Coverage (total dimension): the total amount of structure that can be represented — determined by capacity
Fit (effective dimension): the part of it that is aligned with the target structure — determined by data and the training distribution
```

The three walls of this paper correspond exactly:

```
· The engineering wall limits the growth of "coverage"
· The observation wall limits the direction of "fit" (it can only fit the observed layer)
· The world-in-itself wall determines that "fit" is never "completely fitting F"
```

## 8. Conclusion

```
① "The limits of large models" = the engineering wall + the observation wall, not the limits of the world
② The engineering wall arrives first: the path of scaling up a monolith fails first
③ After that it relies on: modularization (cerebella) + new data layers (interaction/instruments/experiments)
④ The world has not been fully measured ⇒ capability has no endpoint, only walls of a given stage
```

**The positioning of this paper: it is not a prophecy, but a breaking of "limits" into three walls that can be discussed separately and verified separately.**

---

## Appendix: Speculations That Must Be Flagged

- The order-of-magnitude calculation in Section 2 is approximate; the Landauer limit only gives a theoretical lower bound and does not constitute an engineering prediction;
- "Cerebellarization is the only direction" is [speculation]: new training paradigms may also emerge that allow monoliths to continue scaling;
- The division of labor between world models and language models is a framework-level judgment and requires controlled experiments on specific tasks.

> This paper was written by He Qi, with DeepSeek (AI) assisting in the organization; the views and responsibility belong to the author.

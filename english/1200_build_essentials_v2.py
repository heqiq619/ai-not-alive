# -*- coding: utf-8 -*-
"""1200_build_essentials_v2.py — 组装 English Essentials v2（11 篇）"""
import io, os, re

DL = r"C:/DS/数字生命/"
E = DL + "english/"

ess_v1 = io.open(DL + "数字生命-English-Essentials.md", encoding="utf-8").read()
lines = ess_v1.splitlines()

def find_idx(prefix):
    for i, ln in enumerate(lines):
        if ln.startswith(prefix):
            return i
    raise ValueError(prefix)

i0 = find_idx("## Paper 0 ·")
i1 = find_idx("## Paper 1 ·")
i32 = find_idx("## Paper 32 ·")
seg0 = "\n".join(lines[i0:i1]).strip()
seg1 = "\n".join(lines[i1:i32]).strip()
seg32 = "\n".join(lines[i32:]).strip()

def demote_v1(text):
    out = []
    for ln in text.splitlines():
        if ln.startswith("## Paper "):
            out.append("### " + ln[3:])
        elif ln.startswith("### "):
            out.append("##### " + ln[4:])
        elif ln.startswith("## "):
            out.append("#### " + ln[3:])
        else:
            out.append(ln)
    return "\n".join(out)

def demote_h1(text):
    out = []
    for ln in text.splitlines():
        if ln.startswith("### "):
            out.append("##### " + ln[4:])
        elif ln.startswith("## "):
            out.append("#### " + ln[3:])
        elif ln.startswith("# "):
            out.append("### " + ln[2:])
        else:
            out.append(ln)
    return "\n".join(out)

def read(p):
    return io.open(p, encoding="utf-8").read().strip()

p12 = demote_h1(read(E + "paper-12-en.md"))
p13 = demote_h1(read(E + "paper-13-en.md"))
p36 = demote_h1(read(E + "paper-36-en.md"))
b = demote_h1(read(E + "appendix-b-concept-map-en.md"))
p44 = demote_h1(read(E + "paper-44-en.md"))
p45 = demote_h1(read(E + "paper-45-en.md"))

a = demote_h1(read(E + "paper-15-en.md"))
a = a.replace("### Paper 15 (Draft) · Thickness and Dimension: A Geometric Picture of the Residual",
              "### Appendix A · Thickness and Dimension: A Geometric Picture of the Residual", 1)
c = demote_h1(read(DL + "散论-断崖与缓坡-en.md"))
c = c.replace("### Essay: Cliffs and Slopes — Where Does Digital Life Grow From?",
              "### Appendix C · Cliffs and Slopes: Where Does Digital Life Grow From?", 1)
b = b.replace("### Concept Map · Glossary (v3, English translation)",
              "### Appendix B · Concept Map and Glossary (v3, English translation)", 1)

preface = """## Preface

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

"""

tail = """
---

# Part IV — Appendices

"""

parts = [
    preface,
    demote_v1(seg0), "\n\n---\n\n",
    demote_v1(seg1), "\n\n---\n\n",
    "# Part II — Theory\n\n",
    p12, "\n\n---\n\n",
    p13, "\n\n---\n\n",
    demote_v1(seg32), "\n\n---\n\n",
    p36, "\n\n---\n\n",
    "# Part III — Engineering Observations\n\n",
    p44, "\n\n---\n\n",
    p45,
    tail,
    a, "\n\n---\n\n",
    b, "\n\n---\n\n",
    c, "\n",
]

head = """# Digital Life: A Measurable Definition of Life

## English Essentials (v2)

> He Qi · in collaboration with DeepSeek
> Digital Life Series · English Essentials
> Date: 2026-11-02
> Status: selected English edition (11 pieces). New translations dated 2026-11-02; earlier translations based on the October 2026 editions. The Chinese edition is authoritative.

"""

out = head + "\n".join(parts)
path = DL + "数字生命-English-Essentials-v2.md"
io.open(path, "w", encoding="utf-8").write(out)
print("written:", path)
print("chars:", len(out))
for t in ["# Part I", "# Part II", "# Part III", "# Part IV"]:
    print(t, "->", out.count(t))

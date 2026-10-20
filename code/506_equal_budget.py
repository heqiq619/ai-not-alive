# -*- coding: utf-8 -*-
"""506_equal_budget.py · 等数据预算对照：分离「数据量」与「概念新旧」

设计（预算 N 固定 = 最早一年的训练文档数）：
  A：只用最早年份的 N 篇训练（旧概念）
  B：从全部年份均匀采样 N 篇训练（混合）
  C：只用**最近**年份的 N 篇训练（新概念）
在最后一年测试集与第一年测试集上比较 bits/token：
  · 若 C 在新测试集显著优于 A ⇒ 概念新旧有独立效应（不是数据量）
  · 若 B/C 在旧测试集也更好 ⇒ 说明有新数据本身就有用
"""
import os, sys, io, glob, re, math
import numpy as np
from collections import Counter

EN = re.compile(r'[a-z][a-z0-9_\-]*')
VOCAB_MAX = 30000

def load(d):
    docs = []
    for f in sorted(glob.glob(os.path.join(d, '*.txt'))):
        try:
            t = io.open(f, encoding='utf-8-sig', errors='ignore').read().lower()
        except Exception:
            continue
        w = EN.findall(t)
        if len(w) >= 20:
            docs.append(w)
    return docs

def vocab_of(docs):
    c = Counter()
    for d in docs: c.update(d)
    return {w: i for i, (w, _) in enumerate(c.most_common(VOCAB_MAX))}

def to_ids(docs, vocab):
    oov = len(vocab)
    return [[vocab.get(w, oov) for w in d] for d in docs]

class NG:
    def __init__(self, n, V, k=0.1):
        self.n, self.V, self.k = n, V + 1, k
        self.c = Counter(); self.h = Counter()
    def train(self, sents):
        n = self.n
        for s in sents:
            for i in range(len(s)):
                g = tuple(s[max(0, i - n + 1):i + 1])
                self.c[g] += 1
                if len(g) >= 2: self.h[g[:-1]] += 1
    def ce(self, sents):
        n = self.n; tot = 0.0; cnt = 0
        for s in sents:
            for i in range(len(s)):
                pref = tuple(s[max(0, i - n + 1):i])
                num = self.c.get(pref + (s[i],), 0) + self.k
                den = self.h.get(pref, 0) + self.k * self.V
                tot += -math.log2(num / den); cnt += 1
        return tot / max(1, cnt)

def sample(docs, n, rng):
    if len(docs) <= n:
        return list(docs)
    idx = rng.choice(len(docs), size=n, replace=False)
    return [docs[i] for i in idx]

def main():
    dirs = sys.argv[1:]
    if len(dirs) < 2:
        print(__doc__); return
    years = [os.path.basename(d.rstrip('/\\')) for d in dirs]
    rng = np.random.RandomState(0)
    print('=== 等数据预算对照 ===', flush=True)
    docs = [load(d) for d in dirs]
    for y, ds in zip(years, docs):
        print('  %s: %d 篇' % (y, len(ds)), flush=True)
    def sp(ds, frac=0.6):
        m = max(1, int(len(ds) * frac)); return ds[:m], ds[m:]
    trains, tests = [], []
    for ds in docs:
        a, b = sp(ds); trains.append(a); tests.append(b)
    all_train = [w for tr in trains for w in tr]
    vocab = vocab_of(all_train)
    N = len(trains[0])
    print('  预算 N = %d 篇（= %s 训练集大小）' % (N, years[0]), flush=True)

    A = NG(3, len(vocab)); A.train(to_ids(trains[0][:N], vocab))
    Bdocs = sample(all_train, N, rng)
    B = NG(3, len(vocab)); B.train(to_ids(Bdocs, vocab))
    Cd = sample(trains[-1], N, rng)
    C = NG(3, len(vocab)); C.train(to_ids(Cd, vocab))

    last_test = to_ids(tests[-1], vocab)
    first_test = to_ids(tests[0], vocab)
    rows = [('A 只用最早年份', A), ('B 混合全部年份', B), ('C 只用最近年份', C)]
    print('\n  %-16s %14s %14s' % ('模型', '%s测试' % years[-1], '%s测试' % years[0]))
    for name, m in rows:
        print('  %-16s %13.3f %13.3f' % (name, m.ce(last_test), m.ce(first_test)), flush=True)
    print('\n  解读要点：')
    print('   · C 在新测试集优于 A ⇒ 概念新鲜度有独立价值')
    print('   · 若三者在旧测试集上也差异很大 ⇒ 数据分布差异本身有影响')

if __name__ == '__main__':
    main()

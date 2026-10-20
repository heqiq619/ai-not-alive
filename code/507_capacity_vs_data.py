# -*- coding: utf-8 -*-
"""507_capacity_vs_data.py · 加容量 vs 换数据：参数能否补偿语言升维

固定数据量 N=1800 篇。分三组，仅改变 n-gram 阶数（容量代理）：
  OLD  : 只用 2018 训练
  MIX  : 从 4 年均匀采样
  REC  : 只用 2024
评估：2024 测试集 bits/token。
若 OLD 曲线随阶数上升能追平 MIX ⇒ 参数可补偿升维；否则 ⇒ 数据不可替代。
"""
import os, sys, io, glob, re, math
import numpy as np
from collections import Counter

EN = re.compile(r'[a-z][a-z0-9_\-]*')
MAXW = 30000

def load(d):
    docs = []
    for f in sorted(glob.glob(os.path.join(d, '*.txt'))):
        try:
            t = io.open(f, encoding='utf-8-sig', errors='ignore').read().lower()
        except Exception:
            continue
        w = EN.findall(t)
        if len(w) >= 20: docs.append(w)
    return docs

def vocab_of(docs):
    c = Counter()
    for d in docs: c.update(d)
    return {w: i for i, (w, _) in enumerate(c.most_common(MAXW))}

def ids(docs, V):
    o = len(V); return [[V.get(w, o) for w in d] for d in docs]

class NG:
    def __init__(self, n, V, k=0.1):
        self.n, self.V, self.k = n, V + 1, k
        self.c = Counter(); self.h = Counter()
    def train(self, ss):
        n = self.n
        for s in ss:
            for i in range(len(s)):
                g = tuple(s[max(0, i - n + 1):i + 1])
                self.c[g] += 1
                if len(g) >= 2: self.h[g[:-1]] += 1
    def ce(self, ss):
        n = self.n; t = 0.0; c = 0
        for s in ss:
            for i in range(len(s)):
                pref = tuple(s[max(0, i - n + 1):i])
                num = self.c.get(pref + (s[i],), 0) + self.k
                den = self.h.get(pref, 0) + self.k * self.V
                t += -math.log2(num / den); c += 1
        return t / max(1, c)

def main():
    dirs = sys.argv[1:]
    if len(dirs) < 4:
        print('需要 4 个年份目录'); return
    rng = np.random.RandomState(0)
    docs = [load(d) for d in dirs]
    years = [os.path.basename(d.rstrip('/\\')) for d in dirs]
    print('=== 加容量 vs 换数据 ===', flush=True)
    def sp(ds, frac=0.6):
        m = max(1, int(len(ds) * frac)); return ds[:m], ds[m:]
    tr, te = [], []
    for ds in docs:
        a, b = sp(ds); tr.append(a); te.append(b)
    alltr = [w for t in tr for w in t]
    V = vocab_of(alltr)
    N = len(tr[0])
    def smp(src, n):
        if len(src) <= n: return list(src)
        idx = rng.choice(len(src), size=n, replace=False)
        return [src[i] for i in idx]
    old_d = tr[0][:N]
    mix_d = smp(alltr, N)
    rec_d = smp(tr[-1], N)
    test = ids(te[-1], V)
    print('  N=%d 篇；测试=%s 留出 %d 篇' % (N, years[-1], len(te[-1])), flush=True)
    print('\n  %-6s %12s %12s %12s' % ('阶数', 'OLD', 'MIX', 'REC'), flush=True)
    for n in (2, 3, 4, 5):
        row = []
        for name, dd in (('old', old_d), ('mix', mix_d), ('rec', rec_d)):
            m = NG(n, len(V)); m.train(ids(dd, V))
            row.append(m.ce(test))
        print('  %-6d %12.3f %12.3f %12.3f' % (n, row[0], row[1], row[2]), flush=True)
    print('\n  解读：若 OLD 列随阶数下降并能追平 MIX ⇒ 参数可补偿升维；')
    print('        否则 ⇒ 新数据/新概念不可替代。')

if __name__ == '__main__':
    main()

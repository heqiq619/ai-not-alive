# -*- coding: utf-8 -*-
"""508_backoff_capacity.py · 带插值的 n-gram：真正的容量测试

修正 507 的问题：无回退的高阶 n-gram 会因稀疏变差。
本脚本用 Jelinek-Mercer 插值：
    p(w|ctx_m) = λ·p_ML(w|ctx_m) + (1-λ)·p(w|ctx_{m-1})
    p(w) = 加一平滑
⇒ 阶数越高 = 容量越大 = CE 应单调下降（数据够时）

容量代理：最大阶数 m = 2,3,4,5,6
三组同数据量 N=1800：OLD(2018) / MIX(4年均匀) / REC(2024)
问题：OLD 加大容量能否追平 MIX？⇒ 参数可否补偿升维
"""
import os, sys, io, glob, re, math
import numpy as np
from collections import Counter, defaultdict

EN = re.compile(r'[a-z][a-z0-9_\-]*')
MAXW = 30000
LAM = 0.8          # 插值权重
MAX_ORDER = 6

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

class InterpNG:
    def __init__(self, V, max_order=MAX_ORDER, lam=LAM):
        self.V = V + 1; self.M = max_order; self.lam = lam
        self.c = [defaultdict(Counter) for _ in range(max_order + 1)]
        self.tot = [dict() for _ in range(max_order + 1)]
        self.uni = Counter(); self.uni_tot = 0
    def train(self, sents):
        for s in sents:
            for i, w in enumerate(s):
                self.uni[w] += 1; self.uni_tot += 1
                for k in range(1, min(self.M, i) + 1):
                    pref = tuple(s[i - k:i])
                    self.c[k][pref][w] += 1
                    self.tot[k][pref] = self.tot[k].get(pref, 0) + 1
    def logp(self, w, hist):
        p = (self.uni.get(w, 0) + 1.0) / (self.uni_tot + self.V)
        for k in range(1, min(self.M, len(hist)) + 1):
            pref = tuple(hist[-k:])
            cw = self.c[k].get(pref, {}).get(w, 0)
            ct = self.tot[k].get(pref, 0)
            if ct > 0:
                p = self.lam * (cw / ct) + (1 - self.lam) * p
        return p
    def ce(self, sents, upto=None):
        M = self.M if upto is None else upto
        old_M, self.M = self.M, M
        tot = 0.0; cnt = 0
        for s in sents:
            for i, w in enumerate(s):
                p = self.logp(w, s[max(0, i - MAX_ORDER):i])
                tot += -math.log2(max(p, 1e-12)); cnt += 1
        self.M = old_M
        return tot / max(1, cnt)

def main():
    dirs = sys.argv[1:]
    if len(dirs) < 4: print('需要4个年份目录'); return
    rng = np.random.RandomState(0)
    docs = [load(d) for d in dirs]
    years = [os.path.basename(d.rstrip('/\\')) for d in dirs]
    print('=== 带插值的容量测试 ===', flush=True)
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
    groups = {'OLD': tr[0][:N], 'MIX': smp(alltr, N), 'REC': smp(tr[-1], N)}
    test = ids(te[-1][:600], V)
    print('  N=%d；测试 %s 留出 %d 篇' % (N, years[-1], len(test)), flush=True)
    models = {}
    for name, dd in groups.items():
        m = InterpNG(len(V)); m.train(ids(dd, V)); models[name] = m
        print('  训练完成: %s (%d 篇)' % (name, len(dd)), flush=True)
    print('\n  %-8s %10s %10s %10s %12s' % ('最大阶', 'OLD', 'MIX', 'REC', 'OLD−MIX'))
    for m in (2, 3, 4, 5, 6):
        row = {name: models[name].ce(test, upto=m) for name in groups}
        print('  %-8d %10.3f %10.3f %10.3f %+12.3f'
              % (m, row['OLD'], row['MIX'], row['REC'], row['OLD'] - row['MIX']), flush=True)
    print('\n  解读：OLD−MIX 随阶数缩小甚至消失 ⇒ 参数可补偿；持续为正 ⇒ 数据不可替代。')

if __name__ == '__main__':
    main()

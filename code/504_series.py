# -*- coding: utf-8 -*-
"""504_series.py · 多年份 v_L 与失配序列

用法:
  python 504_series.py <年目录1> <年目录2> [<年目录3> ...]
  例如:
  python 504_series.py 语料\2018 语料\2020 语料\2022 语料\2024

每对相邻年份报告:
  · 新概念占比（df>=3 且上一年未出现）  ⇒ 升维速率 v_L (%/年)
  · 3-gram 失配 M = CE(旧模型②新语料) − CE(新模型②新语料)  （bits/token）
  · 对照：在旧语料上反向差值
"""
import os, sys, io, glob, re, math
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

def vocab_of(docs, maxn=VOCAB_MAX):
    c = Counter()
    for d in docs: c.update(d)
    return {w: i for i, (w, _) in enumerate(c.most_common(maxn))}

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

def new_share(old_docs, new_docs, min_df=3):
    def df(docs):
        c = Counter()
        for d in docs: c.update(set(d))
        return c
    o, n = df(old_docs), df(new_docs)
    newt = {t: v for t, v in n.items() if v >= min_df and o.get(t, 0) == 0}
    tok = sum(len(d) for d in new_docs)
    return len(newt), sum(newt.values()) / max(1, tok) * 100.0, newt

def analyze(dirs, years, span=2.0):
    print('=== 多年份序列（cs.AI）===')
    print('  %-14s %8s %8s %10s %10s' % ('年份对', '新词占比', 'v_L(%/年)', 'M(bits/tok)', '对照'))
    for i in range(len(dirs) - 1):
        o = load(dirs[i]); n = load(dirs[i + 1])
        if not o or not n:
            print('  语料不足:', dirs[i]); continue
        def sp(docs, frac=0.6):
            m = max(1, int(len(docs) * frac)); return docs[:m], docs[m:]
        o_tr, o_te = sp(o); n_tr, n_te = sp(n)
        vocab = vocab_of(o_tr + n_tr)
        ids = lambda ds: to_ids(ds, vocab)
        mo = NG(3, len(vocab)); mo.train(ids(o_tr))
        mn = NG(3, len(vocab)); mn.train(ids(n_tr))
        n_te_i = ids(n_te); o_te_i = ids(o_te)
        M = mo.ce(n_te_i) - mn.ce(n_te_i)
        Mctl = mo.ce(o_te_i) - mn.ce(o_te_i)
        cnt, share, _ = new_share(o, n)
        print('  %-14s %7.2f%% %7.2f %+10.3f %+10.3f'
              % ('%s→%s' % (years[i], years[i + 1]), share, share / span, M, Mctl))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(0)
    dirs = sys.argv[1:]
    years = [os.path.basename(d.rstrip('/\\')) for d in dirs]
    span = 2.0
    analyze(dirs, years, span)

# -*- coding: utf-8 -*-
"""505_cumulative_mismatch.py · 修正版失配测量：累积参照系

修正 503/504 的方法错误：
  旧做法：旧模型(仅旧语料) vs 新模型(仅新语料)  ⇒ 对称差异，测不出「落后」
  新做法：旧模型(仅旧语料) vs **累积模型(全部语料)** 在同一测试集上比较
        ⇒ M > 0 才真正意味着「不更新就落后」

用法:
  python 505_cumulative_mismatch.py <年目录1> <年目录2> ... <最后一年>
  例: python 505_cumulative_mismatch.py 语料\2018 语料\2020 语料\2022 语料\2024

对每个截止年 c（不含最后一年）报告：
  M      = CE(旧模型, 最后一年留出) − CE(累积模型, 最后一年留出)
  M_ctl  = CE(旧模型, 第一年留出)   − CE(累积模型, 第一年留出)
  （M_ctl 应 ≤ 0：累积模型包含旧语料，不应更差）
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

def main():
    dirs = sys.argv[1:]
    if len(dirs) < 2:
        print(__doc__); return
    years = [os.path.basename(d.rstrip('/\\')) for d in dirs]
    print('=== 累积参照系失配 ===')
    print('  载入语料...', flush=True)
    all_docs = [load(d) for d in dirs]
    for y, ds in zip(years, all_docs):
        print('    %s: %d 篇' % (y, len(ds)), flush=True)
    # 每一年切 train/test
    def sp(docs, frac=0.6):
        m = max(1, int(len(docs) * frac)); return docs[:m], docs[m:]
    trains, tests = [], []
    for ds in all_docs:
        a, b = sp(ds); trains.append(a); tests.append(b)
    vocab = vocab_of([w for tr in trains for w in tr])
    print('  词表 %d' % len(vocab), flush=True)
    # 累积模型（全部训练集）
    cum = NG(3, len(vocab)); cum.train(to_ids([w for tr in trains for w in tr], vocab))
    print('  累积模型训练完成', flush=True)
    last_test = to_ids(tests[-1], vocab)
    first_test = to_ids(tests[0], vocab)
    ce_cum_last = cum.ce(last_test)
    ce_cum_first = cum.ce(first_test)
    print('\n  累积模型: 最后一年测试 %.3f | 第一年测试 %.3f bits/token'
          % (ce_cum_last, ce_cum_first))
    print('\n  %-10s %10s %10s %10s %10s' % ('截止年', 'M(新测试)', 'M_ctl(旧测试)', '旧模型@新', '旧模型@旧'))
    for c in range(len(dirs) - 1):
        old_tr = [w for tr in trains[:c + 1] for w in tr]
        mo = NG(3, len(vocab)); mo.train(to_ids(old_tr, vocab))
        ce_o_last = mo.ce(last_test)
        ce_o_first = mo.ce(first_test)
        M = ce_o_last - ce_cum_last
        Mctl = ce_o_first - ce_cum_first
        print('  %-10s %+10.3f %+12.3f %10.3f %10.3f'
              % (years[c], M, Mctl, ce_o_last, ce_o_first), flush=True)

if __name__ == '__main__':
    main()

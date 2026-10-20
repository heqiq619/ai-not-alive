# -*- coding: utf-8 -*-
"""503_mismatch_ngram.py · 不该训练的「失配」测量：旧模型解释新语料要多少比特

核心（M(K) 的极简版，不需要下载大模型）：
  用 2018 语料训练一个 n-gram 语言模型（=「只有旧概念」）
  用 2024 语料训练另一个（=「有新概念」）
  在同一份 2024 测试集上算 bits/token：
      M = CE(旧模型 @ 2024测试) − CE(新模型 @ 2024测试)
  M > 0 ⇒ 旧概念解释新语料更贵 ⇒ 存在不可约的新维度

对照：在 2018 测试集上反过来应出现 M' < 0（旧模型更好）
     ⇒ 说明差异不是"数据难度"，而是"概念新旧"

用法:
  python 503_mismatch_ngram.py <语料根> [grams] [smooth]
  默认读 根/cs_AI/old 与 根/cs_AI/new
"""
import os, sys, io, glob, re, math
from collections import Counter

EN = re.compile(r'[a-z][a-z0-9_\-]*')
VOCAB_MAX = 30000

def load_docs(d):
    files = sorted(glob.glob(os.path.join(d, '*.txt')))
    docs = []
    for f in files:
        try:
            t = io.open(f, encoding='utf-8-sig', errors='ignore').read().lower()
        except Exception:
            continue
        docs.append(EN.findall(t))
    return [x for x in docs if len(x) >= 20]

def build_vocab(docs, maxn=VOCAB_MAX):
    c = Counter()
    for d in docs: c.update(d)
    vocab = {w: i for i, (w, _) in enumerate(c.most_common(maxn))}
    return vocab

def to_ids(docs, vocab):
    oov = len(vocab)
    return [[vocab.get(w, oov) for w in d] for d in docs]

class NGram:
    def __init__(self, n, vocab_size, smooth=0.1):
        self.n = n; self.V = vocab_size + 1; self.k = smooth
        self.c = Counter()          # n-gram counts
        self.hist = Counter()       # (n-1)-gram prefix counts
    def train(self, sents):
        n = self.n
        for s in sents:
            for i in range(len(s)):
                gram = tuple(s[max(0, i - n + 1):i + 1])
                self.c[gram] += 1
                if len(gram) >= 2:
                    self.hist[gram[:-1]] += 1
    def logprob(self, sents):
        n = self.n; tot = 0.0; cnt = 0
        for s in sents:
            for i in range(len(s)):
                w = s[i]
                pref = tuple(s[max(0, i - n + 1):i])
                num = self.c.get(pref + (w,), 0) + self.k
                den = self.hist.get(pref, 0) + self.k * self.V
                tot += -math.log2(num / den); cnt += 1
        return tot / max(1, cnt)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser('~'), 'Desktop', 'arxiv_语料')
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    k = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
    old = load_docs(os.path.join(root, 'cs_AI', 'old'))
    new = load_docs(os.path.join(root, 'cs_AI', 'new'))
    if not old or not new:
        print('语料缺失'); return
    # 切分：new 分成 new_train / new_test；old 分成 old_train / old_test
    def split(docs, frac=0.6):
        m = max(1, int(len(docs) * frac))
        return docs[:m], docs[m:]
    o_tr, o_te = split(old)
    n_tr, n_te = split(new)
    vocab = build_vocab(o_tr + n_tr)
    id_o = lambda ds: to_ids(ds, vocab)
    o_tr_i, o_te_i = id_o(o_tr), id_o(o_te)
    n_tr_i, n_te_i = id_o(n_tr), id_o(n_te)
    print('=== 失配测量（%s）===' % (' '.join([str(n)] + ['gram'])))
    print('  旧模型: 训练 %d 篇(2018)   新模型: 训练 %d 篇(2024)' % (len(o_tr), len(n_tr)))
    print('  测试: 2018 留出 %d 篇 / 2024 留出 %d 篇' % (len(o_te), len(n_te)))
    print('  词表 %d' % len(vocab))
    M_old = NGram(n, len(vocab), k); M_old.train(o_tr_i)
    M_new = NGram(n, len(vocab), k); M_new.train(n_tr_i)
    ce_o_on_new = M_old.logprob(n_te_i)
    ce_n_on_new = M_new.logprob(n_te_i)
    ce_o_on_old = M_old.logprob(o_te_i)
    ce_n_on_old = M_new.logprob(o_te_i)
    print('\n  [2024 测试集]')
    print('    旧模型(只懂2018): %.3f bits/token' % ce_o_on_new)
    print('    新模型(懂2024)  : %.3f bits/token' % ce_n_on_new)
    print('    M = 旧 − 新     : %+.3f bits/token   ← 核心数字' % (ce_o_on_new - ce_n_on_new))
    print('\n  [2018 测试集 · 对照]')
    print('    旧模型: %.3f | 新模型: %.3f | 差 %+.3f bits/token'
          % (ce_o_on_old, ce_n_on_old, ce_o_on_old - ce_n_on_old))
    print('\n  解读：M>0 且对照为负 ⇒ 新语料里确实有「旧概念解释不了」的部分；')

if __name__ == '__main__':
    main()

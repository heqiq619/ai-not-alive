# -*- coding: utf-8 -*-
"""501_vl_newterm.py · 用「新概念出现率」测领域升维速率 v_L

用法:
  python 501_vl_newterm.py <语料根目录> [跨度年数]
  或
  python 501_vl_newterm.py <旧语料目录> <新语料目录> [跨度年数]

目录约定（推荐）:
  语料/AI/old/*.txt      语料/AI/new/*.txt
  语料/医学/old/*.txt    语料/医学/new/*.txt
  脚本会按每个领域分别报告。

输出:
  · 词表规模、新词数、新词占比（按词频加权）
  · v_L 代理 = 新词占比 / 跨度年数
  · 前 20 个新概念（1-gram 与 2-gram）
"""
import os, sys, io, glob, re
from collections import Counter

EN = re.compile(r'[A-Za-z][A-Za-z0-9_\-]*')
CJK = re.compile(r'[\u4e00-\u9fff]+')

def tokens_of(text):
    """英文按词；中文按 2~3 字词片（不依赖分词库）"""
    text = text.lower()
    toks = EN.findall(text)
    for run in CJK.findall(text):
        for n in (2, 3):
            for i in range(len(run) - n + 1):
                toks.append(run[i:i + n])
    return toks
MAX_CHARS = 4000
MAX_DOCS = 20000
MIN_DF = 3          # 新词至少出现在这么多篇里才算（过滤噪声）

def load_dir(d):
    files = sorted(glob.glob(os.path.join(d, '*.txt')))[:MAX_DOCS]
    docs = []
    for f in files:
        try:
            t = io.open(f, encoding='utf-8-sig', errors='ignore').read()
        except Exception:
            continue
        t = ' '.join(t.split())[:MAX_CHARS]
        if len(t) >= 50:
            docs.append(t)
    return docs

def terms_of(docs):
    """返回 (1-gram df 计数, 2-gram df 计数, 总词数)"""
    uni = Counter(); bi = Counter(); total = 0
    for t in docs:
        toks = tokens_of(t)
        total += len(toks)
        uni.update(set(toks))
        bigrams = set(zip(toks, toks[1:]))
        bi.update({' '.join(b) for b in bigrams})
    return uni, bi, total

def analyze(domain, old_docs, new_docs, span_years):
    u_o, b_o, tok_o = terms_of(old_docs)
    u_n, b_n, tok_n = terms_of(new_docs)
    if not old_docs or not new_docs:
        print('  [%s] 语料不足，跳过' % domain); return
    # 新词：新语料 df>=MIN_DF 且旧语料 df==0（1-gram 与 2-gram 合并）
    new_terms = {}
    for term, df in u_n.items():
        if df >= MIN_DF and u_o.get(term, 0) == 0:
            new_terms[term] = df
    for term, df in b_n.items():
        if df >= MIN_DF and b_o.get(term, 0) == 0 and ' ' in term:
            new_terms[term] = df
    # 新词在「新语料总词数」里的占比（按 df 加权近似）
    new_token_mass = sum(new_terms.values())
    share = new_token_mass / max(1, tok_n) * 100.0
    v_l = share / max(0.1, span_years)
    print('  [%s] 旧文档 %d / 新文档 %d；词表 %d → %d'
          % (domain, len(old_docs), len(new_docs), len(u_o), len(u_n)))
    print('    新概念数 %d，新词占比 %.2f%%，v_L(代理) = %.3f %%/年'
          % (len(new_terms), share, v_l))
    top = sorted(new_terms.items(), key=lambda kv: -kv[1])[:20]
    print('    新概念 Top20: ' + '、'.join(t for t, _ in top))

def discover(root):
    """找 根/领域/old, 根/领域/new"""
    pairs = []
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d)
        if not os.path.isdir(p): continue
        old = os.path.join(p, 'old'); new = os.path.join(p, 'new')
        if os.path.isdir(old) and os.path.isdir(new):
            pairs.append((d, load_dir(old), load_dir(new)))
    return pairs

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    if len(sys.argv) >= 3 and os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]) \
       and not os.path.isdir(os.path.join(sys.argv[1], 'old')):
        old_docs = load_dir(sys.argv[1]); new_docs = load_dir(sys.argv[2])
        span = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0
        analyze('对比', old_docs, new_docs, span)
        return
    root = sys.argv[1]
    span = float(sys.argv[2]) if len(sys.argv) > 2 else 5.0
    pairs = discover(root)
    if not pairs:
        print('未找到 根/领域/old 与 根/领域/new 结构'); return
    print('=== 新概念出现率分析（跨度 %.1f 年）===' % span)
    for name, o, n in pairs:
        analyze(name, o, n, span)

if __name__ == '__main__':
    main()

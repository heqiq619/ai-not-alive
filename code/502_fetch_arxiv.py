# -*- coding: utf-8 -*-
"""502_fetch_arxiv.py · 按分类+年份抓 arXiv 标题+摘要，存成 old/new 供 501 分析

用法:
  python 502_fetch_arxiv.py <分类> <旧年> <新年> [根目录] [每边条数]

例子:
  python 502_fetch_arxiv.py cs.AI 2018 2024
   ⇒ 生成 根目录/cs_AI/old/*.txt 与 根目录/cs_AI/new/*.txt

说明:
  · 用 arXiv API（export.arxiv.org），免费、无需登录
  · 每篇存：标题 + 摘要
  · 按提交日期过滤年份
  · 自动分页（每页 100 条）
"""
import os, sys, time, io, ssl, urllib.request, urllib.parse
_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE   # 本机缺 CA 证书：关闭校验（仅抓公开摘要）
import xml.etree.ElementTree as ET

API = 'http://export.arxiv.org/api/query'
NS = {'a': 'http://www.w3.org/2005/Atom'}

def fetch_page(cat, year, start, max_results):
    q = 'cat:%s AND submittedDate:[%d01010000 TO %d12312359]' % (cat, year, year)
    url = API + '?' + urllib.parse.urlencode({
        'search_query': q, 'start': start, 'max_results': max_results,
        'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60, context=_CTX) as r:
                return r.read()
        except Exception as e:
            if attempt == 2:
                print('  抓取失败(%d): %s' % (start, e)); return None
            time.sleep(3)

def parse(xml):
    out = []
    try:
        root = ET.fromstring(xml)
    except Exception:
        return out
    for e in root.findall('a:entry', NS):
        t = e.find('a:title', NS)
        s = e.find('a:summary', NS)
        if t is None or s is None: continue
        title = ' '.join((t.text or '').split())
        summ = ' '.join((s.text or '').split())
        if len(title) + len(summ) > 100:
            out.append(title + '\n' + summ)
    return out

def fetch_year(cat, year, n, outdir):
    os.makedirs(outdir, exist_ok=True)
    got = 0; start = 0
    while got < n:
        xml = fetch_page(cat, year, start, min(100, n - got))
        if not xml: break
        docs = parse(xml)
        if not docs: break
        for d in docs:
            if got >= n: break
            io.open(os.path.join(outdir, '%05d.txt' % got), 'w', encoding='utf-8').write(d)
            got += 1
        start += 100
        print('    %s %d: 已抓 %d' % (cat, year, got), flush=True)
        time.sleep(3)          # arXiv 要求：请求间至少 3 秒
    return got

def main():
    if len(sys.argv) < 4:
        print(__doc__); return
    cat, y_old, y_new = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    root = sys.argv[4] if len(sys.argv) > 4 else os.path.join(os.path.expanduser('~'), 'Desktop', 'arxiv_语料')
    n = int(sys.argv[5]) if len(sys.argv) > 5 else 3000
    dom = cat.replace('.', '_')
    base = os.path.join(root, dom)
    print('=== 抓取 %s: %d (%d条) vs %d (%d条) ===' % (cat, y_old, n, y_new, n))
    g1 = fetch_year(cat, y_old, n, os.path.join(base, 'old'))
    g2 = fetch_year(cat, y_new, n, os.path.join(base, 'new'))
    print('完成: old=%d, new=%d ⇒ %s' % (g1, g2, base))
    print('下一步: python 501_vl_newterm.py "%s" %d' % (root, y_new - y_old))

if __name__ == '__main__':
    main()

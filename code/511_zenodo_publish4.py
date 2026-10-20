# -*- coding: utf-8 -*-
"""511_zenodo_publish4.py · 发布第四章到 Zenodo + 生成知乎发布版"""
import io, json, os, urllib.request, urllib.error, urllib.parse, ssl

BASE = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
TOKEN_FILE = r'C:\Users\Administrator\zenodo_token.txt'
API = 'https://zenodo.org/api'
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE

def req(method, url, token, data=None, raw=None):
    if 'access_token' not in url:
        url = url + ('&' if '?' in url else '?') + 'access_token=' + token
    h = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    r = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=180, context=CTX) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print('HTTPError', e.code, e.read()[:300]); raise

def main():
    token = io.open(TOKEN_FILE, encoding='utf-8').read().strip()
    dep = req('POST', API + '/deposit/depositions', token, data={})
    dep_id = dep['id']; bucket = dep['links']['bucket']
    print('deposit:', dep_id)
    files = [BASE + '论文-04-AI对齐.md', BASE + '论文-04-AI对齐.txt']
    for f in files:
        name = os.path.basename(f)
        data = io.open(f, 'rb').read()
        url = bucket + '/' + urllib.parse.quote(name)
        r = urllib.request.Request(url, data=data, method='PUT', headers={
            'Authorization': 'Bearer ' + token, 'Content-Type': 'application/octet-stream'})
        with urllib.request.urlopen(r, timeout=180, context=CTX) as resp:
            print('  上传', name, resp.status)
    meta = {'metadata': {
        'title': '对齐是解压的约束：为什么对齐会漂移，以及为什么“替换”会毁掉它',
        'upload_type': 'publication', 'publication_type': 'preprint',
        'language': 'zho', 'access_right': 'open', 'license': 'cc-by-4.0',
        'creators': [{'name': '何淇'}],
        'keywords': ['AI对齐', 'RLHF', '对齐漂移', '压缩陷阱', '歧义', '模型崩塌', '持续学习'],
        'related_identifiers': [
            {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23488543'},
            {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23503050'},
            {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23503559'},
        ],
        'description': (
            '主流对齐研究（RLHF、宪法式 AI、可扩展监督）默认模型可被稳定塑造。'
            '本文用前三章框架指出：AI 是对人类语言的再解压，对齐 = 对这个解压的约束。'
            '由此得到三条可检验推论：（1）对齐漂移——语言在升维，冻结模型对齐的是训练时刻的语言；'
            '（2）歧义集中——压缩陷阱根源是语言有损，对齐失败应集中在人类语言的歧义处；'
            '（3）替换侵蚀——对齐信号藏在人类数据里，替换而非累积会切断价值信号链。'
            '本文给出三个对应实验方案，并指出：对齐不是一次性训练问题，而是维持累积通道的持续工程问题。'
        ),
    }}
    req('PUT', API + '/deposit/depositions/%d' % dep_id, token, data=meta)
    print('元数据已设置')
    pub = req('POST', API + '/deposit/depositions/%d/actions/publish' % dep_id, token)
    doi = pub.get('doi', '')
    print('已发布！DOI: https://doi.org/' + doi)

    # 知乎发布版
    body = io.open(BASE + '论文-04-AI对齐.txt', encoding='utf-8').read()
    top = ('标题（复制进知乎标题栏）：\n'
           '对齐是解压的约束：为什么对齐会漂移，以及为什么“替换”会毁掉它\n\n'
           '【正文从这里开始复制】\n\n')
    bot = ('\n\n---\n本文已发布为预印本，DOI：https://doi.org/' + doi + '\n'
           '系列前三章：\n'
           ' 第一章《现在的 AI 为什么不是生命》 https://doi.org/10.5281/zenodo.23488543\n'
           ' 第二章《容量不能替代数据的更新》 https://doi.org/10.5281/zenodo.23503050\n'
           ' 第三章《替换与累积》 https://doi.org/10.5281/zenodo.23503559\n'
           '代码与全文：https://github.com/heqiq619/ai-not-alive\n\n'
           '本文由何淇创作，AI（DeepSeek）协助整理；全部观点由作者负责。\n\n'
           '标签：#人工智能 #AI对齐 #RLHF #大语言模型 #模型崩塌')
    io.open(r'C:\Users\Administrator\Desktop\知乎发-第四章.txt', 'w', encoding='utf-8-sig').write(top + body + bot)
    print('知乎发布版已生成: 桌面\\知乎发-第四章.txt')

if __name__ == '__main__':
    main()

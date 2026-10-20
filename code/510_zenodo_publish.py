# -*- coding: utf-8 -*-
"""510_zenodo_publish.py · 用 API 发布第三章到 Zenodo
token 从 C:\\Users\\Administrator\\zenodo_token.txt 读取（不打印）
"""
import io, json, os, sys, urllib.request, urllib.error, ssl

BASE = 'C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
TOKEN_FILE = r'C:\Users\Administrator\zenodo_token.txt'
API = 'https://zenodo.org/api'
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE

def req(method, url, token, data=None, headers=None, raw=None):
    url = url + ('&' if '?' in url else '?') + 'access_token=' + token
    h = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    if headers: h.update(headers)
    body = raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    r = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        resp = urllib.request.urlopen(r, timeout=120, context=CTX)
    except urllib.error.HTTPError as e:
        print('HTTPError', e.code, e.read()[:300]); raise
    with resp:
        return json.loads(resp.read().decode())

def main():
    token = io.open(TOKEN_FILE, encoding='utf-8').read().strip()
    # 1) 创建 deposit
    dep = req('POST', API + '/deposit/depositions', token, data={})
    dep_id = dep['id']; bucket = dep['links']['bucket']
    print('deposit 创建:', dep_id)
    # 2) 上传文件
    files = [
        BASE + '论文-03-替换与累积.md',
        BASE + '论文-03-替换与累积.txt',
    ]
    for f in files:
        name = os.path.basename(f)
        data = io.open(f, 'rb').read()
        url = bucket + '/' + urllib.parse.quote(name)
        r = urllib.request.Request(url, data=data, headers={
            'Authorization': 'Bearer ' + token, 'Content-Type': 'application/octet-stream'},
            method='PUT')
        with urllib.request.urlopen(r, timeout=180, context=CTX) as resp:
            print('  上传:', name, resp.status)
    # 3) 元数据
    meta = {
        'metadata': {
            'title': '替换与累积：模型崩塌、压缩陷阱与持续学习是同一个问题',
            'upload_type': 'publication',
            'publication_type': 'preprint',
            'language': 'zho',
            'creators': [{'name': '何淇'}],
            'keywords': ['模型崩塌', '压缩陷阱', '持续学习', 'scaling law',
                         '合成数据', '累积升维', 'model collapse'],
            'access_right': 'open',
            'license': 'cc-by-4.0',
            'description': (
                '当前 AI 领域有三个看似独立的热点争议：模型崩塌（用模型生成数据训练导致退化）、'
                '压缩陷阱（追求压缩可能牺牲真相）、scaling vs 持续学习（堆参数还是持续更新）。'
                '本文指出：这三者是同一个问题的三个侧面——语言是累积升维的；替换（而非累积）'
                '会切断维度生长。模型崩塌 = 用模型数据替换人类数据 ⇒ 累积链断裂 ⇒ 维度退化；'
                '压缩陷阱 = 压缩对象是有损的人类语言，最省编码不等于最符合世界；'
                'scaling vs 持续学习 = 容量只能接收维度、不能生成维度（第二章实测支持）。'
                '由此得到可检验推论：人类数据与模型数据必须混合（累积），不能完全替换（纯合成=崩塌）。'
            ),
            'related_identifiers': [
                {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23488543'},
                {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23503050'},
            ],
        }
    }
    req('PUT', API + '/deposit/depositions/%d' % dep_id, token, data=meta)
    print('元数据已设置')
    # 4) 发布
    pub = req('POST', API + '/deposit/depositions/%d/actions/publish' % dep_id, token)
    doi = pub.get('doi', '')
    print('已发布！DOI: https://doi.org/' + doi)

if __name__ == '__main__':
    main()

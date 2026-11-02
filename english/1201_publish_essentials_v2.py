# -*- coding: utf-8 -*-
"""1201_publish_essentials_v2.py — 发布 English Essentials v2（11 篇）"""
import io, json, os, shutil, subprocess, time, urllib.parse

DL = 'C:/DS/数字生命/'
API = 'https://zenodo.org/api'; PROXY = 'http://127.0.0.1:7897'; CURL = 'curl.exe'
TOK = io.open(r'C:\Users\Administrator\zenodo_token.txt', encoding='utf-8').read().strip()
ARCH = DL + '发布存档/'
BASE = '数字生命-English-Essentials-v2'
FILES = [BASE + e for e in ('.md', '.txt', '.docx', '.pdf')]
V1_ID = 23640116  # English Essentials v1

DESC = (
    'Selected English edition of the Digital Life series (v2), 11 pieces.\n\n'
    'Part I — Definition: Paper 0 (Introduction), Paper 1 (Why Today\'s AI Is Not Alive).\n'
    'Part II — Theory: Paper 12 (Information Non-Increase Theorem), '
    'Paper 13 (Contraction of Functionizable Content), Paper 32 (The Life Function), '
    'Paper 36 (Language and the Brain).\n'
    'Part III — Engineering Observations: Paper 44 (Gating and Sparse Execution, consolidated), '
    'Paper 45 (Frozen Submodels: Interfaces, Coordination and Hierarchy — two minimal experiments).\n'
    'Part IV — Appendices: A (Thickness and Dimension), B (Concept Map and Glossary), '
    'C (Cliffs and Slopes: Where Does Digital Life Grow From?).\n\n'
    'v2 (2026-11-02) adds Papers 12, 13, 36, 44, 45 and Appendix B, translated in November 2026. '
    'Papers 0, 1, 32 and Appendix A are earlier translations (October 2026) included for completeness. '
    'The Chinese edition is authoritative and remains the full reference; this volume is selective.\n\n'
    'Scope note: the series makes a definitional claim (life = p_life + R_life; p_life is a family of '
    'dynamic functions that is kept) and explores measurable consequences. It does not claim that current AI '
    'is alive, does not claim consciousness, and does not claim validation at the scale of real biological brains. '
    'R is declared, not expanded; experimental results are small-scale, mostly single-seed observations.'
)

def curl(args, timeout=900, tries=6):
    last = ''
    for i in range(tries):
        r = subprocess.run([CURL, '-s', '--proxy', PROXY, '--max-time', str(timeout)] + args,
                           capture_output=True, text=True)
        if r.stdout and not r.stdout.lstrip().startswith('<'):
            return r.stdout
        last = (r.stdout or r.stderr or '')[:120]; time.sleep(4 * (i + 1))
    raise RuntimeError('curl fail: ' + last)

def api(m, url, data=None):
    args = ['-X', m, '-H', 'Authorization: Bearer ' + TOK, '-H', 'Content-Type: application/json']
    if data is not None:
        args += ['-d', json.dumps(data)]
    args.append(url)
    out = curl(args)
    try:
        return json.loads(out)
    except Exception:
        return {'__raw__': out[:300]}

def main():
    for fn in FILES:
        shutil.copy2(DL + fn, ARCH + 'v2-essentials-' + fn)
    draft = api('POST', API + '/deposit/depositions/%d/actions/newversion' % V1_ID)
    did = int(draft['links']['latest_draft'].rstrip('/').split('/')[-1])
    dep = api('GET', API + '/deposit/depositions/%d' % did)
    for f in dep.get('files', []):
        api('DELETE', API + '/deposit/depositions/%d/files/%s' % (did, f['id']))
    bucket = api('GET', API + '/deposit/depositions/%d' % did)['links']['bucket']
    for fn in FILES:
        curl(['-X', 'PUT', '-H', 'Authorization: Bearer ' + TOK,
              '-H', 'Content-Type: application/octet-stream',
              '--upload-file', DL + fn, bucket + '/' + urllib.parse.quote(fn)])
    dep = api('GET', API + '/deposit/depositions/%d' % did)
    remote = {f['filename']: f['filesize'] for f in dep.get('files', [])}
    bad = [(fn, remote.get(fn), os.path.getsize(DL + fn)) for fn in FILES if remote.get(fn) != os.path.getsize(DL + fn)]
    print('大小校验:', 'OK' if not bad else ('FAIL ' + str(bad)))
    if bad:
        return
    meta = {k: v for k, v in dep.get('metadata', {}).items()
            if k in {'title', 'description', 'creators', 'keywords', 'access_right', 'license',
                     'upload_type', 'publication_type', 'language', 'related_identifiers',
                     'communities', 'publication_date'}}
    meta['title'] = 'Digital Life: A Measurable Definition of Life — English Essentials (v2)'
    meta['description'] = DESC
    meta['version'] = 'v2'
    meta['notes'] = ('v2 (2026-11-02): 11 pieces: Papers 0, 1, 12, 13, 32, 36, 44, 45; '
                     'Appendices A, B, C. New translations: 12, 13, 36, 44, 45, B.')
    meta['keywords'] = ['digital life', 'definition of life', 'functionizable', 'information theory',
                        'language and brain', 'gating', 'frozen submodels', 'modularity']
    meta['language'] = 'eng'
    meta['related_identifiers'] = [
        {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23543322'},
        {'relation': 'isPartOf', 'identifier': '10.5281/zenodo.23543323'},
        {'relation': 'references', 'identifier': '10.5281/zenodo.23859935'},
        {'relation': 'isNewVersionOf', 'identifier': '10.5281/zenodo.23640116'},
        {'relation': 'references', 'identifier': '10.5281/zenodo.23697916'},
    ]
    r = api('PUT', API + '/deposit/depositions/%d' % did, data={'metadata': meta})
    if 'id' not in r:
        print('metadata 失败:', str(r)[:200]); return
    pub = api('POST', API + '/deposit/depositions/%d/actions/publish' % did)
    doi = pub.get('doi')
    print('published:', doi)
    io.open(DL + 'zenodo-essentials-v2.json', 'w', encoding='utf-8').write(
        json.dumps({'essentials_v2': doi}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()

import io, json, os, urllib.request, urllib.error, urllib.parse, ssl
BASE='C:/Users/Administrator/Documents/deepseek-harness/default-workspace/digital-life/'
TOK=r'C:\Users\Administrator\zenodo_token.txt'
API='https://zenodo.org/api'
CTX=ssl.create_default_context(); CTX.check_hostname=False; CTX.verify_mode=ssl.CERT_NONE
def req(m,u,t,data=None,raw=None):
    if 'access_token' not in u: u=u+('&' if '?' in u else '?')+'access_token='+t
    h={'Authorization':'Bearer '+t,'Content-Type':'application/json'}
    b=raw if raw is not None else (json.dumps(data).encode() if data is not None else None)
    r=urllib.request.Request(u,data=b,headers=h,method=m)
    try:
        with urllib.request.urlopen(r,timeout=180,context=CTX) as resp: return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print('HTTPError',e.code,e.read()[:300]); raise
def main():
    t=io.open(TOK,encoding='utf-8').read().strip()
    dep=req('POST',API+'/deposit/depositions',t,data={}); did=dep['id']; bucket=dep['links']['bucket']
    print('deposit:',did)
    for f in ['论文-05-安全.md','论文-05-安全.txt']:
        data=io.open(BASE+f,'rb').read()
        url=bucket+'/'+urllib.parse.quote(f)
        r=urllib.request.Request(url,data=data,method='PUT',headers={'Authorization':'Bearer '+t,'Content-Type':'application/octet-stream'})
        with urllib.request.urlopen(r,timeout=180,context=CTX) as resp: print(' 上传',f,resp.status)
    meta={'metadata':{'title':'安全：当它是生命防，还是当它是工具防？','upload_type':'publication','publication_type':'preprint','language':'zho','access_right':'open','license':'cc-by-4.0','creators':[{'name':'何淇'}],'keywords':['AI安全','对齐','工具风险','过度信任','失配漂移','生命定义'],'related_identifiers':[{'relation':'isPartOf','identifier':'10.5281/zenodo.23488543'},{'relation':'isPartOf','identifier':'10.5281/zenodo.23503050'},{'relation':'isPartOf','identifier':'10.5281/zenodo.23503559'},{'relation':'isPartOf','identifier':'10.5281/zenodo.23503728'}],'description':'当前 AI 安全讨论混杂两种恐惧：被滥用（工具风险）与它自己活了（生命风险）。两者需要不同威胁模型。按第一章判据，AI 不是生命（冻结函数点、更新在外部、不自我维持），因此正确框架是工具安全而非防生命。但工具风险真实：误用、过度信任、失配漂移三类可测失效。本文给出对应评测与治理方向，并指出把安全锚定在是否会觉醒既高估了它也低估了真实风险。'}}
    req('PUT',API+'/deposit/depositions/%d'%did,t,data=meta)
    print('元数据已设置')
    pub=req('POST',API+'/deposit/depositions/%d/actions/publish'%did,t)
    doi=pub.get('doi','')
    print('已发布！DOI: https://doi.org/'+doi)
    body=io.open(BASE+'论文-05-安全.txt',encoding='utf-8').read()
    top='标题（复制进知乎标题栏）：\n安全：当它是生命防，还是当它是工具防？\n\n【正文从这里开始复制】\n\n'
    bot=('\n\n---\n本文已发布为预印本，DOI：https://doi.org/'+doi+'\n'
         '系列前四章：\n 第一章 https://doi.org/10.5281/zenodo.23488543\n 第二章 https://doi.org/10.5281/zenodo.23503050\n 第三章 https://doi.org/10.5281/zenodo.23503559\n 第四章 https://doi.org/10.5281/zenodo.23503728\n'
         '代码与全文：https://github.com/heqiq619/ai-not-alive\n\n本文由何淇创作，AI（DeepSeek）协助整理；全部观点由作者负责。\n\n标签：#人工智能 #AI安全 #对齐 #大语言模型 #生命')
    io.open(r'C:\Users\Administrator\Desktop\知乎发-第五章.txt','w',encoding='utf-8-sig').write(top+body+bot)
    print('知乎发布版: 桌面\\知乎发-第五章.txt')
if __name__=='__main__': main()

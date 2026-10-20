# -*- coding: utf-8 -*-
"""405_test_division.py · 决定性检验：结构是「抱团」还是「分工」＋ 2000 tick 长跑

检验逻辑：
  ① 基因距离：强连接相邻个体对 vs 随机个体对
       · 若相连对距离 **更低** ⇒ 克隆抱团（不是分工）
       · 若相连对距离 **更高** ⇒ 互补专业化（分工）
  ② 邻居信息的决定性：把邻居贡献去掉后，最终预测有多少位会翻
       · 比例显著 > 0 ⇒ 最终预测真的依赖邻居（功能耦合）
  ③ 长跑 2000 tick：连接强度 / 空间聚集度 / 表达长度 的时间趋势

注意：测量使用独立 numpy RNG，不消耗宇宙的真实熵（不影响宇宙演化）。
"""
import importlib.util, sys
import numpy as np

spec = importlib.util.spec_from_file_location('u', '400_universe_s6.py')
u = importlib.util.module_from_spec(spec); sys.modules['u'] = u; spec.loader.exec_module(u)

TICKS = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
hist, gains, accs, births, deaths, links = u.run(TICKS, seed=11, verbose=False)

alive = u.alive; genome = u.genome; link = u.link; world = u.world
m = alive
idx = np.nonzero(m)[0]

print('=== 长跑 %d tick ===' % TICKS)
print('  人口 %.1f  CV %.4f  出生/轮 %.1f  死亡/轮 %.1f'
      % (hist[-300:].mean(), hist[-300:].std()/max(1e-9,hist[-300:].mean()),
         births[-300:].mean(), deaths[-300:].mean()))
print('  压缩收益 %.4f bit/tick（末期300轮）' % gains[-300:].mean())
print('  连接强度时间序列(每200tick): %s' % np.round(links[::200], 2).tolist())

# ---- ① 基因距离检验 ----
THR = 50
pairs_linked = []
for i in idx:
    for d in range(4):
        j = u.NB[i, d]
        if alive[j] and link[i, d] >= THR:
            pairs_linked.append((i, j))
pairs_linked = np.array(pairs_linked, dtype=np.int64).reshape(-1, 2) if pairs_linked else np.zeros((0,2),dtype=np.int64)

rng = np.random.RandomState(2024)
n_rand = max(2000, len(pairs_linked) * 3)
pa = rng.choice(idx, n_rand); pb = rng.choice(idx, n_rand)
pairs_rand = np.stack([pa, pb], axis=1)

FIELDS = {'预测表[0:160)': (0,160), '输出表[160:192)': (160,192),
          '长度[192:200)': (192,200), '阈值[200:204)': (200,204),
          '连接律[204:220)': (204,220), '权重[220:222)': (220,222),
          '上下文表达[222:247)': (222,247)}
def hamming(pairs, lo, hi):
    if len(pairs) == 0: return float('nan')
    a = genome[pairs[:,0], lo:hi]; b = genome[pairs[:,1], lo:hi]
    return float((a != b).mean())

print('\n=== ① 基因距离：相连 vs 随机 ===')
print('  相连个体对数量 = %d' % len(pairs_linked))
for name,(lo,hi) in FIELDS.items():
    dl = hamming(pairs_linked, lo, hi)
    dr = hamming(pairs_rand, lo, hi)
    verdict = ''
    if not np.isnan(dl):
        if dl > dr * 1.15: verdict = ' ← 相连更**相异**(分工迹象)'
        elif dl < dr * 0.85: verdict = ' ← 相连更**相似**(抱团迹象)'
        else: verdict = ' ← 无明显差异'
    print('  %-14s 相连 %.3f | 随机 %.3f%s' % (name, dl, dr, verdict))

# ---- ② 邻居信息决定性 ----
rows = np.arange(u.N)
LEN = u.bits_to_int(genome[:,192:200]) % 65
THRv = u.bits_to_int(genome[:,200:204]) / 16.0 * u.THR_MAX
L_eff = np.where(u.energy < THRv, LEN // 2, LEN)
obs = u.observe()
expr = obs < L_eff
ctx = np.clip(alive[u.NB].sum(axis=1).astype(np.int64), 0, 4)
ctxlut = genome[:, 222:247].reshape(u.N, 5, 5)
slotmask = ctxlut[rows[:,None], ctx[:,None], np.arange(5)[None,:]]
pred5 = np.zeros((u.N,5), dtype=np.uint8)
for k in range(5):
    lut = genome[:, k*32:(k+1)*32][rows, obs]
    pred5[:,k] = np.where(expr & (slotmask[:,k]==1), lut, 0)
w_own = 1.0 + u.bits_to_int(genome[:,220:222])
lk = link / float(u.LINK_MAX)
nb_pred = pred5[u.NB][rows[:,None], np.arange(4)[None,:], u.OPP[None,:]]
wsum = w_own + lk.sum(axis=1)
score = w_own*pred5[:,0] + (lk*nb_pred).sum(axis=1)
final_vote = (score > 0.5*wsum).astype(np.uint8)
self_only = (w_own*pred5[:,0] > 0.5*w_own).astype(np.uint8)   # 只看自己时的判断
diff = (final_vote != self_only)
print('\n=== ② 邻居信息是否决定性 ===')
print('  有连接个体中，邻居改变了最终预测的比例 = %.3f'
      % (float(diff[m & (lk.sum(axis=1)>0)].mean()) if (m & (lk.sum(axis=1)>0)).any() else 0.0))
print('  （>0 说明最终行为真的依赖邻居 ⇒ 功能耦合，而不是各自为政）')

# ---- ③ 结构趋势 ----
print('\n=== ③ 长跑趋势 ===')
q = max(1, TICKS//10)
segs = [links[i*q:(i+1)*q].mean() for i in range(10)]
print('  连接强度 10 段均值: %s' % np.round(segs, 2).tolist())
print('  末段 vs 首段: %+.1f%%' % (100*(segs[-1]-segs[0])/max(1e-9,segs[0])))

# 空间聚集度
a = link.sum(axis=1).astype(np.float64)
nbmean = a[u.NB].mean(axis=1)
c_ = float(np.corrcoef(a[m], nbmean[m])[0,1])
print('  空间聚集度 = %+.3f' % c_)
LENm = u.bits_to_int(genome[:,192:200]) % 65
print('  表达长度 中位 %.1f 均值 %.1f' % (float(np.median(LENm[m])), float(LENm[m].mean())))
print('  强连接个体数 %d / %d = %.1f%%'
      % (int((m & (link.sum(axis=1)>=THR)).sum()), int(m.sum()),
         100.0*float((m & (link.sum(axis=1)>=THR)).mean())))


# ================= S6 专项测量 =================
print('\n=== S6-A 分化表达：不同上下文是否表达不同槽 ===')
m2 = alive
ctx_all = np.clip(alive[u.NB].sum(axis=1).astype(np.int64), 0, 4)
ctxlut_all = genome[:, 222:247].reshape(u.N, 5, 5)
sm = ctxlut_all[rows[:,None], ctx_all[:,None], np.arange(5)[None,:]]
print('  行=上下文(存活邻居数 0..4)  列=槽(0自身/1北/2南/3西/4东) 值为表达频率')
for c in range(5):
    sel = m2 & (ctx_all == c)
    if sel.sum() > 20:
        print('  ctx=%d (%5d人): %s' % (c, int(sel.sum()), np.round(sm[sel].mean(axis=0), 2).tolist()))
print('\n=== S6-B 相连个体的表达互补性 ===')
if len(pairs_linked):
    dl = float((sm[pairs_linked[:,0]] != sm[pairs_linked[:,1]]).mean())
    dr = float((sm[pairs_rand[:,0]] != sm[pairs_rand[:,1]]).mean())
    print('  表达表距离: 相连 %.3f | 随机 %.3f ⇒ %s'
          % (dl, dr, '互补(分工)' if dl > dr*1.15 else ('相似(抱团)' if dl < dr*0.85 else '无差异')))
print('\n=== S6-C 上下文互补性：相连对是否一个邻居多一个邻居少 ===')
if len(pairs_linked):
    dc = np.abs(ctx_all[pairs_linked[:,0]] - ctx_all[pairs_linked[:,1]]).mean()
    dr2 = np.abs(ctx_all[pairs_rand[:,0]] - ctx_all[pairs_rand[:,1]]).mean()
    print('  邻居数差: 相连 %.3f | 随机 %.3f' % (dc, dr2))

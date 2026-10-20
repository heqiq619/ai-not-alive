# -*- coding: utf-8 -*-
"""400_universe_s5.py · S5：双通道世界 + 细胞类型（分化表达 ⇒ 分工必需）

======================= 为什么（S4 的结论） =======================
S4 加了每槽独立表达，但决定性检验仍是「克隆抱团」（相连 0.078 vs 随机 0.461）
根因：**重复不是代价** —— 所有细胞做同一个任务，克隆冗余没有损失
⇒ 分工需要的不是「能分工」，而是「不分工就活不好」

======================= S5 的设计 =======================
世界有两条独立通道 A、B（两套 CA + 独立噪声）
细胞有「类型基因」type ∈ {A, B}，决定它**只能观测一条通道**
  · A 型：观测 A 通道 5 位邻域，输出位写入 A 通道
  · B 型：同理 B
每个细胞必须预测**自己格的两条通道下一状态**（tA 和 tB），收入 = 两者收益平均
  · 它只能观测一条 ⇒ 自己那条能学会，另一条学不到
  · 但它可以**投票采纳邻居的预测**（邻居观测的是邻居的类型通道）
  ⇒ **A 型需要 B 型邻居，B 型需要 A 型邻居**
  ⇒ 同型抱团 = 冗余 = 一半收入拿不到 ⇒ 被淘汰
  ⇒ 异型相连 = 互补 = 全额收入 ⇒ 被选择

======================= 基因组（383 比特） =======================
[0:160)   预测表 A：5 槽 × 32（目标 = 各槽的 tA）
[160:320) 预测表 B：5 槽 × 32（目标 = 各槽的 tB）
[320:352) 输出表：32 项（写自己类型通道的输出位）
[352:360) 表达长度 LEN % 65
[360:364) 调节阈值 THR
[364:380) 连接律 LUT：8 项 × 2bit
[380:382) 自身投票权重 w_own = 1+value
[382]     类型位 type（0=A, 1=B）

======================= 物理（不变、普适） =======================
P1 2D 周期格点，一格一粒子
P2 两通道 CA：wX_next[c] = outX[c] ⊕ outX[4邻居] ⊕ 噪声(NOISE_P，真熵)
   （outX 只有类型 X 的细胞贡献非零）
P3 能量通量守恒；income = base*(1+GAIN_K*gain_bits)
   gain_bits = 0.5*(gainA + gainB)，各自 = log2 p_model − log2 p_base
   cost = BASE_COST + clip(L,0,32)*(2*Σslot_bits + slot_bits0)*COST_PER_BIT + 连接成本
P4 复制：局部、逐位变异、**子代继承连接强度**（表观遗传）
P5 死亡：E≤0（无老化）
P6 全部演化随机来自 os.urandom
固定组合规则：加权投票
"""
import os, sys, time
import numpy as np
import ast

W = 128; H = 128; N = W * H
FLUX_TOTAL   = 24.0
BASE_COST = 0.006
GAIN_K = 8.0
COST_PER_BIT = 0.000004
CONF         = 0.9
COPY_AT      = 0.050
START_E      = 0.040
INIT_P       = 0.02
MUT_P        = 0.01
THR_MAX      = 0.040
NOISE_P      = 0.10
LINK_STEP    = 6
LINK_MAX     = 100
LINK_COST = 0.0004
G_LEN        = 383
OPP = np.array([1, 0, 3, 2], dtype=np.int64)

def neighbor_table():
    idx = np.arange(N).reshape(H, W)
    return np.stack([np.roll(idx, -1, 0).ravel(), np.roll(idx, 1, 0).ravel(),
                     np.roll(idx, -1, 1).ravel(), np.roll(idx, 1, 1).ravel()],
                    axis=1).astype(np.int64)
NB = neighbor_table()

def real_bits(k):
    if k <= 0: return np.zeros(0, dtype=np.uint8)
    return np.unpackbits(np.frombuffer(os.urandom((k + 7) // 8), dtype=np.uint8))[:k].astype(np.uint8)
def real_int(n, hi):
    if hi <= 1 or n <= 0: return np.zeros(max(0, n), dtype=np.int64)
    k = max(1, int(np.ceil(np.log2(hi))))
    b = real_bits(n * k).reshape(n, k)
    return (b @ (1 << np.arange(k - 1, -1, -1))) % hi
def bits_to_int(bits):
    return (bits.astype(np.int64) @ (1 << np.arange(bits.shape[-1] - 1, -1, -1)))

alive    = np.zeros(N, dtype=bool)
genome   = np.zeros((N, G_LEN), dtype=np.uint8)
energy   = np.zeros(N, dtype=np.float64)
predA_prev = np.zeros(N, dtype=np.uint8)
predB_prev = np.zeros(N, dtype=np.uint8)
out_now  = np.zeros(N, dtype=np.uint8)
wA       = np.zeros(N, dtype=np.uint8)
wB       = np.zeros(N, dtype=np.uint8)
link     = np.zeros((N, 4), dtype=np.int16)
last_gA  = np.zeros(N, dtype=np.float64)
last_gB  = np.zeros(N, dtype=np.float64)

def init_universe(seed=11):
    global genome, predA_prev, predB_prev, out_now, wA, wB, link, last_gA, last_gB
    rng = np.random.RandomState(seed)
    occ = rng.rand(N) < INIT_P
    alive[:] = occ
    energy[:] = START_E
    genome[:] = (rng.rand(N, G_LEN) < 0.5).astype(np.uint8)
    genome[~occ] = 0
    predA_prev[:] = 0; predB_prev[:] = 0; out_now[:] = 0
    link[:] = 0; last_gA[:] = 0; last_gB[:] = 0
    wA[:] = real_bits(N); wB[:] = real_bits(N)

def observe_of(w):
    nb = w[NB]
    return ((w << 4) | (nb[:, 0] << 3) | (nb[:, 1] << 2) |
            (nb[:, 2] << 1) | nb[:, 3]).astype(np.uint8)

def step():
    global alive, energy, genome, predA_prev, predB_prev, out_now, wA, wB, link, last_gA, last_gB
    n_alive = int(alive.sum())
    if n_alive == 0:
        return 0, 0.0, 0, 0
    rows = np.arange(N)
    LEN = bits_to_int(genome[:, 352:360]) % 65
    THR = bits_to_int(genome[:, 360:364]) / 16.0 * THR_MAX
    L_eff = np.where(energy < THR, LEN // 2, LEN)
    slot_bits = genome[:, 382:383]                       # 用类型位之外的简单门控：全部表达
    # ★简化：为控制基因组规模，槽表达仍用统一 LEN（S4 已验证不影响结论）
    typ = genome[:, 382]                                 # 0=A型 1=B型
    obsA = observe_of(wA); obsB = observe_of(wB)
    obs = np.where(typ == 0, obsA, obsB)                 # 只看自己类型的通道
    expr = obs < L_eff

    # 5 槽预测（两个目标各一套表）
    predA = np.zeros((N, 5), dtype=np.uint8)
    predB = np.zeros((N, 5), dtype=np.uint8)
    for k in range(5):
        lutA = genome[:, k*32:(k+1)*32][rows, obs]
        lutB = genome[:, 160+k*32:160+(k+1)*32][rows, obs]
        predA[:, k] = np.where(expr, lutA, 0)
        predB[:, k] = np.where(expr, lutB, 0)
    out_new = np.where(expr, genome[:, 320:352][rows, obs], 0).astype(np.uint8)
    out_now = np.where(alive, out_new, 0).astype(np.uint8)

    # 组合（加权投票）——邻居对「我格」的预测
    w_own = 1.0 + bits_to_int(genome[:, 380:382])
    lk = link / float(LINK_MAX)
    nbA = predA[NB][rows[:, None], np.arange(4)[None, :], OPP[None, :]]
    nbB = predB[NB][rows[:, None], np.arange(4)[None, :], OPP[None, :]]
    wsum = w_own + lk.sum(axis=1)
    finalA = ((w_own*predA[:, 0] + (lk*nbA).sum(axis=1)) > 0.5*wsum).astype(np.uint8)
    finalB = ((w_own*predB[:, 0] + (lk*nbB).sum(axis=1)) > 0.5*wsum).astype(np.uint8)
    finalA[~alive] = 0; finalB[~alive] = 0

    # P2 两通道 CA：只接收对应类型细胞的输出
    isA = alive & (typ == 0); isB = alive & (typ == 1)
    oA = np.where(isA, out_now, 0).astype(np.uint8)
    oB = np.where(isB, out_now, 0).astype(np.uint8)
    nA = oA[NB]; nB = oB[NB]
    nA2 = (oA ^ nA[:,0] ^ nA[:,1] ^ nA[:,2] ^ nA[:,3]).astype(np.uint8)
    nB2 = (oB ^ nB[:,0] ^ nB[:,1] ^ nB[:,2] ^ nB[:,3]).astype(np.uint8)
    nz = real_int(N, 10**6) < int(NOISE_P*10**6)
    flip = real_bits(int(nz.sum()))
    nA2[nz] ^= flip; nB2[nz] ^= flip
    wA = nA2; wB = nB2

    # 压缩收益：tA 与 tB 各自计
    p1A = float(np.clip(wA.mean(), 0.01, 0.99)); p1B = float(np.clip(wB.mean(), 0.01, 0.99))
    def gain_of(pred, target, p1):
        ok = (pred == target)
        pm = np.where(ok, CONF, 1.0-CONF)
        pb = np.where(target == 1, p1, 1.0-p1)
        g = np.clip(np.log2(pm) - np.log2(pb), -4.0, 4.0)
        g[~alive] = 0.0
        return g
    gA = gain_of(predA_prev, wA, p1A)
    gB = gain_of(predB_prev, wB, p1B)
    gain = 0.5*(gA + gB)
    last_gA = gA; last_gB = gB

    # 连接律（基因 LUT）
    co = (out_now[NB] == out_now[:, None]).astype(np.int64)
    bucket = np.clip(link // 25, 0, 3)
    lutz = genome[:, 364:380].reshape(N, 8, 2)
    idx = co*4 + bucket
    lutv = lutz[rows[:, None], idx, 0]*2 + lutz[rows[:, None], idx, 1]
    delta = np.where(lutv == 0, -LINK_STEP, np.where(lutv == 1, 0, LINK_STEP))
    link = np.clip(link + delta, 0, LINK_MAX).astype(np.int16)

    # P3 能量
    base = FLUX_TOTAL / n_alive
    income = base * (1.0 + GAIN_K * gain)
    link_cost = LINK_COST * (link.sum(axis=1) / float(LINK_MAX))
    cost = BASE_COST + 2.0*np.clip(L_eff,0,32)*COST_PER_BIT + link_cost
    energy[alive] += (income - cost)[alive]
    predA_prev = np.where(alive, finalA, 0).astype(np.uint8)
    predB_prev = np.where(alive, finalB, 0).astype(np.uint8)

    # P4 复制（表观遗传：继承连接）
    cand = np.nonzero(alive & (energy >= COPY_AT))[0]
    if cand.size > 1: cand = cand[real_int(cand.size, cand.size)]
    ncopy = 0
    if cand.size > 0:
        pick_slot = real_int(cand.size, 4)
        mut_rand = real_int(cand.size*G_LEN, 10**6).reshape(cand.size, G_LEN)
        for k, c in enumerate(cand):
            opts = NB[c][~alive[NB[c]]]
            if opts.size == 0: continue
            slot = int(opts[pick_slot[k] % opts.size])
            if alive[slot]: continue
            flips = (mut_rand[k] < int(MUT_P*10**6)).astype(np.uint8)
            e_half = energy[c]*0.5
            energy[c] = e_half
            alive[slot] = True
            energy[slot] = e_half
            genome[slot] = genome[c] ^ flips
            predA_prev[slot] = 0; predB_prev[slot] = 0
            link[slot] = link[c]                        # 表观遗传
            ncopy += 1

    dead = alive & (energy <= 0.0)
    ndeath = int(dead.sum())
    if ndeath:
        alive[dead] = False; energy[dead] = 0.0; genome[dead] = 0
        predA_prev[dead] = 0; predB_prev[dead] = 0; link[dead] = 0
    return int(alive.sum()), float(gain[alive].mean()) if alive.any() else 0.0, ncopy, ndeath

def run(ticks=800, seed=11, verbose=True):
    init_universe(seed)
    hist, gains, births, deaths, links, mixed = [], [], [], [], [], []
    t0 = time.perf_counter(); next_report = 200
    for t in range(1, ticks+1):
        n, g, nc, nd = step()
        hist.append(n); gains.append(g); births.append(nc); deaths.append(nd)
        links.append(float(link[alive].mean()) if alive.any() else 0.0)
        if verbose and t >= next_report:
            print('  tick %5d 粒子 %5d gain %+.4f 连接均 %6.2f 出生 %3d 死亡 %3d 用时 %.0fs'
                  % (t, n, g, links[-1], nc, nd, time.perf_counter()-t0), flush=True)
            next_report += 200
    return np.array(hist), np.array(gains), np.array(births), np.array(deaths), np.array(links)

def verify(ticks=2000):
    print('=== S5 验证（双通道 + 细胞类型）：%d ticks ===' % ticks)
    hist, gains, births, deaths, links = run(ticks, seed=11)
    m = alive; idx = np.nonzero(m)[0]
    print('\n=== V1 稳态+周转 ===')
    print('  人口 %.1f CV %.4f 出生 %.1f 死亡 %.1f' % (hist[-300:].mean(),
          hist[-300:].std()/max(1e-9,hist[-300:].mean()), births[-300:].mean(), deaths[-300:].mean()))
    print('  压缩收益 %.4f bit/tick' % gains[-300:].mean())
    print('\n=== V7 连接结构 ===')
    print('  末期连接均值 %.2f  时间序列(每400tick) %s' % (links[-300:].mean(), np.round(links[::400],2).tolist()))
    # 基因距离 + 类型混合度
    THR=50
    lp=[]
    for i in idx:
        for d in range(4):
            j=NB[i,d]
            if alive[j] and link[i,d]>=THR: lp.append((i,j))
    lp=np.array(lp,dtype=np.int64).reshape(-1,2) if lp else np.zeros((0,2),dtype=np.int64)
    rng=np.random.RandomState(2024)
    nr=max(2000,len(lp)*3)
    rp=np.stack([rng.choice(idx,nr), rng.choice(idx,nr)],axis=1)
    print('\n=== ① 基因距离（相连 vs 随机）===')
    for name,(lo,hi) in {'预测表A[0:160)':(0,160),'预测表B[160:320)':(160,320),'类型位[382]':(382,383)}.items():
        dl=float((genome[lp[:,0],lo:hi]!=genome[lp[:,1],lo:hi]).mean()) if len(lp) else float('nan')
        dr=float((genome[rp[:,0],lo:hi]!=genome[rp[:,1],lo:hi]).mean())
        tag=''
        if not np.isnan(dl):
            tag = ' ← 相连更**相异**(分工)' if dl>dr*1.15 else (' ← 相连更**相似**(抱团)' if dl<dr*0.85 else ' ← 无差异')
        print('  %-18s 相连 %.3f | 随机 %.3f%s' % (name, dl, dr, tag))
    print('\n=== ② 异型配对比例（分工的直接证据）===')
    if len(lp):
        mix_l = float((genome[lp[:,0],382] != genome[lp[:,1],382]).mean())
        mix_r = float((genome[rp[:,0],382] != genome[rp[:,1],382]).mean())
        print('  相连对异型比例 %.3f | 随机对异型比例 %.3f' % (mix_l, mix_r))
    print('\n=== ③ 类型分布 ===')
    print('  A型 %d  B型 %d' % (int((m&(genome[:,382]==0)).sum()), int((m&(genome[:,382]==1)).sum())))
    print('\n=== ④ 邻居决定性 ===')
    rows=np.arange(N)
    LEN=bits_to_int(genome[:,352:360])%65
    THRv=bits_to_int(genome[:,360:364])/16.0*THR_MAX
    L_eff=np.where(energy<THRv,LEN//2,LEN)
    obsA=observe_of(wA); obsB=observe_of(wB); typ=genome[:,382]
    obs=np.where(typ==0,obsA,obsB); expr=obs<L_eff
    predA=np.zeros((N,5),dtype=np.uint8)
    for k in range(5): predA[:,k]=np.where(expr, genome[:,k*32:(k+1)*32][rows,obs],0)
    w_own=1.0+bits_to_int(genome[:,380:382]); lk=link/float(LINK_MAX)
    nbA=predA[NB][rows[:,None],np.arange(4)[None,:],OPP[None,:]]
    wsum=w_own+lk.sum(axis=1)
    fA=((w_own*predA[:,0]+(lk*nbA).sum(axis=1))>0.5*wsum).astype(np.uint8)
    sA=(w_own*predA[:,0]>0.5*w_own).astype(np.uint8)
    print('  邻居改变最终预测的比例 = %.3f' % float((fA!=sA)[m&(lk.sum(axis=1)>0)].mean() if (m&(lk.sum(axis=1)>0)).any() else 0))
    print('  空间聚集度 = %+.3f' % float(np.corrcoef(link.sum(axis=1)[m], link.sum(axis=1)[NB].mean(axis=1)[m])[0,1]))

if __name__=='__main__':
    verify(int(sys.argv[1]) if len(sys.argv)>1 else 2000)

# -*- coding: utf-8 -*-
"""400_universe_s3.py · S3：表观遗传 —— 连接结构跨组件换代保持

======================= S3 相对 S2b 的唯一改动 =======================
S2b 的诊断：合作收益巨大（强连接个体 gain 高 8 倍），但连接强度**不可遗传**
           ⇒ 下一代从 0 重建 ⇒ 选择看不到收益 ⇒ 连接萎缩
S3 的改动：**子代继承父代的连接强度向量**（line: link[slot] = link[c]）
           ⇒ 结构成为可遗传的表观状态 ⇒ 「组织跨代保持」有了物质基础
           这也是「在离散时刻序列里保持还是它自己」的最小实现

======================= 其余（继承 S2b） =======================
5 槽预测 + 连接加权投票 + CA 世界 + 压缩收益记账 + 无老化 + 无神迹


======================= 为什么改（自审结论） =======================
旧 S2：每个粒子只预测「自己格的下一世界位」，连接投票却用邻居对自己格的预测
      ⇒ **目标不一致** ⇒ 投票无信息 ⇒ 连接长不起来（实测平均强度仅 1.71）
新 S2b：每个粒子预测**自己邻域 5 个格**（自身+4邻居）的下一世界位
      ⇒ 我格有 5 份预测：我自己的 + 4 个邻居对我的格做的
      ⇒ 邻居看到我看不到的角度 ⇒ **信息互补** ⇒ 加权投票有真实收益
      ⇒ 分工有了经济意义：不同细胞负责不同预测槽

======================= 生命定义（用户） =======================
生命 = 一类高维、动态、自指、能自我维持的函数；它以比特结构存在，
靠压缩世界（匹配源分布）挣取自己存在的代价，并在离散的时刻序列里
保持「还是它自己」。

======================= 物理（不变、普适） =======================
P1  2D 周期格点，一格一粒子
P2' 世界 w_next[c] = out[c] ⊕ out[4邻居] ⊕ 噪声(NOISE_P，真熵)
P3  能量通量守恒 base=FLUX_TOTAL/n；income = base*(1+GAIN_K*gain_bits)
    gain_bits = log2 p_model(y) − log2 p_base(y)   ← 压缩收益
    cost = BASE_COST + (6*clip(L_eff,0,32))*COST_PER_BIT + LINK_COST*Σlink/100
P4  复制：局部放置、逐位翻转、**子代连接强度=0**
P5  死亡：E≤0（无老化）
P6  全部演化随机来自 os.urandom
物理里的固定组合规则：**加权投票**（信号怎么合成）+ 观测/目标定义

======================= 基因组（222 比特） =======================
[0:160)   预测表：5 槽 × 32 项（槽 0=自身格，1=北，2=南，3=西，4=东）
[160:192) 输出表：32 项（决定自己写出的位，驱动世界 CA）
[192:200) 表达长度 LEN = value % 65
[200:204) 调节阈值 THR = value/16*THR_MAX
[204:220) 连接律 LUT：8 项×2bit（输入=共激活×强度档，输出=衰减/不变/加强）
[220:222) 自身投票权重 w_own = 1 + value ∈ {1..4}

======================= S2b 判据 =======================
V1 稳态+周转 / V2 gain_bits>0 / V3 长度受压 / V4 无神迹 / V5 真熵
V6 基因多样性 / V7 连接强度随时间上升 / V8 有连接个体 gain > 无连接
"""
import os, sys, time
import numpy as np
import ast

W = 128; H = 128; N = W * H
FLUX_TOTAL   = 24.0
BASE_COST    = 0.010
GAIN_K       = 2.5
COST_PER_BIT = 0.00001
CONF         = 0.9
COPY_AT      = 0.050
START_E      = 0.040
INIT_P       = 0.02
MUT_P        = 0.01
THR_MAX      = 0.040
NOISE_P      = 0.10
LINK_STEP    = 6
LINK_MAX     = 100
LINK_COST    = 0.0008
G_LEN        = 222
OPP = np.array([1, 0, 3, 2], dtype=np.int64)   # 邻居槽位反转（纯几何）

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

alive     = np.zeros(N, dtype=bool)
genome    = np.zeros((N, G_LEN), dtype=np.uint8)
energy    = np.zeros(N, dtype=np.float64)
pred_prev = np.zeros(N, dtype=np.uint8)
out_now   = np.zeros(N, dtype=np.uint8)
world     = np.zeros(N, dtype=np.uint8)
link      = np.zeros((N, 4), dtype=np.int16)
last_gain = np.zeros(N, dtype=np.float64)

def init_universe(seed=11):
    global genome, pred_prev, out_now, world, link, last_gain
    rng = np.random.RandomState(seed)
    occ = rng.rand(N) < INIT_P
    alive[:] = occ
    energy[:] = START_E
    genome[:] = (rng.rand(N, G_LEN) < 0.5).astype(np.uint8)
    genome[~occ] = 0
    pred_prev[:] = 0; out_now[:] = 0
    link[:] = 0; last_gain[:] = 0
    world[:] = real_bits(N)

def observe():
    nb = world[NB]
    return ((world << 4) | (nb[:, 0] << 3) | (nb[:, 1] << 2) |
            (nb[:, 2] << 1) | nb[:, 3]).astype(np.uint8)

def step():
    global alive, energy, genome, pred_prev, out_now, world, link, last_gain
    n_alive = int(alive.sum())
    if n_alive == 0:
        return 0, 0.0, 0.0, 0, 0

    rows = np.arange(N)
    LEN = bits_to_int(genome[:, 192:200]) % 65
    THR = bits_to_int(genome[:, 200:204]) / 16.0 * THR_MAX
    L_eff = np.where(energy < THR, LEN // 2, LEN)
    obs = observe()
    expr = obs < L_eff

    # ---- 5 槽预测（槽0=自身格，1..4=北南西东）----
    pred5 = np.zeros((N, 5), dtype=np.uint8)
    for k in range(5):
        lut = genome[:, k * 32:(k + 1) * 32][rows, obs]
        pred5[:, k] = np.where(expr, lut, 0)
    out_new = np.where(expr, genome[:, 160:192][rows, obs], 0).astype(np.uint8)
    out_now = np.where(alive, out_new, 0).astype(np.uint8)

    # ---- 组合：自己 slot0 + 邻居对我的格的预测（按强度加权）----
    w_own = 1.0 + bits_to_int(genome[:, 220:222])
    lk = link / float(LINK_MAX)
    nb_pred_for_me = pred5[NB][rows[:, None], np.arange(4)[None, :], OPP[None, :]]  # (N,4)
    wsum = w_own + lk.sum(axis=1)
    score = w_own * pred5[:, 0] + (lk * nb_pred_for_me).sum(axis=1)
    pred_final = (score > 0.5 * wsum).astype(np.uint8)
    pred_final[~alive] = 0

    # ---- 世界 CA ----
    nb_out = out_now[NB]
    w_next = (out_now ^ nb_out[:, 0] ^ nb_out[:, 1] ^ nb_out[:, 2] ^ nb_out[:, 3]).astype(np.uint8)
    nz = real_int(N, 10 ** 6) < int(NOISE_P * 10 ** 6)
    w_next[nz] ^= real_bits(int(nz.sum()))
    world = w_next

    # ---- 压缩收益 ----
    target = world
    p1 = float(np.clip(world.mean(), 0.01, 0.99))
    correct = (pred_prev == target)
    p_model = np.where(correct, CONF, 1.0 - CONF)
    p_base  = np.where(target == 1, p1, 1.0 - p1)
    gain_bits = np.clip(np.log2(p_model) - np.log2(p_base), -4.0, 4.0)
    gain_bits[~alive] = 0.0
    last_gain = gain_bits
    raw_acc = float(correct[alive].mean())

    # ---- 连接更新律（基因 LUT）----
    co = (out_now[NB] == out_now[:, None]).astype(np.int64)
    bucket = np.clip(link // 25, 0, 3)
    lutz = genome[:, 204:220].reshape(N, 8, 2)
    idx = co * 4 + bucket
    lutv = lutz[rows[:, None], idx, 0] * 2 + lutz[rows[:, None], idx, 1]
    delta = np.where(lutv == 0, -LINK_STEP, np.where(lutv == 1, 0, LINK_STEP))
    link = np.clip(link + delta, 0, LINK_MAX).astype(np.int16)

    # ---- P3 能量 ----
    base = FLUX_TOTAL / n_alive
    income = base * (1.0 + GAIN_K * gain_bits)
    link_cost = LINK_COST * (link.sum(axis=1) / float(LINK_MAX))
    cost = BASE_COST + 6.0 * np.clip(L_eff, 0, 32) * COST_PER_BIT + link_cost
    energy[alive] += (income - cost)[alive]
    pred_prev = np.where(alive, pred_final, 0).astype(np.uint8)

    # ---- P4 复制 ----
    cand = np.nonzero(alive & (energy >= COPY_AT))[0]
    if cand.size > 1:
        cand = cand[real_int(cand.size, cand.size)]
    ncopy = 0
    if cand.size > 0:
        pick_slot = real_int(cand.size, 4)
        mut_rand = real_int(cand.size * G_LEN, 10 ** 6).reshape(cand.size, G_LEN)
        for k, c in enumerate(cand):
            opts = NB[c][~alive[NB[c]]]
            if opts.size == 0: continue
            slot = int(opts[pick_slot[k] % opts.size])
            if alive[slot]: continue
            flips = (mut_rand[k] < int(MUT_P * 10 ** 6)).astype(np.uint8)
            e_half = energy[c] * 0.5
            energy[c] = e_half
            alive[slot] = True
            energy[slot] = e_half
            genome[slot] = genome[c] ^ flips
            pred_prev[slot] = 0
            link[slot] = link[c]        # ★S3 表观遗传：子代继承父代连接强度向量
            ncopy += 1

    # ---- P5 死亡 ----
    dead = alive & (energy <= 0.0)
    ndeath = int(dead.sum())
    if ndeath:
        alive[dead] = False
        energy[dead] = 0.0
        genome[dead] = 0
        pred_prev[dead] = 0
        link[dead] = 0
        last_gain[dead] = 0.0
    return int(alive.sum()), float(gain_bits[alive].mean()) if alive.any() else 0.0, raw_acc, ncopy, ndeath

def run(ticks=800, seed=11, verbose=True):
    init_universe(seed)
    hist, gains, accs, births, deaths, links = [], [], [], [], [], []
    t0 = time.perf_counter(); next_report = 100
    for t in range(1, ticks + 1):
        n, g, a, nc, nd = step()
        hist.append(n); gains.append(g); accs.append(a)
        births.append(nc); deaths.append(nd)
        links.append(float(link[alive].mean()) if alive.any() else 0.0)
        if verbose and t >= next_report:
            m = alive
            LEN = bits_to_int(genome[:, 192:200]) % 65
            print('  tick %5d 粒子 %5d gain %+.4f 连接均 %6.2f 出生 %3d 死亡 %3d LEN均 %.1f 用时 %.1fs'
                  % (t, n, g, links[-1], nc, nd,
                     float(LEN[m].mean()) if m.any() else 0, time.perf_counter() - t0), flush=True)
            next_report += 100
    return (np.array(hist), np.array(gains), np.array(accs),
            np.array(births), np.array(deaths), np.array(links))

FORBIDDEN_NAMES = ['uid', 'rank', 'leader', 'merged', 'MAXGROUP', 'share',
                   'gate', 'combine', 'elite', 'privilege', 'special']
FORBIDDEN_TIME_MOD = ['tick', 't', 'round', 'r', 'step', 'gen']
def audit_semantics():
    tree = ast.parse(open(__file__, encoding='utf-8').read())
    names, attrs, kws, tmods = set(), set(), set(), []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name): names.add(node.id)
        elif isinstance(node, ast.Attribute): attrs.add(node.attr)
        elif isinstance(node, ast.keyword) and node.arg: kws.add(node.arg)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            for side in (node.left, node.right):
                if isinstance(side, ast.Name) and side.id in FORBIDDEN_TIME_MOD:
                    tmods.append(side.id)
    out = [(n, 'name') for n in FORBIDDEN_NAMES if n in names]
    out += [(n, 'attr') for n in FORBIDDEN_NAMES if n in attrs]
    out += [(n, 'kw') for n in FORBIDDEN_NAMES if n in kws]
    out += [(n, 'time-mod') for n in set(tmods)]
    return out

def verify(ticks=800):
    print('=== S3 验证（5 槽预测 + 连接投票 + 表观遗传继承）：%d ticks ===' % ticks)
    hist, gains, accs, births, deaths, links = run(ticks, seed=11)
    tail = 300
    h, g, b, d, L = hist[-tail:], gains[-tail:], births[-tail:], deaths[-tail:], links[-tail:]
    print('\n=== V1 稳态+周转 ===')
    print('  人口 %.1f CV %.4f 出生/轮 %.1f 死亡/轮 %.1f 最小 %d'
          % (h.mean(), h.std()/max(1e-9,h.mean()), b.mean(), d.mean(), hist.min()))
    print('\n=== V2 压缩收益 ===')
    print('  mean gain_bits = %+.4f bit/tick' % g.mean())
    print('\n=== V7 连接结构 ===')
    print('  末期平均强度 %.2f（初始 0）  最大 %d' % (L.mean(), int(link[alive].max()) if alive.any() else 0))
    print('  强度时间序列: 每 100 tick 采样 %s' % np.round(links[::100], 2).tolist())
    print('\n=== V8 合作净收益 ===')
    m = alive
    if m.any():
        tot_link = link.sum(axis=1)
        hi = m & (tot_link >= 50); lo = m & (tot_link == 0)
        print('  强连接(%d人) gain %+.4f | 无连接(%d人) gain %+.4f | 差 %+.4f'
              % (int(hi.sum()), float(last_gain[hi].mean()) if hi.any() else 0,
                 int(lo.sum()), float(last_gain[lo].mean()) if lo.any() else 0,
                 (float(last_gain[hi].mean()) if hi.any() else 0) - (float(last_gain[lo].mean()) if lo.any() else 0)))
    print('\n=== V9 空间聚集度（组织是否成簇）===')
    if m.sum() > 100:
        a = link.sum(axis=1).astype(np.float64)
        nbmean = a[NB].mean(axis=1)
        c_ = float(np.corrcoef(a[m], nbmean[m])[0, 1])
        print('  相邻格连接强度相关系数 = %+.3f（>0 ⇒ 成簇；≈0 ⇒ 随机散布）' % c_)
    else:
        print('  存活个体不足')

    print('\n=== V3 长度 ===')
    LEN = bits_to_int(genome[:, 192:200]) % 65
    print('  分位 %s' % (np.percentile(LEN[m], [0,25,50,75,100]).round(1).tolist() if m.any() else '无'))
    print('\n=== V4 审计 ===')
    found = audit_semantics()
    print('  ✅ 无神迹' if not found else '  ⚠️ %s' % found)
    print('\n=== 物理 vs 基因 ===')
    print('  物理: 格点/CA世界/能量通量/压缩收益/复制死亡/**加权投票组合方式**')
    print('  基因: 5槽预测表160位 输出表32 长度8 阈值4 **连接律16** 权重2')

if __name__ == '__main__':
    verify(int(sys.argv[1]) if len(sys.argv) > 1 else 800)

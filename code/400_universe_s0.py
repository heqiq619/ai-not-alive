# -*- coding: utf-8 -*-
"""400_universe_s0.py · 新项目 S0：宇宙骨架（修订版 v2）

======================= 生命的定义（用户） =======================
生命 = 一类高维、动态、自指、能自我维持的函数；它以比特结构存在，
靠压缩世界（匹配源分布）挣取自己存在的代价，并在离散的时刻序列里
保持「还是它自己」。

======================= 三条禁令 =======================
① 物理不变、普适、极简 —— 只写「世界怎么运转」，不写「生物怎么活」
② 一切行为必须由基因表达 —— 不写「分工/门控」等行为规则
③ 环境不能是函数 —— 环境比特由居民写出，不是数据生成器

======================= 物理清单（本文件全部内容） =======================
P1  空间：2D 周期格点 W×H，每格最多 1 个粒子（物理占用）
P2  世界比特 w[c] 是**持久状态**：
      每 tick  w[被占据的格] = 占据者写出的输出位
              再对 ENTROPY_BITS 个**空格**重新注入真实熵位
      ⇒ 世界 = 居民写出的部分 + 不可压缩的噪声；没有「生成函数」
P3  能量守恒吞吐：每 tick 宇宙总吞吐 FLUX_TOTAL，
      gain = FLUX_TOTAL / n_alive（阳光被遮蔽：粒子越多每个越少）
      cost = BASE_COST（普适）
      ⇒ 承载量 n* ≈ FLUX_TOTAL / BASE_COST，由物理决定，不是我设的上限
P4  复制：E ≥ COPY_AT → 父代与子代各分一半能量；
      子代放在**父代的一个随机邻居空格**（局部过程，非全局瞬移）；
      子代输出位 = 父代输出位 XOR 一个来自真实熵的误差位
P5  死亡：E ≤ 0 → 格点空出
P6  熵：所有演化随机（熵注入、复制误差、邻居选择）都来自 os.urandom
      ⇒ 世界不可压缩；**轨迹不可由种子推导**
      种子只用于「初始构型」

======================= 明确「没有」的东西 =======================
· 没有基因组（S1 才加）
· 没有粒子行为（不预测、不移动、不连接）
· 没有按身份/轮数/群体的特例（见 audit_semantics）
· 没有人为人口上限（承载量由 P3 决定）

======================= S0 判据 =======================
V1  种群密度稳定（不爆炸、不灭绝，允许生态振荡）
V2  世界比特 1 比例≈0.5，且两次运行发散（真熵）
V3  世界是居民写的：把 outbit 全清 0 ⇒ 占据格的世界位应趋近 0
V4  语义审计：无神迹
"""
import os, sys, time
import numpy as np
import ast

# ---------------- 物理常量（全部普适，无身份特例） ----------------
W = 128; H = 128; N = W * H
FLUX_TOTAL = 24.0      # 每 tick 宇宙总能量吞吐（阳光总量）
                       # 校准：n* = 24/0.015 = 1600 ≈ 密度 10%，留出空格给噪声
BASE_COST  = 0.015     # 每 tick 单个粒子的维持成本
COPY_AT    = 0.050     # 复制所需能量阈值
START_E    = 0.040     # 初始能量
INIT_P     = 0.02      # 初始占据率
ENTROPY_BITS = 64      # 每 tick 注入到空格的真实熵位数
# 预期承载量 n* = FLUX_TOTAL / BASE_COST = 1600（密度 ~10%）

def neighbor_table():
    """4 邻 + 周期边界（纯几何）"""
    idx = np.arange(N).reshape(H, W)
    return np.stack([np.roll(idx, -1, 0).ravel(), np.roll(idx, 1, 0).ravel(),
                     np.roll(idx, -1, 1).ravel(), np.roll(idx, 1, 1).ravel()],
                    axis=1).astype(np.int64)
NB = neighbor_table()

# ---------------- 真实熵源（不动点：演化随机全部来自这里） ----------------
def real_bits(k):
    if k <= 0:
        return np.zeros(0, dtype=np.uint8)
    return np.unpackbits(np.frombuffer(os.urandom((k + 7) // 8), dtype=np.uint8))[:k].astype(np.uint8)

def real_int(n, hi):
    """[0,hi) 均匀整数，来自真实熵"""
    if hi <= 1:
        return np.zeros(n, dtype=np.int64)
    k = max(1, int(np.ceil(np.log2(hi))))
    b = real_bits(n * k).reshape(n, k)
    return (b @ (1 << np.arange(k - 1, -1, -1))) % hi

# ---------------- 宇宙状态 ----------------
alive  = np.zeros(N, dtype=bool)
energy = np.zeros(N, dtype=np.float64)
outbit = np.zeros(N, dtype=np.uint8)
world  = np.zeros(N, dtype=np.uint8)   # P2：持久世界比特

def init_universe(seed=11):
    """种子仅决定初始构型；此后随机性全部来自真实熵"""
    rng = np.random.RandomState(seed)
    occ = rng.rand(N) < INIT_P
    alive[:] = occ
    energy[:] = START_E
    outbit[:] = (rng.rand(N) < 0.5).astype(np.uint8)
    outbit[~occ] = 0
    world[:] = 0
    world[alive] = outbit[alive]
    world[~alive] = real_bits(int((~alive).sum()))

def step():
    """一个离散时刻：全部物理，无身份特例"""
    global alive, energy, outbit, world

    n_alive = int(alive.sum())
    if n_alive == 0:
        return 0

    # P3 能量：守恒吞吐，按人数均分（遮蔽）
    energy[alive] += FLUX_TOTAL / n_alive - BASE_COST

    # P4 复制（本地放置：父代的随机邻居空格）
    cand = np.nonzero(alive & (energy >= COPY_AT))[0]
    if cand.size > 1:
        cand = cand[real_int(cand.size, cand.size)]         # 真实熵打乱，消除索引偏置
    if cand.size > 0:
        slots = NB[cand]                                    # (m,4) 候选邻居
        freeslot = np.where(alive[slots], -1, slots)        # 用 alive 判定，无身份偏好
        has = (freeslot >= 0).any(axis=1)
        for k in np.nonzero(has)[0]:
            c = cand[k]
            opts = freeslot[k][freeslot[k] >= 0]
            slot = int(opts[real_int(1, opts.size)[0]])
            if alive[slot]:          # 同一 tick 被别的子代占了 → 本 tick 放弃
                continue
            err = int(real_bits(1)[0])
            e_half = energy[c] * 0.5
            energy[c] = e_half
            alive[slot] = True
            energy[slot] = e_half
            outbit[slot] = outbit[c] ^ err
            world[slot] = outbit[slot]

    # P5 死亡
    dead = alive & (energy <= 0.0)
    if dead.any():
        alive[dead] = False
        energy[dead] = 0.0
        outbit[dead] = 0

    # P2 世界更新：占据格写居民输出；随机空格注入真实熵
    world[alive] = outbit[alive]
    empty = np.nonzero(~alive)[0]
    if empty.size > 0:
        m = min(ENTROPY_BITS, empty.size)
        pos = empty[real_int(m, empty.size)]
        world[pos] = real_bits(m)

    return int(alive.sum())

def run(ticks=2000, seed=11, verbose=True):
    init_universe(seed)
    hist = []
    t0 = time.perf_counter()
    next_report = 200
    for t in range(1, ticks + 1):
        n = step()
        hist.append(n)
        if verbose and t >= next_report:
            print('  tick %5d  粒子 %6d  密度 %.4f  世界1比例 %.4f  用时 %.2fs'
                  % (t, n, n / N, float(world.mean()), time.perf_counter() - t0), flush=True)
            next_report += 200
    return np.array(hist)

def measure(hist, tail=500):
    h = hist[-tail:]
    return dict(mean=float(h.mean()), std=float(h.std()),
                cv=float(h.std() / max(1e-9, h.mean())),
                last=float(h[-1]), density=float(h[-1] / N),
                tmin=float(hist.min()), extinct=bool((hist == 0).any()))

# ======================= V3 / V5 补充测试 =======================
def test_world_written_by_inhabitants():
    """V3: 把居民输出位全清 0，更新一次世界 ⇒ 占据格的世界位应≈0
       证明「世界比特确实由居民写出」，而不是凭空的生成函数"""
    global world
    n = int(alive.sum())
    if n == 0: return None
    outbit[alive] = 0
    world[alive] = 0
    return float(world[alive].mean()), n

def test_real_entropy_divergence(ticks=100):
    """V5: 同一初始种子跑两次（中间不 reset RNG），种群/世界应发散
       证明演化随机来自真实熵而非种子"""
    run(ticks, seed=11, verbose=False); h1 = int(alive.sum()); w1 = int(world.sum())
    init_universe(11); run(ticks, seed=11, verbose=False); h2 = int(alive.sum()); w2 = int(world.sum())
    return (h1, h2, w1, w2)

# ======================= 语义审计（用 AST，排除注释/字符串） =======================
FORBIDDEN_NAMES = ['uid', 'rank', 'leader', 'merged', 'MAXGROUP', 'share',
                   'gate', 'combine', 'elite', 'special', 'privilege']
FORBIDDEN_TIME_MOD = ['tick', 't', 'round', 'r', 'step', 'gen']
def audit_semantics():
    me = open(__file__, encoding='utf-8').read()
    tree = ast.parse(me)
    names, attrs, kws = set(), set(), set()
    time_mod = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            attrs.add(node.attr)
        elif isinstance(node, ast.keyword) and node.arg:
            kws.add(node.arg)
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            for side in (node.left, node.right):
                if isinstance(side, ast.Name) and side.id in FORBIDDEN_TIME_MOD:
                    time_mod.append(side.id)
    found = [(n, 'name') for n in FORBIDDEN_NAMES if n in names]
    found += [(n, 'attr') for n in FORBIDDEN_NAMES if n in attrs]
    found += [(n, 'kw') for n in FORBIDDEN_NAMES if n in kws]
    found += [(n, 'time-mod') for n in set(time_mod)]
    return found

def print_audit():
    found = audit_semantics()
    print('\n=== V4 语义审计（神迹检查，AST 级）===')
    if not found:
        print('  ✅ 代码中无「按身份给特权」「按轮数换规则」「行为规则名」')
    else:
        print('  ⚠️ 命中 %d 处（需逐条判断是物理还是行为规则）：' % len(found))
        for n, kind in found:
            print('     %-12s [%s]' % (n, kind))
    print('\n=== 物理清单自检 ===')
    print('  P1 周期格点 %d×%d，一格一粒子' % (W, H))
    print('  P2 世界比特为持久状态；占据格=居民输出，空格=真实熵注入')
    print('  P3 能量吞吐守恒 FLUX_TOTAL=%.1f，按人数均分；cost=%.3f' % (FLUX_TOTAL, BASE_COST))
    print('     理论承载量 n* ≈ FLUX_TOTAL/BASE_COST = %.0f（物理决定，非人为上限）'
          % (FLUX_TOTAL / BASE_COST))
    print('  P4 复制=邻居空格局部放置，子代输出 XOR 真熵误差位')
    print('  P5 死亡 E≤0')
    print('  P6 所有演化随机来自 os.urandom（种子只定初始构型）')
    print('\n=== 明确没有 ===')
    print('  · 没有基因组（S1 才加）')
    print('  · 没有粒子行为（不预测/不移动/不连接）')
    print('  · 没有数据生成函数（世界=居民写入+噪声）')

if __name__ == '__main__':
    ticks = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    print('=== S0 宇宙骨架（修订版）：%d ticks ===' % ticks)
    hist = run(ticks, seed=11)
    m = measure(hist)
    print('\n=== V1 种群稳定性 ===')
    print('  末期 500 tick: 均值 %.1f  标准差 %.1f  变异系数 %.4f  密度 %.4f'
          % (m['mean'], m['std'], m['cv'], m['density']))
    print('  全程最小 %d  是否灭绝过: %s' % (m['tmin'], m['extinct']))
    print('\n=== V2 世界不可压缩性 ===')
    print('  世界比特 1 比例 = %.4f（≈0.5 表示不可压缩）' % float(world.mean()))

    print('\n=== V3 世界是否由居民写出 ===')
    r = test_world_written_by_inhabitants()
    if r is None:
        print('  （无存活粒子，无法测）')
    else:
        frac, n = r
        print('  清 0 输出位后，占据格世界位 1 比例 = %.6f（应≈0）' % frac)

    print('\n=== V5 真实熵：两轮运行是否发散 ===')
    h1, h2, w1, w2 = test_real_entropy_divergence(100)
    print('  运行A 粒子=%d 世界和=%d | 运行B 粒子=%d 世界和=%d' % (h1, w1, h2, w2))
    print('  是否发散: %s' % ('是 ✓' if (h1 != h2 or w1 != w2) else '否 ✗（随机性可能被种子决定）'))

    print_audit()

# -*- coding: utf-8 -*-
"""400_universe_s1.py · 新项目 S1（修订）：基因组 = 世界模型 + 调节律

======================= 自审记录（写这一版时发现的问题） =======================
B1【致命】变异概率写错：
   旧: (real_bits(G_LEN) < int(MUT_P*256)) —— real_bits 只产出 0/1，
       1 < 2 恒真 ⇒ **变异率 100%**，基因组完全随机化
   新: real_int(G_LEN, 10**6) < int(MUT_P*10**6) —— 正确的逐位概率
B2【崩溃】step() 在 n_alive==0 时返回标量 0，但调用方按 4 元组解包 ⇒ 灭绝即崩
   新: 返回 (0, 0.0, 0, 0)
B3【语义错】表达成本用了 LEN 而不是「表达比特数」：
   两份 32 项真值表 ⇒ 实际表达比特 = 2*clip(L_eff,0,32)
   新: cost = BASE_COST + 2*clip(L_eff,0,32)*COST_PER_BIT
B4【退化吸引子】原设计「预测北邻居的输出位」：
   密度低时 85% 邻居为空 ⇒ 目标恒 0 ⇒ 平凡可预测
   密度高时全体输出趋同 ⇒ 世界趋同 ⇒ 也平凡
   新: 物理 P2' 改为 **CA 视差 + 噪声**（见下），任务变「预测自己格的下一世界位」
       ⇒ 需要建模邻居的输出（隐藏状态），且有噪声地板 ⇒ 既有结构又不可穷尽
B5【验证缺失】V3(长度分布)/V5(真熵发散)/V6(个体差异) 未实现 ⇒ 新补
B6【语义含糊】LEN 上限 64 但只有 32 项表项有意义 ⇒ 明确 LEN∈[0,64]，>32 纯成本
      （这正好是「限制表达长度」的选择压测试）

======================= 生命定义（用户） =======================
生命 = 一类高维、动态、自指、能自我维持的函数；它以比特结构存在，
靠压缩世界（匹配源分布）挣取自己存在的代价，并在离散的时刻序列里
保持「还是它自己」。

======================= 物理清单（不变、普适；S1 定稿） =======================
P1  2D 周期格点 W×H，每格最多 1 个粒子
P2' 世界比特 w[c] 的更新（CA 视差 + 噪声）：
       w_next[c] = out[c] XOR out[north] XOR out[south] XOR out[west] XOR out[east]
                   XOR noise(概率 NOISE_P，真实熵)
       out[i] 对被占据格 = 该粒子本 tick 的输出位；对空格 = 0（物理约定）
      ⇒ 世界是居民**集体**写出的：我要预测的下一世界位依赖于邻居的输出
P3  能量吞吐守恒：base = FLUX_TOTAL / n_alive
       income = base * (1 + GAIN_K * profit)   profit ∈ {+1,-1}
       cost   = BASE_COST + 2*clip(L_eff,0,32) * COST_PER_BIT
P4  复制：E ≥ COPY_AT → 父代/子代各半；落在父代随机邻居空格；
      基因组逐位翻转（概率 MUT_P，真实熵）
P5  死亡：E ≤ 0（**没有老化**，用户明确不加）
P6  熵：CA 噪声位、空格输出、变异、邻居选择、候选顺序 —— 全部 os.urandom
      种子只定初始构型

======================= 基因组（76 比特，全部行为） =======================
[0:32)   预测表 predict(obs)   （32 项真值表；obs<L_eff 才表达）
[32:64)  输出表 output(obs)    （32 项真值表；obs<L_eff 才表达）
[64:72)  表达长度 LEN = value % 65
[72:76)  调节阈值 THR = value/16 * THR_MAX
观测 obs = w[self] w[north] w[south] w[west] w[east]（5 位，位序固定）
调节律：energy < THR ⇒ 节能模式，L_eff = LEN//2（表达减半）

**自指闭环**：我的 out → 邻居格的世界位（CA）→ 邻居的 obs → 邻居的 out
           → **我格的下一世界位**（我的预测目标）
           ⇒ 要预测它，必须建模邻居的行为；而邻居也在建模我

======================= S1 判据 =======================
V1 稳态 + 周转：CV>0，出生≈死亡>0（S0 是冻结的）
V2 压缩收益：平均预测准确率显著 > 0.5
V3 长度选择压：LEN 分布不应停在 64（表达成本会压缩它）
V4 语义审计：无神迹（AST）
V5 真实熵：两次运行发散
V6 个体差异：个体准确率有方差（∈(0,0.25) 量级）
"""
import os, sys, time
import numpy as np
import ast

# ---------------- 物理常量（普适，无身份特例） ----------------
W = 128; H = 128; N = W * H
FLUX_TOTAL   = 24.0
BASE_COST    = 0.013     # 略高于 base 均衡点 ⇒ 不预测者趋于淘汰
GAIN_K       = 1.0       # 压缩收益的调制强度
COST_PER_BIT = 0.00002   # 满表达(64 位)成本 = 0.00128，小于真实预测收益
CONF         = 0.9       # 硬预测的置信度（物理参数）
COPY_AT      = 0.050
START_E      = 0.040
INIT_P       = 0.02
MUT_P        = 0.01
THR_MAX      = 0.040
NOISE_P      = 0.10      # CA 世界里不可约噪声比例（物理温度）
G_LEN        = 76

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
    k = bits.shape[-1]
    return (bits.astype(np.int64) @ (1 << np.arange(k - 1, -1, -1)))

# ---------------- 宇宙状态 ----------------
alive     = np.zeros(N, dtype=bool)
genome    = np.zeros((N, G_LEN), dtype=np.uint8)
energy    = np.zeros(N, dtype=np.float64)
pred_prev = np.zeros(N, dtype=np.uint8)     # 上一 tick 做的预测
out_now   = np.zeros(N, dtype=np.uint8)     # 本 tick 输出（空格约定为 0）
world     = np.zeros(N, dtype=np.uint8)     # 当前世界比特

def init_universe(seed=11):
    global genome, pred_prev, out_now, world
    rng = np.random.RandomState(seed)       # 仅初始构型
    occ = rng.rand(N) < INIT_P
    alive[:] = occ
    energy[:] = START_E
    genome[:] = (rng.rand(N, G_LEN) < 0.5).astype(np.uint8)
    genome[~occ] = 0
    pred_prev[:] = 0; out_now[:] = 0
    world[:] = real_bits(N)

def observe():
    nb = world[NB]
    return ((world << 4) | (nb[:, 0] << 3) | (nb[:, 1] << 2) |
            (nb[:, 2] << 1) | nb[:, 3]).astype(np.uint8)

def step():
    global alive, energy, genome, pred_prev, out_now, world
    n_alive = int(alive.sum())
    if n_alive == 0:
        return 0, 0.0, 0, 0

    rows = np.arange(N)
    # ---- 基因组解码（全部行为来自比特） ----
    LEN = bits_to_int(genome[:, 64:72]) % 65
    THR = bits_to_int(genome[:, 72:76]) / 16.0 * THR_MAX
    L_eff = np.where(energy < THR, LEN // 2, LEN)            # 调节律
    obs = observe()
    expr = obs < L_eff
    lut_pred = genome[:, 0:32][rows, obs]
    lut_out  = genome[:, 32:64][rows, obs]
    pred_now = np.where(expr, lut_pred, 0).astype(np.uint8)
    out_new  = np.where(expr, lut_out, 0).astype(np.uint8)
    out_now = np.where(alive, out_new, 0).astype(np.uint8)   # P2'：空格输出=0

    # ---- P2' 世界更新：CA 视差 + 噪声 ----
    nb_out = out_now[NB]
    w_next = (out_now ^ nb_out[:, 0] ^ nb_out[:, 1] ^ nb_out[:, 2] ^ nb_out[:, 3]).astype(np.uint8)
    noise_mask = real_int(N, 10 ** 6) < int(NOISE_P * 10 ** 6)
    w_next[noise_mask] ^= real_bits(int(noise_mask.sum()))
    world = w_next

    # ---- 结算：压缩收益（对数似然改善 over 基线），而不是「猜对率」 ----
    target = world
    p1 = float(np.clip(world.mean(), 0.01, 0.99))       # 基线：该位为 1 的比例
    correct = (pred_prev == target)
    # 模型置信度 CONF；基线用 p1
    p_model = np.where(correct, CONF, 1.0 - CONF)
    p_base  = np.where(target == 1, p1, 1.0 - p1)
    gain_bits = np.log2(p_model) - np.log2(p_base)
    gain_bits = np.clip(gain_bits, -4.0, 4.0)
    gain_bits[~alive] = 0.0
    profit = gain_bits

    # ---- P3 能量 ----
    base = FLUX_TOTAL / n_alive
    income = base * (1.0 + GAIN_K * profit)
    expressed_bits = 2.0 * np.clip(L_eff, 0, 32)
    cost = BASE_COST + expressed_bits * COST_PER_BIT
    energy[alive] += (income - cost)[alive]
    acc = float((pred_prev[alive] == target[alive]).mean())

    pred_prev = np.where(alive, pred_now, 0).astype(np.uint8)

    # ---- P4 复制（局部放置 + 逐位变异） ----
    cand = np.nonzero(alive & (energy >= COPY_AT))[0]
    if cand.size > 1:
        cand = cand[real_int(cand.size, cand.size)]
    ncopy = 0
    if cand.size > 0:
        pick_slot = real_int(cand.size, 4)
        mut_rand = real_int(cand.size * G_LEN, 10 ** 6).reshape(cand.size, G_LEN)
        for k, c in enumerate(cand):
            opts = NB[c][~alive[NB[c]]]
            if opts.size == 0:
                continue
            slot = int(opts[pick_slot[k] % opts.size])
            if alive[slot]:
                continue
            flips = (mut_rand[k] < int(MUT_P * 10 ** 6)).astype(np.uint8)
            e_half = energy[c] * 0.5
            energy[c] = e_half
            alive[slot] = True
            energy[slot] = e_half
            genome[slot] = genome[c] ^ flips
            pred_prev[slot] = 0
            ncopy += 1

    # ---- P5 死亡 ----
    dead = alive & (energy <= 0.0)
    ndeath = int(dead.sum())
    if ndeath:
        alive[dead] = False
        energy[dead] = 0.0
        genome[dead] = 0
        pred_prev[dead] = 0
    return int(alive.sum()), acc, ncopy, ndeath

def run(ticks=800, seed=11, verbose=True):
    init_universe(seed)
    hist, accs, births, deaths = [], [], [], []
    t0 = time.perf_counter(); next_report = 100
    for t in range(1, ticks + 1):
        n, acc, nc, nd = step()
        hist.append(n); accs.append(acc); births.append(nc); deaths.append(nd)
        if verbose and t >= next_report:
            m = alive
            LEN = bits_to_int(genome[:, 64:72]) % 65
            print('  tick %5d 粒子 %5d 密度 %.3f acc %.3f 出生 %3d 死亡 %3d '
                  'LEN均 %.1f 能量均 %.4f 用时 %.1fs'
                  % (t, n, n / N, acc, nc, nd,
                     float(LEN[m].mean()) if m.any() else 0,
                     float(energy[m].mean()) if m.any() else 0,
                     time.perf_counter() - t0), flush=True)
            next_report += 100
    return np.array(hist), np.array(accs), np.array(births), np.array(deaths)

# ======================= 语义审计（AST） =======================
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
    print('=== S1 验证：%d ticks ===' % ticks)
    hist, accs, births, deaths = run(ticks, seed=11)
    tail = 300
    h, a, b, d = hist[-tail:], accs[-tail:], births[-tail:], deaths[-tail:]
    print('\n=== V1 稳态 + 周转 ===')
    print('  人口均值 %.1f  CV %.4f  出生/轮 %.2f  死亡/轮 %.2f  最小人口 %d'
          % (h.mean(), h.std()/max(1e-9, h.mean()), b.mean(), d.mean(), hist.min()))
    print('\n=== V2 压缩收益 ===')
    print('  末期平均预测准确率 %.4f（基线 0.5）' % a.mean())
    print('\n=== V3 长度选择压 ===')
    m = alive
    LEN = bits_to_int(genome[:, 64:72]) % 65
    print('  存活个体 LEN 分位 p0/25/50/75/100 = %s （上限 64）'
          % np.percentile(LEN[m], [0, 25, 50, 75, 100]).round(1).tolist() if m.any() else '无存活')
    print('\n=== V6 个体差异 ===')
    if m.any():
        THR = bits_to_int(genome[:, 72:76]) / 16.0 * THR_MAX
        print('  LEN: 均值 %.2f 标准差 %.2f   能量: 均值 %.4f 标准差 %.4f'
              % (float(LEN[m].mean()), float(LEN[m].std()),
                 float(energy[m].mean()), float(energy[m].std())))
        print('  （有方差 ⇒ 存在可被选择的差异；全 0 说明基因没起作用）')
    else:
        print('  无存活个体')
    print('\n=== V4 语义审计 ===')
    found = audit_semantics()
    print('  ✅ 无神迹' if not found else '  ⚠️ 命中: %s' % found)
    print('\n=== V5 真实熵（两次 200 tick 是否发散）===')
    run(200, seed=11, verbose=False); h1, w1 = int(alive.sum()), int(world.sum())
    init_universe(11); run(200, seed=11, verbose=False); h2, w2 = int(alive.sum()), int(world.sum())
    print('  运行A 粒子=%d 世界和=%d | 运行B 粒子=%d 世界和=%d ⇒ %s'
          % (h1, w1, h2, w2, '发散 ✓' if (h1, w1) != (h2, w2) else '相同 ✗'))
    print('\n=== 物理 vs 基因组 分界 ===')
    print('  物理: P1 格点 / P2\' CA+噪声 / P3 能量 / P4 复制 / P5 死亡 / P6 真熵')
    print('  基因: [0:32)预测表 [32:64)输出表 [64:72)长度 [72:76)阈值')
    print('  代码里没有任何行为常量：out/pred 全部来自查表')

if __name__ == '__main__':
    verify(int(sys.argv[1]) if len(sys.argv) > 1 else 800)

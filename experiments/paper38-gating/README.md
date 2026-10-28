# 论文-38 复现材料：按 token 的是/否门控

对应论文：《按 token 的是/否门控：从组合结构到真实减算》
DOI: https://doi.org/10.5281/zenodo.23720545

## 目录

```
scripts/
  1199_gpt2_gates.py          # GPT-2 模拟门控（全算、后处理），得到 PPL 103→64
  1204_gpt2_real_skip.py      # GPT-2 真实减算（按 token 挑子集计算），得到 PPL 121→107
  1192_token_gates.py         # 合成：每 token 门控 + 有效组合图
  1194_cross_layer_gates2.py  # 合成：跨层门控 + 用进废退
  1196_iterative_steps.py     # 合成：按需迭代（简单 0 步、复杂 8 步）
  1197_dk_frontier.py         # 合成：空间-时间前沿（d,k）
  1198_adaptive_dk.py         # 合成：自适应迭代（含门控）
data/
  数据-GPT2门控.json          # 模拟门控 PPL 与开门率
  数据-真实减算门控.json      # 真实减算 PPL、激活比例、剪枝
  数据-每token门控.json       # 合成：每 token 门控
  数据-跨层门控2.json         # 合成：跨层门 + 用进废退
  数据-按需迭代.json          # 合成：按需迭代
  数据-dk前沿.json            # 合成：(d,k) 前沿
  数据-自适应dk.json          # 合成：自适应 (d,k)
```

## 环境

- Python 3.12
- torch（CPU 即可；有 CUDA 更快）
- transformers（4.46.x）
- 本地 GPT-2（transformers 格式，默认 `./models/gpt2`）
- 语料：tinyshakespeare，存为 `_tinyshakespeare.txt`

## 复现关键数字

### GPT-2 模拟门控（1199）

```bash
python scripts/1199_gpt2_gates.py
```

- 基础 PPL ≈ 103.1（40 个验证批）
- 训练门控后（模拟，全算）PPL ≈ 64.1
- 各层开门率 ≈ 0.83–0.99

### GPT-2 真实减算（1204）

```bash
python scripts/1204_gpt2_real_skip.py
```

必须验证的两件事：

1. **正确性检查**：真实执行、全开门时，PPL 必须等于标准前向（本机为 121.18 = 121.18）。若不等，说明 gather/scatter 实现有问题。
2. **随机跳层对照**：随机跳过同样比例的层，PPL 应爆炸（本机 5% 随机跳 → 345），反衬门学到的是结构。

本机结果：

| 设置 | PPL | 真实激活比例 |
|---|---|---|
| 基础 | 121.18 | — |
| 真实执行 + 全开门 | 121.18 | 0.992 |
| 真实执行 + 学到的门 | 107.28 | 0.950（省约 5%） |
| 用进废退剪枝后 | 117.16 | 0.875（省约 12.5%） |

### 合成实验（1192/1194/1196/1197/1198）

直接运行即可；脚本内带打印与保存 JSON。

## 注意事项

- 所有数字来自单种子、小验证集（10–40 个批次），有方差；不是大模型结论。
- GPT-2 实验是"冻结模型 + 门后训练"，与 MoD 等"从零联合训练"的方式不同（见论文第六节）。
- 模拟门控不省算力；只有"真实减算"（1204）才是真省。

## 引用

He Qi. (2026). 按 token 的是/否门控：从组合结构到真实减算 [Preprint]. Zenodo.
https://doi.org/10.5281/zenodo.23720545

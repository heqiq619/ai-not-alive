# GPT-2 门控实验 · 云端一键包（阿里云 PAI-DSW）

## 一、在 DSW 里做什么

1. 打开 PAI-DSW 控制台，新建实例：
   - 镜像：PyTorch 2.x（GPU）
   - 规格：V100 / A10 / T4 均可（GPT-2 124M 够用）
   - 用「免费试用」或按量付费
2. 把本目录（或 zip）上传到 DSW 的工作目录，例如 `/mnt/workspace/gpt2_gating/`
3. 打开终端，运行：

```bash
cd /mnt/workspace/gpt2_gating
bash run.sh
```

## 二、run.sh 会做什么

```bash
pip install -q transformers datasets
export HF_ENDPOINT=https://hf-mirror.com
python - <<'PY'
from transformers import GPT2LMHeadModel, GPT2Tokenizer
GPT2LMHeadModel.from_pretrained('gpt2')
GPT2Tokenizer.from_pretrained('gpt2')
PY
curl -L -o tinyshakespeare.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
STEPS=1500 python gpt2_gating_lagrange.py
```

- 若 GitHub 下载慢，可换成：`wget -O tinyshakespeare.txt https://hf-mirror.com/datasets/... ` 或手动上传（本包已带 `tinyshakespeare.txt`，可直接用）
- GPT-2 权重若下载失败，改用 ModelScope：
  `pip install modelscope && modelscope download --model AI-ModelScope/gpt2 --local_dir ./gpt2`
  然后把脚本里 `from_pretrained('gpt2')` 改成 `from_pretrained('./gpt2')`

## 三、跑完把什么发回来

```
results_gpt2_gating.json   ← 必须
终端日志（训练过程的 PPL/层均/λ）
```

## 四、预期时间与费用

```
· 环境 + 下载：5~10 分钟
· 三组训练（1500 步）：约 30~50 分钟（V100）
· 费用：免费试用额度内，或按量 ¥10~30
```

## 五、脚本里的三组对照

| 组 | 说明 |
|---|---|
| plain | 普通微调，无门，全 12 层 |
| frozen_gate | 冻结主干，只训门；拉格朗日目标平均 6 层 |
| joint_gate | 主干 + 门共同训练；拉格朗日目标平均 6 层 |

评测：验证 PPL、平均计算层数。

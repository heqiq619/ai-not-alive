#!/usr/bin/env bash
set -e
echo "== 安装依赖 =="
pip install -q transformers
export HF_ENDPOINT=https://hf-mirror.com
echo "== 准备 GPT-2 权重 =="
python - <<'PY'
from transformers import GPT2LMHeadModel, GPT2Tokenizer
GPT2LMHeadModel.from_pretrained('gpt2')
GPT2Tokenizer.from_pretrained('gpt2')
print('GPT-2 权重就绪')
PY
echo "== 准备数据 =="
if [ ! -f tinyshakespeare.txt ]; then
  curl -L -o tinyshakespeare.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
fi
echo "== 开始训练（三组） =="
STEPS=${STEPS:-1500} python gpt2_gating_lagrange.py
echo "== 完成，结果：results_gpt2_gating.json =="
ls -la results_gpt2_gating.json

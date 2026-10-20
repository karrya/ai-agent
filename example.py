#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 00:29
@Author :   likai.com
@File   :   example.py.py
"""
import dotenv
from openai import OpenAI

# 加载 .env 中的 OPENAI_API_KEY / OPENAI_BASE_URL，OpenAI SDK 会自动读取
dotenv.load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手。"},
        {"role": "user", "content": "你好，1+1等于多少？"}
    ]
)

print(completion.choices[0].message.content)

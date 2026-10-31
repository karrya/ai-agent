#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 18:10
@Author :   likai.com
@File   :   1.LLM与ChatModel使用技巧.py
"""
from datetime import datetime

import dotenv

dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAI

# 加载 .env 中的 OPENAI_API_KEY / OPENAI_BASE_URL，OpenAI SDK 会自动读取

# 1、编排prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个OpenAI机器人，现在时间是：{now}"),
     ("human", "{query}")]
).partial(now=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# 2、创建大语言模型
llm = ChatOpenAI(model="kimi-k3")

stream_response = llm.stream(
    prompt.invoke({"query": "你好，简单介绍哦一下LLM和LLMOps的区别"})
)

for str_content in stream_response:
   print(str_content.content, end="", flush=True)

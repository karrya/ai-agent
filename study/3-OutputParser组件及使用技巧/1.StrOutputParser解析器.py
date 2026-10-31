#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 19:30
@Author :   likai.com
@File   :   1.StrOutputParser解析器.py
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import dotenv

dotenv.load_dotenv()


# 解析器
parser = StrOutputParser()

content = parser.parse("成吃啥藕粉")
print(content)

llm = ChatOpenAI(model="kimi-k3")

template = ChatPromptTemplate.from_template("{query}")

template.invoke({"query": "你好，你是？"})

content = parser.invoke(llm.invoke(template.invoke({"query": "你好，你是？"})))

print(content)

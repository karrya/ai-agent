#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 19:30
@Author :   likai.com
@File   :   1.StrOutputParser解析器.py
"""
import dotenv
dotenv.load_dotenv()

from langchain_core.output_parsers import JsonOutputParser
from pydantic.v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# 1、创建一个json数据结构，用于告诉打语言模型这个json长啥样
class Joker(BaseModel):
    # 冷笑话
    joke: str = Field(description="回答用户的冷笑话")
    # 冷笑话的笑点
    punchline: str = Field(description="这个冷笑话的笑点")


parser = JsonOutputParser(pydantic_object=Joker)

# print(parser.get_format_instructions())
# 2、构建提示模板
prompt = (ChatPromptTemplate.from_template("请根据用户的提问进行回答，\n{format_instructions}\n{query}")
          .partial(format_instructions=parser.get_format_instructions()))

# print(prompt)

# print(prompt.format(query="请讲一个关于程序员的冷笑话"))


# 3、构建一个大语言模型
llm = ChatOpenAI(model="kimi-k3")

invoke = parser.invoke(llm.invoke(prompt.invoke({"query": "请讲一个关于程序员的冷笑话"})))

print(invoke)
print(type(invoke))
print(invoke.get("punchline"))
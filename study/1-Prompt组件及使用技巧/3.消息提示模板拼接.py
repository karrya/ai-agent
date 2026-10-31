#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 12:10
@Author :   likai.com
@File   :   3.消息提示模板拼接.py
"""
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

zhangsan = PromptTemplate.from_template("你好，我是{name1}111。")
lisi = PromptTemplate.from_template("你好，我是{name2}222。")



chat_prompt = zhangsan + lisi

print(chat_prompt.format(name1="张三", name2="李四"))


print("=" * 80)

messages1 = ChatPromptTemplate.from_messages([("system", "测试{test}")])
messages2 = ChatPromptTemplate.from_messages([HumanMessage("wahahh")])

messages3 = messages1 + messages2

print(messages3.invoke({"test": "AAA"}).to_string())
#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 11:10
@Author :   likai.com
@File   :   1.Prompt组件基础用法.py
"""
from datetime import datetime

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

from langchain_core.messages import AIMessage


"""
PromptTemplate 使用
"""
prompt = PromptTemplate.from_template("请将一个关于{subject}的笑话")
# format，直接输出文本消息
print(prompt.format(subject="喜剧演员"))

# invoke，输出是一个PromptValue对象
prompt_value = prompt.invoke({"subject": "程序猿"})
# 将对象转为文本消息
print(prompt_value.to_string())
# 将文本转为消息列表
print(prompt_value.to_messages())


print("=" * 80)

"""
ChatPromptTemplate 使用
"""
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，当前时间为：{now}"),
    # 人类消息提示模板
    HumanMessagePromptTemplate.from_template("请将一个关于【{subject}】的笑话"),
    # 有时候还有其他消息，但是不确定，就用消息占位符
    MessagesPlaceholder("chat_history")
])
# 使用partial可以提前为变量赋值，赋值后仍然是个模板
chat_prompt = chat_prompt.partial(now=datetime.now())
# 但是调用invoke必须为所有变量赋值
chat_prompt_value = chat_prompt.invoke({
    "now": datetime.now(),
    "subject": "哇哈哈",
    "chat_history": []
})

print(chat_prompt_value.to_messages())
print(chat_prompt_value)

chat_prompt_value2 = chat_prompt.invoke({
    "now": datetime.now(),
    "subject": "哇哈哈",
    "chat_history": [
        ("human","我叫李凯")
    ]
})

print(chat_prompt_value2)


chat_prompt_value3 = chat_prompt.invoke({
    "now": datetime.now(),
    "subject": "哇哈哈",
    "chat_history": [
        ("human","我叫李凯"),
        AIMessage("你好，我是豆包")
    ]
})

print(chat_prompt_value3)
print(chat_prompt_value3.to_string())

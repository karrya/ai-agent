#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 12:19
@Author :   likai.com
@File   :   4.复用提示词模板.py
"""

from langchain_core.prompts import PromptTemplate

full_template = PromptTemplate.from_template("""
{instruction}
{example}
{start}
""")

# 描述模板
instruction_prompt = PromptTemplate.from_template("你正在模拟{person}")

# 示例模板
example_prompt = PromptTemplate.from_template("""下面是一个交互例子

Q：{example_q}
A：{example_a}

""")

# 开始模板
start_prompt = PromptTemplate.from_template("""现在，你是一个真实的人，请回答用户的问题：
Q：{input}
A：
""")

pipeline_prompt = [
    ("instruction", instruction_prompt),
    ("example", example_prompt),
    ("start", start_prompt),
]

inputs = {
    "person": "雷军",
    "example_q": "你最喜欢的汽车是什么？",
    "example_a": "小米汽车",
    "input": "你最喜欢的手机是什么？",
}

pipline_prompt = PromptTemplate.from_template(
    full_template.format(**{
        name: prompt.format(**inputs)
        for name, prompt in pipeline_prompt
    })
)

print(pipline_prompt.template)

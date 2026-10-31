#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/31 11:47
@Author :   likai.com
@File   :   2.字符串拼接.py
"""

from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("请讲一个关于【{subject}】的冷笑话！" + "，让我开心一下" + "\n使用{language}语言")


print(template.format(subject="科学", language="汉语"))
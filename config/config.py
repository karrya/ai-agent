#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 22:25
@Author :   likai.com
@File   :   config.py
"""

class Config:
    def __init__(self):
        # 关闭csrf保护
        self.WTF_CSRF_ENABLED = False

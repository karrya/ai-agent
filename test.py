#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/15 16:20
@Author :   likai.com
@File   :   test.py
"""
from injector import Injector, inject

class A:
    name: str = "llmops"

@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def f(self):
        print(f"Class A name: {self.a.name}")

injector = Injector()
b =injector.get(B)
b.f()

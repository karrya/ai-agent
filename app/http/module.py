#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/24 13:49
@Author :   likai.com
@File   :   module.py
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Module, Binder

from internal.extension.database_extension import db


# 对象注入模块
class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)

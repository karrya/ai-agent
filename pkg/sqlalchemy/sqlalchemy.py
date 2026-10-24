#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/24 23:59
@Author :   likai.com
@File   :   sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

class SQLAlchemy(_SQLAlchemy):

    # 重写sqlalchemy的核心类，实现自动提交
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e



#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/24 14:20
@Author :   likai.com
@File   :   app_service.py
"""
import uuid
from dataclasses import dataclass

from flask import Flask
from pkg.sqlalchemy import SQLAlchemy

from injector import inject

from exception import FailException
from model import App


@inject
@dataclass
class AppService:
    # 属性
    db: SQLAlchemy

    def create_app(self) -> App:
        # 1、创建模型实体类
        app = App()
        app.account_id = str(uuid.uuid4())
        app.name = "测试机器人"
        app.icon = ""
        app.description = "这是一个测试机器人"

        # 2、将实体类添加会话
        self.db.session.add(app)

        # 3、提交会话
        self.db.session.commit()

        return app

    def get(self, id: str) -> App:
        app = self.db.session.query(App).filter(App.id == id).first()
        if not app:
            raise FailException("应用不存在")
        return app

    def get_app_id(self, id: str):
        app = self.db.session.get(App, id)
        return app

    def update_app(self, id: str):
        with self.db.auto_commit():
            app = self.db.session.get(App, id)
            app.name = "哇哈哈"
        return app

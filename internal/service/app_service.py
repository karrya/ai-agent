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
from flask_sqlalchemy import SQLAlchemy

from injector import inject

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



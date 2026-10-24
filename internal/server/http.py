#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 15:51
@Author :   likai.com
@File   :   http.py
"""
from flask import Flask
from internal.router import Router
from config import Config
from internal.exception import CustomException
from model import App
from pkg.http_code import HttpCode
from pkg.response import Json, Response
from flask_sqlalchemy import SQLAlchemy


class Http(Flask):

    # 注册路由
    def __init__(self, *args, config: Config, router: Router, db: SQLAlchemy, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册路由
        router.register_router(self)

        # 注册异常处理
        self.register_error_handler(Exception, self._handle_custom_exception)

        # 加载配置
        self.config.from_object(config)

        # 注册数据库（必须先 init_app，再 create_all）
        db.init_app(self)
        with self.app_context():
            _ = App()
            db.create_all()

    def _handle_custom_exception(self, e: Exception):
        # 自定义异常处理，如果是自定义异常，则提取message和code
        if isinstance(e, CustomException):
            return Json(Response(code=e.code,
                                 message=e.message,
                                 data=e.data if e.data is not None else {}))

        # 其他异常处理
        if self.debug:
            raise e
        else:
            return Json(Response(code=HttpCode.FAIL, message=str(e), data={}))

#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 15:41
@Author :   likai.com
@File   :   router.py
"""
from dataclasses import dataclass
from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    app_handler: AppHandler

    def register_router(self, flask: Flask):
        # 1、创建蓝图（相当于@RequestMapping）
        bp = Blueprint("llmops", __name__, url_prefix="/api/v1")

        # 2、创建路由（相当于@RequestMapping）
        # 注意： view_func=app_handler.ping是与方法做绑定，如果是 view_func=app_handler.ping()，则会报错，是与方法返回的结果做绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping, methods=["GET"])
        bp.add_url_rule("/app/completion", view_func=self.app_handler.completion, methods=["POST"])
        bp.add_url_rule("/app/create", view_func=self.app_handler.create_app, methods=["POST"])
        bp.add_url_rule("/app/get", view_func=self.app_handler.get_app, methods=["GET"])
        bp.add_url_rule("/app/get/<string:id>", view_func=self.app_handler.get_app_id, methods=["GET"])
        bp.add_url_rule("/app/update/<string:id>", view_func=self.app_handler.update_app, methods=["POST"])

        # 3、注册蓝图
        flask.register_blueprint(bp)

#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 15:38
@Author :   likai.com
@File   :   app_handler.py
"""
import os
from dataclasses import dataclass
from platform import release

from flask import request
from injector import inject
from openai import OpenAI
import dotenv
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException
from pkg.response import success_json, validation_error_json
from service import AppService

# 加载 .env 中的 OPENAI_API_KEY / OPENAI_BASE_URL，OpenAI SDK 会自动读取
dotenv.load_dotenv()


# 相当于：建立了一个Controller类
@inject
@dataclass
class AppHandler:

    app_service: AppService

    # 相当于：建立了一个Controller的方法
    def ping(self):
        raise FailException("ping failed")
        # return {"ping": "pong"}

    def create_app(self):
        app = self.app_service.create_app()
        return success_json(f"应用已经创建成功，id为{app.id}")


    def completion(self):
        # 1、获取请求体中的 query 字段
        req = CompletionReq()

        if not req.validate():
            return validation_error_json(req.errors)

        query = request.json.get("query")


        # 2、调用 Anthropic API
        # Kimi for Coding 端点（api.kimi.com/coding）只支持 Anthropic 协议
        client = OpenAI()


        # 3、调用 Anthropic API
        response = client.chat.completions.create(
            model="kimi-k3",
            messages=[
                {"role": "system", "content": "你是OpenAI的聊天机器人，请根据用户的输入回应信息"},
                {"role": "user", "content": query},
            ],
        )

        content = response.choices[0].message.content

        return success_json(content)

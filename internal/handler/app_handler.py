#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 15:38
@Author :   likai.com
@File   :   app_handler.py
"""
from dataclasses import dataclass

import dotenv
from flask import request
from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validation_error_json
from internal.service import AppService

# 加载 .env 中的 OPENAI_API_KEY / OPENAI_BASE_URL，OpenAI SDK 会自动读取
dotenv.load_dotenv()


# 相当于：建立了一个Controller类
@inject
@dataclass
class AppHandler:
    service: AppService

    def ping(self):
        raise FailException("ping failed")
        # return {"ping": "pong"}

    def create_app(self):
        app = self.service.create_app()
        return success_json(f"应用已经创建成功，id为{app.id}")

    def get_app(self):
        id = request.args.get("id") or (request.get_json(silent=True) or {}).get("id")
        app = self.service.get(id)
        return success_json({
            "id": app.id,
            "account_id": app.account_id,
            "name": app.name,
            "icon": app.icon,
            "description": app.description,
            "updated_at": app.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "created_at": app.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

    def get_app_id(self, id: str):
        app = self.service.get_app_id(id)
        return success_json({
            "id": app.id,
            "account_id": app.account_id,
            "name": app.name,
            "icon": app.icon,
            "description": app.description,
            "updated_at": app.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "created_at": app.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

    def update_app(self, id: str):
        update_app = self.service.update_app(id)
        return success_json(f"应用已经更新成功，id为{update_app.name}")

    # def completion(self):
    #     # 1、获取请求体中的 query 字段
    #     req = CompletionReq()
    #
    #     if not req.validate():
    #         return validation_error_json(req.errors)
    #
    #     query = request.json.get("query")
    #
    #     # 2、调用 Anthropic API
    #     # Kimi for Coding 端点（api.kimi.com/coding）只支持 Anthropic 协议
    #     client = OpenAI()
    #
    #     # 3、调用 Anthropic API
    #     response = client.chat.completions.create(
    #         model="kimi-k3",
    #         messages=[
    #             {"role": "system", "content": "你是OpenAI的聊天机器人，请根据用户的输入回应信息"},
    #             {"role": "user", "content": query},
    #         ],
    #     )
    #
    #     content = response.choices[0].message.content
    #
    #     return success_json(content)

    def completion(self):
        # 1、获取请求体中的 query 字段
        req = CompletionReq()

        if not req.validate():
            return validation_error_json(req.errors)

        # 构建大模型Prompt
        prompt = ChatPromptTemplate.from_template("{query}")
        # 构建大模型客户端
        llm = ChatOpenAI(model="kimi-k3")
        # 客户端调用提示词进行访问
        ai_message = llm.invoke(prompt.invoke({"query": request.json.get("query")}))
        # 获取访问结果，并解析
        parser = StrOutputParser()
        content = parser.invoke(ai_message)

        return success_json(content)

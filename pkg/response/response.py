#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :   2026/10/20 23:30
@Author :   likai.com
@File   :   response.py
"""
from dataclasses import field, dataclass, asdict
from typing import Any

from flask import jsonify

from pkg.http_code import HttpCode


@dataclass
class Response:
    """统一接口响应结构"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def Json(data: Response = None):
    """将 Response 转换为 Flask JSON 响应"""
    if data is None:
        data = Response()
    return jsonify(asdict(data))


def success_json(data: Any = None):
    """成功响应"""
    return Json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    """失败响应"""
    return Json(Response(code=HttpCode.FAIL, message="", data=data))


def validation_error_json(errors: dict = None):
    """参数校验失败响应，提取第一个错误信息作为 message"""
    message = ""
    if errors:
        first_key = next(iter(errors))
        if errors[first_key]:
            message = errors[first_key][0]
    return Json(Response(code=HttpCode.VALIDATION_ERROR, message=message, data=errors))

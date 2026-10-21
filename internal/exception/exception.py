#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 22:52
@Author :   likai.com
@File   :   exception.py
"""
from dataclasses import field
from typing import Any

from pkg.http_code import HttpCode

class CustomException(Exception):
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = "", data: Any = None):
        super().__init__(message)
        self.data = data
        self.message = message


class FailException(CustomException):
    """
    失败异常
    """
    code: HttpCode = HttpCode.FAIL

class NotFoundException(CustomException):
    """
    未找到异常
    """
    code: HttpCode = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    """
    未授权异常
    """
    code: HttpCode = HttpCode.UNAUTHORIZED

class ForbiddenException(CustomException):
    """
    禁止异常
    """
    code: HttpCode = HttpCode.FORBIDDEN

class ValidationException(CustomException):
    """
    验证异常
    """
    code: HttpCode = HttpCode.VALIDATION_ERROR

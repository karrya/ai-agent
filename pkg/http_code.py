#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 22:51
@Author :   likai.com
@File   :   http_code.py
"""
from enum import Enum
from wtforms.validators import DataRequired



class HttpCode(str, Enum):
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    FORBIDDEN = "forbidden"
    UNAUTHORIZED = "unauthorized"
    BAD_REQUEST = "bad_request"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    VALIDATION_ERROR = "validation_error"

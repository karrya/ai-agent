#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 22:19
@Author :   likai.com
@File   :   app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊请求参数验证"""
    query = StringField("query", validators=[DataRequired(message="用户的请求参数必填！"),
                                             Length(max=100, message="用户的请求参数不能超过100个字符！")])

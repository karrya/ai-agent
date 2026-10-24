#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/20 22:25
@Author :   likai.com
@File   :   config.py
"""
import os
from typing import Any
from .default_config import DEFAULT_CONFIG

# 获取环境变量
def _get_env(key: str) -> Any:
    return os.getenv(key, DEFAULT_CONFIG.get(key))

# 获取环境变量，返回bool类型
def _get_env_bool(key: str) -> bool:
    env = _get_env(key)
    return env.lower() == "true" if env is not None else False

class Config:
    def __init__(self):
        # 关闭csrf保护
        self.WTF_CSRF_ENABLED = _get_env_bool("WTF_CSRF_ENABLED")

        # 配置数据库配置
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ECHO = _get_env_bool("SQLALCHEMY_ECHO")
        self.SQLALCHEMY_RECORD_QUERIES = _get_env_bool("SQLALCHEMY_RECORD_QUERIES")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "max_overflow": int(_get_env("SQLALCHEMY_MAX_OVERFLOW")),
            "pool_timeout": int(_get_env("SQLALCHEMY_POOL_TIMEOUT")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
            "pool_pre_ping": _get_env_bool("SQLALCHEMY_POOL_PRE_PING")
        }

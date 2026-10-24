#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/24 13:28
@Author :   likai.com
@File   :   default_config.py
"""

DEFAULT_CONFIG = {
    # 地址
    "SQLALCHEMY_DATABASE_URI": "",
    # 打印日志
    "SQLALCHEMY_ECHO": "True",
    # 记录查询
    "SQLALCHEMY_RECORD_QUERIES": "True",
    # 数据库连接池配置
    "SQLALCHEMY_POOL_SIZE": "10",
    # 最大溢出连接数
    "SQLALCHEMY_MAX_OVERFLOW": "20",
    # 连接超时时间
    "SQLALCHEMY_POOL_TIMEOUT": "30",
    # 连接回收时间
    "SQLALCHEMY_POOL_RECYCLE": "3600",
    # 连接预检查是否开启
    "SQLALCHEMY_POOL_PRE_PING": "False",

    # WTF保护是否开启: False
    "WTF_CSRF_ENABLED": "False",
}

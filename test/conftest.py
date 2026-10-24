#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/21 20:48
@Author :   likai.com
@File   :   conftest.py.py
"""

import pytest

from app.http.app import app


@pytest.fixture()
def client():
    # 测试模式
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
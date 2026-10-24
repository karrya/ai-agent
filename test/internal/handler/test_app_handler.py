#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/21 20:30
@Author :   likai.com
@File   :   test_app_handler.py
"""
import pytest
from pkg.http_code import HttpCode


class TestAppHandler():

    # 通过pytest.mark.parametrize参数化测试，可以测试多种场景
    @pytest.mark.parametrize("query", [None, "你好"])
    def test_completion(self, client, query: str):
        request = client.post("/api/v1/app/completion", json={"query": query})

        assert request.status_code == 200
        if query is None:
            assert request.json.get("code") == HttpCode.VALIDATION_ERROR
        else:
            assert request.json.get("code") == HttpCode.SUCCESS


        print("响应内容：", request.json)

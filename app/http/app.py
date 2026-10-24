#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 16:00
@Author :   likai.com
@File   :   app.py
"""
from flask_sqlalchemy import SQLAlchemy

from internal.server import Http
from internal.router import Router
from injector import Injector
from config import Config
from .module import ExtensionModule

injector = Injector(modules=[ExtensionModule()])
router = injector.get(Router)
# 关闭WTF的CSRF保护、加载配置
conf = injector.get(Config)
db = injector.get(SQLAlchemy)

app = Http(__name__, config=conf, router=router, db=db)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask
# from injector import Injector
# from internal.router import Router
#
#
# injector = Injector()
#
#
# app = Flask(__name__)
# injector.get(Router).register_router(app)
#
# if __name__ == "__main__":
#     app.run(debug=True)

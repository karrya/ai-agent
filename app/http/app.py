#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/19 16:00
@Author :   likai.com
@File   :   app.py
"""

from internal.server import Http
from internal.router import Router
from injector import Injector
from config import Config

injector = Injector()

conf = injector.get(Config)



app = Http(__name__, config=conf, router=injector.get(Router))

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

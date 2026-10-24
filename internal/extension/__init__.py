#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/15 11:51
@Author :   likai.com
@File   :   __init__.py.py
"""

from .database_extension import db

from .migrate_extersion import migrate
__all__ = ["db", "migrate"]

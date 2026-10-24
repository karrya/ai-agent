#!/usr/bin/env python
# -*- codingL utf-8 -*-
"""
@Time   :   2026/10/24 14:07
@Author :   likai.com
@File   :   app.py
"""
from datetime import datetime
import uuid
from sqlalchemy import (
    Column,
    UUID,
    DateTime,
    String,
    Text,
    PrimaryKeyConstraint,
    Index
)

from internal.extension.database_extension import db


class App(db.Model):
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id"),
    )

    id = Column(UUID, default=uuid.uuid4, primary_key=True, nullable=False)
    account_id = Column(UUID, default=uuid.uuid4, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

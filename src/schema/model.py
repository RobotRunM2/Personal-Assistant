#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\schema\model.py
# Created Date: 2024 03 22nd Friday, 4:11:28 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 4:31:13 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


from typing import Optional
from pydantic import BaseModel as Model


class BaseSchema(Model):
    id: Optional[int] = None


class Account(BaseSchema):
    created: int
    description: Optional[str] = None


class AccountVariable(BaseSchema):
    name: str
    value: Optional[str] = None


class SqliteSequence(BaseSchema):
    name: Optional[str] = None
    seq: Optional[str] = None


class Task(BaseSchema):
    account_id: Optional[int] = None
    cron: Optional[str] = None
    name: Optional[str] = None
    task_id: Optional[int] = None


class TaskTemplate(BaseSchema):
    description: str


class TaskTemplateStep(BaseSchema):
    data: Optional[str] = None
    method: str
    parser_pattern: Optional[str] = None
    query: Optional[str] = None
    save_variable: Optional[str] = None
    task_template_id: int
    url: str

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\model\model.py
# Created Date: 2024 03 22nd Friday, 2:38:05 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 4:28:06 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------
from peewee import SqliteDatabase, Model, IntegerField, TextField, BareField


database = SqliteDatabase(".\pa.db")


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class Account(BaseModel):
    created = IntegerField()
    description = TextField(null=True)

    class Meta:
        table_name = "account"


class AccountVariable(BaseModel):
    name = TextField()
    value = TextField(null=True)

    class Meta:
        table_name = "account_variable"


class Task(BaseModel):
    account_id = IntegerField(null=True)
    cron = TextField(null=True)
    name = TextField(null=True)
    task_id = IntegerField(null=True)

    class Meta:
        table_name = "task"


class TaskTemplate(BaseModel):
    description = TextField()

    class Meta:
        table_name = "task_template"


class TaskTemplateStep(BaseModel):
    data = TextField(null=True)
    method = TextField()
    parser_pattern = TextField(null=True)
    query = TextField(null=True)
    save_variable = TextField(null=True)
    task_template_id = IntegerField()
    url = TextField()

    class Meta:
        table_name = "task_template_step"
        primary_key = False

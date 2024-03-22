#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\dao\dao.py
# Created Date: 2024 03 22nd Friday, 4:24:17 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 5:02:24 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


from ._base import BaseDAO
from model.model import (
    Account as AccountModel,
    AccountVariable as AccountVariableModel,
    Task as TaskModel,
    TaskTemplate as TaskTemplateModel,
    TaskTemplateStep as TaskTemplateStepModel,
)

from schema import (
    Account as AccountSchema,
    AccountVariable as AccountVariableSchema,
    Task as TaskSchema,
    TaskTemplate as TaskTemplateSchema,
    TaskTemplateStep as TaskTemplateStepSchema,
)


class Account(BaseDAO):
    model = AccountModel
    schema = AccountSchema


class AccountVariable(BaseDAO):
    model = AccountVariableModel
    schema = AccountVariableSchema


class Task(BaseDAO):
    model = TaskModel
    schema = TaskSchema


class TaskTemplate(BaseDAO):
    model = TaskTemplateModel
    schema = TaskTemplateSchema


class TaskTemplateStep(BaseDAO):
    model = TaskTemplateStepModel
    schema = TaskTemplateStepSchema

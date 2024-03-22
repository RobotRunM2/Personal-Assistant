#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\dao\_base.py
# Created Date: 2024 03 22nd Friday, 4:03:51 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 5:02:47 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


from peewee import Model, chunked, ForeignKeyField


from playhouse.shortcuts import model_to_dict

from schema import BaseSchema
from model import BaseModel


class BaseDAO(object):
    # 基础数据访问对象类，功能包括增删改查，用于具体的数据访问对象类继承

    model: BaseModel = BaseModel
    schema: BaseSchema = BaseSchema

    @classmethod
    def __model_to_dict(cls, model: Model):
        """将model转换为dict"""

        exclude_fields = []
        # 排除外键字段
        for field_name, field in model._meta.fields.items():
            if isinstance(field, ForeignKeyField):
                exclude_fields.append(field_name)

        # 添加外键id字段
        extra_attrs = [f"{field_name}_id" for field_name in exclude_fields]

        return model_to_dict(
            model,
            max_depth=0,
            recurse=False,
            exclude=exclude_fields,
            extra_attrs=extra_attrs,
        )

    @classmethod
    def __models_to_dicts(cls, models: list[Model]):
        """将models转换为dicts"""
        return [cls.model_to_dict(model) for model in models]

    @classmethod
    def create(cls, schema: BaseSchema):
        """创建数据"""
        model = cls.model.create(**schema.model_dump(exclude={"id"}))
        return cls.__model_to_dict(model)

    @classmethod
    def get(cls, id: int):
        """获取数据"""
        model = cls.model.get_or_none(cls.model.id == id)
        return cls.__model_to_dict(model)

    @classmethod
    def update(cls, schema: BaseSchema):
        """更新数据"""
        cls.model.update(**schema.model_dump(exclude={"id"})).where(
            cls.model.id == schema.id
        ).execute()

        return cls.get(id)

    @classmethod
    def delete(cls, id: int):
        """删除数据"""
        affected_rows = cls.model.delete().where(cls.model.id == id)
        return affected_rows

    @classmethod
    def batch_create(cls, schemas: list[BaseSchema]):
        """批量创建数据"""
        with cls.model._meta.database.atomic():
            for chunk in chunked(schemas, 100):
                cls.model.insert_many(
                    [schema.model_dump(exclude={"id"}) for schema in chunk]
                ).execute()

    @classmethod
    def batch_get(cls, ids: list[int]):
        """批量获取数据"""
        models = cls.model.select().where(cls.model.id.in_(ids))
        return cls.__models_to_dicts(models)

    @classmethod
    def batch_update(cls, schemas: list[BaseSchema]):
        """批量更新数据"""
        with cls.model._meta.database.atomic():
            for schema in schemas:
                cls.model.update(**schema.model_dump(exclude={"id"})).where(
                    cls.model.id == schema.id
                ).execute()

    @classmethod
    def batch_delete(cls, ids: list[int]):
        """批量删除数据"""
        affected_rows = cls.model.delete().where(cls.model.id.in_(ids))
        return affected_rows

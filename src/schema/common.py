#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\schema\common.py
# Created Date: 2024 03 22nd Friday, 12:02:31 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 12:14:29 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


class Method(enumerate):
    """请求方法"""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


class ResponseType(enumerate):
    """响应类型"""

    JSON = "application/json"
    XML = "application/xml"
    HTML = "text/html"
    TEXT = "text/plain"
    MULTIPART = "multipart/form-data"

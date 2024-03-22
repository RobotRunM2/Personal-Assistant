#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\parser\parser_by_re.py
# Created Date: 2024 03 22nd Friday, 10:13:47 am
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 11:35:27 am
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------

from re import compile


def parser_by_re(pattern, text: str) -> list:
    """根据正则表达式返回匹配结果

    Args:
        pattern (_type_): 正则表达式
        text (str): 要匹配的文本

    Returns:
        list: 返回所有匹配的结果列表
    """
    r = compile(pattern)
    results = r.findall(text)
    return results


if __name__ == "__main__":
    text = "1234567891211113457"
    print(parser_by_re("1(.+?)(4)", text))

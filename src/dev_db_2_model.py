#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\dev_db_2_model.py
# Created Date: 2024 03 22nd Friday, 2:35:47 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 2:37:24 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description: 从本地数据库文件生成数据库模型
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


import os


def run():
    # 执行cli命令
    cmd_str = "python -m pwiz -e sqlite  .\pa.db  > model/_temp_model.py"
    os.system(cmd_str)
    print("数据库模型已生成更新到文件", "model/_temp_model.py")


if __name__ == "__main__":
    run()

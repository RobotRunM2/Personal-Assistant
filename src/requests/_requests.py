#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\requests\_requests.py
# Created Date: 2024 03 22nd Friday, 10:13:47 am
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 2:01:49 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


from requests import Session

from schema.common import Method, ResponseType


class RequestHandler:
    """请求处理器"""

    def __init__(
        self, headers: dict = None, encoding: str = None, cookies: dict = None
    ):
        """初始化请求处理器

        Args:
            headers (dict, optional): _description_. Defaults to None.
            encode (str, optional): _description_. Defaults to "utf8".
            cookies (dict, optional): _description_. Defaults to None.
        """
        self.session = Session()

        if headers:
            self.session.headers.update(headers)

        if cookies:
            self.session.cookies.update(cookies)

        self.encoding = encoding

    def request(
        self,
        url: str,
        method: Method,
        response_type: ResponseType,
        data: dict = None,
        params: dict = None,
    ):
        """访问网页并返回结果

        Args:
            url (str): 请求地址
            method (Method): 请求方法
            response_type (ResponseType): 响应类型
            data (dict, optional): 请求数据. Defaults to None.
            params (dict, optional): 请求参数. Defaults to None.

        Returns:
            _type_: _description_
        """
        r = self.session.request(method=method, url=url, params=params, data=data)

        # 设置网页编码
        if self.encoding:
            r.encoding = self.encoding

        # 根据response_type 返回响应数据
        if response_type == ResponseType.JSON:
            return r.json()
        elif response_type == ResponseType.XML:
            return r.xml()
        elif response_type == ResponseType.HTML:
            return r.text
        elif response_type == ResponseType.TEXT:
            return r.text
        elif response_type == ResponseType.MULTIPART:
            return r.multipart


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    r = RequestHandler(headers=headers)
    res = r.request("http://www.baidu.com/s", method="GET", data={"wd": "python"})

    print(res)

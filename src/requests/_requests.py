"""
Author: wdjoys
Date: 2022-04-07 14:41:06
LastEditors: wdjoys
LastEditTime: 2022-04-07 16:09:07
FilePath: \Personal-Assistant\src\requests\_requests.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
"""
Author: wdjoys
Date: 2022-04-07 14:41:06
LastEditors: wdjoys
LastEditTime: 2022-04-07 15:45:55
FilePath: \Personal-Assistant\src\requests\_requests.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""


from requests import Session


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
        method: str,
        is_api: bool = False,
        data: dict = None,
        params: dict = None,
    ):
        """http请求函数

        Args:
            url (str): _description_
            method (str): _description_
            is_api (bool, optional): _description_. Defaults to False.
            data (dict, optional): _description_. Defaults to None.
            params (dict, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        r = self.session.request(method=method, url=url, params=params, data=data)

        # 设置网页编码
        if self.encoding:
            r.encoding = self.encoding

        if is_api:
            return {"json": r.json, "status_code": r.status_code}
        else:
            return {"html": r.text, "status_code": r.status_code}


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    r = RequestHandler(headers=headers)
    res = r.request("http://www.baidu.com/s", method="GET", data={"wd": "python"})

    print(res)

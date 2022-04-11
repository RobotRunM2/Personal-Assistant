"""
Author: wdjoys
Date: 2022-04-11 22:45:51
LastEditors: wdjoys
LastEditTime: 2022-04-11 22:45:52
FilePath: \Personal-Assistant\src\parser\re.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
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

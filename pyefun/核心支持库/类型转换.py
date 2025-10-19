"""
类型转换。

提供常见类型间的转换：文本与字节串、数值、整数、时间以及 JSON 编解码。
"""
from .日期时间操作 import *
import json

def 到文本(bytes):
    """
    将 UTF-8 字节串转换为字符串。

    Args:
        bytes (bytes): 字节串。

    Returns:
        str: 解码后的字符串。
    """
    return str(bytes, encoding="utf-8")


def 到字节集(str):
    """
    将字符串按 UTF-8 编码为字节串。

    Args:
        str (str): 文本。

    Returns:
        bytes: 编码结果。
    """
    return bytes(str, encoding='utf-8')


def 到数值(val):
    """
    将文本或数字转换为浮点数。

    Args:
        val (Any): 文本或数字。

    Returns:
        float: 浮点数。
    """
    return float(val)


def 到整数(val):
    """
    将文本或小数转换为整数（先转 float 再取整）。

    Args:
        val (Any): 文本或数字。

    Returns:
        int: 整数值。
    """
    return int(float(val))


def 到时间(str):
    """
    通过文本创建 日期时间 对象。

    Args:
        str (str): 时间文本，如 "2020-01-01 12:00:00" 或 "now"。

    Returns:
        日期时间: 日期时间对象。
    """
    return 创建日期时间(str)



def json到文本(obj):
    """
    将对象编码为 JSON 文本。

    Args:
        obj (Any): Python 对象（可序列化）。

    Returns:
        str: JSON 字符串。
    """
    return json.dumps(obj)


def json解析(obj):
    """
    解析 JSON 文本为对象。

    Args:
        obj (str): JSON 字符串。

    Returns:
        Any: 解析后的 Python 对象。
    """
    return json.loads(obj)

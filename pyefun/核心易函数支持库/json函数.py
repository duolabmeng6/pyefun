"""
json 编解码高性能库封装

优先使用 ultrajson(ujson)，如需其它库可在此扩展：
- https://github.com/ijl/orjson
- https://github.com/ultrajson/ultrajson
"""
from pyefun.核心支持库.公用函数 import _动态导包


def json到文本(data, html编码=True, ascii编码=False, 斜杠转义=True, 缩进=0):
    """将 Python 对象编码为 JSON 文本。

    :param data: 待编码的对象
    :param html编码: 是否对 HTML 特殊字符进行编码
    :param ascii编码: 是否仅使用 ASCII 编码（True 时非 ASCII 会被转义）
    :param 斜杠转义: 是否转义正斜杠 '/'
    :param 缩进: 格式化缩进空格数，0 表示紧凑模式
    :return: JSON 字符串
    """
    ujson = _动态导包("ujson")
    return ujson.dumps(data,
                       encode_html_chars=html编码,
                       ensure_ascii=ascii编码,
                       escape_forward_slashes=斜杠转义,
                       indent=缩进)


def json加载(data):
    """将 JSON 文本解码为 Python 对象。

    :param data: JSON 字符串
    :return: 解析后的 Python 对象
    """
    ujson = _动态导包("ujson")
    return ujson.loads(data)

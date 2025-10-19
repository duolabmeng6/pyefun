"""
json编码解码飞快的库


https://github.com/ijl/orjson
还有
https://github.com/ultrajson/ultrajson
"""
from pyefun.核心支持库.公用函数 import _动态导包


def json到文本(data, html编码=True, ascii编码=False, 斜杠转义=True, 缩进=0):
    """
    json到文本 的功能说明（请补充）。

    Args:
        data: 参数说明。
        html编码 (可选): 参数说明。默认值为 True。
        ascii编码 (可选): 参数说明。默认值为 False。
        斜杠转义 (可选): 参数说明。默认值为 True。
        缩进 (可选): 参数说明。默认值为 0。

    """
    ujson = _动态导包("ujson")
    return ujson.dumps(data,
                       encode_html_chars=html编码,
                       ensure_ascii=ascii编码,
                       escape_forward_slashes=斜杠转义,
                       indent=缩进)


def json加载(data):
    """
    json加载 的功能说明（请补充）。

    Args:
        data: 参数说明。

    """
    ujson = _动态导包("ujson")
    return ujson.loads(data)


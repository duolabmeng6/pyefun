"""
json编码解码飞快的库


https://github.com/ijl/orjson
还有
https://github.com/ultrajson/ultrajson
"""
from pyefun.核心支持库.公用函数 import _动态导包


def json到文本(data, html编码=True, ascii编码=False, 斜杠转义=True, 缩进=0):
    ujson = _动态导包("ujson")
    return ujson.dumps(data,
                       encode_html_chars=html编码,
                       ensure_ascii=ascii编码,
                       escape_forward_slashes=斜杠转义,
                       indent=缩进)


def json加载(data):
    ujson = _动态导包("ujson")
    return ujson.loads(data)


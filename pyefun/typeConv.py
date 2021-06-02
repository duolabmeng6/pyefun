"""

.. Hint::
    类型转换


.. literalinclude:: ../../../pyefun/typeConv_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
from .timeBase import *
import json

def 到文本(bytes):
    return str(bytes, encoding="utf-8")

def 到字节集(str):
    return bytes(str, encoding='utf-8')

def 到数值(val):
    return float(val)

def 到整数(val):
    return int(float(val))

def 到时间(str):
    return 创建日期时间(str)


def json到文本(obj):
    return json.dumps(obj)

def json解析(obj):
    return json.loads(obj)
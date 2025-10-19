"""
类型转换模块的单元测试。

覆盖文本与字节、数值与整数转换、时间创建以及 JSON 编解码用例。
"""
import unittest

from pyefun import *


class TestTypeConv(unittest.TestCase):
    """类型转换相关测试用例。"""

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        pass
        data = 到文本(b"123")
        print(type(data), data)

        data = 到字节集("123")
        print(type(data), data)

        data = 到整数("123.123")
        print(type(data), data)

        data = 到数值("123.123")
        print(type(data), data)

        data = 到时间("2021-05-18")
        print(type(data), data)

    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        data = json到文本({"a": 1, "b": 2,"name":"你好"})
        print(data)
        data = json解析(data)
        print(repr(data))
        print(data['a'])
        print(data['b'])
        print(data['name'])

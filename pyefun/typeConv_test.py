import unittest

from .__init__ import *


class TestTypeConv(unittest.TestCase):

    def test_1(self):
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
        data = json到文本({"a": 1, "b": 2,"name":"你好"})
        print(data)
        data = json解析(data)
        print(repr(data))
        print(data['a'])
        print(data['b'])
        print(data['name'])

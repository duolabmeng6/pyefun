import unittest

from .typeConv import *


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

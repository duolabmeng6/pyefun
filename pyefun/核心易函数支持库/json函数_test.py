import unittest

from .json函数 import *


class Testjson函数(unittest.TestCase):

    def test_1(self):
        pass
        res = json到文本({"a": 1, "b": 2})
        print(res)
        self.assertEqual(res, '{"a":1,"b":2}')
        res = json加载('{"a":1,"b":2}')
        print(res)
        self.assertEqual(res, {"a": 1, "b": 2})

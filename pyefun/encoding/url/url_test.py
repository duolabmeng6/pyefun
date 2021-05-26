import unittest

from .url import *


class TestUrl(unittest.TestCase):

    def test_1(self):
        data = url编码("你好123456798", "gbk")
        self.assertEqual(data, "%C4%E3%BA%C3123456798")
        data = url解码(data, "gbk")
        self.assertEqual(data, "你好123456798")

        data = url编码("你好123456798")
        self.assertEqual(data, "%E4%BD%A0%E5%A5%BD123456798")
        data = url解码(data)
        self.assertEqual(data, "你好123456798")

        data = url编码("你好123456798")
        self.assertEqual(data, "%E4%BD%A0%E5%A5%BD123456798")
        data = url解码(data)
        self.assertEqual(data, "你好123456798")

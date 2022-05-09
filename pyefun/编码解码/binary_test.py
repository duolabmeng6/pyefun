import unittest

from .binary import *


class TestBinary(unittest.TestCase):

    def test_1(self):
        data = binary编码(b"123456798")
        self.assertEqual(data, b"313233343536373938")
        data = binary解码(data)
        self.assertEqual(data, b"123456798")

        data = binary编码("你好")
        self.assertEqual(data, b"e4bda0e5a5bd")
        data = binary解码(data)
        self.assertEqual(data, b'\xe4\xbd\xa0\xe5\xa5\xbd')
        self.assertEqual(data.decode("utf-8"), "你好")

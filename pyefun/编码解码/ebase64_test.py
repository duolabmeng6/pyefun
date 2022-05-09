import unittest

from .ebase64 import *


class TestBase64(unittest.TestCase):

    def test_1(self):
        data = base64编码("123456798")
        self.assertEqual(data, "MTIzNDU2Nzk4")
        data = base64解码(data)
        self.assertEqual(data, b"123456798")

        data = base64编码(b"123456798")
        self.assertEqual(data, "MTIzNDU2Nzk4")
        data = base64解码(data)
        self.assertEqual(data, b"123456798")

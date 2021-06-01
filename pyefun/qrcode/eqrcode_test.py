import unittest

from .eqrcode import *


class TestEqrcode(unittest.TestCase):

    def test_1(self):
        pass
        二维码字节集 = 二维码生成("你好 祖国")

        识别结果 = 二维码识别(二维码字节集)

        self.assertEqual(识别结果, "你好 祖国")

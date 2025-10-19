import unittest

from 二维码 import *


class TestEqrcode(unittest.TestCase):

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        pass
        二维码字节集 = 二维码生成("你好 祖国")

        识别结果 = 二维码识别(二维码字节集)

        self.assertEqual(识别结果, "你好 祖国")

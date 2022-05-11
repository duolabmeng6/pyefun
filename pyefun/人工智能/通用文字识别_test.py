import unittest

from .通用文字识别 import *


class Test通用文字识别(unittest.TestCase):
    def test_ocr(self):
        文字位置, 文字内容 = 通用文字识别(r"C:\pyefun\pyefun\a\1.png")
        # print(文字位置)
        print(文字内容)
        文字内容 = 通用文字识别获取文字(r"C:\pyefun\pyefun\a\1.png")
        print(文字内容)
        Json内容 = 通用文字识别获取Json(r"C:\pyefun\pyefun\a\1.png")
        print(Json内容)

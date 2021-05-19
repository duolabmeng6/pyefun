import unittest

from .codeConv import *
from .dirkBase import *


class TestCodeConv(unittest.TestCase):

    def test_1(self):
        pass
        # E文本编码转换(编码_UTF8编码("你好aaaa"), "", "utf-8")
        text = 编码_UTF8编码("大家好我是gbk编码你好aaaa")
        print(type(text))
        text2 = 文本编码转换(text, "", "gbk")
        print(type(text2))
        print(text2)
        print(编码_检查(text2))

        写到文件("gbk.txt",text2)
        print("--------------")

        text = 编码_GBK编码("大家好我是gbk编码你好aaaa")
        print(type(text))
        text2 = 文本编码转换(text, "", "utf-8")
        print(type(text2))
        print(text2)
        print(编码_检查(text2))
        写到文件("utf-8.txt",text2)

    def test_2(self):
        data = 编码_URL编码("你好ABC")
        print(data)

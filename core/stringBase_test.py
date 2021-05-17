import unittest

from .stringBase import *

class TestString(unittest.TestCase):

    def test_1(self):
        data = 取文本长度("1234")
        self.assertEqual(data, 4)
        data = 取文本长度("你好")
        self.assertEqual(data, 2)

    def test_2(self):
        data = 取文本左边("1234", 2)
        self.assertEqual(data, "12")
        data = 取文本左边("1234", 10)
        self.assertEqual(data, "1234")

    def test_3(self):
        data = 取文本右边("1234", 2)
        self.assertEqual(data, "34")
        data = 取文本右边("1234", 10)
        self.assertEqual(data, "1234")

        data = 取文本中间("123abc123", 3,3)
        self.assertEqual(data, "abc")
        data = 取文本中间("123abc123", 3,10)
        self.assertEqual(data, "abc123")


    def test_4(self):
        data = 字符(65)
        self.assertEqual(data, "A")
        data = 字符(97)
        self.assertEqual(data, "a")
        data = 字符(66)
        self.assertEqual(data, "B")

    def test_5(self):
        data = 取代码("A")
        self.assertEqual(data, 65)
        data = 取代码("a")
        self.assertEqual(data, 97)

    def test_6(self):
        data = 寻找文本("ABCDEFG", "A")
        self.assertEqual(data, 0)
        data = 寻找文本("ABCDEFG", "B")
        self.assertEqual(data, 1)
        data = 寻找文本("ABCDEFG", "G")
        self.assertEqual(data, 6)
        data = 寻找文本("ABCDEFGA", "A", 1)
        self.assertEqual(data, 7)
        data = 寻找文本("BBBAACCCAAA", "A", 3)
        self.assertEqual(data, 3)
        data = 寻找文本("BBBAACCCAAA", "A", 4)
        self.assertEqual(data, 4)
        data = 寻找文本("BBBAACCCAAA", "A", 5, 7)
        self.assertEqual(data, -1)
        data = 寻找文本("祖国你好", "你好")
        self.assertEqual(data, 2)

    def test_7(self):
        data = 倒找文本("ABCDEFG", "A")
        self.assertEqual(data, 0)
        data = 倒找文本("ABCDEFGA", "A")
        self.assertEqual(data, 7)
        data = 倒找文本("ABCDEFGAa", "A", 2)
        self.assertEqual(data, 7)

    def test_8(self):
        data = 到大写("abc")
        self.assertEqual(data, "ABC")
        data = 到小写("ABC")
        self.assertEqual(data, "abc")

        data = 到全角("abc123456789,./;'[]")
        self.assertEqual(data, "ａｂｃ１２３４５６７８９，．／；＇［］")
        data = 到半角("ａｂｃ１２３４５６７８９，．／；＇［］")
        self.assertEqual(data, "abc123456789,./;'[]")

    def test_9(self):
        data = 删首空("     abc")
        self.assertEqual(data, "abc")
        data = 删尾空("abc     ")
        self.assertEqual(data, "abc")
        data = 删首尾空("     abc     ")
        self.assertEqual(data, "abc")
        data = 删全部空("     a b c     ")
        self.assertEqual(data, "abc")

        data = 子文本替换("1234567890123", "123", "")
        self.assertEqual(data, "4567890")

        data = 子文本替换("1234567890123", "123", "", 1)
        self.assertEqual(data, "4567890123")

        data = 取空白文本(10)
        self.assertEqual(data, "          ")
        data = 取重复文本(10, "a")
        self.assertEqual(data, "aaaaaaaaaa")

        data = 分割文本("1 2 3 4 5 6 7 8 9 0 ", " ")
        self.assertEqual(data, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ''])

        data = 分割文本("1 2 3 4 5 6 7 8 9 0 ", " ",5)
        self.assertEqual(data, ['1', '2', '3', '4', '5', '6 7 8 9 0 '])

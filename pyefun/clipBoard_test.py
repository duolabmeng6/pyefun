import unittest

from .clipBoard import *
from . import *


class TestclipBoard(unittest.TestCase):

    def test_1(self):
        pass
        置剪辑板文本("易函数")

        self.assertEqual(取剪辑板文本(), "易函数")
        清除剪辑板()
        self.assertEqual(取剪辑板文本(), "")


    def test_2(self):
        pass
        # data = 取鼠标位置()
        # print(data.x)
        # print(data.y)

import unittest

from 剪切板操作 import *
from pyefun import *


class TestclipBoard(unittest.TestCase):

    def test_1(self):
        pass
        置剪辑板文本("易函数")
        self.assertEqual(取剪辑板文本(), "易函数")
        清除剪辑板()
        self.assertEqual(取剪辑板文本(), "")


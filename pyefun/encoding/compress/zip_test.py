import unittest

from zip import *
from pyefun import *


class Testezip(unittest.TestCase):

    def test_1(self):
        zip解压("C:/python/pyefun/pyefun/pyefun/encoding/compress/zip.zip", 取运行目录()+"/test")
    def test_2(self):
        zip压缩(r"C:/python/pyefun/pyefun/pyefun/encoding/compress/test.zip", 取运行目录()+"/test/")
    def test_3(self):
        zip压缩(r"C:/python/pyefun/pyefun/pyefun/encoding/compress/test单文件.zip", 取运行目录()+"/test/zip.py")

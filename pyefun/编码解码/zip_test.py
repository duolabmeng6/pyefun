import unittest

from zip import *
from pyefun import *


class Testezip(unittest.TestCase):

    def test_1(self):
        zip解压("./test.zip", 取运行目录()+"/test2")
    def test_2(self):
        zip压缩(取运行目录()+"/test.zip", 取运行目录()+"/")
    def test_3(self):
        zip压缩("./test单文件.zip", 取运行目录()+"/test/zip.py")

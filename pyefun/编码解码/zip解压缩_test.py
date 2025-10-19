import unittest

from zip解压缩 import *
from pyefun import *


class Testezip(unittest.TestCase):

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        zip解压("./test.zip", 取运行目录()+"/test2")
    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        zip压缩(取运行目录()+"/test.zip", 取运行目录()+"/")
    def test_3(self):
        """
        test_3 的功能说明（请补充）。

        """
        zip压缩("./test单文件.zip", 取运行目录()+"/test/zip.py")

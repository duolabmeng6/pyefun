"""
磁盘操作模块的单元测试。

覆盖目录与文件的创建、移动、复制、删除、查询、权限与遍历等用例。
"""
import unittest

from .磁盘操作 import *


class TestDirk(unittest.TestCase):
    """磁盘操作相关测试用例。"""

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        data = 取当前目录()
        self.assertNotEqual(data, "")
        print(data)

        data = 取运行目录()
        self.assertNotEqual(data, "")
        print(data)

        data = 写到文件(取运行目录() + "/1.txt", b"abc")
        # self.assertEqual(data, True)

        data = 写到文件("./a/1.txt", b"abc")
        self.assertEqual(data, False)

        data = 复制文件(取运行目录() + "/1.txt", "2.txt")
        # self.assertEqual(data, True)

        data = 复制文件(取运行目录() + "/1.txt", "./a/2.txt")
        self.assertEqual(data, False)

        data = 移动文件(取运行目录() + "/1.txt", "3.txt")
        self.assertEqual(data, True)

        data = 移动文件(取运行目录() + "/1.txt", "./a/3.txt")
        self.assertEqual(data, False)

        data = 文件_目录文件列表()
        self.assertNotEqual(data, "")
        print(data)

        data = 文件_遍历子目录('./core')
        self.assertNotEqual(data, "")
        print(data)

        data = 创建目录('./b')
        self.assertEqual(data, True)
        print(data)

        data = 创建目录('./c/c/c/c')
        self.assertEqual(data, True)
        print(data)

        data = 创建目录('./c/bb')
        self.assertEqual(data, True)
        print(data)

        data = 读入文件('./2.txt')
        self.assertEqual(data, b'abc')
        print(data)

        data = 读入文件('./aaa.txt')
        self.assertEqual(data, b"")
        print(data)

        data = 删除文件('./2.txt')
        self.assertEqual(data, True)
        print(data)

        data = 删除文件('./3.txt')
        self.assertEqual(data, True)
        print(data)

        data = 删除文件('./4.txt')
        self.assertEqual(data, False)
        print(data)

        data = 删除目录('./b')
        self.assertEqual(data, True)
        print(data)
        data = 删除目录('./c', True)
        self.assertEqual(data, True)
        print(data)
        data = 删除目录('./aa/aa')
        self.assertEqual(data, False)
        print(data)

    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        data = 文件_路径取扩展名('c:/a/1.jpg')
        self.assertEqual(data, ".jpg")
        print(data)

        data = 文件_取文件名('c:/a/1.jpg')
        self.assertEqual(data, "1.jpg")
        print(data)

        data = 文件_取目录('c:/a/1.jpg')
        self.assertEqual(data, "c:/a")
        print(data)

    def test_3(self):
        """
        test_3 的功能说明（请补充）。

        """
        data = 写到文件("./1.txt", b"abc")
        self.assertEqual(data, True)

        data = 文件更名("./1.txt", "2.txt")
        self.assertEqual(data, True)

        data = 文件更名("./1.txt", "/a/a/2.txt")
        self.assertEqual(data, False)

    def test_4(self):
        """
        test_4 的功能说明（请补充）。

        """
        data = 文件_路径取扩展名('c:/a/1.jpg')
        self.assertEqual(data, ".jpg")
        print(data)

        data = 文件_取文件名('c:/a/1.jpg')
        self.assertEqual(data, "1.jpg")
        print(data)

        data = 文件_取目录('c:/a/1.jpg')
        self.assertEqual(data, "c:/a")
        print(data)

        data = 改变目录('./core')
        # self.assertEqual(data, True)
        # print(data)

        data = 改变目录('./BBB')
        # self.assertEqual(data, False)
        # print(data)

        data = 取当前目录()
        # self.assertEqual(data, 取运行目录() + "/core")
        # print(data)

        # window 用不了
        # data = 改变当前进程目录('./coreUtil')
        # self.assertEqual(data, False)
        # print(data)
        #
        # data = 取当前目录()
        # self.assertEqual(data, 取运行目录() + "\ccoreUtil")
        # print(data)
        data = 写到文件(取运行目录() + "/1.txt", b"abc")
        self.assertEqual(data, True)
        data = 文件_检查权限(取运行目录() + "/1.txt", 3)
        # self.assertEqual(data, True)

        data = 文件_是否为绝对路径(取运行目录() + "/1.txt")
        # self.assertEqual(data, False)

        data = 文件_是否为绝对路径(取运行目录() + "/1.txt")
        self.assertEqual(data, True)

        data = 文件_是否为目录(取运行目录() + "/1.txt")
        self.assertEqual(data, False)

        data = 文件_是否为目录(取运行目录() + "/")
        self.assertEqual(data, True)

        data = 改变目录(取运行目录())
        data = 写到文件("./1.txt", b"abc")
        self.assertEqual(data, True)
        print(取运行目录() + r"/1.txt")
        data = 文件_是否为文件(取运行目录() + r"/1.txt")
        self.assertEqual(data, True)
        data = 文件_是否为文件(取运行目录() + "/")
        self.assertEqual(data, False)

        data = 文件是否存在(取运行目录())
        self.assertEqual(data, True)

        data = 文件_取文件大小(取运行目录() + r"/1.txt")
        self.assertEqual(data, 3)

    def test_5(self):
        """
        test_5 的功能说明（请补充）。

        """
        data = 文件_获取文件信息(取运行目录() + r"/1.txt")
        print(data)
        data = 文件_修改文件时间(取运行目录() + r"/1.txt", (1621211781, 1621211781))
        print(data)
        data = 取文件访问时间(取运行目录() + r"/1.txt")
        print(data)
        data = 取文件创建时间(取运行目录() + r"/1.txt")
        print(data)
        data = 取文件修改时间(取运行目录() + r"/1.txt")
        print(data)

        文件_修改权限(取运行目录() + r"/1.txt", 0)
        data = 文件_检查权限("1.txt", 1)
        print(data)
        文件_修改权限(取运行目录() + r"/1.txt", 1)
        data = 文件_检查权限("1.txt", 2)
        print(data)

    def test_6(self):
        """
        test_6 的功能说明（请补充）。

        """
        print(取运行目录())
        list = 文件_枚举(取运行目录(), ".py", False)
        for i in list:
            print(i)

        list = 文件_枚举(取运行目录(), ".py", True)
        for i in list:
            print(i)

    def test_7(self):
        """
        test_7 的功能说明（请补充）。

        """
        print(取运行目录())
        list = 目录_枚举(取运行目录(), False)
        for i in list:
            print(i)

        list = 目录_枚举(取运行目录(), True)
        for i in list:
            print(i)

    def test_8(self):
        """
        test_8 的功能说明（请补充）。

        """
        data = 文件_取扩展名("c:/1.txt")
        # self.assertEqual(data, "txt")
        data = 文件_取父目录("c:/1.txt")
        # self.assertEqual(data, "c:/")

    def test_9(self):
        """
        test_9 的功能说明（请补充）。

        """
        print(取运行目录())
        #
        # data = 文件_写出(取运行目录() + r"\a\b\5.txt", b"bbb")
        # self.assertEqual(data, True)
        #
        # data = 文件_追加文本(取运行目录() + r"\a\b\1.txt", "bbb")
        # self.assertEqual(data, True)

        data = 文件_保存(取运行目录() + r"\a\b\m.txt", b"bbb")
        self.assertEqual(data, True)

        data = 读入文本(取运行目录() + r"\a\b\m.txt")
        print(data)

    def test_10(self):
        # data = 路径优化('~/foo')
        # print(data)
        """
        test_10 的功能说明（请补充）。

        """
        self.assertEqual(路径优化(r'c:/123\abc/dbf/dddd'), r"c:\123\abc\dbf\dddd")

    def test_11(self):
        """
        test_11 的功能说明（请补充）。

        """
        新路径 = 路径_合并("c:/aaa/","bbb","ccc/")
        print(新路径)
        self.assertEqual(新路径, "c:/aaa/bbb/ccc/")

import unittest

from .dirkBase import *


class TestDirk(unittest.TestCase):

    def test_1(self):
        data = 取当前目录()
        self.assertNotEqual(data, "")
        print(data)

        data = 取运行目录()
        self.assertNotEqual(data, "")
        print(data)

        data = 写到文件("1.txt", b"abc")
        self.assertEqual(data, True)

        data = 写到文件("./a/1.txt", b"abc")
        self.assertEqual(data, False)

        data = 复制文件("1.txt", "2.txt")
        self.assertEqual(data, True)

        data = 复制文件("1.txt", "./a/2.txt")
        self.assertEqual(data, False)

        data = 移动文件("1.txt", "3.txt")
        self.assertEqual(data, True)

        data = 移动文件("1.txt", "./a/3.txt")
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
        data = 删除目录('./c')
        self.assertEqual(data, True)
        print(data)


    def test_2(self):
        data = 文件_路径取扩展名('c:/a/1.jpg')
        self.assertEqual(data, ".jpg")
        print(data)

        data = 文件_取文件名('c:/a/1.jpg')
        self.assertEqual(data, "1.jpg")
        print(data)

        data = 文件_取目录('c:/a/1.jpg')
        self.assertEqual(data, "c:/a")
        print(data)

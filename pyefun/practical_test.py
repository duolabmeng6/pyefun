import unittest

from .practical import *


class TestPractical(unittest.TestCase):
    def test12(self):
        data = 取主机名()
        print(data)

        # self.assertEqual(data, "commonlyUtil.py")
        data = 转换为IP地址(取主机名())
        # self.assertEqual(data, "commonlyUtil.py")

        print(data)


    def test11(self):
        data = 标准输出("请输入一个数", ":")

        #data = 标准输入()
        print(data)

    def test14(self):
        data = 结束()

    def test14(self):
        data = 取uuid()
        print(data)
        data = 取短id()
        print(data)
    def test10(self):
        data = 取执行文件名()
        self.assertEqual(data, "practical.py")

        data = 读环境变量("path")
        print(data)

        data = 写环境变量("aaa", "bbb")
        self.assertEqual(data, "bbb")

        data = 读环境变量("aaa")
        self.assertEqual(data, "bbb")
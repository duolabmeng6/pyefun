import unittest

from pyefun.模块.苹果系统操作 import *
from pyefun import *



class Test苹果系统操作(unittest.TestCase):
    def test_文本朗读(self):
        文本朗读("您好,祖国")
        time.sleep(1)

        文本朗读("hello world")
        time.sleep(1)

    def test_系统通知(self):
        系统通知("通知", "您好,祖国")
        time.sleep(1)

        系统通知("通知", "hello world")
        time.sleep(1)

    def test_系统对话框(self):
        系统对话框("通知", "您好,祖国")
        time.sleep(1)

        系统对话框("通知", "hello world")
        time.sleep(1)


    def test_显示系统信息(self):
        系统信息 = 显示系统信息()
        print("系统信息",系统信息)

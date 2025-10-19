import unittest

from pyefun.模块.苹果系统操作 import *
from pyefun import *


class Test苹果系统操作(unittest.TestCase):
    def test_文本朗读(self):
        """
        test_文本朗读 的功能说明（请补充）。

        """
        文本朗读("您好,祖国")
        time.sleep(1)

        文本朗读("hello world")
        time.sleep(1)

    def test_系统通知(self):
        """
        test_系统通知 的功能说明（请补充）。

        """
        系统通知("通知", "您好,祖国")
        time.sleep(1)

        系统通知("通知", "hello world")
        time.sleep(1)

    def test_系统对话框(self):
        """
        test_系统对话框 的功能说明（请补充）。

        """
        系统对话框("通知", "您好,祖国")
        time.sleep(1)

        系统对话框("通知", "hello world")
        time.sleep(1)

    def test_显示系统信息(self):
        """
        test_显示系统信息 的功能说明（请补充）。

        """
        系统信息 = 显示系统信息()
        print("系统信息", 系统信息)

    def test_设置开机自启动项(self):
        """
        test_设置开机自启动项 的功能说明（请补充）。

        """
        设置开机自启动项("/usr/local/bin/aria2c")
        # 取消开机自启动项("aria2c")

    def test_plist设置开机自启动项(self):
        """
        test_plist设置开机自启动项 的功能说明（请补充）。

        """
        使用plist文件设置开机自启动项("/usr/local/bin/aria2c", "/Users/yhm/Downloads", "aria2")
        # time.sleep(10)
        # 删除开机自启动项的plist文件("aria2")
        # time.sleep(10)

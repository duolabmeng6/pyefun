import unittest

from .文件下载 import *


class Test文件下载(unittest.TestCase):

    def test_文件下载1(self):
        def 进度(进度百分比, 已下载大小, 文件大小, 下载速率, 剩余时间):
            信息 = f"进度 {进度百分比}% 已下载 {已下载大小}MB 文件大小 {文件大小}MB 下载速率 {下载速率}MB 剩余时间 {剩余时间}秒"
            print(f"\r {信息}", end="")

        下载文件("https://github.com/duolabmeng6/QtEasyDesigner/releases/download/0.0.32/QtEasyDesigner_MacOS.zip",
             "QtEasyDesigner_MacOS.zip", 进度)

    def test_文件下载进度条(self):
        下载文件进度条("https://github.com/duolabmeng6/QtEasyDesigner/releases/download/0.0.32/QtEasyDesigner_MacOS.zip",
                "QtEasyDesigner_MacOS.zip")

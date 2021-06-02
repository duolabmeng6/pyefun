import unittest
import warnings

from .seleniumUtil import *
from pyefun import *


class TestseleniumUtil(unittest.TestCase):

    def test_1(self):
        pass
        浏览器初始化本地环境()

        浏览器 = 浏览器类()
        浏览器.打开chrome()

        浏览器.浏览网页("https://www.baidu.com")
        print(浏览器.取页面标题())
        print(浏览器.取名称())
        # print(浏览器.取页面链接())
        # print(浏览器.取页面源码())
        with 时间统计("就绪"):
            print(浏览器.等待元素显示(5, "s_ipt"))

        延时(1)

        搜索输入框 = 浏览器.取元素从id("kw")
        百度一下按钮 = 浏览器.取元素从id("su")

        搜索输入框.输入("pyefun")
        百度一下按钮.点击()

        延时(1)

        with 时间统计("结果就绪"):
            print(浏览器.等待元素显示(5, "result"))

        搜索结果 = 浏览器.取元素从class_name("result")
        print("搜索结果多少条", len(搜索结果))
        for 元素 in 搜索结果:
            print(元素.取文本())
            # print(元素.取源码())

        延时(1)
        浏览器.退出()

    def test_2(self):
        pass

        warnings.simplefilter('ignore', ResourceWarning) # 屏蔽一堆错误

        浏览器 = 浏览器类()
        远程浏览器地址 = "http://127.0.0.1:4444/wd/hub"
        while 浏览器.远程浏览器是否就绪(远程浏览器地址) == False:
            延时(1)
            print("浏览器未就绪")

        浏览器.获取远程chrome(远程浏览器地址)

        浏览器.浏览网页("https://www.baidu.com")
        print(浏览器.取页面标题())
        print(浏览器.取名称())
        # print(浏览器.取页面链接())
        # print(浏览器.取页面源码())
        with 时间统计("就绪"):
            print(浏览器.等待元素显示(5, "s_ipt"))

        延时(1)

        搜索输入框 = 浏览器.取元素从id("kw")
        百度一下按钮 = 浏览器.取元素从id("su")

        搜索输入框.输入("pyefun")
        百度一下按钮.点击()

        延时(1)

        with 时间统计("结果就绪"):
            print(浏览器.等待元素显示(5, "result"))

        搜索结果 = 浏览器.取元素从class_name("result")
        print("搜索结果多少条", len(搜索结果))
        for 元素 in 搜索结果:
            print(元素.取文本())
            # print(元素.取源码())

        延时(1)
        浏览器.退出()

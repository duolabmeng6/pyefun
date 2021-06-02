import unittest

from .seleniumUtil import *
from pyefun import *


class TestseleniumUtil(unittest.TestCase):

    def test_1(self):
        pass
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

        搜索输入框.输入("aaa")
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

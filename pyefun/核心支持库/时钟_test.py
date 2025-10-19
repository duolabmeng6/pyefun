"""
时钟模块的单元测试。

验证定时器函数与装饰器的基本行为。
"""
import unittest

from .时钟 import *


class Test时钟(unittest.TestCase):
    """时钟功能相关测试用例。"""

    def test_1(self):
        pass

        @时钟周期事件(时钟周期=1000)
        def 定时任务():
            print("定时任务")
            # return True
            return False

    def test_2(self):
        pass

        def 定时任务():
            print("定时任务")
            # return True
            return False
        时钟(定时任务, 时钟周期=1000)

"""
时钟模块的单元测试。

验证定时器函数与装饰器的基本行为。
"""
import unittest

from .时钟 import *


class Test时钟(unittest.TestCase):
    """时钟功能相关测试用例。"""

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        pass

        @时钟周期事件(时钟周期=1000)
        def 定时任务():
            """
            定时任务 的功能说明（请补充）。

            """
            print("定时任务")
            # return True
            return False

    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        pass

        def 定时任务():
            """
            定时任务 的功能说明（请补充）。

            """
            print("定时任务")
            # return True
            return False
        时钟(定时任务, 时钟周期=1000)

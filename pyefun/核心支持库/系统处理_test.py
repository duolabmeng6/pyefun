"""
系统处理模块的单元测试。

覆盖命令运行等基础用例。
"""
import unittest

from pyefun import *


class TestSystemProcessingBase(unittest.TestCase):
    """系统处理相关测试用例。"""

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        pass
        data = 运行("ipconfig")
        print(data)

    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        pass
        # data = 取鼠标位置()
        # print(data.x)
        # print(data.y)

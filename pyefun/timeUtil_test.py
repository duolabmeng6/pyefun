import unittest

from .timeUtil import *
from .timeBase import *
from .systemProcessingBase import *


class TestTimeUtil(unittest.TestCase):

    def test_1(self):
        # with 计时器() as t:
        #     延时(1)
        # print(t.取耗时())

        t = 时间统计()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        t.开始()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())

        t = 计时器()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        t.开始()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())



    def test_4(self):
        with 时间统计("买东西业务") as t:
            延时(1)
            t.取耗时("出门")
            延时(1)
            t.取耗时("到店")
            延时(1)
            t.取耗时("购买")
        print("总耗时", t.取总耗时())

    def test_5(self):
        with 时间统计("测试耗时"):
            延时(1)

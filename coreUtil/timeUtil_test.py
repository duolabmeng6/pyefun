import unittest

from .timeUtil import *
from core.timeBase import *
from core.systemProcessingBase import *


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



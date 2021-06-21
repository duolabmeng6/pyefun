import unittest

from .timerit import *
from pyefun.systemProcessingBase import *
from pyefun.arithmeticOperationBase import *


class TestTimeUtil(unittest.TestCase):
    def test_2(self):
        for _ in 计时统计(次数=1000, 显示信息=3):
            math.factorial(10000)

    def test_3(self):
        t1 = 计时统计(次数=10, 标签="运行", 取样=20, 显示信息=3, 单位='ms')
        for timer in t1:
            setup_vars = 10000
            with timer:
                延时(0.01 + 取随机数(1, 2) / 10)
                math.factorial(setup_vars)
        print('总耗时 = %r' % (t1.取耗时(),))
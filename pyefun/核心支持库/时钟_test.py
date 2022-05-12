import unittest

from .__init__ import *


class TestClock(unittest.TestCase):

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

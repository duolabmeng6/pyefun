"""

.. Hint::
    时间工具类 时间统计


.. literalinclude:: ../../../pyefun/timeUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import datetime
import time


class 时间统计():
    """
    计时器，对于需要计时的代码进行with操作：
    with 计时器() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self, 名称=""):
        self.开始()
        self.名称 = 名称
        self.zstart = self.start
        if self.名称:
            print("时间统计: %s 开始 %s" % (self.名称, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def __enter__(self):
        return self

    def 开始(self):
        """
        重新计算开始时间
        """
        self.start = time.perf_counter()

    def 取耗时(self, 名称=""):
        """
        每次计时后重置 如果需要总耗时的话 取总耗时() 即可
        """
        self.end = time.perf_counter()
        self.ms = int((self.end - self.start) * 1000)
        self.开始()
        if 名称 != "":
            print("时间统计: %s %s %sms" % (self.名称, 名称, self.ms))
        elif self.名称 != "":
            print("时间统计: %s %sms" % (self.名称, self.ms))

        return self.ms

    def 取总耗时(self):
        """
        自对象创建以来的总耗时
        """
        self.end = time.perf_counter()
        self.ms = int((self.end - self.zstart) * 1000)
        return self.ms

    def 取毫秒(self):
        return self.取耗时()

    def 取秒(self):
        return self.取耗时() / 1000

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.名称 != "":
            print("时间统计: %s 结束 %sms %s" % (self.名称, self.取总耗时(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return exc_type is None


def 计时器():
    return 时间统计()


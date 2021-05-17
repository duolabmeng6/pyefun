import time
from core.arithmeticOperationBase import *


class 时间统计(object):
    """
    计时器，对于需要计时的代码进行with操作：
    with 计时器() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self):
        self.开始()

    def __enter__(self):
        return self

    def 开始(self):
        self.start = time.time()

    def 取耗时(self):
        self.end = time.time()
        self.ms = int((self.end - self.start) * 1000)
        return self.ms

    def 取毫秒(self):
        return self.取耗时()

    def 取秒(self):
        return self.取耗时() / 1000

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.取耗时()
        return exc_type is None


def 计时器():
    return 时间统计()

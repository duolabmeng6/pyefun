import unittest

from .threadingUtil import *
from .__init__ import *

lock = 互斥锁()
lock2 = 递归锁()


def 工作线程(参数):
    lock.进入()
    print(取现行时间(), 参数, "启动线程了")
    lock.退出()

def 工作线程2(参数):
    print(取现行时间(), 参数, "无锁")
def 工作线程3(参数):
    lock2.进入()
    print(取现行时间(), 参数, "启动线程了 递归锁")
    lock2.退出()



class TestThreadingUtil(unittest.TestCase):

    def test_1(self):
        for i in range(10):
            data = 启动线程(工作线程, [i])

        延时(1)

    def test_4(self):
        for i in range(10):
            data = 启动线程(工作线程2, [i])
        延时(1)

    def test_5(self):
        for i in range(10):
            data = 启动线程(工作线程3, [i])
        延时(1)


    def test_2(self):
        lock = 互斥锁()
        lock.进入()
        lock.退出()

    def test_3(self):
        data = 网页_访问("https://www.baidu.com/")
        print(data.字节集.decode('utf-8'))

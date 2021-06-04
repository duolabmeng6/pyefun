import unittest

from .threadingUtil import *
from .__init__ import *
from .asyncPoolGevent.asyncPoolGevent import *
# from .asyncPool.asyncPool import * 无法在测试用例中测试
# import asyncio

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


def 工作线程4(参数):
    with 时间统计() as t:
        延时(取随机数(4, 4))
        # 延时(取随机数(5, 5))
        print(time.time(), t.取耗时(), 参数, "线程类测试")
        # print(取现行时间(), t.取耗时(), 参数, "线程类测试")


def 线程初始化(data):
    print("初始化", data, 取当前线程名称())


互斥锁 = 互斥锁()


def 任务函数(i):
    time.sleep(1)
    互斥锁.进入()
    print(i)
    互斥锁.退出()
    return "返回参数" + str(i)


def 任务完成(future):
    print("当前线程", 取当前线程名称())
    print("future", future.result())


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
        pass
        # lock = 互斥锁()
        # lock.进入()
        # lock.退出()

    def test_3(self):
        data = 网页_访问("https://www.baidu.com/")
        print(data.字节集.decode('utf-8'))

    #
    # def test_4(self):
    #     pool = 线程池(
    #         工作线程数量=2,
    #         队列数量=10,
    #     )
    #     for i in range(5):
    #         # print("投递任务1",i)
    #
    #         # 一直等待直到了有位置
    #         pool.投递任务(工作线程4, i)
    #         # 超时返回false
    #         # while pool.投递任务(工作线程4, i, 等待时间=None) == False:
    #         #     print("队列已满")
    #         print("投递任务", 取现行时间(), i)
    #     pool.等待()
    #     print("任务完成")

    def test_4(self):

        pool = 协程池(协程数量=9)
        任务列表 = []
        # "创建一批任务 一起运行等待完成"
        for i in range(11):
            print("创建任务", i)
            任务列表.append(pool.投递任务(工作线程4, i))
        pool.等待协程完成任务(任务列表)
        print("任务完成1")

        pool.等待()
        print("任务完成2")

    def test_10(self):
        # 创建任务直接运行不需要等待
        pool = 协程池(协程数量=9)
        for i in range(11):
            print("创建任务", i)
            pool.投递任务(工作线程4, i)
        pool.等待()

    def test_5(self):

        print("线程_取活动对象数", 线程_取活动对象数())
        print("线程_取当前线程", 线程_取当前线程())
        print("线程_取线程标识符", 线程_取线程标识符())
        print("线程_取所有活动对象", 线程_取所有活动对象())
        print("线程_取主线程", 线程_取主线程())

    def test_6(self):

        任务池 = 线程池(4, "pyefun", 线程初始化, [0])

        for url in range(10):
            future = 任务池.投递任务(任务函数, url)
            任务池.设置任务结束回调函数(future, 任务完成)

        任务池.等待()

        任务池.批量投递任务(任务函数, range(1, 12))  # map取代了for+submit
        任务池.等待()

    def test_8(self):
        pass
        # # 创建任务直接运行不需要等待
        # pool = 协程池Asyncio(协程数量=9, 线程池数量=10)
        # for i in range(11):
        #     print("创建任务", i)
        #     pool.投递任务(任务函数, i, 回调函数=任务完成)
        # pool.释放线程()
        # pool.等待()

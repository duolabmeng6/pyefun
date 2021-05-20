"""
线程操作类

"""

import threading
from .public import *

@异常处理返回类型逻辑型
def 启动线程(函数名, 参数=(), 跟随主线程结束=False):
    "成功返回线程对象,参数用元组形式传入,返回线程对象,daemon属性为False，主线程结束时会检测该子线程是否结束"
    线程 = threading.Thread(target=函数名, args=参数, daemon=跟随主线程结束)
    线程.start()
    return 线程



class 互斥锁:
    '类似许可证,这个可能会造成死锁'
    def __init__(self):
        self.__互斥锁 = threading.Lock()

    @异常处理返回类型逻辑型
    def 进入(self):
        self.__互斥锁.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.__互斥锁.release()


class 递归锁:
    '类似许可证，互斥锁的升级版，这个不会造成死锁'
    def __init__(self):
        self.__递归锁 = threading.RLock()

    @异常处理返回类型逻辑型
    def 进入(self):
        self.__递归锁.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.__递归锁.release()


class 信号量:
    '设置最大同时运行的线程数'
    def __init__(self,数量=1):
        self.__信号量 = threading.BoundedSemaphore(数量)

    @异常处理返回类型逻辑型
    def 进入(self):
        self.__信号量.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.__信号量.release()


class 事件锁:
    def __init__(self):
        self.__事件锁 = threading.Event()

    @异常处理返回类型逻辑型
    def 通行(self):
        self.__事件锁.set()

    @异常处理返回类型逻辑型
    def 堵塞(self):
        self.__事件锁.clear()

    @异常处理返回类型逻辑型
    def 等待(self):
        '这里会判断事件状态,如果为通行状态则继续向下运行,否则会一直等待'
        self.__事件锁.wait()


class 线程:
    def __init__(self):
        import threading as 线程
        self.__线程 = 线程
        self.__线程列表 = []

    @异常处理返回类型逻辑型
    def 启动线程(self, 函数名, 参数=(), 跟随主线程结束=False):
        "成功返回线程对象,参数用元组形式传入,daemon属性为False，主线程结束时会检测该子线程是否结束"
        线程 = self.__线程.Thread(target=函数名, args=参数, daemon=跟随主线程结束)
        线程.start()
        self.__线程列表.append(线程)
        return 线程


    @异常处理返回类型逻辑型
    def 等待线程结束(self, 最长等待时间=0):
        '顺利结束返回True如果启动线程参数daemon设置为True,则可以设置最长等待时间,超过时间强制结束线程'
        for i in self.__线程列表:
            if 最长等待时间 <= 0:
                i.join()
            else:
                i.join(最长等待时间)
        return True


    @异常处理返回类型逻辑型
    def 取运行中的线程对象(self):
        return self.__线程.enumerate()


    @异常处理返回类型逻辑型
    def 线程是否在运行(self, 线程对象):
        '返回True或False'
        return 线程对象.is_alive()


    @异常处理返回类型逻辑型
    def 取运行的线程数(self):
        '只返回该类创建后使用该类启动线程创建的线程数量'
        for x in self.__线程列表:
            if x.is_alive() == False:
                self.__线程列表.remove(x)
        return len(self.__线程列表)


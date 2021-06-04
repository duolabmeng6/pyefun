"""

.. Hint::
    线程操作有线程池


.. literalinclude:: ../../../pyefun/threadingUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

from .public import *
import threading

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread


@异常处理返回类型逻辑型
def 启动线程(函数名, 参数=(), 跟随主线程结束=False):
    "成功返回线程对象,参数用元组形式传入,返回线程对象,daemon属性为False，主线程结束时会检测该子线程是否结束"
    线程 = threading.Thread(target=函数名, args=参数, daemon=跟随主线程结束)
    线程.start()
    return 线程


class 互斥锁:
    '类似许可证,这个可能会造成死锁'

    def __init__(self):
        self.lock = threading.Lock()

    @异常处理返回类型逻辑型
    def 进入(self):
        self.lock.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.lock.release()


class 递归锁:
    '类似许可证，互斥锁的升级版，这个不会造成死锁'

    def __init__(self):
        self.lock = threading.RLock()

    @异常处理返回类型逻辑型
    def 进入(self):
        self.lock.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.lock.release()


class 信号量:
    '设置最大同时运行的线程数'

    def __init__(self, 数量=1):
        self.lock = threading.BoundedSemaphore(数量)

    @异常处理返回类型逻辑型
    def 进入(self):
        self.lock.acquire()

    @异常处理返回类型逻辑型
    def 退出(self):
        self.lock.release()


class 事件锁:
    def __init__(self):
        self.lock = threading.Event()

    @异常处理返回类型逻辑型
    def 通行(self):
        self.lock.set()

    @异常处理返回类型逻辑型
    def 堵塞(self):
        self.lock.clear()

    @异常处理返回类型逻辑型
    def 等待(self):
        '这里会判断事件状态,如果为通行状态则继续向下运行,否则会一直等待'
        self.lock.wait()


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


# 过时的库不用了
# import threadpool
# class 线程池(threadpool.ThreadPool):
#     def __init__(self, 工作线程数量, 队列数量=0):
#         """
#             创建线程池
#             工作线程数量 线程池的线程数量
#             队列数量 为投递任务时队列的数量
#         """
#         super().__init__(工作线程数量, q_size=队列数量, resq_size=0, poll_timeout=5)
#
#     @异常处理返回类型逻辑型
#     def 投递任务(self, 任务函数, 参数, 等待时间=None):
#         """投递一个任务函数到线程池任务队列中。"""
#         requests = threadpool.makeRequests(任务函数, [参数])
#         for req in requests:
#             self.putRequest(req, True, 等待时间)
#
#     def 等待(self):
#         """等待所有任务完成"""
#         self.wait()


def 线程_取活动对象数():
    """
    返回Thread当前活动的对象数。返回的计数等于所返回列表的长度
    """
    return threading.active_count()


def 线程_取当前线程():
    """
    返回与Thread调用方的控制线程相对应的当前对象。如果未通过threading模块创建调用者的控制 线程，则返回功能有限的虚拟线程对象。
    """
    return threading.current_thread()


def 线程_取线程标识符():
    """
    返回当前线程的“线程标识符”。这是一个非零整数。它的值没有直接的意义。它旨在用作魔术Cookie，例如用于索引线程特定数据的字典。当一个线程退出并创建另一个线程时，线程标识符可以被回收。
    """

    return threading.get_ident()


def 线程_取所有活动对象():
    """
返回Thread当前所有活动对象的列表。该列表包括守护线程，由创建的伪线程对象 current_thread()和主线程。它不包括终止的线程和尚未启动的线程。
    """
    return threading.enumerate()


def 线程_取主线程():
    """
 返回主要Thread对象。在正常情况下，主线程是启动Python解释器的线程。

  """
    return threading.main_thread()


def 取当前线程名称():
    return current_thread().name


class 线程池(ThreadPoolExecutor):
    """
    当有大量并发任务需要处理时，再使用传统的多线程就会造成大量的资源创建销毁导致服务器效率的下降。这时候，线程池就派上用场了。线程池技术为线程创建、销毁的开销问题和系统资源不足问题提供了很好的解决方案。

    用法

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

    任务池 = 线程池(4, "pyefun", 线程初始化, [0])

    for url in range(10):
        future = 任务池.投递任务(任务函数, url)
        任务池.设置任务结束回调函数(future, 任务完成)

    任务池.等待()
    """

    def __init__(self, 最大线程数量, 线程名称前缀='',
                 线程初始化函数=None, 初始化函数参数=()):
        """
            创建线程池

            :param 最大线程数量:
            :param 线程名称前缀:
            :param 线程初始化函数:
            :param 初始化函数参数:
        """

        super().__init__(
            max_workers=最大线程数量,
            thread_name_prefix=线程名称前缀,
            initializer=线程初始化函数,
            initargs=初始化函数参数
        )

    def 投递任务(self, *任务函数, **传入参数):
        """
        投递任务

        :param 任务函数:
        :param 传入参数:
        :return: Future 对象可以 设置任务结束回到函数
        """
        Future = self.submit(*任务函数, **传入参数)
        return Future

    def 设置任务结束回调函数(self, future, 回到函数):
        """
        投递任务返回的对象

        def 回到函数(线程返回的结果):
            print("当前线程", current_thread().name)
            print("线程返回的结果", future.result())

        """
        future.add_done_callback(回到函数)

    def 等待(self):
        self.shutdown(True)

    def 批量投递任务(self, 任务函数, *任务参数数组, 超时=None, chunksize=1):
        """
        批量投递任务 不能设置回到函数
        :param 任务函数:
        :param 任务参数数组:
        :param 超时:
        :param chunksize:
        :return:
        """
        return self.map(任务函数, *任务参数数组, timeout=超时, chunksize=chunksize)

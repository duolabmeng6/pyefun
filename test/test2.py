from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from pyefun import *


def 取当前线程名称():
    return current_thread().name


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


class 线程池(ThreadPoolExecutor):
    def __init__(self, 最大线程数量, 线程名称前缀='',
                 线程初始化函数=None, 初始化函数参数=()):
        """
        创建线程池

        :param 最大线程数量:
        :param 线程名称前缀:
        :param 线程初始化函数:
        :param 初始化函数参数:

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
        super().__init__(最大线程数量, 线程名称前缀, 线程初始化函数, 初始化函数参数)

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

    def 投递任务批量(self, 任务函数, *任务参数数组, 超时=None, chunksize=1):
        """
        批量投递任务 不能设置回到函数
        :param 任务函数:
        :param 任务参数数组:
        :param 超时:
        :param chunksize:
        :return:
        """
        return self.map(任务函数, *任务参数数组, timeout=超时, chunksize=chunksize)


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2


if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=3)
    # executor.map(task, range(1, 12))  # map取代了for+submit
    # executor.shutdown(True)

    任务池 = 线程池(4, "pyefun", 线程初始化, [0])

    # for url in range(10):
    #     future = 任务池.投递任务(任务函数, url)
    #     任务池.设置任务结束回调函数(future, 任务完成)

    任务池.投递任务批量(任务函数, range(1, 12))  # map取代了for+submit
    任务池.等待()
    print('主线程', 取当前线程名称())

"""
.. Hint::
    进程池使用方法，便捷地使用 Python 开启多进程。

    本模块对 multiprocessing 进行了一层中文封装，提供进程、进程池与进程安全队列等常用能力。
"""

import multiprocessing

from pyefun import 事件锁


class 进程队列:
    """基于 multiprocessing.Queue 的进程安全队列封装。

    提供简单的加入与获取数据的方法，适用于多进程之间的数据传递。
    """

    def __init__(self):
        self.队列对象 = multiprocessing.Queue()

    def 加入数据(self, 要加入的数据):
        """向队列加入一条数据。

        :param 要加入的数据: 任意可被序列化的对象
        """
        self.队列对象.put(要加入的数据)

    def 获取数据(self):
        """从队列中获取一条数据（阻塞式）。

        :return: 入队时放入的对象
        """
        return self.队列对象.get()


class 进程:
    """对 multiprocessing.Process 的简易封装。

    通过中文命名的方法更直观地创建、启动、等待和关闭子进程。
    """

    def __init__(self, 子程序名, 元组参数=(), 字典参数=None, 进程名=None):
        """创建进程对象。

        :param 子程序名: 目标函数
        :param 元组参数: 位置参数，使用元组传入
        :param 字典参数: 关键字参数，使用字典传入
        :param 进程名: 进程名称，可选
        """
        if 字典参数 is None:
            字典参数 = {}
        self.进程对象 = multiprocessing.Process(target=子程序名, args=元组参数, kwargs=字典参数, name=进程名)

    def 启动(self):
        """启动子进程。"""
        self.进程对象.start()

    def 关闭(self):
        """关闭进程对象的底层句柄。注意：不会终止已在运行的进程。"""
        self.进程对象.close()

    def 等待进程(self, 超时时间=None):
        """等待子进程结束。

        如果 timeout 为 None，则阻塞直到子进程终止；若为正数，则最多阻塞指定秒数。
        可通过 exitcode 判断进程是否已退出。
        :param 超时时间: 等待的秒数，None 表示无限等待
        """
        self.进程对象.join(超时时间)

    def 取进程名(self):
        """获取进程名称。"""
        return self.进程对象.name

    def 是否存在(self):
        """判断进程是否还在运行。

        :return: True 表示进程仍存活
        """
        return self.进程对象.is_alive()

    def 取pid(self):
        """获取子进程的 PID。"""
        return self.进程对象.pid

    def 终止子进程(self):
        """获取子进程退出代码。

        注意：此方法未发送终止信号，仅返回 exitcode。
        若要立即停止子进程，请调用 multiprocessing.Process.terminate()。
        :return: None 表示进程尚未终止；负值 -N 表示被信号 N 终止
        """
        return self.进程对象.exitcode

    def 守护(self, 是否守护进程=True):
        """设置子进程为守护进程。

        必须在 start() 之前设置。主进程退出时会尝试终止其所有守护子进程。
        :param 是否守护进程: True/False
        """
        self.进程对象.daemon = 是否守护进程


class 进程池:
    """对 multiprocessing.Pool 的简易中文封装。

    支持按最大并行数限制投递任务，并提供阻塞投递与等待等接口。
    """

    def __init__(self, 进程数, 投递任务时阻塞=True):
        """创建进程池。

        :param 进程数: 进程池中的最大并发进程数
        :param 投递任务时阻塞: 当已投递未完成任务数达到上限时，是否阻塞投递
        """
        self.进程池对象 = multiprocessing.Pool(processes=进程数)

        self.投递任务时阻塞 = 投递任务时阻塞
        if 投递任务时阻塞:
            self.已投递任务数量 = 0
            self.最大线程数量 = 进程数
            self.锁 = 事件锁()

    def 投递任务(self, 子程序, 回调函数=None, 回调报错=None, *args, **kwds):
        """投递单个任务到进程池。

        :param 子程序: 需要执行的函数
        :param 回调函数: 任务成功后的回调，形参为函数返回值
        :param 回调报错: 任务异常时的回调，形参为异常对象
        :param args: 位置参数
        :param kwds: 关键字参数
        :return: AsyncResult 对象
        """
        if self.投递任务时阻塞:
            if self.已投递任务数量 >= self.最大线程数量:
                self.锁.堵塞()
                self.锁.等待()
            self.已投递任务数量 = self.已投递任务数量 + 1
            if self.投递任务时阻塞:
                回调函数保存 = 回调函数

                def 回调函数x(e):
                    self.已投递任务数量 = self.已投递任务数量 - 1
                    self.锁.通行()
                    if 回调函数保存 is not None:
                        回调函数保存(e)

                回调函数 = 回调函数x
                回调报错 = 回调函数x

        启动对象 = self.进程池对象.apply_async(func=子程序, args=args, kwds=kwds, callback=回调函数, error_callback=回调报错)
        return 启动对象

    def 投递任务2(self, 子程序, 迭代列表):
        """批量投递任务（map 形式）。

        注意：其中一个子程序报错可能导致整体报错，谨慎使用。
        :param 子程序: 目标函数
        :param 迭代列表: 可迭代对象
        :return: MapResult 对象
        """
        启动对象 = self.进程池对象.map_async(func=子程序, iterable=迭代列表)
        return 启动对象

    def 等待(self):
        """停止接收新任务并等待所有子进程结束。"""
        self.停止添加子进程()
        self.等待子进程结束()

    def 停止添加子进程(self):
        """防止任何更多的任务被提交到池中。

        一旦完成所有任务，工作进程将退出。
        """
        self.进程池对象.close()

    def 终止所有子进程(self):
        """立即停止工作进程而不完成未完成的工作。

        当池对象被垃圾回收时，terminate() 将被立即调用。
        """
        self.进程池对象.terminate()

    def 等待子进程结束(self):
        """等待工作进程退出。

        必须在调用 close() 或 terminate() 后再调用 join()。
        """
        self.进程池对象.join()

    def 取返回值(self, 启动对象):
        """获取异步任务的返回值。

        :param 启动对象: apply_async 或 map_async 返回的对象
        :return: 任务的返回值
        """
        return 启动对象.get()

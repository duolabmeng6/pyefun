"""

.. Hint::
    进程池使用方法

    方便的使用python开启多进程

.. literalinclude:: ..\..\..\example\进程池测试.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-40

"""
import multiprocessing


class 进程队列:
    def __init__(self):
        self.队列对象 = multiprocessing.Queue()

    def 加入数据(self, 要加入的数据):
        self.队列对象.put(要加入的数据)

    def 获取数据(self):
        return self.队列对象.get()


class 进程:
    def __init__(self, 子程序名, 元组参数=(), 字典参数={}, 进程名=None):
        self.进程对象 = multiprocessing.Process(target=子程序名, args=元组参数, kwargs=字典参数, name=进程名)

    def 启动(self):
        self.进程对象.start()

    def 关闭(self):
        self.进程对象.close()

    def 等待进程(self, 超时时间=None):
        """如果可选参数timeout是None，则该方法将阻塞，直到join()调用其方法的进程终止。如果timeout是一个正数，它最多会阻塞超时秒。请注意，None如果方法的进程终止或方法超时，则返回该方法。检查进程exitcode以确定它是否终止。"""
        self.进程对象.join(超时时间)

    def 取进程名(self):
        return self.进程对象.name

    def 是否存在(self):
        """返回逻辑型"""
        return self.进程对象.is_alive()

    def 取pid(self):
        return self.进程对象.pid

    def 终止子进程(self):
        """子进程的退出代码。None如果流程尚未终止，这将是。负值-N表示孩子被信号N终止。"""
        return self.进程对象.exitcode

    def 守护(self, 是否守护进程=True):
        """ 这个必须在 进程启动先 设置,否则无效  进程的守护进程标志，一个布尔值。必须在start()调用之前设置，当进程退出时，它会尝试终止其所有守护进程子进程。"""
        self.进程对象.daemon = 是否守护进程


class 进程池():
    def __init__(self, 进程数):
        self.进程池对象 = multiprocessing.Pool(processes=进程数)

    def 投递任务(self, 子程序, 元组参数=(), 字典参数={}, 回调函数=None, 回调报错=None):
        启动对象 = self.进程池对象.apply_async(func=子程序, args=元组参数, kwds=字典参数, callback=回调函数, error_callback=回调报错)
        return 启动对象

    def 投递任务2(self, 子程序, 迭代列表):
        """这个用的少,一个子程序报错,全部会报错,后面的函数没有补全了"""
        启动对象 = self.进程池对象.map_async(func=子程序, iterable=迭代列表)
        return 启动对象

    def 等待(self):
        self.停止添加子进程()
        self.等待子进程结束()

    def 停止添加子进程(self):
        """ 防止任何更多的任务被提交到池中。 一旦完成所有任务，工作进程将退出。"""
        self.进程池对象.close()

    def 终止所有子进程(self):
        """立即停止工作进程而不完成未完成的工作。当池对象被垃圾收集时，terminate()将立即调用。；"""
        self.进程池对象.terminate()

    def 等待子进程结束(self):
        """ 等待工作进程退出。必须打电话close()或 terminate()使用之前join()。"""
        self.进程池对象.join()

    def 取返回值(self, 启动对象):
        return 启动对象.get()

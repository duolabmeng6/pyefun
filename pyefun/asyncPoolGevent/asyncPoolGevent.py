"""

.. Hint::
    gevent实现的协程池

    调用时需要引入猴子补丁 需要安装gevent

    pip install gevent

    代码中需要引入猴子补丁

    import gevent
    from gevent import monkey
    monkey.patch_all()

    还有另一个版本的协程池实现 asyncPool 为python原生支持的实现

.. literalinclude:: ../../../pyefun/asyncPool/asyncPool_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
import gevent
from gevent import monkey
monkey.patch_all()
from gevent.threadpool import ThreadPool

from pyefun import 事件锁

class 协程池():

    def __init__(self, 协程数量, 投递任务时阻塞=True):
        self.pool = ThreadPool(协程数量)
        self.投递任务时阻塞 = 投递任务时阻塞
        if (投递任务时阻塞 == True):
            self.已投递任务数量 = 0
            self.最大线程数量 = 协程数量
            self.锁 = 事件锁()

    def 等待协程完成任务(self, 任务列表):
        gevent.joinall(任务列表)

    def 投递任务(self, 任务函数, *args, **kwargs):
        if self.投递任务时阻塞:
            if (self.已投递任务数量 >= self.最大线程数量):
                self.锁.堵塞()
                self.锁.等待()
            self.已投递任务数量 = self.已投递任务数量 + 1

        job = self.pool.spawn(任务函数, *args, **kwargs)
        if self.投递任务时阻塞:
            def 回调函数x(e):
                self.已投递任务数量 = self.已投递任务数量 - 1
                self.锁.通行()
            job.rawlink(回调函数x)
        return job

    def 设置任务结束回调函数(self, future, 回调函数):
        """
        投递任务返回的对象
        def 回调函数(线程返回的结果):
            print("当前线程", current_thread().name)
            print("线程返回的结果", future.result())
        """

        def 匿名函数(future):
            回调函数(future.get())

        future.rawlink(匿名函数)

    def 等待(self):
        """等待所有任务完成"""
        self.pool.join()
        # gevent.wait()

    def 关闭(self):
        """等待所有任务完成"""
        self.pool.kill()

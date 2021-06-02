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
from gevent.threadpool import ThreadPool
monkey.patch_all()


class 协程池():
    """
        创建一个协程池运行任务

        pool = 协程池(协程数量=2)
        任务列表 = []
        for i in range(10):
            任务列表.append(pool.创建任务(工作线程4,i))

        pool.运行任务(任务列表)

    """

    def __init__(self, 协程数量):
        self.pool = ThreadPool(协程数量)

    def 等待协程完成任务(self, 任务列表):
        gevent.joinall(任务列表)

    def 投递任务(self, 任务函数, *args, **kwargs):
        return self.pool.spawn(任务函数, *args, **kwargs)

    def 等待(self):
        """等待所有任务完成"""
        self.pool.join()
        # gevent.wait()

    def 关闭(self):
        """等待所有任务完成"""
        self.pool.kill()

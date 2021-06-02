"""

.. Hint::
    asyncio 实现的协程池 asyncio为python原生支持

    调用时需要引入

    import asyncio

    还有另外一个版本的实现 asyncPoolGevent 为 Gevent实现协程

.. literalinclude:: ../../../pyefun/asyncPool/asyncPool_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import asyncio
import queue
from concurrent.futures import ThreadPoolExecutor


class 协程池(object):
    """
    1. 支持动态添加任务
    2. 支持停止事件循环
    3. 支持最大协程数：maxsize
    4. 支持进度条
    5. 实时获取剩余协程数
    6. 支持阻塞协程，需要线程进行支持，注意设置线程池：pool_maxsize
    """

    def __init__(self, 协程数量=1, 线程池数量=None, loop=None):
        """
        初始化
        :param loop: 事件循环对象
        :param maxsize: 默认为1
        :param pool_maxsize: 默认为系统内核数
        """
        # 在jupyter需要这个，不然asyncio运行出错
        # import nest_asyncio
        # nest_asyncio.apply()

        # 任务计数器
        self._task, self._task_done_count, self._task_progress_list = self.task_create()

        # 协程池
        self._loop, self._loop_thread, self._thread_pool = self.start_loop(
            loop,
            pool_maxsize=线程池数量)

        # 限制并发量为500
        self.semaphore = asyncio.Semaphore(协程数量, loop=self._loop)

    @staticmethod
    def task_create():
        """
        创建任务对象

        :param
        :return:
        """
        # 队列，先进先出，根据队列是否为空判断，退出协程
        # self.task_done_count: 任务完成后的计数器
        # 任务组，用来阻塞任务用的
        task = queue.Queue()

        # 任务完成后的计数器
        task_done_count = queue.Queue()

        # 任务进度值存储
        # 确保任务值是唯一的
        task_progress_list = []

        return task, task_done_count, task_progress_list

    def task_add(self, item=1):
        """
        添加任务
        :param item:
        :return:
        """
        self._task.put(item)

    def task_done(self, fn):
        """
        任务完成
        回调函数
        已完成任务计数

        :param fn:
        :return:
        """
        if fn:
            pass
        self._task.get()
        self._task.task_done()

        # 已完成任务计数
        self._task_done_count.put(1)

    def task_progress(self, total):
        """
        任务进度条
        适用于已知任务总数的情况

        :param total: 任务总数
        :return:
        """
        # 任务完成计数
        # 需要剔除任务停止的任务数
        count = self._task_done_count.qsize() - 1
        if count < 0:
            count = 0

        item = int(count / total * 100)
        if count == total:
            # 任务完成
            self._task_progress_list.append(100)
        elif item not in self._task_progress_list:
            # 过程值
            self._task_progress_list.append(item)
        else:
            pass

        self._task_progress_list = list(set(self._task_progress_list))
        self._task_progress_list.sort()
        return self._task_progress_list[-1]

    def get_task(self):
        """
        获取事件循环任务列表
        :return:
        """
        task_list = asyncio.Task.all_tasks(loop=self._loop)
        # task_list = asyncio.all_tasks(loop=self._loop)
        return task_list

    def 等待(self):
        """
        任务阻塞
        等待所有任务执行完毕

        :return:
        """
        self._task.join()
        # self._thread_pool.shutdown()

    @property
    def running(self):
        """
        获取剩余协程数
        :return:
        """
        # 剩余任务数
        # 需要剔除任务停止的任务数
        count = self._task.qsize() - 1
        if count < 0:
            count = 0
        return count

    @staticmethod
    def _start_thread_loop(loop):
        """
        运行事件循环
        :param loop: loop以参数的形式传递进来运行
        :return:
        """
        # 将当前上下文的事件循环设置为循环。
        asyncio.set_event_loop(loop)
        # 开始事件循环
        loop.run_forever()

    async def _stop_thread_loop(self, loop_time=1):
        """
        停止协程
        关闭线程
        :return:
        """
        while True:
            if self._task.empty():
                # 停止协程
                self._loop.stop()
                break
            await asyncio.sleep(loop_time)

    def start_loop(self, loop, pool_maxsize=None):
        """
        运行事件循环
        开启新线程
        :param loop: 协程
        :param pool_maxsize: 线程池大小，默认为系统内核数
        :return:
        """
        # 获取一个事件循环
        if not loop:
            loop = asyncio.new_event_loop()

        # 线程池
        thread_pool = ThreadPoolExecutor(pool_maxsize)

        # 设置线程池
        loop.set_default_executor(thread_pool)

        # from threading import Thread
        # thread_pool = Thread(target=self._start_thread_loop, args=(loop,))
        # 设置守护进程
        # thread_pool.setDaemon(True)
        # 运行线程，同时协程事件循环也会运行
        # thread_pool.start()

        # 启动子线程
        # 协程开始启动
        thread_pool.submit(self._start_thread_loop, loop)

        return loop, thread_pool, thread_pool

    def stop_loop(self, loop_time=1):
        """
        队列为空，则关闭线程
        :param loop_time:
        :return:
        """
        # 关闭线程任务
        asyncio.run_coroutine_threadsafe(self._stop_thread_loop(loop_time), self._loop)

        # 取消单个任务
        # task.cancel()

    def _close(self):
        """
        关闭事件循环，不然会重启
        会导致错误
        # RuntimeError: Cannot close a running event loop
        :return:
        """
        self._loop.close()

    def 释放线程(self, loop_time=1):
        """
        释放线程
        :param loop_time:
        :return:
        """
        self.stop_loop(loop_time)

    async def async_semaphore_func(self, func):
        """
        信号代理
        :param func:
        :return:
        """
        async with self.semaphore:
            return await func

    async def async_thread_pool_func(self, block_func, *args, thread_pool=True):
        """
        信号代理
        线程池代理

        loop: asyncio.AbstractEventLoop

        :param block_func: 阻塞任务
        :param args: 参数
        :param thread_pool: 是否使用自定义线程池
        :return:
        """
        async with self.semaphore:
            if not thread_pool:
                # 默认线程池
                return await self._loop.run_in_executor(None, block_func, *args)

            # 使用自定义线程池
            future = await self._loop.run_in_executor(self._thread_pool, block_func, *args)
            # gather = await asyncio.gather(future)  # 阻塞
            # gather = await asyncio.wait(future)  # 阻塞
            return future

    def _submit(self, func, callback=None):
        """
        非阻塞模式
        提交任务到事件循环

        :param func: 异步函数对象
        :param callback: 回调函数
        :return:
        """
        self.task_add()

        # 将协程注册一个到运行在线程中的循环，thread_loop 会获得一个环任务
        # 注意：run_coroutine_threadsafe 这个方法只能用在运行在线程中的循环事件使用
        # future = asyncio.run_coroutine_threadsafe(func, self.loop)
        future = asyncio.run_coroutine_threadsafe(self.async_semaphore_func(func), self._loop)

        # 添加回调函数,添加顺序调用
        if callback:
            future.add_done_callback(callback)
        future.add_done_callback(self.task_done)

    def 投递任务(self, func, *args, 回调函数=None):
        """
        非阻塞模式
        提交任务到事件循环

        :param func: 异步函数对象
        :param args: 参数
        :param callback: 回调函数
        :return:
        """
        self.task_add()

        # 将协程注册一个到运行在线程中的循环，thread_loop 会获得一个环任务
        # 注意：run_coroutine_threadsafe 这个方法只能用在运行在线程中的循环事件使用
        # future = asyncio.run_coroutine_threadsafe(func, self.loop)
        future = asyncio.run_coroutine_threadsafe(self.async_semaphore_func(func(*args)), self._loop)

        # 添加回调函数,添加顺序调用
        if 回调函数:
            future.add_done_callback(回调函数)
        future.add_done_callback(self.task_done)

    def 投递任务2(self, func, *args, 回调函数=None):
        """
        阻塞模式
        提交任务到事件循环

        :param func: 异步函数对象
        :param args: 入参
        :param callback: 回调函数
        :return:
        """
        self.task_add()

        # 将协程注册一个到运行在线程中的循环，thread_loop 会获得一个环任务
        # 注意：run_coroutine_threadsafe 这个方法只能用在运行在线程中的循环事件使用

        # future = self._loop.run_in_executor(None, func)
        # future = asyncio.ensure_future(self._loop.run_in_executor(None, func))  # 非阻塞
        future = asyncio.run_coroutine_threadsafe(
            self.async_thread_pool_func(func, *args),
            self._loop)

        # 添加回调函数,添加顺序调用
        if 回调函数:
            future.add_done_callback(回调函数)
        future.add_done_callback(self.task_done)

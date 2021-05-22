import asyncio
import time
from asyncPool import *


async def 工作任务(i):
    await asyncio.sleep(1)
    return i


async def thread_example3(i):
    time.sleep(1)
    await asyncio.sleep(0.1)
    return i


def 工作任务4(i):
    time.sleep(0.01)
    return i


def 接受结果(future):
    result = future.result()
    print('返回值: ', result)


def demo():
    # 任务组， 最大协程数
    pool = 协程池(协程数量=10, 线程池数量=10)

    # 插入任务任务
    for i in range(1000):
        # print(i)
        # 非阻塞协程
        pool.投递任务(工作任务, i, 回调函数=接受结果)
        # 阻塞协程
        # pool.投递任务2(工作任务4, i, 回调函数=接受结果)

    print("等待子线程结束1...")

    # 停止子线程
    pool.释放线程()

    print("等待子线程结束2...")

    # 等待
    pool.等待()

    print("等待子线程结束3...")

    #
    # # 进度条使用
    # while True:
    #     value = pool.task_progress(99)
    #     print("value: ", value)
    #
    #     # 获取线程数
    #     print("running: ", pool.running)
    #
    #     if value == 100:
    #         break
    #
    #     # 获取任务
    #     # print(pool.get_task())
    #     time.sleep(0.5)
    #
    # print("等待子线程结束4...")


if __name__ == '__main__':
    start_time = time.time()
    demo()
    end_time = time.time()
    print("run time: ", end_time - start_time)

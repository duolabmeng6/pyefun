import asyncio
import time
from pyefun.asyncPool.asyncPool import *


async def 任务函数(i):
    time.sleep(0.01)
    return i

def 接收结果(future):
    result = future.result()
    print('返回值: ', result)


def demo():
    # 任务组， 最大协程数
    pool = 协程池(协程数量=10, 线程池数量=10)

    # 插入任务任务
    for i in range(1000):
        # 非阻塞协程
        pool.投递任务(任务函数, i, 回调函数=接收结果)
        # 阻塞协程
        # pool.投递任务2(任务函数, i, 回调函数=接收结果)
    pool.释放线程()
    pool.等待()



if __name__ == '__main__':
    start_time = time.time()
    demo()
    end_time = time.time()
    print("run time: ", end_time - start_time)

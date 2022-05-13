import time
from pyefun.模块.协程池 import *


async def 任务函数(i):
    time.sleep(1)
    return i


def 接收结果(future):
    result = future
    print('返回值: ', result)


def demo():
    # 任务组， 最大协程数
    pool = 协程池(协程数量=10, 线程池数量=1, 投递任务时阻塞=True)

    # 插入任务任务
    for i in range(1000):
        print(i)
        # 非阻塞协程
        task = pool.投递任务(任务函数, i)
        pool.设置任务结束回调函数(task, 接收结果)
        # 阻塞协程
        # task = pool.投递任务2(任务函数, i)
        # pool.设置任务结束回调函数(task, 接收结果)

    pool.释放线程()
    pool.等待()


if __name__ == '__main__':
    start_time = time.time()
    demo()
    end_time = time.time()
    print("run time: ", end_time - start_time)

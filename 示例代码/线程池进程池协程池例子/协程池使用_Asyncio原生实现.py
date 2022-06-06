import time
from pyefun import *
from pyefun.模块.协程池 import *


async def 任务函数(i):
    延时(1)
    return i


def 回调结果(接收参数):
    结果 = 接收参数
    print('返回值: ', 结果)


def 工作任务():
    pool = 协程池(协程数量=10, 线程池数量=1, 投递任务时阻塞=True)
    # 插入任务任务
    for i in range(50):
        print(i)
        # 非阻塞协程
        task = pool.投递任务(任务函数, i)
        pool.设置任务结束回调函数(task, 回调结果)
        # 阻塞协程
        # task = pool.投递任务2(任务函数, i)
        # pool.设置任务结束回调函数(task, 回调结果)

    pool.等待()


if __name__ == '__main__':
    t = 时间统计()
    工作任务()
    print("run time: ", t.取耗时())

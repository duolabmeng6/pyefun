from pyefun.processPoolUtil import *
from pyefun import *


def 任务函数(参数1, 参数2, 参数3):
    延时(1)
    print("参数1 {} 参数2 {} 参数3 {}".format(参数1, 参数2, 参数3))
    return "返回值 {}".format(参数1)


def 任务完成(future):
    pass
    返回结果 = future.result()
    print("任务完成 {}".format(返回结果))


def 模式1_全部任务一次性投递():
    print("==========模式1_全部任务一次性投递==========")
    pool = 线程池(3)
    for i in range(9):
        print("======投递任务 {}".format(i))
        task = pool.投递任务(任务函数, i, "b", "c")
        pool.设置任务结束回调函数(task, 任务完成)
    pool.等待()
    print("========================================")


def 模式2_任务完成后投递():
    print("==========模式2_任务完成后投递==========")
    pool = 线程池(3, 投递任务时阻塞=True)
    for i in range(9):
        print("======投递任务 {}".format(i))
        task = pool.投递任务(任务函数, i, "b", "c")
        pool.设置任务结束回调函数(task, 任务完成)
    pool.等待()
    print("========================================")


if __name__ == "__main__":

    模式1_全部任务一次性投递()

    模式2_任务完成后投递()

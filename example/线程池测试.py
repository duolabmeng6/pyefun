from pyefun.processPoolUtil import *
from pyefun import *


def 任务函数(data):
    # print("data:", data)
    延时(2)
    raise Exception("a")
    return "返回值 %s" % data


def 任务完成(data):
    pass
    # print("任务完成")


if __name__ == "__main__":
    pool = 线程池(4)
    tasks = []
    for i in range(100):
        print(i)
        task = pool.投递任务(任务函数, ("%s" % i))
        pool.设置任务结束回调函数(task, 任务完成)

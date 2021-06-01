from pyefun.processPoolUtil import *
from pyefun import *


def 任务函数(data):
    print("data:", data)
    延时(1)
    return "返回值 %s" % data


if __name__ == "__main__":
    pool = 进程池(4)
    tasks = []
    for i in range(10):
        task = pool.投递任务(任务函数, ("%s" % i,))
        tasks.append(task)

    for task in tasks:
        print(task.get())

    task = pool.投递任务2(任务函数, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(task.get())
    pool.等待()



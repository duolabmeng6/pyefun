from pyefun import *
import asyncio
import time
from pyefun.asyncPool.asyncPool import *


# 这里需要添加关键字 async
async def 任务函数(参数1, 参数2, 参数3):
    延时(1)
    print("参数1 {} 参数2 {} 参数3 {}".format(参数1, 参数2, 参数3))
    return "返回值 {}".format(参数1)


完成数量 = 0


def 任务完成(返回结果):
    global 完成数量
    print("任务完成 {}".format(返回结果))
    完成数量 = 完成数量 + 1


def 模式1_全部任务一次性投递():
    print("==========模式1_全部任务一次性投递==========")
    pool = 协程池(3, False)
    for i in range(9):
        print("======投递任务 {}".format(i))
        task = pool.投递任务(任务函数, 参数1=i, 参数2="b", 参数3="c")
        pool.设置任务结束回调函数(task, 任务完成)
    pool.等待()
    print("========================================")


def 模式2_任务完成后投递():
    global 完成数量
    print("==========模式2_任务完成后投递==========")
    pool = 协程池(3, 投递任务时阻塞=True)
    任务数量 = 9
    进度 = 0
    完成数量 = 0
    for i in range(9):
        print("======投递任务 {}".format(i))
        task = pool.投递任务(任务函数, 参数1=i, 参数2="b", 参数3="c")
        pool.设置任务结束回调函数(task, 任务完成)
        进度 = 四舍五入((完成数量 / 任务数量) * 100, 2)
        print("进度 {}% 任务总数 {} 完成数量 {}".format(进度, 任务数量, 完成数量))
    pool.等待()
    进度 = 四舍五入((完成数量 / 任务数量) * 100, 2)
    print("进度 {}% 任务总数 {} 完成数量 {}".format(进度, 任务数量, 完成数量))
    print("========================================")


if __name__ == "__main__":
    模式1_全部任务一次性投递()
    模式2_任务完成后投递()

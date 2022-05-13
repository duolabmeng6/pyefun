from pyefun import *

@时钟周期事件(时钟周期=1000)
def 定时任务():
    print("定时任务")
    # return True
    return False

定时任务2运行状态 = True

def 定时任务2():
    print(1111111111111,定时任务2运行状态)
    return 定时任务2运行状态
    # return False

时钟(定时任务2, 时钟周期=2000)

@时钟周期事件(时钟周期=5000)
def 定时任务3():
    global 定时任务2运行状态
    print("把时钟停止掉")
    定时任务2运行状态 = False
    return False


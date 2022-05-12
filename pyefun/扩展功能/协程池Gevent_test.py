from pyefun.asyncPoolGevent import *
import time
from pyefun.__init__ import *

def 工作线程4(参数):
    with 时间统计() as t:
        延时(取随机数(4, 4))
        # 延时(取随机数(5, 5))
        print(time.time(),t.取耗时(), 参数, "线程类测试")
        # print(取现行时间(), t.取耗时(), 参数, "线程类测试")

pool = 协程池(协程数量=9)
for i in range(11):
    print("创建任务", i)
    pool.投递任务(工作线程4, i)
pool.等待()
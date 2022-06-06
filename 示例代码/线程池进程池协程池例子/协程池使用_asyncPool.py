from pyefun import *
from pyefun.模块.协程池 import *
import asyncio
async def 工作线程4(参数):
    with 时间统计() as t:
        # 延时(取随机数(4, 4))
        await asyncio.sleep(取随机数(1, 4))
        print(取现行时间(),t.取耗时(), 参数, "线程类测试")

pool = 协程池(协程数量=10,线程池数量=10)
for i in range(11):
    print("创建任务", i)
    pool.投递任务(工作线程4, i)
pool.等待()


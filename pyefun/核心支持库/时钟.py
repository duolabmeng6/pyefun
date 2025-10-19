"""
时钟。

提供基于线程定时器的简单周期任务能力，支持函数调用与装饰器两种用法。

示例:
    @时钟周期事件(时钟周期=1000)
    def 定时任务():
        print("定时任务")
        return False  # 返回 False 可停止继续调度
"""


from threading import Timer



def 时钟(func, 时钟周期):
    """
    启动一个定时器，按周期调用指定函数。

    当被调用的函数返回 False 时，停止继续调度，否则持续按设定周期运行。

    Args:
        func (Callable[[], Any]): 待调用函数。返回 False 停止。
        时钟周期 (int): 周期毫秒数。

    Returns:
        threading.Timer: 启动的首次定时器。
    """
    时钟周期 = int(时钟周期 / 1000)
    def 自调用函数():
        if not func() == False:
            return Timer(时钟周期, 自调用函数).start()
    return Timer(时钟周期, 自调用函数).start()


def 时钟周期事件(*args, **kwargs):
    """
    装饰器：为函数添加周期调用行为。

    用法:
        @时钟周期事件(时钟周期=1000)
        def 定时任务():
            print("定时任务")

    Args:
        时钟周期 (int): 周期毫秒数。

    Returns:
        Callable: 装饰器包装函数。
    """
    def warpp(func):
        时钟(func, kwargs['时钟周期'])
    return warpp

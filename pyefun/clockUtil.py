"""

.. Hint::
    时钟

    易语言的时钟组件

    实现了 时钟周期事件

    使用装饰器设置定时任务 函数内返回 false则停止时钟

.. literalinclude:: ../../../pyefun/clockUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

.. code-block:: python
   :linenos:

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


"""


from threading import Timer



def 时钟(func, 时钟周期):
    """
    时钟 定时调用函数  也可以使用装饰器 @时钟周期事件(时钟周期=1000)

    def 定时任务():
        print("定时任务")
        return False 停止时钟周期事件

    时钟(定时任务, 时钟周期=2000)

    :param func: 运行函数 函数返回false 则停止时钟周期事件
    :param 时钟周期: 毫秒
    """
    时钟周期 = int(时钟周期 / 1000)
    def 自调用函数():
        if not func() == False:
            return Timer(时钟周期, 自调用函数).start()
    return Timer(时钟周期, 自调用函数).start()

def 时钟周期事件(*args, **kwargs):
    """
    装饰器

    @时钟周期事件(时钟周期=1000)
    def 定时任务():
        print("定时任务")
    """
    def warpp(func):
        时钟(func, kwargs['时钟周期'])
    return warpp



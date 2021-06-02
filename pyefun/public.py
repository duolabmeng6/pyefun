"""
.. Hint:: 公用模块
    异常处理等等


.. code-block:: python
   :linenos:

   @异常处理返回类型逻辑型
   def 如果函数发生错误即可提示兵忽略:
        print("没问题")
        a = 0/0 # 这个一定报错


"""
import traceback, datetime

异常显示信息 = True


def 设置_异常处理_显示信息(显示信息=2):
    """

    :param 显示信息: 0 不显示 1显示简单的 2显示详细的
    :return:
    """
    global 异常显示信息
    异常显示信息 = 显示信息


def 异常处理返回类型逻辑型(function):
    """
    使用方法 在def上面加上 @异常处理返回类型逻辑型

    例如

.. code-block:: python
   :linenos:

    @异常处理返回类型逻辑型
    def 如果函数发生错误即可提示兵忽略:
        print("没问题")
        a = 0/0 # 这个一定报错

    """

    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            if 异常显示信息 == 2:
                print("函数异常 %s 时间 %s \r\n%s" % (
                    function.__name__,
                    str(datetime.datetime.now()),
                    traceback.format_exc()
                ))
            if 异常显示信息 == 1:
                print("函数异常 %s 时间 %s" % (
                    function.__name__,
                    str(datetime.datetime.now()),
                ))

            return False

    return box

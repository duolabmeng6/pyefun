# -*- coding:utf-8 -*-
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
    '装饰器'

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

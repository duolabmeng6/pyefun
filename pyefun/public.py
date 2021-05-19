# -*- coding:utf-8 -*-
import traceback, datetime

DEBUG = True
# DEBUG = False


def 异常处理返回类型逻辑型(function):
    '装饰器'

    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            if (DEBUG):
                print("函数异常 %s 时间 %s \r\n%s" % (
                    function.__name__,
                    str(datetime.datetime.now()),
                    traceback.format_exc()
                ))
            return False

    return box

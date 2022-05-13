"""

.. Hint::
    日期时间操作 符合中国人思维逻辑的日期时间操作实用函数


.. literalinclude:: ../../../pyefun/核心支持库/日期时间操作_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import time
import pendulum
import copy
from .文本操作 import *


def 时间_设置语言包(名称="zh"):
    pendulum.set_locale(名称)


# 文档
# https://pendulum.eustace.io/docs/#instantiation
class 日期时间:
    t = pendulum.DateTime

    def __init__(self, str="now"):
        pass
        if (type(str) == int):
            self.t = pendulum.from_timestamp(str, tz='Asia/Shanghai')
        elif (str != ""):
            self.t = pendulum.parse(str)

    def 到文本(self, format="YYYY-MM-DD HH:mm:ss"):
        return self.t.format(format)

    def 取时间戳(self):
        return self.t.int_timestamp

    def 取日期(self):
        return self.t.to_date_string()

    def 取年(self):
        return self.t.year

    def 取月(self):
        return self.t.month

    def 取日(self):
        return self.t.day

    def 取小时(self):
        return self.t.hour

    def 取分钟(self):
        return self.t.minute

    def 取秒(self):
        return self.t.second

    def 取微妙(self):
        return self.t.microsecond

    def 取每周的第几天(self):
        return self.t.day_of_week

    def 取每年的第几天(self):
        return self.t.day_of_year

    def 取每月的第几周(self):
        return self.t.week_of_month

    def 取每年的第几周(self):
        return self.t.week_of_year

    def 取月天数(self):
        return self.t.days_in_month

    def 设置年月日(self, year=None, month=None, day=None):
        self.t = self.t.on(year=int(year), month=int(month), day=int(day))
        return self

    def 设置时分秒(self, hour=0, minute=0, second=0):
        self.t = self.t.at(hour, minute, second)
        return self

    def 增减日期时间(self, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        self.t = self.t.add(years=years,
                            months=months,
                            weeks=weeks,
                            days=days,
                            hours=hours,
                            minutes=minutes,
                            seconds=seconds,
                            )
        return self

    def 取时间间隔(self, datetime):

        d = self.t.diff(datetime, abs=False)
        return {
            "years": d.in_years(),
            "months": d.in_months(),
            "days": d.in_days(),
            "hours": d.in_hours(),
            "minutes": d.in_minutes(),
            "seconds": d.in_seconds(),
            "weeks": d.in_weeks(),
        }

    def 取友好时间(self):
        d = self.t.diff_for_humans()
        return d

    def datetime(self):
        return self.t

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return self.到文本()


def 取现行时间戳():
    return int(time.time())


def 日期到时间戳(str="now"):
    return 日期时间(str).取时间戳()


def 取现行时间():
    t = 日期时间()
    return t


def 取现行时间2(格式, 自定义=False):
    """
    自定义  %Y-%m-%d %H:%M:%S    (yyyy-MM-dd HH:mm:ss)这种格式不可以
    格式1 = 2020-10-09 22:11:52   格式2 = 2020-10-09 格式3= 22:13:37 格式4= 2020年10月17日18时27分40秒

    %a  # 本地(local) 简化星期名称
    %A  # 本地完整星期名称
    %b  # 本地简化月份名称
    %B  # 本地完整月份名称
    %c  # 本地相应的日期和时间表示
    %d  # 一个月中的第几天（01-31）
    %H  # 一天中的第几个小时（24小时制00-23）
    %I  # 第几个小时（12小时制01-12）
    %j  # 一年中的第几天（001-366）
    %m  # 月份（01-12）
    %M  # 分钟数（00-59）
    %p  # 本地am或pm的相应符
    %S  # 秒（01-60）
    %U  # 一年中的星期数。（00-53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第0周
    %w  # 一个星期中的第几天（0-6 0是星期天）
    %W  # 和%U基本相同，不同的是%W以星期一为一个星期的开始
    %x  # 本地相应日期
    %X  # 本地相应时间
    %y  # 去掉世纪的年份（00-99）
    %Y  # 完整的年份
    %z  # 时区的名字
    """
    if 自定义:
        return time.strftime(格式, time.localtime())  # 2020-10-09 22:11:52
    if 格式 == 1:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 2020-10-09 22:11:52
    elif 格式 == 2:
        return time.strftime("%Y-%m-%d", time.localtime())  # 2020-10-09
    elif 格式 == 3:
        return time.strftime("%H:%M:%S", time.localtime())  # 22:13:37
    elif 格式 == 4:
        return time.strftime("%Y{}%m{}%d{}%H{}%M{}%S{}", time.localtime()).format('年', '月', '日', '时', '分',
                                                                                  '秒')  # 2020年10月17日18时27分40秒


def now():
    t = 日期时间()
    return t


def 创建日期时间(timestr):
    t = 日期时间(timestr)
    return t


def 时间迭代(start, end):
    """
    为支持单位range()有：years，months，weeks， days，hours，minutes和seconds
    for i in list.range('months'):
        print(i.to_datetime_string())
    """
    return pendulum.period(pendulum.parse(start), pendulum.parse(end))


def date(format, timestr="now"):
    t = 创建日期时间(timestr)
    format = 子文本替换(format, "Y", str(t.取年()))
    format = 子文本替换(format, "m", str(t.取月()))
    format = 子文本替换(format, "d", str(t.取日()))
    format = 子文本替换(format, "H", str(t.取小时()))
    format = 子文本替换(format, "i", str(t.取分钟()))
    format = 子文本替换(format, "s", str(t.取秒()))
    return format

"""
日期时间操作。

基于 pendulum 提供更贴近中文语义的日期时间类型与函数：创建时间、格式化、取时间戳、增减时间、友好时间描述等。
"""

import time
# import pendulum
import copy

from .公用函数 import _动态导包
from .文本操作 import *


def 时间_设置语言包(名称: str = "zh") -> None:
    """
    设置 pendulum 语言包。

    Args:
        名称 (str, 可选): 语言标识，例如 "zh"、"en"。默认 "zh"。

    Returns:
        None: 无返回值。
    """
    pendulum = _动态导包("pendulum")

    pendulum.set_locale(名称)


# 文档
# https://pendulum.eustace.io/docs/#instantiation
class 日期时间:
    """
    基于 pendulum.DateTime 的日期时间封装。

    支持从时间戳或日期文本构造，提供常用的读取、调整与格式化方法。

    示例:
        t = 日期时间("2020-01-01 12:00:00")
        print(t.到文本())  # 2020-01-01 12:00:00
    """

    pendulum = _动态导包("pendulum")

    t = pendulum.DateTime

    def __init__(self, str="now"):
        """
        构造日期时间对象。

        Args:
            str (Union[str, int]): "now"、可解析的日期文本或 10 位时间戳（秒）。
        """
        pass
        if (type(str) == int):
            self.t = pendulum.from_timestamp(str, tz='Asia/Shanghai')
        elif (str != ""):
            self.t = pendulum.parse(str)

    def 到文本(self, format: str = "YYYY-MM-DD HH:mm:ss") -> str:
        """按指定格式输出文本。"""
        return self.t.format(format)

    def 取时间戳(self) -> int:
        """返回 10 位时间戳（秒）。"""
        return self.t.int_timestamp

    def 取日期(self) -> str:
        """返回日期字符串（YYYY-MM-DD）。"""
        return self.t.to_date_string()

    def 取年(self) -> int:
        """返回年份。"""
        return self.t.year

    def 取月(self) -> int:
        """返回月份。"""
        return self.t.month

    def 取日(self) -> int:
        """返回日。"""
        return self.t.day

    def 取小时(self) -> int:
        """返回小时。"""
        return self.t.hour

    def 取分钟(self) -> int:
        """返回分钟。"""
        return self.t.minute

    def 取秒(self) -> int:
        """返回秒。"""
        return self.t.second

    def 取微妙(self) -> int:
        """返回微秒。"""
        return self.t.microsecond

    def 取每周的第几天(self) -> int:
        """返回每周的第几天（0-6）。"""
        return self.t.day_of_week

    def 取每年的第几天(self) -> int:
        """返回每年的第几天（1-366）。"""
        return self.t.day_of_year

    def 取每月的第几周(self) -> int:
        """返回每月的第几周。"""
        return self.t.week_of_month

    def 取每年的第几周(self) -> int:
        """返回每年的第几周。"""
        return self.t.week_of_year

    def 取月天数(self) -> int:
        """返回当月天数。"""
        return self.t.days_in_month

    def 设置年月日(self, year=None, month=None, day=None):
        """
        设置年月日并返回自身。

        Args:
            year (int, 可选): 年。
            month (int, 可选): 月。
            day (int, 可选): 日。

        Returns:
            日期时间: self。
        """
        self.t = self.t.on(year=int(year), month=int(month), day=int(day))
        return self

    def 设置时分秒(self, hour=0, minute=0, second=0):
        """
        设置时分秒并返回自身。

        Args:
            hour (int, 可选): 小时。
            minute (int, 可选): 分钟。
            second (int, 可选): 秒。

        Returns:
            日期时间: self。
        """
        self.t = self.t.at(hour, minute, second)
        return self

    def 增减日期时间(self, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        """
        调整日期时间，支持增加或减少。

        Args:
            years (int, 可选): 年。
            months (int, 可选): 月。
            weeks (int, 可选): 周。
            days (int, 可选): 天。
            hours (int, 可选): 时。
            minutes (int, 可选): 分。
            seconds (int, 可选): 秒。

        Returns:
            日期时间: self。
        """
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
        """
        获取与另一个时间的间隔信息。

        Args:
            datetime (pendulum.DateTime): 另一个时间对象。

        Returns:
            dict: 包含 years、months、days、hours、minutes、seconds、weeks 的差值。
        """

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

    def 取友好时间(self) -> str:
        """返回如“3 天前”“1 小时后”的友好时间字符串。"""
        d = self.t.diff_for_humans()
        return d

    def datetime(self):
        """返回底层 pendulum.DateTime 对象。"""
        return self.t

    def copy(self):
        """深拷贝当前对象。"""
        return copy.deepcopy(self)

    def __str__(self):
        return self.到文本()


def 取现行时间戳() -> int:
    """返回当前时间的 10 位时间戳（秒）。"""
    return int(time.time())


def 日期到时间戳(str: str = "now") -> int:
    """将日期文本或 "now" 转换为时间戳。"""
    return 日期时间(str).取时间戳()


def 取现行时间():
    """返回当前时间的 日期时间 对象。"""
    t = 日期时间()
    return t


def 取现行时间2(格式, 自定义: bool = False):
    """
    以 time.strftime 风格返回当前时间文本。

    当自定义为 True 时，格式参数为 strftime 格式串，例如 "%Y-%m-%d %H:%M:%S"；
    否则格式为数字：1=YYYY-MM-DD HH:mm:ss，2=YYYY-MM-DD，3=HH:mm:ss，4=YYYY年m月d日H时M分S秒。

    Args:
        格式 (Union[int, str]): 数字格式或自定义格式串。
        自定义 (bool, 可选): 是否启用自定义格式。默认 False。

    Returns:
        str: 格式化后的时间文本。
    """
    # strftime 常用格式说明：
    # %Y-%m-%d %H:%M:%S 等，详见 Python 文档 time.strftime。
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
    """别名：返回当前时间的 日期时间 对象。"""
    t = 日期时间()
    return t


def 创建日期时间(timestr):
    """从时间文本创建 日期时间 对象。"""
    t = 日期时间(timestr)
    return t


def 时间迭代(start, end):
    """
    生成时间区间，用于遍历。

    需安装 pendulum，返回 period 对象，可配合 years/months/weeks/days/hours/minutes/seconds 迭代。

    Args:
        start (str): 起始时间文本。
        end (str): 结束时间文本。

    Returns:
        pendulum.period: 时间区间。
    """
    return pendulum.period(pendulum.parse(start), pendulum.parse(end))


def date(format, timestr="now"):
    """
    以简单占位符格式化日期。

    占位符：Y 年、m 月、d 日、H 时、i 分、s 秒。

    Args:
        format (str): 格式模板，例如 "Y-m-d H:i:s"。
        timestr (str, 可选): 源日期，默认 "now"。

    Returns:
        str: 格式化结果。
    """
    t = 创建日期时间(timestr)
    format = 子文本替换(format, "Y", str(t.取年()))
    format = 子文本替换(format, "m", str(t.取月()))
    format = 子文本替换(format, "d", str(t.取日()))
    format = 子文本替换(format, "H", str(t.取小时()))
    format = 子文本替换(format, "i", str(t.取分钟()))
    format = 子文本替换(format, "s", str(t.取秒()))
    return format

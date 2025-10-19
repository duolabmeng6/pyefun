"""
日期时间操作模块的单元测试。

涵盖日期时间创建、格式化、增减、间隔与友好时间等用例。
"""
import unittest

from .日期时间操作 import *


class Test日期时间操作(unittest.TestCase):
    """日期时间操作相关测试用例。"""

    def test_1(self):
        """
        test_1 的功能说明（请补充）。

        """
        pass
        t = 取现行时间()
        print(t)
        print(t.到文本("YYYY年MM月DD日 HH时mm分ss秒"))
        print(t.到文本())
        print("取年", t.取年())
        print("取月", t.取月())
        print("取日", t.取日())
        print("取小时", t.取小时())
        print("取分钟", t.取分钟())
        print("取秒", t.取秒())
        print("取微妙", t.取微妙())
        print("取每周的第几天", t.取每周的第几天())
        print("取每年的第几周", t.取每年的第几周())
        print("取每年的第几天", t.取每年的第几天())
        print("取每月的第几周", t.取每月的第几周())
        print("取日期", t.取日期())
        t.设置年月日(2020, 1, 1)
        print(t.到文本())
        t.设置时分秒(1, 1, 1)
        print(t.到文本())
        t = t.增减日期时间(
            years=1,
            months=1,
            days=1,
            hours=1,
            minutes=1,
            seconds=1,
        )
        print("增减日期时间", t.到文本())

        t1 = 取现行时间()
        t2 = t1.copy()
        print("取现行时间", t1.到文本())
        t2 = t2.增减日期时间(
            years=1,
            months=1,
            days=1,
            hours=1,
            minutes=1,
            seconds=1,
        ).datetime()
        print("t2", t2)
        print("t1", t1)
        print("取时间间隔", t1.取时间间隔(t2))

        t2 = 取现行时间()
        t2 = t2.增减日期时间(
            years=-1,
            months=1,
            days=1,
            hours=1,
            minutes=1,
            seconds=1,
        )
        print("取友好时间", t2.取友好时间())

        t = 取现行时间().取时间戳()
        print(t)


        t = 日期时间("2021-05-17 12:01:42").取时间戳()
        print(t)

        t = 日期到时间戳("2021-05-17 12:01:42")
        print(t)

    def test_2(self):
        """
        test_2 的功能说明（请补充）。

        """
        list = 时间迭代("2021-01-17", "2021-05-27")
        for i in list.range('months'):
            print(i.to_datetime_string())

        # for i in list.range('days'):
        #     print(i.to_datetime_string())

    def test_3(self):
        """
        test_3 的功能说明（请补充）。

        """
        data = date("Y-m-d H:i:s", now().取时间戳())
        print(data)
    def test_4(self):
        """
        test_4 的功能说明（请补充）。

        """
        print(取现行时间2('%d %H:%M:%S',True))

    def test_5(self):
        """
        test_5 的功能说明（请补充）。

        """
        t = 日期时间(取现行时间戳())
        print(t)
        print(t.取时间戳())

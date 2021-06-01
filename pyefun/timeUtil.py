"""
时间工具类

时间统计
"""
import datetime
import time
import sys
from .arithmeticOperationBase import *
from ubelt import *
import ubelt as ub
from collections import OrderedDict


class 时间统计():
    """
    计时器，对于需要计时的代码进行with操作：
    with 计时器() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self, 名称=""):
        self.开始()
        self.名称 = 名称
        self.zstart = self.start
        if self.名称:
            print("时间统计: %s 开始 %s" % (self.名称, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def __enter__(self):
        return self

    def 开始(self):
        """
        重新计算开始时间
        """
        self.start = time.perf_counter()

    def 取耗时(self, 名称=""):
        """
        每次计时后重置 如果需要总耗时的话 取总耗时() 即可
        """
        self.end = time.perf_counter()
        self.ms = int((self.end - self.start) * 1000)
        self.开始()
        if 名称 != "":
            print("时间统计: %s %s %sms" % (self.名称, 名称, self.ms))
        elif self.名称 != "":
            print("时间统计: %s %sms" % (self.名称, self.ms))

        return self.ms

    def 取总耗时(self):
        """
        自对象创建以来的总耗时
        """
        self.end = time.perf_counter()
        self.ms = int((self.end - self.zstart) * 1000)
        return self.ms

    def 取毫秒(self):
        return self.取耗时()

    def 取秒(self):
        return self.取耗时() / 1000

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.名称 != "":
            print("时间统计: %s 结束 %sms %s" % (self.名称, self.取总耗时(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return exc_type is None


def 计时器():
    return 时间统计()


class 计时统计(ub.Timerit):
    """
    计代码块的平均时间
    """

    def __init__(self, 次数=1, 标签=None, 取样=3, 单位=None, 显示信息=None):
        self.t = super().__init__(次数, 标签, 取样, 单位, 显示信息)

    def 取耗时(self):
        return self.total_time

    def report(self, verbose=1):
        """
        Creates a human readable report

        Args:
            verbose (int): verbosity level. Either 1, 2, or 3.

        Returns:
            str: the report

        SeeAlso:
            :func:`Timerit.print`

        Example:
            >>> import math
            >>> ti = Timerit(num=1).call(math.factorial, 5)
            >>> print(ti.report(verbose=1))
            Timed best=...s, mean=...s
        """
        lines = []
        if verbose >= 2:
            # use a multi-line format for high verbosity
            lines.append(self._status_line(tense='past'))
            if verbose >= 3:
                unit, mag = _choose_unit(self.total_time, self.unit,
                                         self._asciimode)
                lines.append('    总耗时: {total:.{pr}{t}} {unit}'.format(
                    total=self.total_time / mag,
                    t=self._precision_type,
                    pr=self._precision, unit=unit))
            lines.append('    统计每次时间: {}'.format(self._seconds_str()))
        else:
            # use a single-line format for low verbosity
            line = 'Timed ' + self._seconds_str()
            if self.label:
                line += ' for ' + self.label
            lines.append(line)
        text = '\n'.join(lines)
        return text

    def _seconds_str(self):
        """
        Returns:
            str: human readable text

        Example:
            >>> self = Timerit(num=100, bestof=10, verbose=0)
            >>> self.call(lambda : sum(range(100)))
            >>> print(self._seconds_str())
            ... 'best=3.423 µs, ave=3.451 ± 0.027 µs'
        """
        mean = self.mean()
        unit, mag = _choose_unit(mean, self.unit, self._asciimode)

        unit_min = self.min() / mag
        unit_mean = mean / mag

        # Is showing the std useful? It probably doesn't hurt.
        std = self.std()
        unit_std = std / mag
        pm = _trychar('±', '+-', self._asciimode)
        fmtstr = ('最佳={min:.{pr1}{t}} {unit}, '
                  '平均={mean:.{pr1}{t}} {pm} {std:.{pr2}{t}} {unit}')
        pr1 = pr2 = self._precision
        if isinstance(self._precision, int):  # pragma: nobranch
            pr2 = max(self._precision - 2, 1)
        unit_str = fmtstr.format(min=unit_min, unit=unit, mean=unit_mean,
                                 t=self._precision_type, pm=pm, std=unit_std,
                                 pr1=pr1, pr2=pr2)
        return unit_str

    def _status_line(self, tense='past'):
        """
        Text indicating what has been / is being done.

        Example:
            >>> print(Timerit()._status_line(tense='past'))
            Timed for: 1 loops, best of 1
            >>> print(Timerit()._status_line(tense='present'))
            Timing for: 1 loops, best of 1
        """
        action = {'past': '计时统计', 'present': '计时开始'}[tense]
        line = '{action} {label}次数: {num:d} 循环, 取样 {bestof:d}'.format(
            label=self.label + ' ' if self.label else '',
            action=action, num=self.num, bestof=min(self.bestof, self.num))
        return line


# 还没我封装的好使呢...
# class 计时(ub.Timer):
#     def __init__(self, label='', verbose=None, newline=True):
#         self.t = super().__init__(label, verbose, newline)
#     def 取耗时(self):
#         return self.elapsed
#
#     def 开始(self):
#         return self.tic()
#     def 启动(self):
#         return self.tic()
#     def 停止(self):
#         return self.toc()
#     def 完成(self):
#         return self.toc()


def _trychar(char, fallback, asciimode=None):
    """
    Logic from IPython timeit to handle terminals that cant show mu

    Args:
        char (str): character, typically unicode, to try to use
        fallback (str): ascii character to use if stdout cannot encode char
        asciimode (bool): if True, always use fallback

    Example:
        >>> char = _trychar('µs', 'us')
        >>> print('char = {}'.format(char))
        >>> assert _trychar('µs', 'us', asciimode=True) == 'us'

    """
    if asciimode is True:
        # If we request ascii mode simply return it
        return fallback
    if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding:  # pragma: nobranch
        try:
            char.encode(sys.stdout.encoding)
        except Exception:  # nocover
            pass
        else:
            return char
    return fallback  # nocover


def _choose_unit(value, unit=None, asciimode=None):
    """
    Finds a good unit to print seconds in

    Args:
        value (float): measured value in seconds
        unit (str): if specified, overrides heuristic decision
        asciimode (bool): if True, forces ascii for microseconds

    Returns:
        tuple[(str, float)]: suffix, mag:
            string suffix and conversion factor

    Example:
        >>> assert _choose_unit(1.1, unit=None)[0] == 's'
        >>> assert _choose_unit(1e-2, unit=None)[0] == 'ms'
        >>> assert _choose_unit(1e-4, unit=None, asciimode=True)[0] == 'us'
        >>> assert _choose_unit(1.1, unit='ns')[0] == 'ns'
    """
    micro = _trychar('µs', 'us', asciimode)
    units = OrderedDict([
        ('s', ('s', 1e0)),
        ('ms', ('ms', 1e-3)),
        ('us', (micro, 1e-6)),
        ('ns', ('ns', 1e-9)),
    ])
    if unit is None:
        for suffix, mag in units.values():  # pragma: nobranch
            if value > mag:
                break
    else:
        suffix, mag = units[unit]
    return suffix, mag

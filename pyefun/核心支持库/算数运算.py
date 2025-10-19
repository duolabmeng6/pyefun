"""
算数运算。

对 Python 常用数学函数的中文封装，包括四舍五入、绝对值、取整、幂函数、三角函数、随机数、取整等。
"""

import math
import random


def 四舍五入(欲被四舍五入的数值: float, 被舍入的位置: int):
    """
    对数值按指定位置进行四舍五入。

    Args:
        欲被四舍五入的数值 (float): 待处理的小数。
        被舍入的位置 (int): 0 表示到整数；>0 表示小数点右边保留位数；<0 表示小数点左侧舍入位置。

    Returns:
        float: 四舍五入后的数值。
    """
    return round(欲被四舍五入的数值, 被舍入的位置)


def 取绝对值(双精度小数型: float):
    """返回数值的绝对值。"""
    return abs(双精度小数型)


def 取整(value):
    """
    取小数的整数部分（向下取整到不大于该数的整数）。

    说明：不同于“绝对取整”，负数将向更小的整数取整，例如 -7.8 -> -8。

    Args:
        value (float): 待处理小数。

    Returns:
        int: 整数部分。
    """
    return int(value)


def 求次方(欲求次方数值: float, 次方数: float):
    """
    计算 a 的 b 次方。

    Args:
        欲求次方数值 (float): a。
        次方数 (float): b。

    Returns:
        float: a ** b。
    """
    return pow(欲求次方数值, 次方数)


def 求平方根(欲求次方数值: float):
    """
    返回指定参数的平方根。

    Args:
        欲求次方数值 (float): 待开方的非负数。

    Returns:
        float: 平方根。
    """
    return math.sqrt(欲求次方数值)


def 求正弦(欲进行计算的角: float):
    """
    求角度（弧度制）的正弦值。

    Args:
        欲进行计算的角 (float): 弧度。

    Returns:
        float: 正弦值。
    """
    return math.sin(欲进行计算的角)


def 求余弦(欲进行计算的角: float):
    """
    求角度（弧度制）的余弦值。

    Args:
        欲进行计算的角 (float): 弧度。

    Returns:
        float: 余弦值。
    """
    return math.cos(欲进行计算的角)


def 求正切(欲进行计算的角: float):
    """
    求角度（弧度制）的正切值。

    Args:
        欲进行计算的角 (float): 弧度。

    Returns:
        float: 正切值。
    """
    return math.tan(欲进行计算的角)


def 求反正切(欲求其反正切值的数值: float):
    """
    求反正切值。

    Args:
        欲求其反正切值的数值 (float): 值。

    Returns:
        float: 反正切结果（弧度）。
    """
    return math.atan(欲求其反正切值的数值)


def 置随机数种子(欲置入的种子数值):
    """
    初始化随机数种子。

    Args:
        欲置入的种子数值 (int): 种子值。若省略使用系统时间。
    """
    random.seed()


def 取随机数(欲取随机数的最小值: int, 欲取随机数的最大值: int):
    """
    返回指定范围内的随机整数。

    Args:
        欲取随机数的最小值 (int): 下界（包含）。
        欲取随机数的最大值 (int): 上界（包含）。

    Returns:
        int: 随机整数。
    """
    return random.randint(欲取随机数的最小值, 欲取随机数的最大值)


def 保留位数(数值, 位数=2):
    """
    保留小数点后指定位数（四舍五入显示）。

    Args:
        数值 (float): 待格式化数值，如 1.12345。
        位数 (int, 可选): 保留位数，默认 2。

    Returns:
        str: 字符串形式的格式化结果，例如 '1.12'。
    """
    return format(数值, '.{}f'.format(位数))


def 取最小数(数值列表):
    """
    返回列表中的最小值。

    Args:
        数值列表 (Iterable[Number]): 数值序列。

    Returns:
        Number: 最小值。
    """
    return min(数值列表)


def 取最大数(数值列表):
    """
    返回列表中的最大值。

    Args:
        数值列表 (Iterable[Number]): 数值序列。

    Returns:
        Number: 最大值。
    """

    return max(数值列表)


def 向下取整(数值):
    """
    向下取整。

    示例: 1.9 -> 1。

    Args:
        数值 (float): 浮点数。

    Returns:
        int: 向下取整结果。
    """
    return math.floor(数值)


def 向上取整(数值):
    """
    向上取整。

    示例: 1.1 -> 2。

    Args:
        数值 (float): 浮点数。

    Returns:
        int: 向上取整结果。
    """
    return math.ceil(数值)


def 取整数(val):
    """
    将小数或字符串表示的小数转为整数（取整）。

    示例: '8852791.5' -> 8852791。

    Args:
        val (str | float): 待转换值。

    Returns:
        int: 转换后的整数。
    """
    return int(float(val))

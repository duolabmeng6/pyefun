"""
数组操作。

提供列表与字典的常用便捷操作，以及简单的排序、取值与随机抽样工具函数。

示例:
    from pyefun.核心支持库.数组操作 import 数组

    arr = 数组([1, 3, 2])
    arr.从小到大()
    print(arr.取所有成员())  # [1, 2, 3]
"""
import random


class 数组:
    """
    封装 Python 列表的常用操作。

    Attributes:
        val (list): 内部存储的列表副本。
    """

    def __init__(self, data: list = []):
        """
        初始化数组。

        Args:
            data (list, 可选): 初始成员，可迭代对象将被复制为列表。默认空列表。
        """
        self.val = list(data)

    def 加入成员(self, object):
        """
        追加一个成员到末尾。

        Args:
            object (Any): 待追加的成员。
        """
        self.val.append(object)

    def 统计成员次数(self, object):
        """
        统计成员在数组中出现的次数。

        Args:
            object (Any): 目标成员。

        Returns:
            int: 出现次数。
        """
        return self.val.count(object)

    def 查找成员(self, object):
        """
        查找成员首次出现的位置。

        Args:
            object (Any): 目标成员。

        Returns:
            int: 成员索引，若不存在将抛出 ValueError。
        """
        return self.val.index(object)

    def 弹出成员(self, index: int = -1):
        """
        弹出并返回指定位置的成员。

        Args:
            index (int, 可选): 索引，默认 -1 表示最后一个。

        Returns:
            Any: 被移除的成员。
        """
        return self.val.pop(index)

    def 插入成员(self, object, index: int = -1):
        """
        在指定位置插入成员。

        Args:
            object (Any): 待插入的成员。
            index (int, 可选): 插入位置，默认 -1（末尾前一个位置的语义与 list.insert 一致）。
        """
        self.val.insert(index, object)

    def 移除成员(self, object):
        """
        删除数组中第一个等于该对象的成员。

        Args:
            object (Any): 目标成员。
        """
        self.val.remove(object)

    def 翻转(self):
        """原地反转数组。"""
        self.val.reverse()

    def 排序(self, **kwargs):
        """
        使用 list.sort 进行排序。

        Args:
            **kwargs: 透传给 list.sort 的参数，如 key、reverse 等。
        """
        # cmp=None, key=None, reverse=False
        # cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
        # key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        # reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
        self.val.sort(**kwargs)

    def 从大到小(self, 下标=0):
        """
        按成员或其子成员从大到小排序。

        Args:
            下标 (int, 可选): 当成员为元组/列表时，按该下标的值排序。默认 0。
        """
        pass
        self.排序(reverse=True, key=lambda d: _func_key(d, 下标))

    def 从小到大(self, 下标=0):
        """
        按成员或其子成员从小到大排序。

        Args:
            下标 (int, 可选): 当成员为元组/列表时，按该下标的值排序。默认 0。
        """
        self.排序(reverse=False, key=lambda d: _func_key(d, 下标))

    def 取所有成员(self):
        """返回内部列表。"""
        return self.val

    def 清空(self):
        """清空所有成员。"""
        self.val = []


def _func_key(d, 下标=0):
    """
    排序辅助：当元素为序列时取其指定下标，否则返回元素本身。

    Args:
        d (Any): 待处理元素。
        下标 (int, 可选): 目标下标。默认 0。

    Returns:
        Any: 用于比较的键值。
    """
    if (type(d) == tuple):
        return d[下标]
    return d


def 字典_取值并删除(字典, 键, 失败返回值=None):
    """
    从字典中取值并删除该键。

    Args:
        字典 (dict): 目标字典。
        键 (Any): 键。
        失败返回值 (Any, 可选): 当键不存在时返回该值。默认 None。

    Returns:
        Any: 取到的值或失败返回值。
    """
    return 字典.pop(键, 失败返回值)


def 字典_取指定键值(字典, 键, 失败返回值=None):
    """
    从字典中取指定键的值。

    Args:
        字典 (dict): 目标字典。
        键 (Any): 键。
        失败返回值 (Any, 可选): 未找到时返回。默认 None。

    Returns:
        Any: 对应的值或失败返回值。
    """
    return 字典.get(键, 失败返回值)


def 字典_清空(字典):
    """
    清空字典。

    Args:
        字典 (dict): 目标字典。

    Returns:
        bool: 成功返回 True。
    """
    字典.clear()
    return True


def 字典_拷贝(新字典, 原字典):
    """
    将原字典浅拷贝到新字典变量。

    说明：Python 赋值是引用，copy 可获得副本。

    Args:
        新字典 (dict): 目标变量名（占位）。
        原字典 (dict): 源字典。

    Returns:
        bool: 成功返回 True。
    """
    新字典 = 原字典.copy()
    return True


def 字典_生成(键值列表, 键值):
    """
    根据键列表创建字典，值统一为给定键值。

    Args:
        键值列表 (Iterable): 键集合。
        键值 (Any): 初始值。

    Returns:
        dict: 新字典。
    """
    return dict.fromkeys(键值列表, 键值)


def 字典_转列表(字典):
    """
    将字典转换为列表形式。

    Returns:
        list[tuple]: 例如 [(k1, v1), (k2, v2)]。
    """
    return list(字典.items())


def 字典_取全部键(字典):
    """返回所有键列表。"""
    return list(字典.keys())


def 字典_取全部值(字典):
    """返回所有值列表。"""
    return list(字典.values())


def 字典_取出并删除最后键值(字典):
    """
    删除并返回最后一个键值对。

    Returns:
        tuple: (键, 值)。
    """
    return 字典.popitem()


def 字典_取值添加(字典, 键, 值=None):
    """
    获取键对应的值，不存在则设置为默认值并返回。

    Args:
        字典 (dict): 目标字典。
        键 (Any): 键。
        值 (Any, 可选): 默认值。默认 None。

    Returns:
        Any: 对应的值。
    """
    return 字典.setdefault(键, 值)


def 列表_转字典(列表):
    """
    将 [(k, v), ...] 转为 {k: v, ...}。

    Args:
        列表 (Iterable[tuple]): 键值二元组序列。

    Returns:
        dict: 合并后的字典。
    """
    字典 = dict()
    for x in 列表: 字典[x[0]] = x[1]
    return 字典


def 列表_合并为字典(列表1, 列表2):
    """
    将两个列表按位置合并成字典。

    Args:
        列表1 (Iterable): 键列表。
        列表2 (Iterable): 值列表。

    Returns:
        dict: 合并后的字典。
    """
    return dict(zip(列表1, 列表2))


def 列表_加入成员(列表, 值):
    """
    在列表尾部追加成员。

    Args:
        列表 (list): 目标列表。
        值 (Any): 成员。

    Returns:
        bool: 成功返回 True。
    """
    列表.append(值)
    return True


def 列表_插入成员(列表, 位置, 值):
    """
    在指定索引插入成员。

    Args:
        列表 (list): 目标列表。
        位置 (int): 插入索引。
        值 (Any): 成员。

    Returns:
        bool: 成功返回 True。
    """
    列表.insert(位置, 值)
    return True


def 列表_取出现次数(列表, 值):
    """
    统计成员在列表中出现次数。

    Args:
        列表 (list): 目标列表。
        值 (Any): 成员。

    Returns:
        int: 次数。
    """
    return 列表.count(值)


def 列表_合并列表(列表, 新列表):
    """
    扩展列表，将新列表成员追加到末尾。

    Args:
        列表 (list): 目标列表。
        新列表 (Iterable): 待追加的序列。

    Returns:
        bool: 成功返回 True。
    """
    列表.extend(新列表)
    return True


def 列表_查找成员位置(列表, 值):
    """返回成员首次出现的索引。"""
    return 列表.index(值)


def 列表_取值并删除(列表, 位置=None):
    """
    取出指定位置成员并删除它。

    Args:
        列表 (list): 目标列表。
        位置 (int, 可选): 索引，None 表示最后一个。

    Returns:
        Any: 被删除的成员。
    """
    if 位置 == None:
        return 列表.pop()
    else:
        return 列表.pop(位置)


def 列表_删除指定值(列表, 值):
    """
    删除列表中第一个等于该值的成员。

    Args:
        列表 (list): 目标列表。
        值 (Any): 目标值。

    Returns:
        bool: 成功返回 True。
    """
    列表.remove(值)
    return True


def 列表_倒序排列(列表):
    """
    将列表成员按相反顺序排列。

    Returns:
        bool: 成功返回 True。
    """
    列表.reverse()
    return True


def 列表_大小排序(列表, 排序方式=False):
    """
    将列表按大小排序。

    Args:
        列表 (list): 目标列表，仅支持可比较的元素。
        排序方式 (bool, 可选): True 为从大到小，False 为从小到大（默认）。

    Returns:
        bool: 成功返回 True。
    """
    列表.sort(reverse=排序方式)
    return True


def 数组_按成员长度排序(数组):
    """
    根据成员长度排序，长度更长的靠前。

    Args:
        数组 (Iterable): 可迭代对象，其成员支持 len()。

    Returns:
        list: 排序后的新列表。
    """
    return sorted(数组, key=lambda i: len(i), reverse=True)


def 数组_按子成员大小排序(数组, 成员索引):
    """
    对二维数组或成员为序列的数组按指定子成员排序。

    Args:
        数组 (Iterable): 成员为序列的可迭代对象。
        成员索引 (int): 作为键的下标。

    Returns:
        list: 排序后的新列表。
    """
    return sorted(数组, key=lambda i: i[成员索引])


def 数组_取随机成员数组(数组, 数量):
    """
    从数组中随机取出指定数量的成员组成新数组。

    Args:
        数组 (Sequence): 源数组。
        数量 (int): 需要抽取的个数。

    Returns:
        list: 随机成员列表。
    """
    return random.sample(数组, 数量)


def 数组_取随机成员(数组):
    """
    从数组中随机取出一个成员。

    Args:
        数组 (Sequence): 源数组。

    Returns:
        Any: 随机成员。
    """
    return random.choice(数组)

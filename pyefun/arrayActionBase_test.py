import unittest

from .arithmeticOperationBase import *
from .arrayActionBase import *
from .stringBase import *


class TestDirk(unittest.TestCase):

    def test_1(self):
        pass
        # arr = 数组(["a", "b", "c"])
        # arr.加入成员("a")
        arr = 数组()
        for i in range(10):
            arr.加入成员(取随机数(1, 100))

        print(arr.取所有成员())
        arr.排序(reverse=False)
        print(arr.取所有成员())
        arr.排序(reverse=True)
        print(arr.取所有成员())

        arr2 = 数组()
        print("arr2???", arr2.取所有成员())

        for i in range(10):
            arr2.加入成员((取随机数(1, 100), 字符(65 + i)))

        print(arr2.取所有成员())
        arr2.排序(reverse=False)
        print(arr2.取所有成员())
        # arr2.排序(reverse=True,)
        arr2.排序(reverse=True, key=lambda d: d[0])
        print(arr2.取所有成员())

    def test_2(self):
        arr = 数组([1, 2, 3, 4, 5, 0, 0, 0])
        arr.加入成员(6)
        arr.插入成员(0, 2)
        print(arr.取所有成员())

        data = arr.统计成员次数(0)
        print(data)

        data = arr.查找成员(3)
        print(data)
        print(arr.取所有成员())
        data = arr.弹出成员()
        print(data)
        print(arr.取所有成员())
        arr.移除成员(2)
        print(arr.取所有成员())

        arr.翻转()
        print(arr.取所有成员())

        arr.清空()
        print(arr.取所有成员())

    def test_3(self):
        # arr = 数组(["a", "b", "c"])
        # arr.加入成员("a")
        arr = 数组()
        for i in range(10):
            arr.加入成员(取随机数(1, 100))

        print(arr.取所有成员())
        arr.从大到小()
        print(arr.取所有成员())
        arr.从小到大()
        print(arr.取所有成员())

        arr2 = 数组()
        print("arr2???", arr2.取所有成员())

        for i in range(10):
            arr2.加入成员((取随机数(1, 100), 取随机数(1, 100),str(取随机数(1, 100)), 字符(65 + i)))
        print(arr2.取所有成员())
        arr2.从大到小(0)
        print(arr2.取所有成员())
        # arr2.排序(reverse=True,)
        arr2.从小到大(2)
        print(arr2.取所有成员())
        arr2.从小到大(3)
        print(arr2.取所有成员())
        arr2.从大到小(3)
        print(arr2.取所有成员())
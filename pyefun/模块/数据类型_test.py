import unittest

from .数据类型 import *


class Test数据类型(unittest.TestCase):

    def test_数据类型(self):
        """
        test_数据类型 的功能说明（请补充）。

        """
        my_dict = 有序字典()
        my_dict['a'] = 1
        my_dict['b'] = 2
        my_dict['c'] = 3
        for key, value in my_dict.items():
            print("{}: {}".format(key, value))


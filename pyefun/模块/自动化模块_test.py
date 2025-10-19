import unittest

import pyautogui
from pyefun.模块.自动化模块 import *


class Test自动化操作(unittest.TestCase):
    def test_1(self):
        auto = 自动化模块()
        鼠标位置 = auto.获取当前鼠标位置()
        print(鼠标位置)
        鼠标位置 = auto.截图(r"C:\pyefun\pyefun\a\1.png", (0, 0, 300, 300))
        图片位置 = auto.找图(r"C:\pyefun\pyefun\a\1.png")
        print(图片位置)
        图片中心点位置 = auto.获取中心点位置(图片位置)
        print(图片中心点位置)

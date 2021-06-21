import unittest

from .imageUtil import *
from .__init__ import *
from .commonlyUtil import *
from PIL import Image


class TestImageUtil(unittest.TestCase):

    def test_1(self):
        pass
        文件路径 = 路径_合并(取运行目录(), r"example\wxefun\2.png")
        # print(文件路径)
        字节集 = 读入文件(文件路径)
        print(len(字节集))

        im = image从字节集加载(字节集)
        # print(im)
        # im.show()
        字节集 = image到字节集(im)
        print(len(字节集))


        im = image从字节集加载(字节集)
        # print(im)
        # im.show()
        字节集 = image到字节集(im)
        print(len(字节集))

        print(image取图片宽度高度(im))

        # image显示图片(im)

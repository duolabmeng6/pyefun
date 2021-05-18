import unittest
from .commonlyUtil import *
from core.dirkBase import *


class TestcommonlyUtil(unittest.TestCase):

    def test_1(self):
        pass
        data = 取哈希("abc")
        print(data)

        写到文件("sha1.txt", "abc")
        data = 取文件哈希("sha1.txt")
        print(data)

    def test_2(self):
        pass
        data = 运行命令("ipconfig")
        print(data)

    def test_3(self):
        pass
        data = 取缓存目录("app")
        print(data)

    def test_4(self):
        pass
        # data = 下载文件("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", 取运行目录() + "/1.png")
        # print(data)

        data = 下载文件缓存("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", 取运行目录() + "/1.png")
        print(data)

    def test_5(self):
        选项 = ['ham', 'jam', 'spam', 'eggs', 'cheese', 'bannana']
        分组 = ['protein', 'fruit', 'protein', 'protein', 'dairy', 'fruit']
        data = 字典_分组(选项, 分组)
        print(data)

        items = [1, 2, 39, 900, 1232, 900, 1232, 2, 2, 2, 900]
        data = 字典_统计(items)
        print(data)

        dict_ = {'K': 3, 'dcvs_clip_max': 0.2, 'p': 0.1}
        subdict_ = 字典_取子集(dict_, ['K', 'dcvs_clip_max'])
        print(subdict_)

        dict_ = {1: 'a', 2: 'b', 3: 'c'}
        print(字典_取值(dict_, [1, 2, 3, 4, 5]))

        dict_ = {'a': [1, 2, 3], 'b': [], 'c': [4, 5, 6]}
        newdict = 字典_根据健重建值(len, dict_)
        print(newdict)

        mapping = {'a': 0, 'A': 1, 'b': 1, 'c': 2, 'C': 2, 'd': 3}
        data = 字典_健值交换(mapping)
        print(data)

        mapping = {'a': 0, 'A': 1, 'b': 1, 'c': 2, 'C': 2, 'd': 3}
        data = 字典_健值交换(mapping, False)
        print(data)

    def test2(self):
        auto = 灵活字典()
        print('auto = {!r}'.format(auto))
        auto[0][10][100] = None
        print('auto = {!r}'.format(auto))
        auto[0][1] = 'hello'
        print('auto = {!r}'.format(auto))
        auto[0][100][1] = 'hello'
        print('auto = {!r}'.format(auto))

    def test3(self):
        写到文件(取运行目录() + r"/test/__init__.py","""
def test():
    print("动态导入的包")
        """)

        data = 导入包_从路径(取运行目录() + r"/test/")
        print(data)
        data.test()


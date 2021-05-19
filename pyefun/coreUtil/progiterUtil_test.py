import unittest

from .progiterUtil import *
import ubelt as ub


class TestOftenUtil(unittest.TestCase):

    def test_cache_1(self):
        cfgstr = 'repr-of-params-that-uniquely-determine-the-process'
        cacher = ub.Cacher('test_process', cfgstr)
        data = cacher.tryload()
        if data is None:
            myvar1 = 'result of expensive process'
            myvar2 = 'another result'
            data = myvar1, myvar2
            cacher.save(data)
        myvar1, myvar2 = data










    def test_3(self):
        pass
        data = {
            'custom_types': [slice(0, 1, None), 1 / 3],
            'nest_dict': {'k1': [1, 2, {3: {4, 5}}],
                          'key2': [1, 2, {3: {4, 5}}],
                          'key3': [1, 2, {3: {4, 5}}],
                          },
            'nest_dict2': {'k': [1, 2, {3: {4, 5}}]},
            'nested_tuples': [tuple([1]), tuple([2, 3]), frozenset([4, 5, 6])],
            'one_tup': tuple([1]),
            'simple_dict': {'spam': 'eggs', 'ham': 'jam'},
            'simple_list': [1, 2, 'red', 'blue'],
        }
        调试输出(data)


    def test_6(self):
        # a = ["a", "b", "c", "d", "e"]
        # prog = ProgIter(iter(a), desc="描述", show_times=False, verbose=3)
        # for n in prog:
        #     pass
        #     prog.set_extra('进度 num {}'.format(n))

        进度 = 进度显示(起始索引=0, 总数=100, 描述="枚举", 启用=False, 信息级别=3, 显示速率=True, 显示时间=True, 进度大小=10)
        进度.开始()
        for n in range(100):
            进度.下一步()
            # 延时(1)
            # print(n,进度.取进度())
        进度.完成()

    def test_7(self):
        p = 进度显示(range(100), 描述="进度", 信息级别=3)
        for n in p:
            pass
            p.附加输出("n=" + str(n))

    def test_8(self):
        for n in 进度显示(range(100), "进度", 信息级别=3):
            pass

    def test_9(self):
        for n in 进度显示(iter(["a", "b", "c", "d", "e", "f"]), "字母", 信息级别=3):
            pass
            print(n)

        p = 进度显示(iter(["a", "b", "c", "d", "e", "f"]), "字母", 信息级别=3)
        for n in p:
            pass
            p.附加输出("n=" + str(n))

    def test_10(self):
        for n in 进度显示(iter(["a", "b", "c", "d", "e", "f"]), "字母"):
            pass
            print(n)

    def test_101(self):
        for n in 进度显示(iter(["a", "b", "c", "d", "e", "f"]), "字母", 进度大小=2):
            pass
            print(n)

    def test_11(self):

        进度 = 进度显示(None, "下载", 100)
        进度.开始()
        for n in range(100):
            进度.下一步()
            # 延时(1)
            # print(n,进度.取进度())
        进度.完成()

        进度 = 进度显示(总数=100, 起始索引=0, 描述="进度")
        进度.开始()
        for n in range(100):
            进度.下一步()
            # 延时(1)
            # print(n,进度.取进度())
        进度.完成()

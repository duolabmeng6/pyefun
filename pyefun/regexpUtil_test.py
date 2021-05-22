import unittest

from .regexpUtil import *
import ubelt as ub


class TestRegexpUtil(unittest.TestCase):

    def test1(self):
        # 精易模块的实现方式
        pass
        str = r"""
        
aaa111bbb444ccc
aaa222bbb555ccc
aaa333bbb666ccc
        """
        zz = 正则表达式类(r"aaa(.*?)bbb(.*?)ccc", str)
        for i in range(zz.取匹配数量()):
            print(zz.取匹配文本(i))
            print(zz.取子匹配数量())
            print(zz.取子匹配文本(i, 0))
            print(zz.取子匹配文本(i, 1))
            print(zz.取子匹配文本(i, 2))
        print("================")

        str = r"""aaa111bbb444ccc
        aaa222bbb555ccc
        aaa333bbb666ccc
        """
        zz = 正则表达式类(r"\d+")
        data = zz.替换("==", str)
        print(data)

        正则结果 = 正则表达式类().创建(r"aaa(.*?)bbb(.*?)ccc").匹配(str).取结果()
        print(正则结果)

        正则结果 = 正则表达式类(r"aaa(.*?)bbb(.*?)ccc", str).取结果()
        print(正则结果)

        正则结果 = 正则表达式类().创建(r"aaa(.*?)bbb(.*?)ccc").替换("替换", str)
        print(正则结果)

        # 与上面不同的是..这里会搜索
        正则结果 = 正则表达式类(r"aaa(.*?)bbb(.*?)ccc", str).替换("替换")
        print(正则结果)

    def test_jingyi(self):
        # 与上面不同的是..这里会搜索
        str = r"""aaa111bbb444ccc
        aaa222bbb555ccc
        aaa333bbb666ccc
        """
        正则结果 = 正则表达式类().创建(r"aaa(.*?)bbb(.*?)ccc", str, 是否区分大小写=True, 是否匹配多行=True).取结果()
        print(正则结果)

        正则结果 = 正则表达式类().创建(r"\d+", str, 是否区分大小写=True, 是否匹配多行=True).替换("替换")
        print(正则结果)

        zz = 正则表达式类()
        zz.创建(r"\d+", str, 是否区分大小写=True, 是否匹配多行=True)
        for i in range(zz.取匹配数量()):
            print("取匹配文本", zz.取匹配文本(i))
            print("取子匹配数量", zz.取子匹配数量())
            for k in range(zz.取子匹配数量()):
                print("取子匹配文本 i= %s k= %s" % (i, k), zz.取子匹配文本(i, k))

    def test_my(self):
        str = r"""aaa111bbb444ccc
        aaa222bbb555ccc
        aaa333bbb666ccc
        AAA444BBB777CCC
        """
        正则结果 = 正则表达式(r"aaa(.*?)bbb(.*?)ccc").搜索(str)
        print(正则结果)

        正则结果 = 正则表达式(r"aaa(.*?)bbb(.*?)ccc").替换("替换", str)
        print(正则结果)

        正则结果 = 正则表达式(r"\d").替换("替换", str)
        print(正则结果)

        正则结果 = 正则表达式(r"AAA\d+BBB", re.M).替换("替换", str)
        print(正则结果)

        正则结果 = 正则表达式(r"AAA(\d+)BBB", re.M).搜索(str)
        print(正则结果)

        正则结果 = 正则表达式(r"AAA(\d+)BBB", 正则.多行模式 | 正则.忽略大小写).搜索(str)
        print(正则结果)

        # 只匹配第一项
        正则结果 = 正则表达式(r"AAA(\d+)BBB", 0).搜索(str)
        print(正则结果)

        正则结果 = 正则表达式(r"AAA(\d+)BBB", 正则.允许注释 | 正则.忽略大小写).搜索(str)
        print(正则结果)

        正则结果 = 正则表达式(r"""
        \d+ # 匹配数字
        """, 正则.多行模式 | 正则.忽略大小写 | 正则.允许注释).搜索(str)
        print(正则结果)


        print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).搜索("123456789"))
        print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).替换("替换", "123456798"))


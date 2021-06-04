import unittest

from .stringUtil import *


class TestStringUtil(unittest.TestCase):

    def test_1(self):
        data = strCut("123abc123", "123$123")
        self.assertEqual(data, "abc")
        data = strCut("123abc456", "abc$")
        self.assertEqual(data, "456")
        data = strCut("123abc456", "$abc")
        self.assertEqual(data, "123")

        data = 文本_取左边("123abc456", "abc")
        self.assertEqual(data, "123")

        data = 文本_取右边("123abc456", "abc")
        self.assertEqual(data, "456")

        data = 文本_取出中间文本("123abc456", "123", "456")
        self.assertEqual(data, "abc")


    def test_2(self):
        data = 文本_取随机字母(10, 0)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机字母(10, 1)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机字母(10, 2)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机字母和数字(10)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机数字(10)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机汉字(10)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机姓氏()
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机姓氏(True)
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机手机号()
        print(data)
        self.assertNotEqual(data, "")

        data = 文本_取随机邮箱()
        print(data)
        self.assertNotEqual(data, "")

    def test_3(self):
        data = 文本_删左边("123abc123", 3)
        self.assertEqual(data, "abc123")
        data = 文本_删右边("123abc123", 3)
        self.assertEqual(data, "123abc")
        data = 文本_删中间("123abc123", 3, 3)
        self.assertEqual(data, "123123")

        data = 文本区分_只取字母("123abc123", 0)
        self.assertEqual(data, "abc")

        data = 文本区分_只取数字("123abc123")
        self.assertEqual(data, "123123")

        data = 判断文本("123abc123", ["123"])
        self.assertEqual(data, True)

        data = 判断文本s("123abc123", ["123", "abc"])
        self.assertEqual(data, "123")

        data = 判断文本("你好", ["123"])
        self.assertEqual(data, False)

        data = 判断文本s("123abc123你好", ["aaa", "你好"])
        self.assertEqual(data, "你好")

        data = 文本_取手机号码("手机号:13588899988 手机号:13588899987")
        self.assertEqual(data, ['13588899988', '13588899987'])

        data = 文本_取IP地址("192.168.1.1")
        self.assertEqual(data, ['192.168.1.1'])

        data = 文本_取电话号码("010-33366669")
        self.assertEqual(data, ['010-33366669'])

        data = 文本_取QQ号码("666655555")
        self.assertEqual(data, ['666655555'])

        data = 文本_取邮政编码("520420")
        self.assertEqual(data, ['520420'])

        data = 文本_取身份证号码("44666655559999666")
        self.assertEqual(data, ['44666655559999666'])

        data = 文本_取双字节字符("你好hello123,./")
        self.assertEqual(data, "你好")

        data = 文本_取网址("http://www.github,com")
        self.assertEqual(data, ['http://www.github,com'])

        data = 文本_取IP跟端口("192.168.0.1:9998")
        self.assertEqual(data, ['192.168.0.1:9998'])

        data = 文本_取邮箱号码("666666@qq.com")
        self.assertEqual(data, ['666666@qq.com'])

        data = 文本_大小写翻转("abc ABC")
        self.assertEqual(data, 'ABC abc')

        data = 文本_是否为大写字母("abc ABC")
        self.assertEqual(data, False)

        data = 文本_是否为大写字母("ABC")
        self.assertEqual(data, True)

        data = 文本_是否为小写字母("abc")
        self.assertEqual(data, True)

        data = 文本_是否为字母("abcABC")
        self.assertEqual(data, True)

        data = 文本_是否为字母("abcABC123")
        self.assertEqual(data, False)

        data = 文本_是否为数字字母("abcABC123")
        self.assertEqual(data, True)

        data = 文本_是否为数字("abc123465")
        self.assertEqual(data, False)

        data = 文本_是否为数字字母("123465")
        self.assertEqual(data, True)

        data = 文本_取出现次数("AAAaaaBBBbbb", "b")
        self.assertEqual(data, 3)

        data = 文本_单词首字母大写("apple")
        self.assertEqual(data, "Apple")

        data = 文本_填充空格_居中("apple", 10)
        self.assertEqual(data, "  apple   ")

        data = 文本_填充空格_左对齐("apple", 10)
        self.assertEqual(data, "apple     ")

        data = 文本_填充空格_右对齐("apple", 10)
        self.assertEqual(data, "     apple")

        data = 文本_自动补零("apple", 10)
        self.assertEqual(data, "00000apple")

        data = 数组_转文本(["a", "b", "c"], "-")
        self.assertEqual(data, "a-b-c")

        data = 文本_判断文本前缀("pro_apple", "pro")
        self.assertEqual(data, True)

        data = 文本_判断文本后缀("pro_apple", "apple")
        self.assertEqual(data, True)

        data = 文本_TAB转空格("\tpro_apple", 4)
        self.assertEqual(data, "    pro_apple")

        data = 文本_取随机IP()
        self.assertNotEqual(data, "")
        print(data)

    def test_4(self):
        data = 文本_取出文本中汉字("你好,祖国,hello")
        self.assertEqual(data, "你好祖国")

        data = 文本_逐字分割("你好,祖国,hello")
        self.assertEqual(data, ['你', '好', ',', '祖', '国', ',', 'h', 'e', 'l', 'l', 'o'])

        data = 文本_颠倒("你好,祖国,hello")
        self.assertEqual(data, "olleh,国祖,好你")

        data = 文本_是否为汉字("你好祖国")
        self.assertEqual(data, True)

        data = 文本_是否为汉字("你好祖国123")
        self.assertEqual(data, False)

        data = 文本_取中间_批量("abc123efg,abc123efg,abc123efg", "abc", "efg")
        self.assertEqual(data, ['123', '123', '123'])

    def test_5(self):
        data = 文本_汉字转拼音("祖国你好", " ")
        print(data)

import unittest

from .正则表达式实用函数 import *


class TestRegexpUtil(unittest.TestCase):

    def test1(self):
        pass
        结果 = 正则匹配手机号码("13800138000")
        self.assertEqual(结果, "13800138000")
        结果 = 正则匹配邮箱("123@qq.com")
        self.assertEqual(结果, "123@qq.com")
        结果 = 正则匹配身份证号码("441234198812093019")
        self.assertEqual(结果, "441234198812093019")
        结果 = 正则匹配银行卡号("6222021001000123456789")
        self.assertEqual(结果, "6222021001000123456789")
        结果 = 正则匹配邮政编码("100100")
        self.assertEqual(结果, "100100")
        结果 = 正则匹配IP地址("192.168.1.1")
        self.assertEqual(结果, "192.168.1.1")
        结果 = 正则匹配URL("http://www.baidu.com")
        self.assertEqual(结果, "http://www.baidu.com")
        结果 = 正则匹配用户名("admin")
        self.assertEqual(结果, "admin")
        结果 = 正则匹配密码("adminAdmin123")
        self.assertEqual(结果, "adminAdmin123")
        结果 = 正则匹配中文("中文")
        self.assertEqual(结果, "中文")
        结果 = 正则匹配英文("abc")
        self.assertEqual(结果, "abc")
        结果 = 正则匹配数字("123")
        self.assertEqual(结果, "123")

import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.百度 import *


class Test百度(unittest.TestCase):

    def test_百度翻译(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        appid = 取环境变量("appid")
        secret = 取环境变量("secret")
        ic(appid)
        ic(secret)

        翻译结果 = 百度翻译(appid, secret, "hello world", "auto", "zh")
        ic(翻译结果)


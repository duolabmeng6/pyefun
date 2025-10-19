import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.有道 import *


class Test火山(unittest.TestCase):

    def test_火山翻译(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        yd_app_id = 取环境变量("yd_app_id")
        yd_SecretAccessKey = 取环境变量("yd_SecretAccessKey")

        ic(yd_app_id)
        ic(yd_SecretAccessKey)

        翻译结果 = 有道翻译(yd_app_id, yd_SecretAccessKey, "hello world", "auto", "zh")
        ic(翻译结果)


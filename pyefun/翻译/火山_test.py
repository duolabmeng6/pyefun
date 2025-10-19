import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.火山 import *


class Test火山(unittest.TestCase):

    def test_火山翻译(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        hs_AccessKeyID = 取环境变量("hs_AccessKeyID")
        hs_SecretAccessKey = 取环境变量("hs_SecretAccessKey")

        ic(hs_AccessKeyID)
        ic(hs_SecretAccessKey)

        翻译结果 = 火山翻译(hs_AccessKeyID, hs_SecretAccessKey, "hello world", "auto", "zh")
        ic(翻译结果)


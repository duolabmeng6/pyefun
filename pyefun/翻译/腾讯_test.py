import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.腾讯 import *


class Test腾讯(unittest.TestCase):

    def test_阿里云(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        tx_secretId = 取环境变量("tx_secretId")
        tx_secretKey = 取环境变量("tx_secretKey")

        ic(tx_secretId)
        ic(tx_secretKey)

        翻译结果 = 腾讯翻译(tx_secretId, tx_secretKey, "hello world", "auto", "zh")
        ic(翻译结果)


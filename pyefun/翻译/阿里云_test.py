import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.阿里云 import *


class Test阿里云(unittest.TestCase):

    def test_阿里云(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")

        ic(access_key_id)
        ic(access_key_secret)

        翻译结果 = 阿里云翻译(access_key_id, access_key_secret, "hello world", "auto", "zh")
        ic(翻译结果)


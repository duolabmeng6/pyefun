import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.彩云小译 import *


class Test彩云小译(unittest.TestCase):

    def test_彩云小译翻译(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        cyxy_token = 取环境变量("cyxy_token")
        ic(cyxy_token)

        翻译结果 = 彩云小译翻译(cyxy_token, "hello world", "auto", "zh")
        ic(翻译结果)


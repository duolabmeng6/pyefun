import unittest

from pyefun import *


class Test百度(unittest.TestCase):

    def test_百度翻译(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")

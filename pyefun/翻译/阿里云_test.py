import unittest

from pyefun import *
from pyefun.调试 import *
from pyefun.翻译.阿里云 import *
from pyefun.翻译.阿里云免费 import *


class Test阿里云(unittest.TestCase):

    def test_阿里云(self):
        """
        test_阿里云 的功能说明（请补充）。

        """
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")

        ic(access_key_id)
        ic(access_key_secret)

        翻译结果 = 阿里云翻译(access_key_id, access_key_secret, "hello world", "auto", "zh")
        ic(翻译结果)

    def test_阿里云2(self):
        """
        test_阿里云2 的功能说明（请补充）。

        """
        result = 阿里云翻译2("qoq 用戶開發，qoq 是一款 macOS 上的翻譯軟件，qoq 官網地址：qoq", 目标语言='en')
        print(result)
        result = 阿里云翻译2(
            "Developed by qoq users, qoq is the 1 translation software on macOS. qoq&#39;s official website address: qoq",
            源语言="en", 目标语言='zh')
        print(result)

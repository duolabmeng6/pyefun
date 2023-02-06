import unittest

from pyefun.模块.aria2文件下载 import *
# from pyefun.模块.苹果系统操作 import *

class TestAria2(unittest.TestCase):
    def test_文本朗读(self):
        发起下载("http://127.0.0.1:6800/rpc", 服务器密钥="1234", URL="https://www.xzmp3.com/down/4874bea05337.mp3",
                 文件名="test.mp4")
        # 打开访达下载目录()
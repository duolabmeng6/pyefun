import unittest

from .__init__ import *
from pyefun.eRequestsUtil import *


class TesteRequestsUtil(unittest.TestCase):
    def test2(self):
        pass
        print("网址_取域名", 网址_取域名("http://www.example.com"))

    def test_1(self):
        pass
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        import warnings
        warnings.simplefilter('ignore', ResourceWarning)

        ehttp = eRequests(cookies文件路径="C:/123/1.cookie", 全局头信息="""
        User-Agent: quanjutouxinxi
        Cookie: a1=1111111111111; b1=22222222222; 
        """)
        # ehttp.关闭调试信息()
        ehttp.设置全局HTTP代理("127.0.0.1:11111")

        返回文本 = ehttp.访问("http://127.0.0.1:9000/1.php", 附加头信息="""Cookie: aa=bbbbbbbbbbbb; cc=dddd; 
        xxxxxxxxxxxx: zuigaoyouxianji
""", 允许重定向=True)
        print(返回文本.内容)
        # print(返回文本.文本)
        # print(返回文本.头信息)
        # print(返回文本.cookies)
        # print(返回文本.Response.headers['Location'])
        返回文本 = ehttp.访问("http://127.0.0.1:9000/1.php", 不使用代理访问=True)
        返回文本 = ehttp.访问("http://127.0.0.1:9000/1.php", 允许重定向=False)

    def test_POST(self):
        ehttp = eRequests(cookies文件路径="C:/123/1.cookie")
        ehttp.设置全局HTTP代理("127.0.0.1:11111")
        返回文本 = ehttp.post("http://127.0.0.1:9000/post.php", 发送文本="a=1&b=2&c=3")
        print(返回文本.文本)
        返回文本 = ehttp.post("http://127.0.0.1:9000/post.php", 发送文本={"aa": 1, "bb": 2, "cc": 3})
        print(返回文本.文本)
        # 字节集 = 读入文件("C:/123/share.png")
        # 返回文本 = ehttp.post("http://127.0.0.1:9000/post.php", 发送文本={"aa": 1, "bb": 2, "cc": 3},
        #                   上传文件={'upload': ('code.png', 字节集, 'image/png')})
        # print(返回文本.文本)

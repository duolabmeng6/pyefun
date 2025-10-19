import unittest

import pyefun
from pyefun.seleniumUtil import *
import oss as 阿里云oss


class TestOSS(unittest.TestCase):

    def test_1(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")

        # print(access_key_id, access_key_secret)

        auth = 阿里云oss.获取授权(access_key_id, access_key_secret)
        bucket = 阿里云oss.初始化Bucket(auth, 'oss-cn-hongkong.aliyuncs.com', 'pythonutil')

        浏览器 = 浏览器类()
        # 浏览器.打开chrome()
        浏览器.打开chrome(无头模式=True)
        浏览器.置浏览器位置(左边=0, 顶边=0, 宽度=1366, 高度=768)

        浏览器.浏览网页("https://www.baidu.com")
        print(浏览器.取页面标题())

        images = 浏览器.截图png()
        浏览器.退出()

        bucket.上传文件("test.png", images)

        data = bucket.列举文件("selenium")
        print(data)

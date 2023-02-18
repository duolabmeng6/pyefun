import unittest

from .ChatGPT import *
from .图像生成 import *


class Testopenid(unittest.TestCase):
    def test_openid(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        api_key = 取环境变量("openai_api_key")
        dingding_pp_secret = 取环境变量("dingding_pp_secret")
        消息 = 聊天机器人(api_key, "用中文回答 你好 你叫什么名字 几岁 现在在做什么")
        print(消息)
        # 图像生成(api_key, "背景是白色的 陶瓷大杯子画着蓝天白云草原")
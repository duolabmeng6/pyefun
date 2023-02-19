import unittest

from .ChatGPT import *
from .图像生成 import *
from pyefun.调试 import *

class Testopenid(unittest.TestCase):
    def test_openid(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        api_key = 取环境变量("openai_api_key")
        dingding_pp_secret = 取环境变量("dingding_pp_secret")

        ic(api_key)
        ic(dingding_pp_secret)

        # 消息 = 聊天机器人(api_key, "用中文回答 你好 你叫什么名字 几岁 现在在做什么")
        # print(消息)
        # 图像生成(api_key, "背景是白色的 陶瓷大杯子画着蓝天白云草原")

    def test_连续对话测试(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        api_key = 取环境变量("openai_api_key")

        机器人 = 机器人连续聊天(api_key)
        回答 = 机器人.发送消息("1请给我5个数字")
        # ic(回答)
        回答 = 机器人.发送消息("2请找出最大的数字")
        # ic(回答)
        回答 = 机器人.发送消息("3请找出最大的数字")
        # ic(回答)
        回答 = 机器人.发送消息("4请找出最大的数字")
        # ic(回答)
        回答 = 机器人.发送消息("5请找出最大的数字")
        # ic(回答)
        回答 = 机器人.发送消息("6请找出最大的数字")
        # ic(回答)
        回答 = 机器人.发送消息("7请找出最大的数字")

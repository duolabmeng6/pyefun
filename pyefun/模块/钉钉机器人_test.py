import unittest

from .钉钉机器人 import *
from pyefun import *


class Test_钉钉机器人(unittest.TestCase):

    def test_1(self):
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        secret = 取环境变量("dingding_secret")
        webhook = 取环境变量("dingding_webhook")
        print(secret, webhook)

        机器人 = 钉钉机器人(webhook, secret)
        # 机器人.发送文本消息("测试")
        # 机器人.发送链接消息("测试", "测试", "https://www.baidu.com", "https://www.baidu.com/img/bd_logo1.png")
        # 机器人.发送markdown消息("# 测试\n## 测试\n### 测试\n#### 测试\n#####")
        # 机器人.发送图片消息("https://www.baidu.com/img/bd_logo1.png")

        # 机器人.整体跳转消息类型("测试", "![选择](https://www.baidu.com/img/bd_logo1.png) \n### 故事是这样子的...", "https://www.baidu.com")
        text = """
下面这句代码将打印一行字符串：

```
print("Hello World!")
```

        """
        机器人.发送markdown消息(text)

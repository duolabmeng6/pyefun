import unittest

from .configEnvUtil import *
from .practical import *


class Testenv(unittest.TestCase):

    def test_1(self):
        pass
        data = """
        DOMAIN=example.org
        ADMIN_EMAIL=admin@${DOMAIN}
        ROOT_URL=${DOMAIN}/app
    
        pass=******
        a=pyefun
        b=goefun
        c=${a}-${b}
        """

        data2 = """
        pass=1234567890
        """

        config = 环境变量_从文本中解析(data)
        print(config)
        环境变量_从文本中加载至系统(data)
        print(读环境变量("a"))
        print(读环境变量("c"))
        print(读环境变量("pass"))
        环境变量_从文本中加载至系统(data2)
        print(读环境变量("pass"))

        config = {
            **环境变量_从文本中解析(data),  # 加载文件
            **环境变量_从文本中解析(data2),  # 加密秘钥
            # **环境变量_获取系统所有变量(),  # 加载系统环境变量
        }
        print(config)


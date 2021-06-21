import unittest

from .configUtil import *
from .typeConv import *
class TestConfigUtil(unittest.TestCase):

    def test_1(self):
        pass

        conf = 配置项().加载("""
        [节名称0]

        项目名称0 = value0
        项目名称1 = value1

        [节名称1]

        项目名称2 = value2
        项目名称3 = value3
        """)
        所有节名 = conf.取所有节名()
        print(所有节名)
        for 节名 in 所有节名:
            print(conf.取所有项名和值(节名))
            print(conf.取所有项名(节名))
            for 项名称 in conf.取所有项名(节名):
                print(conf.读配置项(节名, 项名称))

        conf.写配置项("节3", "项目1", "ok")
        conf.写配置项("节3", "项目2", "ok3")
        conf.写配置项("节4", "项目2", "ok3")
        conf.删除配置项("节4", "项目2")
        conf.删除节名("节4", )
        conf.删除节名("节3", )
        data = conf.取数据()
        print(data)
        字典 = conf.取所有结果()
        print(字典)
        print(字典["节名称0"]["项目名称0"])
        print(json到文本(字典))
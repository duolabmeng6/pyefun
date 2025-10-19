import unittest

from pyefun import *
from pyefun.环境变量 import *
from fc import *

class TestFC(unittest.TestCase):
    def test_4(self):
        pass
        print("111111111111111111111111")

    def test_1(self):
        # 调用http函数
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")
        endpoint = 取环境变量("endpoint")
        """
        access_key_id=
        access_key_secret=
        #endpoint=.cn-beijing.fc.aliyuncs.com
        endpoint=.cn-hangzhou.fc.aliyuncs.com
        """
        fc = 阿里云函数计算(
            endpoint=endpoint,
            accessKeyID=access_key_id,
            accessKeySecret=access_key_secret,
            Timeout=120
        )

        # req = fc.调用http函数("GET", "test1", "fchttp", "", headers={}, params={"a": "aaa"},
        #                   body=bytes('hello_world'.encode('utf-8')))
        # print(req.status_code)
        # print(req.content)


    def test_3(self):
        # 调用事件函数
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")
        endpoint = 取环境变量("endpoint")
        fc = 阿里云函数计算(
            endpoint=endpoint,
            accessKeyID=access_key_id,
            accessKeySecret=access_key_secret,
            Timeout=120
        )

        data = bytes(json.dumps({
            "key": "hello",
        }).encode("utf-8"))
        for v in range(10):
            print(v)
            ret = fc.调用事件函数("fwmc", "get_list", data, 异步调用=True)
        # ret = fc.调用事件函数("fwmc", "get_list", data, 异步调用=False)
        print(ret.data)
        # print(ret.headers)


    def test_2(self):
        # 列出服务和函数
        环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))

        access_key_id = 取环境变量("access_key_id")
        access_key_secret = 取环境变量("access_key_secret")
        endpoint = 取环境变量("endpoint")

        fc = 阿里云函数计算(
            endpoint=endpoint,
            accessKeyID=access_key_id,
            accessKeySecret=access_key_secret,
            Timeout=120
        )
        print(fc.列出服务().data)
        for v in fc.列出服务().data['services']:
            print("-------------------------------")
            print(repr(v))
            print("服务名称", v['serviceName'])
            print("描述", v['description'])
            print("role", v['role'])
            print("serviceId", v['serviceId'])
            print("createdTime", v['createdTime'])
            print(fc.列出函数(v['serviceName']).data)
            for fcv in fc.列出函数(v['serviceName']).data['functions']:
                print("====================================")
                print(repr(fcv))
                print("函数名称", fcv['functionName'])
                print("描述", fcv['description'])
                print("运行环境", fcv['runtime'])
                print("入口函数", fcv['handler'])
                print("超时时间", fcv['timeout'])
            print("-------------------------------")




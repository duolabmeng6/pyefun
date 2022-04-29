"""
.. Hint::
    网络操作


.. literalinclude:: ../../../pyefun/networkUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
import sys
import requests
from .public import *
from requests.adapters import HTTPAdapter

@异常处理返回类型逻辑型
def 网页_取外网IP(返回地区=False):
    '如果设置返回地区则返回两个参数,ip,地区'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"}
    requests.packages.urllib3.disable_warnings()
    try:
        源码 = requests.get("http://pv.sohu.com/cityjson", verify=False, headers=header)
        结果 = eval(源码.text[19:-1])
        if 返回地区 == False:
            return 结果['cip']
        return 结果['cip'], 结果['cname']
    except:
        pass

    try:
        源码 = requests.get("https://ipservice.ws.126.net/locate/api/getLocByIp?callback=bowlder.cb._2", verify=False, headers=header)
        结果 = eval(源码.text[14:-1])
        if 返回地区 == False:
            return 结果['result']['ip']
        return 结果['result']['ip'], "{} {} {}".format(结果['result']['country'] , 结果['result']['province'] , 结果['result']['city'])
    except:
        pass

    try:
        源码 = requests.get("https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp", verify=False, headers=header)
        结果 = eval(源码.text)
        if 返回地区 == False:
            return 结果['data']['addr']
        return 结果['data']['addr'], "{} {} {}".format(结果['data']['country'] , 结果['data']['province'] , 结果['data']['city'])
    except:
        if 返回地区 == False:
            return ''
        return '',''



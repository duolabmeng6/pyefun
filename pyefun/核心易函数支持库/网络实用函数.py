"""
.. Hint::
    网络操作


.. literalinclude:: ../../../pyefun/网络操作_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
from pyefun import *


@异常处理返回类型逻辑型
def 网页_取外网IP():
    ehttp = eRequests()
    ehttp.关闭调试信息()

    返回文本 = ehttp.get("http://pv.sohu.com/cityjson")
    ip = strCut(返回文本.文本, '"cip": "$"')
    if ip != "":
        return ip
    返回文本 = ehttp.get("https://ipservice.ws.126.net/locate/api/getLocByIp?callback=bowlder.cb._2")
    ip = strCut(返回文本.文本, '"ip":"$"')
    if ip != "":
        return ip

    返回文本 = ehttp.get("https://api.bilibili.com/x/web-interface/zone?jsonp=jsonp")
    ip = strCut(返回文本.文本, '"addr":"$"')
    if ip != "":
        return ip

    return ""

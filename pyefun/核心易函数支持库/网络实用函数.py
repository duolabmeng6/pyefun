"""
.. Hint::
    网络操作


.. literalinclude:: ../../../pyefun/网络操作_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""
from pyefun import *
import socket


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


def 取本机ip地址():
    """
    查询本机ip地址 局域网
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def 检测端口是否被占用(ip, port):
    """
    check whether the port is used by other program
    检测端口是否被占用

    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        return True
    except OSError:
        return False
    finally:
        s.close()

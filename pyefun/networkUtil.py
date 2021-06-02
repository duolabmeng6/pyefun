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



@异常处理返回类型逻辑型
def 网页_COOKIE合并更新(原COOKIE, 新COOKIE):
    '传入的Cookie可以是文本型也可以是字典,返回更新后的COOKIE,字典型'
    最新Cookie = {}
    临时Cookie = {}
    if type(原COOKIE) == str:
        if 原COOKIE.find(";") == -1:
            名称 = 原COOKIE[0:原COOKIE.find("=")].strip(' ')
            值 = 原COOKIE[原COOKIE.rfind(名称) + len(名称) + 1:len(原COOKIE)].strip(' ')
            if 名称 and 值:
                最新Cookie = {名称: 值}
        else:
            cookie数组 = cookie.split(';')
            for x in cookie数组:
                名称 = x[0:x.find("=")].strip(' ')
                值 = x[原COOKIE.rfind(名称) + len(名称) + 1:len(x)].strip(' ')
                if 名称 and 值:
                    最新Cookie[名称] = 值
    else:
        最新Cookie = 原COOKIE

    if type(新COOKIE) == str:
        if 新COOKIE.find(";") == -1:
            名称 = 新COOKIE[0:新COOKIE.find("=")].strip(' ')
            值 = 新COOKIE[新COOKIE.rfind(名称) + len(名称) + 1:len(新COOKIE)].strip(' ')
            if 名称 and 值:
                临时Cookie = {名称: 值}
        else:
            cookie数组 = cookie.split(';')
            for x in cookie数组:
                名称 = x[0:x.find("=")].strip(' ')
                值 = x[新COOKIE.rfind(名称) + len(名称) + 1:len(x)].strip(' ')
                if 名称 and 值:
                    临时Cookie[名称] = 值
    else:
        临时Cookie = 新COOKIE

    for x in 临时Cookie:
        最新Cookie[x] = 临时Cookie[x]

    return 最新Cookie


class 网页返回类型:
    def __init__(self):
        self.源码 = ''
        self.字节集 = b'' #返回字节集,如图片,视频等文件需要
        self.cookie = {}
        self.协议头 = {}
        self.状态码 = 0
        self.原对象 = None
        self.json = {}

class 网页_访问_会话:
    'requests.session()'

    def __init__(self,重试次数=0):
        self._requests = requests.session()
        if 重试次数:
            self._requests.mount('http://', HTTPAdapter(max_retries=重试次数))
            self._requests.mount('https://', HTTPAdapter(max_retries=重试次数))

    @异常处理返回类型逻辑型
    def 网页_访问(self,url, 方式=0, 参数='', cookie='', 协议头={}, 允许重定向=True, 代理地址=None, 编码=None, 证书验证=False, 上传文件=None, 补全协议头=True,json={},连接超时=15, 读取超时=15):
        """
        :param url: 链接,能自动补全htpp,去除首尾空格
        :param 方式: 0.get 1.post 2.put 3.delete 4.head 5.options
        :param 参数: 可以是文本也可以是字典
        :param cookie: 可以是文本也可以是字典
        :param 协议头: 可以是文本也可以是字典
        :param 允许重定向: True 或 False 默认允许
        :param 代理地址: 账号:密码@IP:端口  或  IP:端口
        :param 编码: utf8,gbk·······
        :param 证书验证: 默认为False,需要引用证书时传入证书路径
        :param 上传文件: {'upload': ('code.png', 图片字节集, 'image/png')}
        :param 补全协议头: 默认补全常规协议头
        :param json: post提交参数时可能使用的类型
        :param 连接超时: 默认15
        :param 读取超时: 默认15
        :return: 返回网页对象
        """

        网页 = 网页返回类型()
        try:
            url = url.strip(' ')
            url = url if url.startswith('http') else 'http://' + url
            _cookie = {}
            _协议头 = {}
            传入参数 = {}
            if url.find('/', 8) != -1:
                host = url[url.find('://') + 3:url.find('/', 8)]
            else:
                host = url[url.find('://') + 3:]

            if type(协议头) == str:
                协议头数组 = 协议头.split('\n')
                for x in 协议头数组:
                    名称 = x[0:x.find(':')].strip(' ')
                    值 = x[x.rfind(名称) + len(名称) + 1:len(x)].strip(' ')
                    if 名称 and 值:
                        _协议头[名称] = 值
            else:
                _协议头 = 协议头

            if 补全协议头:
                if not 'Host' in _协议头:
                    _协议头['Host'] = host
                if not 'Accept' in _协议头:
                    _协议头['Accept'] = '*/*'
                if not 'Content-Type' in _协议头:
                    _协议头['Content-Type'] = 'application/x-www-form-urlencoded'
                if not 'User-Agent' in _协议头:
                    _协议头['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
                if not 'Referer' in _协议头:
                    _协议头['Referer'] = url

            if type(cookie) == str:
                if cookie.find(";") == -1:
                    名称 = cookie[0:cookie.find("=")].strip(' ')
                    值 = cookie[cookie.rfind(名称) + len(名称) + 1:len(cookie)].strip(' ')
                    if 名称 and 值:
                        _cookie = {名称: 值}
                else:
                    cookie数组 = cookie.split(';')
                    for x in cookie数组:
                        名称 = x[0:x.find("=")].strip(' ')
                        值 = x[cookie.rfind(名称) + len(名称) + 1:len(x)].strip(' ')
                        if 名称 and 值:
                            _cookie[名称] = 值
            else:
                _cookie = cookie

            传入参数['url'] = url
            传入参数['verify'] = 证书验证
            传入参数['cookies'] = _cookie
            传入参数['headers'] = _协议头
            传入参数['allow_redirects'] = 允许重定向
            if 参数:
                if 方式 == 0:
                    传入参数['params'] = 参数
                else:
                    传入参数['data'] = 参数
            if json:
                传入参数['json'] = json
            if 上传文件:
                传入参数['files'] = 上传文件
            if 代理地址:
                传入参数['proxies'] = {"http": "http://" + 代理地址, "https": "https://" + 代理地址}
            if 连接超时 and 读取超时:
                传入参数['timeout'] = (连接超时, 读取超时)

            # 发送
            if 方式 == 0:
                网页对象 = requests.get(**传入参数)
            elif 方式 == 1:
                网页对象 = requests.post(**传入参数)
            elif 方式 == 2:
                网页对象 = requests.put(**传入参数)
            elif 方式 == 3:
                网页对象 = requests.delete(**传入参数)
            elif 方式 == 4:
                网页对象 = requests.head(**传入参数)
            elif 方式 == 5:
                网页对象 = requests.options(**传入参数)

            if 编码:
                网页对象.encoding = 编码

            网页.原对象 = 网页对象
            网页.源码 = 网页对象.text
            网页.cookie = dict(网页对象.cookies)
            网页.状态码 = 网页对象.status_code
            网页.协议头 = 网页对象.headers
            网页.字节集 = 网页对象.content
            try:
                网页.json = 网页对象.json()
            except:
                pass
        except:
            print(sys._getframe().f_code.co_name, "函数发生异常", url)
            # print("错误发生时间：", str(datetime.datetime.now()))
            # print("错误的详细情况：", traceback.format_exc())
        return 网页


# @异常处理返回类型逻辑型
def 网页_访问(url, 方式=0, 参数='', cookie='', 协议头={}, 允许重定向=True, 代理地址=None, 编码=None,证书验证=False, 上传文件=None,补全协议头=True,json={}, 连接超时=15, 读取超时=15):
    """
    :param url: 链接,能自动补全htpp,去除首尾空格
    :param 方式: 0.get 1.post 2.put 3.delete 4.head 5.options
    :param 参数: 可以是文本也可以是字典
    :param cookie: 可以是文本也可以是字典
    :param 协议头: 可以是文本也可以是字典
    :param 允许重定向: True 或 False 默认允许
    :param 代理地址: 账号:密码@IP:端口  或  IP:端口
    :param 编码: utf8,gbk·······
    :param 证书验证: 默认为False,需要引用证书时传入证书路径
    :param 上传文件: {'upload': ('code.png', 图片字节集, 'image/png')}
    :param 补全协议头: 默认补全常规协议头
    :param json: post提交参数时可能使用的类型
    :param 连接超时: 默认15
    :param 读取超时: 默认15
    :return: 返回网页对象
    """

    网页 = 网页返回类型()
    url = url.strip(' ')
    url = url if url.startswith('http') else 'http://' + url
    _cookie = {}
    _协议头 = {}
    传入参数 = {}
    if url.find('/',8) != -1:
        host = url[url.find('://')+3:url.find('/', 8)]
    else:
        host = url[url.find('://')+3:]

    if type(协议头) == str:
        协议头数组 = 协议头.split('\n')
        for x in 协议头数组:
            名称 = x[0:x.find(':')].strip(' ')
            值 = x[x.rfind(名称) + len(名称)+1:len(x)].strip(' ')
            if 名称 and 值:
                _协议头[名称] = 值
    else:
        _协议头 = 协议头

    if 补全协议头:
        if not 'Host' in _协议头:
            _协议头['Host'] = host
        if not 'Accept' in _协议头:
            _协议头['Accept'] = '*/*'
        if not 'Content-Type' in _协议头:
            _协议头['Content-Type'] = 'application/x-www-form-urlencoded'
        if not 'User-Agent' in _协议头:
            _协议头['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
        if not 'Referer' in _协议头:
            _协议头['Referer'] = url

    if type(cookie) == str:
        if cookie.find(";") == -1:
            名称 = cookie[0:cookie.find("=")].strip(' ')
            值 = cookie[cookie.rfind(名称) + len(名称) + 1:len(cookie)].strip(' ')
            if 名称 and 值:
                _cookie = {名称: 值}
        else:
            cookie数组 = cookie.split(';')
            for x in cookie数组:
                名称 = x[0:x.find("=")].strip(' ')
                值 = x[cookie.rfind(名称) + len(名称) + 1:len(x)].strip(' ')
                if 名称 and 值:
                    _cookie[名称] = 值
    else:
        _cookie = cookie


    传入参数['url'] = url
    传入参数['verify'] = 证书验证
    传入参数['cookies'] = _cookie
    传入参数['headers'] = _协议头
    传入参数['allow_redirects'] = 允许重定向
    if 参数:
        if 方式 == 0:
            传入参数['params'] = 参数
        else:
            传入参数['data'] = 参数
    if json:
        传入参数['json'] = json
    if 上传文件:
        传入参数['files'] = 上传文件
    if 代理地址:
        传入参数['proxies'] = {"http": "http://" + 代理地址, "https": "https://" + 代理地址}
    if 连接超时 and 读取超时:
        传入参数['timeout'] = (连接超时,读取超时)

    #发送
    if 方式 == 0:
        网页对象 = requests.get(**传入参数)
    elif 方式 == 1:
        网页对象 = requests.post(**传入参数)
    elif 方式 == 2:
        网页对象 = requests.put(**传入参数)
    elif 方式 == 3:
        网页对象 = requests.delete(**传入参数)
    elif 方式 == 4:
        网页对象 = requests.head(**传入参数)
    elif 方式 == 5:
        网页对象 = requests.options(**传入参数)


    if 编码:
        网页对象.encoding = 编码

    网页.原对象 = 网页对象
    网页.源码 = 网页对象.text
    try:
        网页.cookie = dict(网页对象.cookies)
    except:
        pass
    网页.状态码 = 网页对象.status_code
    网页.协议头 = 网页对象.headers
    网页.字节集 = 网页对象.content
    try:
        网页.json = 网页对象.json()
    except:
        pass
    # except:
        # print(sys._getframe().f_code.co_name, "函数发生异常",url)
        # print("错误发生时间：", str(datetime.datetime.now()))
        # print("错误的详细情况：", traceback.format_exc())
    return 网页

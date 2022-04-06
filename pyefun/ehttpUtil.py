import requests

from pyefun import *
from http.cookiejar import LWPCookieJar


class ehttp响应类(object):
    Response: requests.Response

    def __init__(self, obj):
        self.Response = obj

    def Response(self):
        return self.Response

    @property
    def 内容(self):
        return self.Response.content

    @property
    def 文本(self):
        return self.Response.text

    @property
    def 字节集(self):
        return self.Response.content

    @property
    def 头信息(self):
        return self.Response.headers

    @property
    def 状态码(self):
        return self.Response.status_code

    @property
    def 编码(self):
        return self.Response.encoding

    @property
    def url(self):
        return self.Response.url

    @property
    def cookies(self):
        return self.Response.cookies

    @property
    def 取Location(self):
        return self.Response.headers['Location']

    @property
    def 取重定向URl(self):
        return self.Response.headers['Location']


from urllib.parse import urlparse


def 网址_取域名(url):
    parse_result = urlparse(url)
    return parse_result.netloc


class http类():
    req = requests.session
    cookie文件路径 = ""
    全局HTTP代理 = None
    调试信息 = False
    默认头信息 = """Accept : */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36,
Content-Type: application/x-www-form-urlencoded"""
    全局头信息 = ""

    def __init__(self):
        pass
        self.req = requests.session()
        self.调试信息 = False
        self.cookie文件路径 = ""
        self.全局HTTP代理 = None

    def 设置自动管理cookie(self, 文件路径):
        pass
        self.cookie文件路径 = 文件路径
        self.req.cookies = LWPCookieJar(filename=文件路径)
        if 文件是否存在(文件路径):
            self.req.cookies.load()

    def 设置全局HTTP代理(self, 代理ip):
        pass
        self.全局HTTP代理 = {
            'http': 代理ip,
            'https': 代理ip
        }

    def 设置全局头信息(self, 全局头信息):
        pass
        self.全局头信息 = 全局头信息

    def 关闭调试信息(self, 关闭调试信息=True):
        pass
        self.调试信息 = 关闭调试信息

    def 访问(self, url: str, 访问方法: str = "GET", 发送文本: str = "", 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False):
        pass
        t = 时间统计()

        全局HTTP代理 = self.全局HTTP代理
        if 不使用代理访问 == True:
            全局HTTP代理 = {'http': "", 'https': ""}

        timeout = (超时, 超时)

        headers = {}
        附加头信息 = self.默认头信息 + "\n" + self.全局头信息 + "\n" + 附加头信息

        for 文本内容 in 附加头信息.split('\n'):
            截取位置 = 寻找文本(文本内容, ":")
            名称 = 删首尾空(取文本左边(文本内容, 截取位置))
            值 = 删首尾空(取文本右边(文本内容, 取文本长度(文本内容) - 截取位置 - 1))
            if 名称 and 值:
                headers[名称] = 值

        附加cookies = {}
        cookies = headers.get('Cookie')
        if cookies.find(";") != -1:
            for 文本内容 in cookies.split(';'):
                文本内容 = 删首尾空(文本内容)
                等于号位置 = 寻找文本(文本内容, "=")
                名称 = 取文本左边(文本内容, 等于号位置)
                值 = 取文本右边(文本内容, 取文本长度(文本内容) - 等于号位置 - 1)
                if 名称 and 值:
                    附加cookies[名称] = 值

        # 加入cookie
        requests.utils.add_dict_to_cookiejar(self.req.cookies, 附加cookies)

        # 这里获取cookie貌似是所有的...查阅代码未解决 本想获取当前访问域名的cookies

        # print(self.req.cookies.get_dict(网址_取域名(url),"/"))

        if not self.调试信息:
            # 获取请求之前加载的cookie
            加载cookie = ""
            for k, v in requests.utils.dict_from_cookiejar(self.req.cookies).items():
                if k != "":
                    加载cookie = 加载cookie + "{k}={v}; ".format(k=k, v=v)
            if 加载cookie != "":
                加载cookie = "\r\n" + "加载 Cookies {cookies}".format(cookies=加载cookie)

        if 访问方法 == "POST":
            返回数据 = self.req.post(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                 headers=headers)
        else:
            返回数据 = self.req.get(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                headers=headers)

        if self.cookie文件路径 != "":
            self.req.cookies.save()

        if not self.调试信息:
            耗时 = t.取秒()
            # print(返回数据.headers.get('Set-Cookie'))
            cookies = ""
            for item in 返回数据.cookies.items():
                cookies = cookies + "{0}={1}; ".format(item[0], item[1])
            if cookies != "":
                cookies = "\r\n" + "新增 Cookies {cookies}".format(cookies=cookies)

            重定向地址 = ""
            if 返回数据.status_code == 301 or 返回数据.status_code == 302:
                重定向地址 = "重定向URL " + 返回数据.headers.get('Location')

            代理信息 = 全局HTTP代理.get('http')
            if 代理信息 != "":
                代理信息 = "代理 " + 代理信息

            print("{访问方法} {url} 状态码 {状态码} 耗时 {耗时}s {代理信息} {重定向地址} {加载cookie} {cookies}".format(访问方法=访问方法, url=url,
                                                                                               状态码=返回数据.status_code,
                                                                                               耗时=耗时,
                                                                                               cookies=cookies,
                                                                                               加载cookie=加载cookie,
                                                                                               重定向地址=重定向地址, 代理信息=代理信息))

        return ehttp响应类(返回数据)

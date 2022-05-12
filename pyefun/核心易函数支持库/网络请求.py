"""

.. Hint::
    网络请求 eRequests 是实用的http请求模块
    轻松配置cookie文件保存 全局请求头信息 代理ip
    ehttp = eRequests(cookies文件路径="cookie文件路径",全局头信息="User-Agent: pyefun")
    ehttp.设置全局HTTP代理("127.0.0.1:11111")

    返回文本 = ehttp.get("http://127.0.0.1:9000/1.php")
    print(返回文本.文本)

    返回文本 = ehttp.post("http://127.0.0.1:9000/post.php", 发送文本={"aa": 1, "bb": 2, "cc": 3})
    print(返回文本.文本)

    # 文件上传
    字节集 = 读入文件("share.png")
    返回文本 = ehttp.post("http://127.0.0.1:9000/post.php", 发送文本={"aa": 1, "bb": 2, "cc": 3},
                      上传文件={'upload': ('code.png', 字节集, 'image/png')})

.. literalinclude:: ../../../pyefun/网络请求_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""
from pyefun import *
from pyefun.核心易函数支持库.时间统计 import *  # 时间工具类

from requests.adapters import HTTPAdapter
from http.cookiejar import LWPCookieJar
import requests
from requests import exceptions


class ehttp响应类(object):
    Response: requests.Response

    def __init__(self, obj):
        self.Response = obj

    def Response(self):
        return self.Response

    def json(self):
        return self.Response.json()

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

    @property
    def 访问失败(self):
        # 真 访问失败
        # 假 访问成功
        if self.状态码 == 200 or self.状态码 == 302 or self.状态码 == 301:
            return False
        else:
            return True


from urllib.parse import urlparse


def 网址_取域名(url):
    parse_result = urlparse(url)
    return parse_result.netloc

def 屏蔽Requests中的警告信息():
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)
    requests.packages.urllib3.disable_warnings()

class eRequests(object):
    req = requests.session
    cookies文件路径 = ""
    全局HTTP代理 = None
    调试信息 = False
    默认头信息 = """Accept : */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
Content-Type: application/x-www-form-urlencoded"""
    全局头信息 = ""

    def __init__(self, cookies文件路径="", 访问失败重试次数=0, 全局头信息=""):
        pass
        self.req = requests.session()
        self.调试信息 = False
        self.cookies文件路径 = cookies文件路径
        self.全局HTTP代理 = None
        self.req.mount('http://', HTTPAdapter(max_retries=访问失败重试次数))
        self.req.mount('https://', HTTPAdapter(max_retries=访问失败重试次数))
        self.设置自动管理cookies(cookies文件路径)
        if 全局头信息 != "":
            self.设置全局头信息(全局头信息)
        self.设置全局HTTP代理("")

    def __del__(self):
        if self.cookies文件路径 != "":
            self.req.cookies.save()

    def 设置自动管理cookies(self, 文件路径):
        pass
        self.cookies文件路径 = 文件路径
        self.req.cookies = LWPCookieJar(filename=文件路径)
        if 文件是否存在(文件路径):
            self.req.cookies.load()

    # 默认情况下对象销毁就会自动保存了 无需调用此方法
    def cookies保存到文件(self):
        if self.cookies文件路径 != "":
            self.req.cookies.save()

    def 设置全局HTTP代理(self, 代理ip):
        """格式 127.0.0.1:8080"""
        pass
        self.全局HTTP代理 = {
            'http': 代理ip,
            'https': 代理ip
        }

    def 设置全局头信息(self, 全局头信息):
        """头信息将全局添加到请求头中"""
        # print(type(全局头信息))
        if type(全局头信息) == dict:
            重新处理 = ""
            for k, v in 全局头信息.items():
                重新处理 = 重新处理 + "{k}: {v}\r\n".format(k=k, v=v)
            self.全局头信息 = 重新处理
        else:

            self.全局头信息 = 全局头信息

    def 关闭调试信息(self, 关闭调试信息=True):
        pass
        self.调试信息 = 关闭调试信息

    def get(self, url: str, 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False):
        return self.访问(url=url, 访问方法="GET", 发送文本="", 附加头信息=附加头信息, 允许重定向=允许重定向, 超时=超时, 不使用代理访问=不使用代理访问)

    def delete(self, url: str, 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False):
        return self.访问(url=url, 访问方法="GET", 发送文本="", 附加头信息=附加头信息, 允许重定向=允许重定向, 超时=超时, 不使用代理访问=不使用代理访问)

    def head(self, url: str, 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False):
        return self.访问(url=url, 访问方法="GET", 发送文本="", 附加头信息=附加头信息, 允许重定向=允许重定向, 超时=超时, 不使用代理访问=不使用代理访问)

    def options(self, url: str, 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False):
        return self.访问(url=url, 访问方法="GET", 发送文本="", 附加头信息=附加头信息, 允许重定向=允许重定向, 超时=超时, 不使用代理访问=不使用代理访问)

    def post(self, url: str, 发送文本: str = "", 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False, 上传文件=None):
        return self.访问(url=url, 访问方法="POST", 发送文本=发送文本, 附加头信息=附加头信息, 允许重定向=允许重定向, 超时=超时, 不使用代理访问=不使用代理访问, 上传文件=上传文件)

    def 访问(self, url: str, 访问方法: str = "GET", 发送文本: str = "", 附加头信息: str = "", 允许重定向=True, 超时=15, 不使用代理访问=False,
           上传文件=None):
        if not self.调试信息:
            t = 时间统计()


        全局HTTP代理 = self.全局HTTP代理
        if 不使用代理访问 == True:
            全局HTTP代理 = {'http': "", 'https': ""}

        timeout = (超时, 超时)

        headers = {}

        # 兼容各种传入方式
        if type(附加头信息) == dict:
            重新处理 = ""
            for k, v in 附加头信息.items():
                重新处理 = 重新处理 + "{k}: {v}\r\n".format(k=k, v=v)
            _附加头信息 = 重新处理
        else:
            _附加头信息 = 附加头信息

        附加头信息 = self.默认头信息 + "\n" + self.全局头信息 + "\n" + _附加头信息

        for 文本内容 in 附加头信息.split('\n'):
            截取位置 = 寻找文本(文本内容, ":")
            名称 = 删首尾空(取文本左边(文本内容, 截取位置))
            值 = 删首尾空(取文本右边(文本内容, 取文本长度(文本内容) - 截取位置 - 1))
            if 名称 and 值:
                headers[名称] = 值

        附加cookies = {}
        cookies = headers.get('Cookie', "")
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

        try:
            if 访问方法 == "POST":
                返回数据 = self.req.post(url=url, data=发送文本, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向,
                                     verify=False,
                                     headers=headers, files=上传文件)
            if 访问方法 == "GET":
                返回数据 = self.req.get(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                    headers=headers)
            if 访问方法 == "delete":
                返回数据 = self.req.delete(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                       headers=headers)
            if 访问方法 == "head":
                返回数据 = self.req.head(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                     headers=headers)
            if 访问方法 == "options":
                返回数据 = self.req.options(url=url, proxies=全局HTTP代理, timeout=timeout, allow_redirects=允许重定向, verify=False,
                                        headers=headers)


        except Exception as e:
            # print('http请求错误:' + str(e))
            返回数据 = ehttp响应类(requests.Response())
            返回数据.status_code = 0
            if not self.调试信息:
                self._输出调试信息(访问方法, url, 加载cookie, 全局HTTP代理, t, 返回数据, "\r\n错误信息 " + str(e))
            return 返回数据

        if not self.调试信息:
            self._输出调试信息(访问方法, url, 加载cookie, 全局HTTP代理, t, 返回数据)

        return ehttp响应类(返回数据)

    def _输出调试信息(self, 访问方法, url, 加载cookie, 全局HTTP代理, t, 返回数据, 错误信息=""):
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

            代理信息 = 全局HTTP代理.get('http', "")
            if 代理信息 != "":
                代理信息 = "代理 " + 代理信息
            状态码 = 返回数据.status_code

            print(
                "{访问方法} {url} 状态码 {状态码} 耗时 {耗时}s {代理信息} {重定向地址} {加载cookie} {cookies} {错误信息}".format(访问方法=访问方法, url=url,
                                                                                                    状态码=状态码,
                                                                                                    耗时=耗时,
                                                                                                    cookies=cookies,
                                                                                                    加载cookie=加载cookie,
                                                                                                    重定向地址=重定向地址,
                                                                                                    代理信息=代理信息,
                                                                                                    错误信息=错误信息))

from pyefun import *

import pyefun.翻译.百度 as 百度
import pyefun.翻译.彩云小译 as 彩云小译
import pyefun.翻译.有道 as 有道
import pyefun.翻译.火山 as 火山
import pyefun.翻译.腾讯 as 腾讯
import pyefun.翻译.阿里云 as 阿里云
import pyefun.翻译.必应免费 as 必应免费
import pyefun.翻译.阿里云免费 as 阿里云免费


class 翻译工厂类:
    def __init__(self):
        self.translators = {}

    def 注册翻译模块(self, name, translator):
        self.translators[name] = translator

    def 取翻译模块(self, name):
        return self.translators.get(name)

    def 列出翻译模块(self):
        return list(self.translators.keys())


class 谷歌翻译类:
    def 翻译(self, 内容, 源语言, 目标语言):
        return "你好世界"


class 百度翻译类:
    def __init__(self, app_id, secret_key):
        self.app_id = app_id
        self.secret_key = secret_key

    def 翻译(self, 内容, 源语言, 目标语言):
        return 百度.百度翻译(self.app_id, self.secret_key, 内容, 源语言=源语言, 目标语言=目标语言)


class 必应翻译类:
    def __init__(self):
        pass

    def 翻译(self, 内容, 源语言, 目标语言):
        return 必应免费.必应翻译(内容, 源语言=源语言, 目标语言=目标语言)


class 彩云小译翻译类:
    def __init__(self, token):
        self.token = token

    def 翻译(self, 内容, 源语言, 目标语言):
        return 彩云小译.彩云小译翻译(self.token, 内容, 源语言=源语言, 目标语言=目标语言)


class 有道翻译类:
    def __init__(self, app_id, SecretAccessKey):
        self.app_id = app_id
        self.SecretAccessKey = SecretAccessKey

    def 翻译(self, 内容, 源语言, 目标语言):
        return 有道.有道翻译(self.app_id, self.SecretAccessKey, 内容, 源语言=源语言, 目标语言=目标语言)


class 火山翻译类:
    def __init__(self, AccessKeyID, SecretAccessKey):
        self.AccessKeyID = AccessKeyID
        self.SecretAccessKey = SecretAccessKey

    def 翻译(self, 内容, 源语言, 目标语言):
        return 火山.火山翻译(self.AccessKeyID, self.SecretAccessKey, 内容, 源语言=源语言, 目标语言=目标语言)


class 腾讯翻译类:
    def __init__(self, SecretId, SecretKey):
        self.SecretId = SecretId
        self.SecretKey = SecretKey

    def 翻译(self, 内容, 源语言, 目标语言):
        return 腾讯.腾讯翻译(self.SecretId, self.SecretKey, 内容, 源语言=源语言, 目标语言=目标语言)


class 阿里云翻译类:
    def __init__(self, AccessKeyID, AccessKeySecret):
        self.AccessKeyID = AccessKeyID
        self.AccessKeySecret = AccessKeySecret

    def 翻译(self, 内容, 源语言, 目标语言):
        return 阿里云.阿里云翻译(self.AccessKeyID, self.AccessKeySecret, 内容, 源语言=源语言, 目标语言=目标语言)


class 阿里云2翻译类:
    def __init__(self):
        pass

    def 翻译(self, 内容, 源语言, 目标语言):
        return 阿里云免费.阿里云翻译2(内容, 源语言=源语言, 目标语言=目标语言)


if __name__ == '__main__':

    环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
    百度_appid = 取环境变量("appid")
    百度_secret = 取环境变量("secret")
    彩云小译_token = 取环境变量("cyxy_token")
    yd_app_id = 取环境变量("yd_app_id")
    yd_SecretAccessKey = 取环境变量("yd_SecretAccessKey")
    hs_AccessKeyID = 取环境变量("hs_AccessKeyID")
    hs_SecretAccessKey = 取环境变量("hs_SecretAccessKey")
    tx_secretId = 取环境变量("tx_secretId")
    tx_secretKey = 取环境变量("tx_secretKey")
    access_key_id = 取环境变量("access_key_id")
    access_key_secret = 取环境变量("access_key_secret")

    factory = 翻译工厂类()
    # factory.注册翻译模块('google', 谷歌翻译类())
    # factory.注册翻译模块('百度', 百度翻译类(百度_appid, 百度_secret))
    factory.注册翻译模块('彩云小译', 彩云小译翻译类(彩云小译_token))
    # factory.注册翻译模块('必应', 必应翻译类())
    # factory.注册翻译模块('有道', 有道翻译类(yd_app_id, yd_SecretAccessKey))
    # factory.注册翻译模块('火山', 火山翻译类(hs_AccessKeyID, hs_SecretAccessKey))
    # factory.注册翻译模块('腾讯', 腾讯翻译类(tx_secretId, tx_secretKey))
    # factory.注册翻译模块('阿里云', 阿里云翻译类(access_key_id, access_key_secret))

    for name in factory.列出翻译模块():
        print(name)
        translator = factory.取翻译模块(name)
        if translator:
            data = translator.翻译('アイコンを取得', 'ja', 'en')
            print(data)

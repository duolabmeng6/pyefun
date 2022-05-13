#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from pyefun import *
from pyefun.网络请求 import *
from pyefun.javascript引擎 import *

屏蔽Requests中的警告信息()

def 百度翻译(内容):
    ehttp = eRequests(全局头信息={
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://fanyi.baidu.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
    # ehttp.关闭调试信息()
    # ehttp.设置全局HTTP代理("127.0.0.1:11111")
    返回文本 = ehttp.get('https://fanyi.baidu.com')
    # 写到文件("test.html",返回文本.内容)
    返回文本 = ehttp.get('https://fanyi.baidu.com')
    # 写到文件("test.html",返回文本.内容)
    token = strCut(返回文本.文本, r"token: '$',")
    window_gtk = strCut(返回文本.文本, r"window.gtk = '$';")
    # print(token)
    # print(window_gtk)
    # data = '你叫什么名字?'
    data = 内容
    js = javscript("JScript")
    js.加载代码(到文本(读入文件("./百度翻译.js")))
    encryption_data = js.执行('e', window_gtk, data)
    返回文本 = ehttp.post('https://fanyi.baidu.com/v2transapi?from=zh&to=en', {
        'from': 'zh',
        'to': 'en',
        'query': data,
        'simple_means_flag': '3',
        'sign': encryption_data,
        'token': token,
        'domain': 'common',
    })
    # print(返回文本.文本)
    # print(返回文本.json()['trans_result']['data'][0]['dst'])
    return 返回文本.json()['trans_result']['data'][0]['dst']


原文 = '你叫什么名字?'
返回文本 = 百度翻译(原文)
print("{原文} \r\n{返回文本}".format(原文=原文, 返回文本=返回文本))

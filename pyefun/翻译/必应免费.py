# -*- coding: utf-8 -*-
import requests
import json

def 必应翻译( 欲翻译文本, 源语言='auto', 目标语言='zh-CHS'):
    # 定义常量
    常量1 = """:authority: api.cognitive.microsofttranslator.com
:method: POST
:path: /translate?from=&to=zh-CHS&api-version=3.0&includeSentenceLength=true
:scheme: https
accept: */*
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
authorization: 参_authorization
content-length: 140
content-type: application/json
origin: https://gsp.lazada-seller.cn
referer: https://gsp.lazada-seller.cn/
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"""

    # 定义变量
    authorization = ''
    url = ''
    type = 0
    post_data = ''
    header = ''
    json_obj = []
    return_value = ''

    # 获取授权信息
    response = requests.get("https://edge.microsoft.com/translate/auth")
    authorization = response.text.strip()

    if authorization == '':
        for i in range(10):
            response = requests.get("https://edge.microsoft.com/translate/auth")
            authorization = response.text.strip()
            if authorization != '':
                break
            else:
                pass

    # 添加授权信息到请求头
    authorization = "Bearer " + authorization

    # 设置请求参数
    url = f"https://api.cognitive.microsofttranslator.com/translate?from=&to={目标语言}&api-version=3.0&includeSentenceLength=true"
    type = 1
    json_obj.append({})
    json_obj[0]['Text'] = 欲翻译文本

    # 发送请求并解析返回结果
    post_data = json.dumps(json_obj)
    header = 常量1.replace("参_authorization", authorization)
    response = requests.post(url, data=post_data,
                             headers={'Content-Type': 'application/json', 'Authorization': authorization})
    return_value = response.text
    json_obj = json.loads(return_value)
    return_value = json_obj[0]['translations'][0]['text']

    # 返回翻译结果
    return return_value

if __name__ == '__main__':
    print(必应翻译("hello world"))
    print(必应翻译("你好世界", 目标语言='en'))
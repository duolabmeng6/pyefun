import hashlib
import json
import random
import requests


def 百度翻译(app_id, secret_key, 欲翻译文本, 源语言='auto', 目标语言='zh'):
    """
    该函数使用百度翻译 API 来将给定文本从一种语言翻译成另一种语言。下面是该函数中各个参数的说明：

    app_id：在百度翻译开放平台申请的 App ID。
    secret_key：在百度翻译开放平台申请的密钥。
    欲翻译文本：要翻译的文本。
    源语言：源语言的代码，默认为 'auto'（自动检测源语言）。
    目标语言：目标语言的代码，默认为 'zh'（中文）。
    该函数首先设置了 API 请求所需的参数：欲翻译文本、源语言、目标语言、随机数和签名。签名使用了 MD5 哈希函数。然后，该函数使用 requests 模块发送翻译请求，并将返回的 JSON 响应解析成 Python 对象。最后，该函数返回翻译结果，如果发生错误，则返回 None。
    """

    # 设置 API 请求参数
    q = 欲翻译文本
    from_lang = 源语言
    to_lang = 目标语言
    salt = random.randint(32768, 65536)
    sign = app_id + q + str(salt) + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?appid=' + app_id \
          + '&q=' + requests.utils.quote(q)  + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        # 发送翻译请求
        返回结果 = requests.get(url)
        json数据 = json.loads(返回结果.text)
        dst = str(json数据["trans_result"][0]["dst"])  # 获取翻译结果
        return dst
    except Exception as e:
        print(e)
        return None

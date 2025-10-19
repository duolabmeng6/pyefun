import json
import requests
import time
import random


def getRandomNumber():
    """
    getRandomNumber 的功能说明（请补充）。

    """
    random.seed(time.time())
    num = random.randint(0, 99999) + 8300000
    return num * 1000


def DeepL翻译(欲翻译文本, 源语言='auto', 目标语言='zh'):
    """
    DeepL翻译 的功能说明（请补充）。

    Args:
        欲翻译文本: 参数说明。
        源语言 (可选): 参数说明。默认值为 'auto'。
        目标语言 (可选): 参数说明。默认值为 'zh'。

    """
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9'
    }

    data = {
        'jsonrpc': '2.0',
        'method': 'LMT_handle_texts',
        'params': {
            'splitting': 'newlines',
            'lang': {
                'source_lang_user_selected': 源语言.upper(),
                'target_lang': 目标语言.upper()
            },
            'texts': [{
                'text': 欲翻译文本,
                'requestAlternatives': 3
            }],
            'timestamp': int(time.time() * 1000),
        },
        'id': getRandomNumber()
    }
    response = requests.post('https://www2.deepl.com/jsonrpc', headers=headers, data=json.dumps(data).encode('utf-8'),
                             # proxies={'http': '127.0.0.1:6667', 'https': '127.0.0.1:6667'}
                             )
    # print(response.text)
    result = response.json()
    return result.get("result", {}).get("texts", [{}])[0].get("text", "")


if __name__ == '__main__':
    print(DeepL翻译("hello world", 目标语言='zh'))
    print(DeepL翻译("你好世界", 目标语言='en'))

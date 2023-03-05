import hashlib
import requests


def 爱词霸翻译(欲翻译文本, 源语言='auto', 目标语言='zh'):
    key = "6key_web_fanyiifanyiweb8hc9s98e" + 欲翻译文本.strip()
    sign = hashlib.md5(key.encode()).hexdigest()[:16]

    params = {
        'c': 'trans',
        'm': 'fy',
        'client': 6,
        'auth_user': 'key_web_fanyi',
        'sign': sign
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'q': 欲翻译文本, 'from': 源语言, 'to': 目标语言}
    response = requests.post("http://ifanyi.iciba.com/index.php", data=data, params=params, headers=headers)

    result = response.json()
    # print(result)

    content = result.get('content', {})
    to_paragraphs = content.get('out', '')

    return to_paragraphs


if __name__ == '__main__':
    print(搜狗翻译("hello world"))
    print(搜狗翻译("你好世界", 目标语言='en'))

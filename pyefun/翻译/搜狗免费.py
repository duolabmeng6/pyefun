import requests
import re


def 搜狗翻译(欲翻译文本, 源语言='auto', 目标语言='zh'):
    """
    搜狗翻译 的功能说明（请补充）。

    Args:
        欲翻译文本: 参数说明。
        源语言 (可选): 参数说明。默认值为 'auto'。
        目标语言 (可选): 参数说明。默认值为 'zh'。

    """
    url = 'https://fanyi.sogou.com/text'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {
        'keyword': 欲翻译文本,
        'transfrom': 源语言,
        'transto': 目标语言,
        'model': 'general',
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.text

    # 提取翻译结果
    pattern = r'"dit":"([^"]*)"'
    match = re.search(pattern, data)
    text = match.group(1) if match else ''
    return text


if __name__ == '__main__':
    print(搜狗翻译("hello world"))
    print(搜狗翻译("你好世界", 目标语言='en'))

import requests


def 阿里云翻译2(欲翻译文本, 源语言='auto', 目标语言='zh'):
    # 欲翻译文本 url编码
    """
    阿里云翻译2 的功能说明（请补充）。

    Args:
        欲翻译文本: 参数说明。
        源语言 (可选): 参数说明。默认值为 'auto'。
        目标语言 (可选): 参数说明。默认值为 'zh'。

    """
    欲翻译文本 = requests.utils.quote(欲翻译文本)

    url = f"https://translate.alibaba.com/api/translate/text?domain=general&query={欲翻译文本}&srcLang={源语言}&tgtLang={目标语言}"
    headers = {
        "Host": "translate.alibaba.com",
        "Cookie": "xman_us_f=x_l=1; xman_t=V6c1xatsl3xJqeIlbQ++JhI7Btqfg488sRpAoO/5Amt7JsaysHLnVdbDg3LLo7O6; acs_usuc_t=acs_rt=87ba93aba09f4703b0d8709b8873ca8c; acs_t=jlhH5HD3A+qW6FE5oN0ZUh/hPFB54QO9BW0GhyHc8Y+1+upx+iu1wenSF5t+HHAg; xman_f=NaoZ/ox90EPhyKabS/QZYOyauY+wntq5gPQIrco4qC/RWSX454dJwEfT64fwTBnms09wRIQayGfryUGc+Neg2UMBtn0dbR5xzNuNM7JgLvOE9vsD53HiDQ==; __itrace_wid=cfacd9a5-93a4-48ae-097e-3817f7932d5a; cna=jvWAHDS/rikCAcor6mg9NxST; xlly_s=1; tfstk=ciHVBQVX9R0SL5n9J82ZT2okCFeAZLFzTLr3iFsMIAXAZ7Pci37TqGbi4cjPSSf..; l=fBQEEB8RTq2QnCxhBOfZourza77TAIRfguPzaNbMi9fP_D5p5tKfB68wRvY9CnGVEsK653--PjLJB0LnBy49lTYhxJRVakp09dTnwpzHU; isg=BPX1ocu9-k7kRB7y4UMfO7XBBHevcqmE6vdiO3cammy7ThRAO8PiVX2ImBL4DsE8",
        "accept": "*/*",
        "origin": "https://translate.alibaba.com",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "accept-language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "referer": "https://translate.alibaba.com/",
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    if not data['success']:
        return data['message']

    return data['data']['translateText']


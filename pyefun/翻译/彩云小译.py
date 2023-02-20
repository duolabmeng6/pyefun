import requests
import json

def 彩云小译翻译(token, 欲翻译文本, 源语言='auto', 目标语言='zh'):
    try:
        url = "http://api.interpreter.caiyunai.com/v1/translator"
        payload = {
            "source": [欲翻译文本],
            "trans_type": 源语言 + "2" + 目标语言,
            "request_id": "demo",
            "detect": True,
        }
        headers = {
            'content-type': "application/json",
            'x-authorization': "token " + token,
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        # print(response.text)
        # print(json.loads(response.text)['target'][0])
        return json.loads(response.text)['target'][0]

    except Exception as e:
        print(e)
        return None

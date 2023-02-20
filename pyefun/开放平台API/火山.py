"""
需要安装
   pip install --upgrade volcengine

"""
import json

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service

def 火山翻译(AccessKeyID, SecretAccessKey, 欲翻译文本, 源语言='auto', 目标语言='zh'):

    try:
        k_access_key = AccessKeyID  # https://console.volcengine.com/iam/keymanage/
        k_secret_key = SecretAccessKey
        k_service_info = \
            ServiceInfo('open.volcengineapi.com',
                        {'Content-Type': 'application/json'},
                        Credentials(k_access_key, k_secret_key, 'translate', 'cn-north-1'),
                        5,
                        5)
        k_query = {
            'Action': 'TranslateText',
            'Version': '2020-06-01'
        }
        k_api_info = {
            'translate': ApiInfo('POST', '/', k_query, {}, {})
        }
        service = Service(k_service_info, k_api_info)
        if 源语言 == 'auto':
            源语言 = ''
        body = {
            'SourceLanguage': 源语言,
            'TargetLanguage': 目标语言,
            'TextList': [欲翻译文本],
        }
        # {'TranslationList': [{'Translation': '你好世界', 'DetectedSourceLanguage': 'en', 'Extra': None}], 'ResponseMetaData': {'RequestId': '20230220232842232FAD39F84F7DD4FC60', 'Action': 'TranslateText', 'Version': '2020-06-01', 'Service': 'translate', 'Region': 'cn-north-1'}}
        res = service.json('translate', {}, json.dumps(body))
        # print(json.loads(res))
        return json.loads(res)['TranslationList'][0]['Translation']
    except Exception as e:
        print(e)

        return None

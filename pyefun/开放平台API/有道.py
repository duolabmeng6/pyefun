import sys
import uuid
import requests
import hashlib
from imp import reload

import time

reload(sys)


def 有道翻译(app_id, SecretAccessKey, 欲翻译文本, 源语言='auto', 目标语言='zh'):
    try:
        YOUDAO_URL = 'https://openapi.youdao.com/api'
        APP_KEY = app_id
        APP_SECRET = SecretAccessKey

        def encrypt(signStr):
            hash_algorithm = hashlib.sha256()
            hash_algorithm.update(signStr.encode('utf-8'))
            return hash_algorithm.hexdigest()

        def truncate(q):
            if q is None:
                return None
            size = len(q)
            return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

        def do_request(data):
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            return requests.post(YOUDAO_URL, data=data, headers=headers)

        q = 欲翻译文本
        data = {}
        data['from'] = 源语言
        data['to'] = 目标语言
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
        sign = encrypt(signStr)
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign
        # data['vocabId'] = "您的用户词表ID"
        response = do_request(data)
        # print(response.json())
        return response.json()['translation'][0]
    except Exception as e:
        print(e)
        return None

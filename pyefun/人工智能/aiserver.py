import logging
import json

from flask import Flask, abort
from flask import jsonify
from flask import request

from pyefun import *
from pyefun.调试 import *

import hmac
import hashlib
import base64
from datetime import datetime
import pytz
import logging

环境变量_从文本中加载至系统(读入文本(取运行目录() + "/.env"))
openai_api_key = 取环境变量("openai_api_key")
dingding_pp_secret = 取环境变量("dingding_pp_secret")
ic(openai_api_key)
ic(dingding_pp_secret)



LOG_FORMAT = '%(asctime)s -%(name)s- %(threadName)s-%(thread)d - %(levelname)s - %(message)s'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#日志配置
logging.basicConfig(level=logging.INFO,format=LOG_FORMAT,datefmt=DATE_FORMAT)



def validate_sign(sign, ts, **kwargs):

    if not sign or not ts:
        return False

    """时间有效期 10 秒"""
    # 获取服务端当前时间戳
    china_timezone = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz=china_timezone)
    server_timestamp = int(now.timestamp() * 1000)
    if server_timestamp - int(ts) > 10000:
        logging.info("dingding requests ts:= " + str(ts) + "server_ts:= " + str(server_timestamp))
        return False

    # 校验sign
    client_timestamp = ts
    app_secret = dingding_pp_secret

    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(client_timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')

    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    new_sign = base64.b64encode(hmac_code).decode('utf-8')

    if sign == new_sign:
        return True
    else:
        logging.info("dingding requests c_sign:= " + ts + "s_sign:= " + new_sign)
        return False


LOG_FORMAT = '%(asctime)s -%(name)s- %(threadName)s-%(thread)d - %(levelname)s - %(message)s'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# 日志配置
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello dingding bot!'

import ChatGPT
import 图像生成

@app.route('/aichat', methods=['POST'])
def aichat():
    data = request.get_json()
    headers = request.headers

    """校验sign"""
    sign = headers.get("Sign")
    ts = headers.get("Timestamp")

    if not validate_sign(sign, ts):
        logging.error("dingding request sign is invalid")
        abort(403)

    logging.info("dingding request body: data:= " + json.dumps(data) + "; headers:= " + json.dumps(dict(headers)))
    收到的内容 = data['text']['content']

    # 机器人文字回答
    # 收到的内容 = data['text']['content']
    # 机器人回答 = ChatGPT.聊天机器人(openai_api_key,收到的内容)
    # ic(收到的内容)
    # ic(机器人回答)
    # rsp_json = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": "回答:" + 机器人回答
    #     }
    # }
    # 回复图片
    图片地址 = 图像生成.图像生成(openai_api_key,收到的内容)
    # 图片地址 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-plJUbB0vyfjyl4L6c0WhhiQl/user-PEqbKP15TT4oNWQqC8hlA8tF/img-YTp0EKjLMJaeCMlZIJxy6iyK.png?st=2023-02-18T18%3A21%3A29Z&se=2023-02-18T20%3A21%3A29Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-18T18%3A18%3A08Z&ske=2023-02-19T18%3A18%3A08Z&sks=b&skv=2021-08-06&sig=cb%2Bd8BdZE1o1EQ4v5BGHLSJmxMDiDC1HgV%2B92Z/mSQM%3D"
    # print(图片地址)
    rsp_json = {
            "msgtype": "markdown",
            "markdown": {
                "title": "已生成",
                "text": 收到的内容 + "\n ![screenshot]({0})".format(图片地址),
            },
    }
    return jsonify(rsp_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6688)

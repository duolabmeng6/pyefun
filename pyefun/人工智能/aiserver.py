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
dingding_pp_secret_image = 取环境变量("dingding_pp_secret_image")

钉钉webhook机器人地址 = 取环境变量("钉钉webhook机器人地址")
钉钉webhook机器人秘钥 = 取环境变量("钉钉webhook机器人秘钥")

ic(openai_api_key)
ic(dingding_pp_secret)
ic(dingding_pp_secret_image)
ic(钉钉webhook机器人地址)
ic(钉钉webhook机器人秘钥)

LOG_FORMAT = '%(asctime)s -%(name)s- %(threadName)s-%(thread)d - %(levelname)s - %(message)s'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# 日志配置
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def validate_sign(sign, ts, app_secret, **kwargs):
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
from pyefun.模块.钉钉机器人 import *

全局机器人 = []


@app.route('/aichat', methods=['POST'])
def aichat():
    global 全局机器人
    data = request.get_json()
    headers = request.headers
    sign = headers.get("Sign")
    ts = headers.get("Timestamp")
    if not validate_sign(sign, ts, dingding_pp_secret):
        logging.error("dingding request sign is invalid")
        abort(403)

    logging.info("dingding request body: data:= " + json.dumps(data) + "; headers:= " + json.dumps(dict(headers)))
    senderCorpId = data['senderCorpId']

    收到的内容 = data['text']['content']

    # 检查全局机器人是否存在 senderCorpId
    机器人对象 = None
    for i in 全局机器人:
        if i['senderCorpId'] == senderCorpId:
            机器人对象 = i['机器人对象']
            break
    if 机器人对象 == None:
        机器人对象 = ChatGPT.机器人连续聊天(openai_api_key)
        全局机器人.append({
            "senderCorpId": senderCorpId,
            "机器人对象": 机器人对象
        })

    if 判断文本(收到的内容, ["清空"]):
        机器人对象.清空对话()
        return jsonify({
            "msgtype": "text",
            "text": {
                "content": "清空成功"
            }
        })

    # 机器人对象 = ChatGPT.机器人连续聊天(openai_api_key)
    机器人回答 = 机器人对象.发送消息(删首尾空(收到的内容))

    #
    # 收到的内容 = 删首尾空(收到的内容)
    # 机器人回答 = ChatGPT.聊天机器人(openai_api_key, 收到的内容)
    #
    # ic(收到的内容)
    # ic(机器人回答)
    # if 机器人回答 == "":
    #     机器人回答 = "我不知道"

    rsp_json = {
        # "text": {
        #     "content": 机器人回答
        # },
        # "msgtype": "text"
        "msgtype": "empty"
    }

    机器人 = 钉钉机器人(钉钉webhook机器人地址, 钉钉webhook机器人秘钥)
#     机器人.发送markdown消息("""### {0} \n__________ \n
# {1}""".format(收到的内容, 机器人回答))

    机器人.发送markdown消息("""{1}""".format(收到的内容, 机器人回答))

    return jsonify(rsp_json)


@app.route('/aichat_image', methods=['POST'])
def aichat_image():
    data = request.get_json()
    headers = request.headers

    """校验sign"""
    sign = headers.get("Sign")
    ts = headers.get("Timestamp")

    if not validate_sign(sign, ts, dingding_pp_secret_image):
        logging.error("dingding request sign is invalid")
        abort(403)
    logging.info("dingding request body: data:= " + json.dumps(data) + "; headers:= " + json.dumps(dict(headers)))

    收到的内容 = data['text']['content']
    图片地址 = 图像生成.图像生成(openai_api_key, 收到的内容)
    ic(收到的内容)
    ic(图片地址)
    rsp_json = {
        "msgtype": "markdown",
        "markdown": {
            "title": "已生成",
            "text": """### {0} \n__________ \n  
![screenshot]({1})""".format(收到的内容, 图片地址),
        },
    }
    return jsonify(rsp_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6688)

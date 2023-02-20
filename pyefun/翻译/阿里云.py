"""
需要安装
pip install aliyun-python-sdk-core # 安装阿里云SDK核心库
pip install aliyun-python-sdk-alimt # 安装机器翻译


"""

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalimt.request.v20181012 import TranslateRequest
import json


def 阿里云翻译(AccessKeyID, AccessKeySecret, 欲翻译文本, 源语言='auto', 目标语言='zh'):
    # 创建AcsClient实例
    client = AcsClient(
        AccessKeyID,  # 阿里云账号的AccessKey ID
        AccessKeySecret,  # 阿里云账号Access Key Secret
        "cn-hangzhou"  # 地域ID
    );
    # 创建request，并设置参数
    try:
        request = TranslateRequest.TranslateRequest()
        request.set_SourceLanguage(源语言)  # 源语言
        request.set_Scene("general")  # 设置场景，商品标题：title，商品描述：description，商品沟通：communication
        request.set_SourceText(欲翻译文本)  # 原文
        request.set_FormatType("text")  # 翻译文本的格式
        request.set_TargetLanguage(目标语言)  # 目标语言
        request.set_method("POST")
        # 发起API请求并显示返回值
        response = client.do_action_with_exception(request)
        json数据 = json.loads(response)
        return json数据["Data"]["Translated"]
    except Exception as e:
        print(e)
        return None


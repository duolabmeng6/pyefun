import requests
from pyefun import *
from pyefun.encoding.ebase64 import *

# 用 docker 部署 PaddleOCR 开箱即用 通用文字识别
# https://github.com/duolabmeng6/paddlehub_ppocr

def ocr(文件地址):
    image = base64编码(读入文件(文件地址))
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://127.0.0.1:9000/predict/ocr_system", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")

print(ocr("./test.png"))

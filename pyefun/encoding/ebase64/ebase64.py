import base64


def base64编码(data):
    """
        支持 bytes 字节类型 和 文本类型编码为base64
    """
    if (type(data) == str):
        data_bytes = data.encode("utf-8")
    else:
        data_bytes = data
    return str(base64.b64encode(data_bytes), encoding='utf-8')

def base64解码(data):
    """
        将base64字符串 解码为 bytes 字节集
    """
    return base64.b64decode(data)

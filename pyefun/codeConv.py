"""

.. Hint::
    编码转换


.. literalinclude:: ../../../pyefun/codeConv_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""

import binascii, hashlib, base64, hmac
from urllib import parse
from .public import *
import chardet
import io


def 编码_检查(bytes):
    """
    检测文件编码
    #Return:
    #    fileencoding: 文件编码
    #    confidence: 检测结果的置信度，百分比
    """
    detector = chardet.detect(bytes)
    # confidence = detector['confidence']
    if detector['encoding'] is None:
        detector['encoding'] = 'unknown'
        # confidence = 0.99
    return detector['encoding']


def 文本编码转换(内容: str, 来源编码: str, 目标编码: str):
    if 来源编码 == "":
        s = 内容
        来源编码 = 编码_检查(s)
        if 来源编码 == 目标编码:
            return 内容
        if not (来源编码 == "gbk" or 来源编码 == "utf-8" or 来源编码 == "GB2312"):
            return 内容

    with io.BytesIO(内容) as data:
        with io.TextIOWrapper(data, encoding=来源编码, errors='replace') as f:
            newtext = f.read().encode(encoding=目标编码)
    return newtext


@异常处理返回类型逻辑型
def 编码_UTF8编码(内容):
    return 内容.encode(encoding='UTF-8', errors='strict')


@异常处理返回类型逻辑型
def 编码_UTF8解码(内容):
    return 内容.decode(encoding='UTF-8', errors='strict')


@异常处理返回类型逻辑型
def 编码_URL编码(内容):
    return parse.quote(内容)


@异常处理返回类型逻辑型
def 编码_URL解码(内容):
    return parse.unquote(内容)


@异常处理返回类型逻辑型
def 编码_GBK编码(内容):
    return 内容.encode(encoding='GBK', errors='strict')


@异常处理返回类型逻辑型
def 编码_GBK解码(内容):
    return 内容.decode(encoding='GBK', errors='strict')


@异常处理返回类型逻辑型
def 编码_ANSI到USC2(内容):
    return ascii(内容)


@异常处理返回类型逻辑型
def 编码_USC2到ANSI(内容):
    return 内容.encode('utf-8').decode('unicode_escape')


@异常处理返回类型逻辑型
def 编码_BASE64编码(内容):
    '要编码的内容支持文本跟字节集'
    if type(内容) == str:
        return base64.b64encode(内容.encode('UTF-8')).decode("UTF-8")
    else:
        return base64.b64encode(内容).decode("UTF-8")


@异常处理返回类型逻辑型
def 编码_BASE64解码(内容, 返回字节集=False):
    '字节集用于解码图片'
    if 返回字节集:
        return base64.b64decode(内容)
    else:
        return base64.b64decode(内容).decode("UTF-8")


@异常处理返回类型逻辑型
def 加密_MD5(内容, 编码="utf-8"):
    MD5 = hashlib.md5()
    MD5.update(内容.encode(encoding=编码))
    return MD5.hexdigest()


@异常处理返回类型逻辑型
def 加密_SHA(内容, 方式=0):
    '方式： 0.SHA1 1.SHA224 2.SHA256 3.SHA384 4.SHA512'
    字典 = {0: hashlib.sha1(), 1: hashlib.sha224(), 2: hashlib.sha256(), 3: hashlib.sha384(), 4: hashlib.sha512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常处理返回类型逻辑型
def 加密_SHA3(内容, 方式=0):
    '方式： 0.SHA224 1.SHA256 2.SHA384 3.SHA512'
    字典 = {0: hashlib.sha3_224(), 1: hashlib.sha3_256(), 2: hashlib.sha3_384(), 3: hashlib.sha3_512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常处理返回类型逻辑型
def 加密_HmacSHA256(key, 内容):
    return base64.b64encode(
        hmac.new(bytes(key, encoding='utf-8'), bytes(内容, encoding='utf-8'), digestmod=hashlib.sha256).digest()).decode(
        "utf-8")


@异常处理返回类型逻辑型
def 加密_CRC32(内容):
    return binascii.crc32(内容.encode("utf-8"))


@异常处理返回类型逻辑型
def 进制_十到二(十进制数):
    """
    将十进制转换成二进制
    """
    return bin(十进制数)


@异常处理返回类型逻辑型
def 进制_十到八(十进制数):
    """
    将十进制转换成八进制(返回八进制文本)
    """
    return oct(十进制数)


@异常处理返回类型逻辑型
def 进制_十到十六(十进制长整数):
    """
    十进制到十六进制
    """
    return hex(十进制长整数)


@异常处理返回类型逻辑型
def 进制_二到十(二进制文本):
    """
    将二进制转换成十进制(返回十进制整数)
    """
    return int(二进制文本, base=2)


@异常处理返回类型逻辑型
def 进制_八到十(八进制文本:str):
    """
        将八进制转换成十进制(返回十进制整数)
    """
    return int(八进制文本, base=8)


@异常处理返回类型逻辑型
def 进制_十六到十(十六进制文本):
    return int(十六进制文本, base=16)

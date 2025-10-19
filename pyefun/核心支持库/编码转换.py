"""
编码转换。

提供常见编码检测与文本编解码、URL 编解码、哈希计算以及进制转换等工具。

依赖：chardet（用于自动检测编码）。
"""

import binascii, hashlib, base64, hmac
from urllib import parse
from .公用函数 import *
import io
from pyefun.核心支持库.公用函数 import _动态导包


def 编码_检查(bytes):
    """
    检测字节序列的文本编码。

    Args:
        bytes (bytes): 待检测的字节串。

    Returns:
        str: 编码名称；无法检测时返回 'unknown'。
    """
    chardet = _动态导包('chardet')
    detector = chardet.detect(bytes)
    # confidence = detector['confidence']
    if detector['encoding'] is None:
        detector['encoding'] = 'unknown'
        # confidence = 0.99
    return detector['encoding']


def 文本编码转换(内容: str, 来源编码: str, 目标编码: str):
    """
    将文本从来源编码转换为目标编码（返回字节串）。

    当来源编码为空字符串时尝试自动检测。

    Args:
        内容 (bytes | str): 原始内容。
        来源编码 (str): 源编码名称，例如 'utf-8'、'gbk'。
        目标编码 (str): 目标编码名称。

    Returns:
        bytes: 转换后的字节串。若无法识别或不支持的编码将原样返回。
    """
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
    """将字符串以 UTF-8 编码为字节串。"""
    return 内容.encode(encoding='UTF-8', errors='strict')


@异常处理返回类型逻辑型
def 编码_UTF8解码(内容):
    """将 UTF-8 字节串解码为字符串。"""
    return 内容.decode(encoding='UTF-8', errors='strict')


@异常处理返回类型逻辑型
def 编码_URL编码(内容):
    """对字符串做 URL 编码。"""
    return parse.quote(内容)


@异常处理返回类型逻辑型
def 编码_URL解码(内容):
    """对字符串做 URL 解码。"""
    return parse.unquote(内容)


@异常处理返回类型逻辑型
def 编码_GBK编码(内容):
    """以 GBK 编码为字节串。"""
    return 内容.encode(encoding='GBK', errors='strict')


@异常处理返回类型逻辑型
def 编码_GBK解码(内容):
    """将 GBK 字节串解码为字符串。"""
    return 内容.decode(encoding='GBK', errors='strict')


@异常处理返回类型逻辑型
def 编码_ANSI到USC2(内容):
    """将字符串转为其转义表示（类似 ASCII 展示）。"""
    return ascii(内容)


@异常处理返回类型逻辑型
def 编码_USC2到ANSI(内容):
    """从 Unicode 转义字符串恢复为正常 UTF-8 字符串。"""
    return 内容.encode('utf-8').decode('unicode_escape')


@异常处理返回类型逻辑型
def 编码_BASE64编码(内容):
    """
    Base64 编码。

    Args:
        內容 (str | bytes): 文本或字节串。

    Returns:
        str: Base64 文本。
    """
    '要编码的内容支持文本跟字节集'
    if type(内容) == str:
        return base64.b64encode(内容.encode('UTF-8')).decode("UTF-8")
    else:
        return base64.b64encode(内容).decode("UTF-8")


@异常处理返回类型逻辑型
def 编码_BASE64解码(内容, 返回字节集=False):
    """
    Base64 解码。

    Args:
        内容 (str): Base64 文本。
        返回字节集 (bool, 可选): True 返回 bytes，False 返回 UTF-8 字符串。默认 False。

    Returns:
        bytes | str: 解码结果。
    """
    '字节集用于解码图片'
    if 返回字节集:
        return base64.b64decode(内容)
    else:
        return base64.b64decode(内容).decode("UTF-8")


@异常处理返回类型逻辑型
def 加密_MD5(内容, 编码="utf-8"):
    """计算字符串的 MD5 十六进制摘要。"""
    MD5 = hashlib.md5()
    MD5.update(内容.encode(encoding=编码))
    return MD5.hexdigest()


@异常处理返回类型逻辑型
def 加密_SHA(内容, 方式=0):
    """
    计算 SHA1/224/256/384/512 摘要。

    Args:
        内容 (Any): 将以 UTF-8 编码为字节串再计算。
        方式 (int, 可选): 0=SHA1, 1=SHA224, 2=SHA256, 3=SHA384, 4=SHA512。默认 0。

    Returns:
        str: 十六进制摘要字符串。
    """
    '方式： 0.SHA1 1.SHA224 2.SHA256 3.SHA384 4.SHA512'
    字典 = {0: hashlib.sha1(), 1: hashlib.sha224(), 2: hashlib.sha256(), 3: hashlib.sha384(), 4: hashlib.sha512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常处理返回类型逻辑型
def 加密_SHA3(内容, 方式=0):
    """
    计算 SHA3-224/256/384/512 摘要。

    Args:
        内容 (Any): 将以 UTF-8 编码为字节串再计算。
        方式 (int, 可选): 0=SHA224, 1=SHA256, 2=SHA384, 3=SHA512。默认 0。

    Returns:
        str: 十六进制摘要字符串。
    """
    '方式： 0.SHA224 1.SHA256 2.SHA384 3.SHA512'
    字典 = {0: hashlib.sha3_224(), 1: hashlib.sha3_256(), 2: hashlib.sha3_384(), 3: hashlib.sha3_512()}
    字典[方式].update(str(内容).encode('utf-8'))
    return 字典[方式].hexdigest()


@异常处理返回类型逻辑型
def 加密_HmacSHA256(key, 内容):
    """
    计算 HMAC-SHA256 并以 Base64 编码返回。

    Args:
        key (str): 密钥。
        内容 (str): 文本内容。

    Returns:
        str: Base64 文本。
    """
    return base64.b64encode(
        hmac.new(bytes(key, encoding='utf-8'), bytes(内容, encoding='utf-8'), digestmod=hashlib.sha256).digest()).decode(
        "utf-8")


@异常处理返回类型逻辑型
def 加密_CRC32(内容):
    """计算字符串的 CRC32 值（以 int 返回）。"""
    return binascii.crc32(内容.encode("utf-8"))


@异常处理返回类型逻辑型
def 进制_十到二(十进制数):
    """
    将十进制转换成二进制。

    Args:
        十进制数 (int): 十进制整数。

    Returns:
        str: 形如 '0b...' 的二进制表示。
    """
    return bin(十进制数)


@异常处理返回类型逻辑型
def 进制_十到八(十进制数):
    """
    将十进制转换成八进制。

    Args:
        十进制数 (int): 十进制整数。

    Returns:
        str: 形如 '0o...' 的八进制表示。
    """
    return oct(十进制数)


@异常处理返回类型逻辑型
def 进制_十到十六(十进制长整数):
    """
    将十进制转换成十六进制。

    Args:
        十进制长整数 (int): 十进制整数。

    Returns:
        str: 形如 '0x...' 的十六进制表示。
    """
    return hex(十进制长整数)


@异常处理返回类型逻辑型
def 进制_二到十(二进制文本):
    """
    将二进制文本转换成十进制整数。

    Args:
        二进制文本 (str): 例如 '0b1010' 或 '1010'。

    Returns:
        int: 十进制整数。
    """
    return int(二进制文本, base=2)


@异常处理返回类型逻辑型
def 进制_八到十(八进制文本: str):
    """
    将八进制文本转换成十进制整数。

    Args:
        八进制文本 (str): 例如 '0o77' 或 '77'。

    Returns:
        int: 十进制整数。
    """
    return int(八进制文本, base=8)


@异常处理返回类型逻辑型
def 进制_十六到十(十六进制文本):
    """
    将十六进制文本转换成十进制整数。

    Args:
        十六进制文本 (str): 例如 '0xff' 或 'ff'。

    Returns:
        int: 十进制整数。
    """
    return int(十六进制文本, base=16)

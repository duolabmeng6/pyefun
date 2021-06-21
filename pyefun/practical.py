import uuid
import hashlib
import random
from .dirkBase import *


def 取uuid():
    return str(uuid.uuid4())

def 取短id():
    array = ["a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
             "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
             "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"]
    id = str(uuid.uuid4()).replace("-", '')
    buffer = []

    for i in range(0, 8):
        start = i * 4
        end = i * 4 + 4
        val = int(id[start:end], 16)
        buffer.append(array[val % 62])
    return "".join(buffer)

def 取md5(内容, 编码="utf-8"):
    MD5 = hashlib.md5()
    MD5.update(内容.encode(encoding=编码))
    return MD5.hexdigest()

def 数组_随机排序(items):
    return random.shuffle(items)


def 取执行文件名():
    """
    调用格式： 〈文本型〉 取执行文件名 （） - 系统核心支持库->环境存取

    英文名称：GetRunFileName

    取当前被执行的易程序文件的名称。本命令为初级命令。

    操作系统需求： Windows

    :return: commonlyUtil.py
    """
    return 文件_取文件名(__file__)


def 读环境变量(环境变量名称: str) -> str:
    """
        调用格式： 〈文本型〉 读环境变量 （文本型 环境变量名称） - 系统核心支持库->环境存取

        英文名称：GetEnv

        返回文本，它关连于一个操作系统环境变量。成功时返回所取得的值，失败则返回空文本。本命令为初级命令。

        参数<1>的名称为“环境变量名称”，类型为“文本型（text）”。

        操作系统需求： Windows、Linux

    """
    return os.environ.get(环境变量名称)


def 写环境变量(环境变量名称: str, 欲写入内容: str) -> bool:
    """
    调用格式： 〈逻辑型〉 写环境变量 （文本型 环境变量名称，文本型 欲写入内容） - 系统核心支持库->环境存取

    英文名称：PutEnv

    修改或建立指定的操作系统环境变量。成功返回真，失败返回假。本命令为初级命令。

    参数<1>的名称为“环境变量名称”，类型为“文本型（text）”。

    参数<2>的名称为“欲写入内容”，类型为“文本型（text）”。

    操作系统需求： Windows、Linux


    """
    return os.environ.setdefault(环境变量名称, 欲写入内容)


import socket


def 取主机名():
    """
    调用格式： 〈文本型〉 取主机名 （） - 系统核心支持库->网络通信

    英文名称：GetHostName

    返回本机的主机名，用作在网络通讯中标志本机地址。本命令为初级命令。

    操作系统需求： Windows

    :return:

    """
    return socket.gethostname()


def 转换为IP地址(欲转换主机名):
    """
    调用格式： 〈文本型〉 转换为IP地址 （文本型 欲转换主机名） - 系统核心支持库->网络通信

    英文名称：HostNameToIP

    将指定的主机名转换为其 IP 地址。如果失败返回空文本。本命令为初级命令。

    参数<1>的名称为“欲转换主机名”，类型为“文本型（text）”。

    操作系统需求： Windows

    """
    return socket.gethostbyname(欲转换主机名)


def 标准输入():
    """
    调用格式： 〈文本型〉 标准输入 （［逻辑型 是否回显］） - 系统核心支持库->控制台操作

    英文名称：fgets

    在标准输入设备上请求输入最多包含2048个字符的一行文本，返回用户所输入的内容。注意本命令只能在控制台程序中使用。本命令为初级命令。

    参数<1>的名称为“是否回显”，类型为“逻辑型（bool）”，可以被省略。本参数决定输入时是否显示所输入字符，为假不显示，为真显示。如果被省略，默认值为真，即回显。可以通过将本参数设置为假以输入密码等特殊信息。

    操作系统需求： Windows、Linux


    """
    return input()


def 标准输出(*args):
    """
    调用格式： 〈无返回值〉 标准输出 （［整数型 输出方向］，通用型 欲输出内容，... ） - 系统核心支持库->控制台操作

    英文名称：fputs

    在标准输出设备或标准错误设备上输出指定的内容，注意本命令只能在控制台程序中使用。本命令为初级命令。命令参数表中最后一个参数可以被重复添加。

    参数<1>的名称为“输出方向”，类型为“整数型（int）”，可以被省略。本参数提供内容所输出到的设备，可以为以下常量值之一： 1、#标准输出设备； 2、#标准错误设备。如果省略本参数，默认为“#标准输出设备”。

    参数<2>的名称为“欲输出内容”，类型为“通用型（all）”。本参数只能为文本、数值、逻辑值或日期时间。如果内容为文本且包含多行，可在各行之间用回车符 (即“字符 (13)”)、换行符 (即“字符 (10)”) 或回车换行符的组合 (即：“字符 (13) + 字符 (10)”) 来分隔。

    操作系统需求： Windows、Linux

    """
    return print(*args)


def 结束(*args, **kwargs):
    """
    调用格式： 〈无返回值〉 结束 （） - 系统核心支持库->流程控制

    英文名称：end

    本命令结束当前易程序的运行。本命令为初级命令。

    操作系统需求： Windows、Linux、Unix
    """
    return exit(args, **kwargs)


def 运行python代码(代码,全局变量=None,局部变量=None):
    '动态执行python代码并返回值'
    return eval(代码,全局变量,局部变量)

def 执行python代码(代码,全局变量=None,局部变量=None):
    '动态执行python代码,只返回None'
    return exec(代码,全局变量,局部变量)


def 目录_取文件夹大小(path):
    '传入路径是文件夹'
    size = 0.0
    for root, dirs, files in os.walk(path):
        size += sum([os.path.getsize(os.path.join(root, file)) for file in files])
    size = round(size / 1024 / 1024, 2)
    if size > 1000:
        size = round(size / 1024, 2)
        return str(size)+'-GB'
    return str(size)+'-MB'

def 取桌面目录():
    '返回当前电脑的桌面路径'
    return os.path.join(os.path.expanduser("~"),'Desktop')


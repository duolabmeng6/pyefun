"""
系统处理。

提供控制台编码设置、系统平台判断、延时与命令运行等常用系统工具函数。
"""

import time
import os
import platform
import sys
import io

def 控制台_设置编码为UTF8():
    """
    将标准输出与标准错误的编码设置为 UTF-8。

    注意：在部分环境中重设编码可能影响外部重定向行为，请评估后使用。
    """
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)


def 控制台_取当前编码为():
    """返回当前标准输出的编码。"""
    return sys.stdout.encoding


def 系统_是否为window系统():
    """判断是否为 Windows 系统。"""
    return platform.system().lower() == 'windows'


def 系统_是否为linux系统():
    """判断是否为 Linux 系统。"""
    return platform.system().lower() == 'linux'


def 系统_是否为mac系统():
    """判断是否为 macOS 系统。"""
    return platform.system().lower() == 'darwin'


# 运行
# 打开内存文件
# 取剪辑板文本
# 置剪辑板文本
# 剪辑板中可有文本
# 清除剪辑板
# 取屏幕宽度
# 取屏幕高度
# 取鼠标水平位置
# 取鼠标垂直位置
# 取颜色数
# 输入框
# 信息框
# 取文本注册项
# 取数值注册项
# 取字节集注册
# 写注册项
# 删除注册项
# 注册项是否存在
# 取默认底色
# 快照
# 读配置项
# 写配置项
# 取配置节名
# 取操作系统类别
# 多文件对话框


def 延时(秒: int):
    """休眠指定秒数。"""
    time.sleep(秒)


def 运行(cmd):
    """
    在系统 Shell 中运行命令并返回输出文本。

    Args:
        cmd (str): 命令字符串。

    Returns:
        str: 标准输出的全部文本内容。
    """
    终端 = os.popen(cmd)
    返回内容 = 终端.read()
    终端.close()
    return 返回内容

def 是否为PyInstaller编译后环境():
    """判断当前是否运行在 PyInstaller 单文件打包后的环境。"""
    try:
        base_path = sys._MEIPASS
        return True
    except Exception:
        return False

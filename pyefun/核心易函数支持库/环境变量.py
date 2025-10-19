"""
环境变量工具

- 读取 .env 文本并解析为字典
- 将 .env 文本加载到系统环境变量
- 获取与设置系统环境变量
"""

import io
import os
# import dotenv
from pyefun.核心支持库.公用函数 import _动态导包


def 环境变量_从文本中解析(env文件数据):
    """从 .env 文本中解析键值对为字典。

    :param env文件数据: 字符串形式的 .env 文件内容
    :return: dict 形式的键值对
    """
    dotenv = _动态导包("dotenv", "python-dotenv")
    fp = io.StringIO(env文件数据)
    config = dotenv.dotenv_values(stream=fp)
    fp.close()
    return config


def 环境变量_从文本中加载至系统(env文件数据, 覆盖=True) -> bool:
    """将 .env 文本内容加载进系统环境变量。

    :param env文件数据: 字符串形式的 .env 文件内容
    :param 覆盖: 是否覆盖已存在的环境变量
    :return: True/False 表示是否成功
    """
    dotenv = _动态导包("dotenv", "python-dotenv")

    fp = io.StringIO(env文件数据)
    config = dotenv.load_dotenv(stream=fp, override=覆盖)
    fp.close()
    return config


def 取系统所有环境变量():
    """获取系统的所有环境变量字典。"""
    return os.environ


def 取环境变量(环境变量名称: str) -> str:
    """读取系统环境变量。

    :param 环境变量名称: 变量名
    :return: 变量值，不存在时返回 None
    """
    return os.environ.get(环境变量名称)


def 置环境变量(环境变量名称: str, 欲写入内容: str) -> bool:
    """设置系统环境变量（若不存在则创建）。

    :param 环境变量名称: 变量名
    :param 欲写入内容: 变量值
    :return: True 表示设置成功
    """
    return os.environ.setdefault(环境变量名称, 欲写入内容)


def 环境变量_获取(环境变量名称: str) -> str:
    """读取系统环境变量（别名）。

    :param 环境变量名称: 变量名
    :return: 变量值，不存在时返回 None
    """
    return os.environ.get(环境变量名称)


def 环境变量_设置(环境变量名称: str, 欲写入内容: str) -> bool:
    """设置系统环境变量（别名）。

    :param 环境变量名称: 变量名
    :param 欲写入内容: 变量值
    :return: True 表示设置成功
    """
    return os.environ.setdefault(环境变量名称, 欲写入内容)

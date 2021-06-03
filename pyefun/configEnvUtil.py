"""

.. Hint::
    环境变量

    读入.env并且加载到系统环境变量中

.. literalinclude:: ..\..\..\example\python读取env文件.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-40

"""
from dotenv import dotenv_values, load_dotenv
import io
import os

def 环境变量_从文本中解析(env文件数据):
    fp = io.StringIO(env文件数据)
    config = dotenv_values(stream=fp)
    fp.close()
    return config

def 环境变量_从文本中加载至系统(env文件数据, 覆盖=True) -> bool:
    fp = io.StringIO(env文件数据)
    config = load_dotenv(stream=fp, override=覆盖)
    fp.close()
    return config

def 取系统所有环境变量():
    return os.environ

def 取环境变量(环境变量名称: str) -> str:
    """
        返回文本，它关连于一个操作系统环境变量。成功时返回所取得的值，失败则返回空文本。本命令为初级命令。
    """
    return os.environ.get(环境变量名称)

def 置环境变量(环境变量名称: str, 欲写入内容: str) -> bool:
    """
    修改或建立指定的操作系统环境变量。成功返回真，失败返回假。本命令为初级命令。
    """
    return os.environ.setdefault(环境变量名称, 欲写入内容)


def 环境变量_获取(环境变量名称: str) -> str:
    """
        返回文本，它关连于一个操作系统环境变量。成功时返回所取得的值，失败则返回空文本。本命令为初级命令。
    """
    return os.environ.get(环境变量名称)

def 环境变量_设置(环境变量名称: str, 欲写入内容: str) -> bool:
    """
    修改或建立指定的操作系统环境变量。成功返回真，失败返回假。本命令为初级命令。
    """
    return os.environ.setdefault(环境变量名称, 欲写入内容)

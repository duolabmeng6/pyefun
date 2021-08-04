"""

.. Hint::
    系统处理


.. literalinclude:: ../../../pyefun/systemProcessingBase_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import time
import os
import platform
import sys
import io

def 控制台_设置编码为UTF8():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)

def 控制台_取当前编码为():
    return sys.stdout.encoding


def 系统_是否为window系统():
    return platform.system().lower() == 'windows'


def 系统_是否为linux系统():
    return platform.system().lower() == 'linux'


def 系统_是否为mac系统():
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
    time.sleep(秒)


def 运行(cmd):
    p = os.popen(cmd)
    x = p.read()
    p.close()
    return x

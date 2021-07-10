"""

.. Hint::
    磁盘操作

.. literalinclude:: ../../../pyefun/dirkBase.py
    :language: python
    :caption: 代码示例
    :linenos:


"""
import os
import sys
import stat
import shutil
from .public import *
from .stringBase import *


# 取磁盘总空间
# 取磁盘剩余空间
# 取磁盘卷标
# 置磁盘卷标
# 改变驱动器
# 改变目录 -
# 取当前目录 -
# 创建目录 -
# 删除目录 -
# 复制文件 -
# 移动文件 -
# 删除文件 -
# 文件更名 -
# 文件是否存在 -
# 寻找文件
# 取文件时间
# 取文件尺寸
# 取文件属性
# 置文件属性
# 取临时文件名
# 读入文件 -
# 写到文件 -


def 取运行目录():
    return sys.path[0]


def 取当前目录():
    return os.getcwd()


# 调用格式： 〈逻辑型〉 复制文件 （文本型 被复制的文件名，文本型 复制到的文件名） - 系统核心支持库->磁盘操作
# 英文名称：FileCopy
# 成功返回真，失败返回假。本命令为初级命令。
# 参数<1>的名称为“被复制的文件名”，类型为“文本型（text）”。
# 参数<2>的名称为“复制到的文件名”，类型为“文本型（text）”。
#
# 操作系统需求： Windows、Linux
@异常处理返回类型逻辑型
def 复制文件(被复制的文件名, 复制到的文件名):
    shutil.copyfile(被复制的文件名, 复制到的文件名)
    return True


@异常处理返回类型逻辑型
def 复制目录(被复制的目录, 复制到的目录):
    shutil.copytree(被复制的目录, 复制到的目录)
    return True


# 调用格式： 〈逻辑型〉 移动文件 （文本型 被移动的文件，文本型 移动到的位置） - 系统核心支持库->磁盘操作
# 英文名称：FileMove
# 将文件从一个位置移动到另外一个位置。成功返回真，失败返回假。本命令为初级命令。
# 参数<1>的名称为“被移动的文件”，类型为“文本型（text）”。
# 参数<2>的名称为“移动到的位置”，类型为“文本型（text）”。
#
# 操作系统需求： Windows、Linux
@异常处理返回类型逻辑型
def 移动文件(被移动的文件, 移动到的位置):
    shutil.move(被移动的文件, 移动到的位置)
    return True


def 文件_目录文件列表(路径='.'):
    '.为单前目录，..为上级目录，目录下的文件名,文件夹名,不带路径'
    return os.listdir(路径)


def 文件_遍历子目录(路径='.'):
    '成功返回列表：(路径, [包含目录], [包含文件]),用法 for root, dirs, files in os.walk("..", topdown=False):'
    return list(os.walk(路径))


@异常处理返回类型逻辑型
def 创建目录(路径, 自动创建目录=True):
    if 文件是否存在(路径):
        return True
    if 自动创建目录:
        try:
            access = 0o777
            original_umask = os.umask(000)
            os.makedirs(路径, access)
        finally:
            os.umask(original_umask)
    else:
        os.mkdir(路径)
    return True


# 调用格式： 〈逻辑型〉 写到文件 （文本型 文件名，字节集 欲写入文件的数据，... ） - 系统核心支持库->磁盘操作
# 英文名称：WriteFile
# 本命令用作将一个或数个字节集顺序写到指定文件中，文件原有内容被覆盖。成功返回真，失败返回假。本命令为初级命令。命令参数表中最后一个参数可以被重复添加。
# 参数<1>的名称为“文件名”，类型为“文本型（text）”。
# 参数<2>的名称为“欲写入文件的数据”，类型为“字节集（bin）”。
#
# 操作系统需求： Windows、Linux

@异常处理返回类型逻辑型
def 写到文件(文件名, 欲写入文件的数据):
    if (type(欲写入文件的数据) == str):
        欲写入文件的数据 = bytes(欲写入文件的数据, encoding="utf-8")

    with open(文件名, 'wb') as f:
        f.write(欲写入文件的数据)
    return True


def 读入文件(文件名):
    if 文件是否存在(文件名) == False:
        return b""
    '方式默认用r 字节集用rb 长度默认读取全部,更多模式参考https://www.runoob.com/python3/python3-func-open.html'
    with open(文件名, 'rb') as f:
        return f.read(-1)


@异常处理返回类型逻辑型
def 删除文件(路径):
    '成功返回True,用于删除文件,如果文件是一个目录则返回一个错误'
    os.remove(路径)
    return True


@异常处理返回类型逻辑型
def 删除目录(路径, 递归删除=False):
    if 文件是否存在(路径) == False:
        return False
    if 递归删除:
        shutil.rmtree(路径)
    else:
        os.rmdir(路径)
    return True


@异常处理返回类型逻辑型
def 文件更名(原文件名, 新文件名):
    '成功返回True,可以是文件或文件夹'
    # os.rename(原文件名, 新文件名)
    shutil.move(原文件名, 新文件名)

    return True


def 文件_路径取扩展名(路径):
    return os.path.splitext(路径)[1]


def 文件_取文件名(路径, 是否需要拓展名=True):
    if 是否需要拓展名:
        return os.path.basename(路径)
    else:
        return os.path.splitext(os.path.basename(路径))[0]


def 路径_取目录名(路径):
    return os.path.basename(路径)


def 文件_取目录(路径):
    '去掉文件名，返回目录路径'
    return os.path.dirname(路径)


@异常处理返回类型逻辑型
def 改变目录(路径):
    '成功返回True'
    os.chdir(路径)
    return True


@异常处理返回类型逻辑型
def 改变当前进程目录(路径):
    '成功返回True'
    os.chroot(路径)
    return True


def 文件_检查权限(路径, 权限=os.F_OK):
    '类型：0 是否存在 1 是否可读 2 是否可写 3 是否可执行，返回True或False'
    # {0: os.F_OK, 1: os.R_OK, 2: os.W_OK, 3: os.X_OK}
    return os.access(路径, 权限)


def 文件_是否为绝对路径(路径):
    '传入路径返回True或False'
    return os.path.isabs(路径)


def 文件_是否为目录(路径):
    '传入路径返回True或False'
    return os.path.isdir(路径)


def 文件_是否为文件(路径):
    '传入路径返回True或False'
    return os.path.isfile(路径)


def 文件是否存在(路径):
    '传入路径返回True或False'
    return os.path.exists(路径)


def 文件_取文件大小(路径):
    '返回文件长度'
    return os.path.getsize(路径)


def 文件_获取文件信息(路径):
    '成功返回(上次访问时间,修改时间,文件大小)，返回的是10位时间戳'
    结果 = os.stat(路径)
    return (结果.st_atime, 结果.st_mtime, 结果.st_size)


def 文件_修改文件时间(路径, 时间):
    '成功返回True,传入的时间为10位时间戳元组类型(访问时间戳,修改时间戳)'
    os.utime(路径, 时间)
    return True


# 调用格式： 〈日期时间型〉 取文件时间 （文本型 文件名） - 系统核心支持库->磁盘操作
# 英文名称：FileDateTime
# 返回指定文件被创建或最后修改后的日期和时间。如果该文件不存在，将返回100年1月1日。本命令为初级命令。
# 参数<1>的名称为“文件名”，类型为“文本型（text）”。
#
# 操作系统需求： Windows、Linux
def 取文件访问时间(路径):
    '返回时间戳'
    return os.path.getatime(路径)


def 取文件创建时间(路径):
    '返回时间戳'
    return os.path.getctime(路径)


def 取文件修改时间(路径):
    '返回时间戳'
    return os.path.getmtime(路径)


def 文件_修改权限(路径, 权限=stat.S_IRWXU):
    'http://www.runoob.com/python/os-chmod.html'
    # stat.S_IREAD 只读
    # stat.S_IWRITE 取消只读
    # stat.S_IRWXU 读写执行
    return os.chmod(路径, 权限)


def 文件_枚举(欲寻找的目录=".", name=".jpg", 递归子目录=True):
    list = []
    for item in os.listdir(欲寻找的目录):
        item_path = os.path.join(欲寻找的目录, item)
        if os.path.isdir(item_path):
            if (递归子目录):
                newlist = 文件_枚举(item_path, name, 递归子目录)
                for item_path in newlist:
                    list.append(item_path)
        elif os.path.isfile(item_path):
            if name in item:
                list.append(item_path)
    return list


def 目录_枚举(欲寻找的目录=".", 递归子目录=True):
    list = []
    for item in os.listdir(欲寻找的目录):
        item_path = os.path.join(欲寻找的目录, item)
        if os.path.isdir(item_path):
            list.append(item_path)
            if (递归子目录):
                newlist = 目录_枚举(item_path, 递归子目录)
                for item_path in newlist:
                    list.append(item_path)
    return list


def 文件_删除(欲删除的文件名: str) -> bool:
    return 删除文件(欲删除的文件名)


def 文件_取扩展名(路径: str) -> str:
    return 子文本替换(文件_路径取扩展名(路径), ".", "")


def 文件_更名(原文件名, 新文件名) -> bool:
    return 文件更名(原文件名, 新文件名)


def 文件_取父目录(路径) -> str:
    return os.path.dirname(路径)


def 文件_写出(文件名: str, 欲写入文件的数据) -> bool:
    dir = 文件_取父目录(文件名)
    if 文件是否存在(dir) == False:
        创建目录(dir)
    return 写到文件(文件名, 欲写入文件的数据)


@异常处理返回类型逻辑型
def 文件_追加文本(文件名: str, 欲追加的文本: str) -> bool:
    dir = 文件_取父目录(文件名)
    if 文件是否存在(dir) == False:
        创建目录(dir)
    with open(文件名, "a") as f:
        f.write(str(欲追加的文本) + "\n")
    return True


@异常处理返回类型逻辑型
def 读入文本(文件名: str) -> str:
    return 读入文件(文件名).decode('utf-8')


def 文件_保存(文件名: str, 欲写入文件的数据: bytes) -> str:
    dir = 文件_取父目录(文件名)
    if 文件是否存在(dir) == False:
        创建目录(dir)
        return 文件_写出(文件名, 欲写入文件的数据)
    else:
        data = 读入文件(文件名)
        wdata = 欲写入文件的数据
        if (data != wdata):
            return 文件_写出(文件名, 欲写入文件的数据)
    return True


def 文件从列表中选取存在的文件路径(路径列表):
    """
    匹配文件是否存在 存在则返回文件路径
    
.. code-block:: python
   :linenos:

    labelsPath = 文件从列表中选取存在的文件路径([
        "./model/labels.txt",
        "/opt/labels.txt",
        "/opt/model/labels.txt",
    ])
    """
    for v in 路径列表:
        if os.path.exists(v):
            return v
    return ''


def 路径优化(path):
    """
    把\\ // 乱七八糟的路径转化为规整的
    :param path:
    :return:
    """
    if 寻找文本(path, "\\") > -1:
        path = 子文本替换(path, "\\", "/")
    if 寻找文本(path, r"\\") > -1:
        path = 子文本替换(path, r"\\", "/")
    if 寻找文本(path, r"//") > -1:
        path = 子文本替换(path, r"//", "/")
    return os.path.normpath(path)

"""
磁盘操作。

封装文件与目录的常见操作：创建、删除、复制、移动、遍历、读写、权限与时间属性等。

说明：涉及到文件系统的函数多返回布尔值表示成功与否，异常处理通过装饰器进行兜底，不改变原有函数行为。
"""
import os
import sys
import stat
import shutil
import json
from .公用函数 import *
from .文本操作 import *


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


def 取资源文件路径(relative_path: str = "") -> str:
    """
    获取资源文件的绝对路径（兼容 PyInstaller 单文件模式）。

    Args:
        relative_path (str, 可选): 相对资源路径。默认空。

    Returns:
        str: 合成后的绝对路径。
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def 取运行目录() -> str:
    """
    获取程序运行目录。

    - 在 PyInstaller 打包后的单文件环境，返回可执行文件所在目录。
    - 其他情况返回 sys.path[0]。
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.realpath(sys.argv[0]))
    else:
        return sys.path[0]


def 取当前目录() -> str:
    """返回当前工作目录。"""
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
    """复制文件到指定位置。成功返回 True。"""
    shutil.copyfile(被复制的文件名, 复制到的文件名)
    return True


@异常处理返回类型逻辑型
def 复制目录(被复制的目录, 复制到的目录):
    """递归复制目录到指定位置。成功返回 True。"""
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
    """移动文件或目录到新位置。成功返回 True。"""
    shutil.move(被移动的文件, 移动到的位置)
    return True


def 文件_目录文件列表(路径: str = '.') -> list:
    """
    列出目录下的文件和子目录（不带路径）。

    说明：'.' 为当前目录，'..' 为上级目录。

    Args:
        路径 (str, 可选): 目标目录。默认当前目录。

    Returns:
        list[str]: 名称列表。
    """
    return os.listdir(路径)


def 文件_遍历子目录(路径: str = '.') -> list:
    """
    递归遍历目录。

    Returns:
        list[tuple]: (路径, [包含目录], [包含文件]) 列表，等价于 list(os.walk(...))。
    """
    return list(os.walk(路径))


def 文件_递归获取所有文件(路径: str = '.') -> list:
    """
    获取文件夹下所有文件的绝对路径（递归）。

    Args:
        路径 (str, 可选): 起始目录。默认当前目录。

    Returns:
        list[str]: 所有文件的绝对路径列表。
    """
    filess = []
    listFiles = os.listdir(路径)
    for i in range(0, len(listFiles)):
        path = os.path.join(路径, listFiles[i])
        if os.path.isdir(path):
            filess.extend(文件_递归获取所有文件(path))
        elif os.path.isfile(path):
            filess.append(path)
    return filess


@异常处理返回类型逻辑型
def 创建目录(路径, 自动创建目录=True):
    """
    创建目录。

    Args:
        路径 (str): 目录路径。
        自动创建目录 (bool, 可选): 使用 makedirs 递归创建并设置权限。默认 True。

    Returns:
        bool: 目录已存在或创建成功返回 True。
    """
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
    """
    将数据写入到文件（覆盖写）。

    - 当数据为 dict 或 list 时自动序列化为 JSON 文本；
    - 当数据为 str 时以 UTF-8 编码写入；
    - 其他类型应为 bytes。

    Args:
        文件名 (str): 目标文件。
        欲写入文件的数据 (bytes | str | dict | list): 写入内容。

    Returns:
        bool: 成功返回 True。
    """
    变量类型 = type(欲写入文件的数据)
    if (变量类型 == dict or 变量类型 == list):
        # 解析为json文本
        欲写入文件的数据 = json.dumps(欲写入文件的数据)
    if (type(欲写入文件的数据) == str):
        欲写入文件的数据 = bytes(欲写入文件的数据, encoding="utf-8")

    with open(文件名, 'wb') as f:
        f.write(欲写入文件的数据)
    return True


def 读入文件(文件名):
    """
    以二进制方式读入文件全部内容。

    Args:
        文件名 (str): 文件路径。

    Returns:
        bytes: 文件内容；若不存在返回空字节串。
    """
    if 文件是否存在(文件名) == False:
        return b""
    # 方式默认用r 字节集用rb 长度默认读取全部,更多模式参考https://www.runoob.com/python3/python3-func-open.html
    with open(文件名, 'rb') as f:
        return f.read(-1)


@异常处理返回类型逻辑型
def 删除文件(路径):
    """
    删除文件。

    Args:
        路径 (str): 文件路径。

    Returns:
        bool: 成功返回 True；若路径为目录将抛出异常。
    """
    os.remove(路径)
    return True


@异常处理返回类型逻辑型
def 删除目录(路径, 递归删除=False):
    """
    删除目录。

    Args:
        路径 (str): 目录路径。
        递归删除 (bool, 可选): True 则删除整个目录树，False 仅删除空目录。

    Returns:
        bool: 成功返回 True；路径不存在返回 False。
    """
    if 文件是否存在(路径) == False:
        return False
    if 递归删除:
        shutil.rmtree(路径)
    else:
        os.rmdir(路径)
    return True


@异常处理返回类型逻辑型
def 文件更名(原文件名, 新文件名):
    """
    文件或目录更名/移动。

    Returns:
        bool: 成功返回 True。
    """
    # os.rename(原文件名, 新文件名)
    shutil.move(原文件名, 新文件名)

    return True


def 文件_路径取扩展名(路径: str) -> str:
    """返回路径的扩展名（包含点）。"""
    return os.path.splitext(路径)[1]


def 文件_取文件名(路径: str, 是否需要拓展名: bool = True) -> str:
    """
    返回文件名。

    Args:
        路径 (str): 文件路径。
        是否需要拓展名 (bool, 可选): True 返回带扩展名，False 仅文件名。默认 True。

    Returns:
        str: 文件名文本。
    """
    if 是否需要拓展名:
        return os.path.basename(路径)
    else:
        return os.path.splitext(os.path.basename(路径))[0]


def 路径_取目录名(路径: str) -> str:
    """返回路径的末级目录名称。"""
    return os.path.basename(路径)


def 文件_取目录(路径: str) -> str:
    """去掉文件名，返回目录路径。"""
    return os.path.dirname(路径)


@异常处理返回类型逻辑型
def 改变目录(路径):
    """切换当前工作目录。成功返回 True。"""
    os.chdir(路径)
    return True


@异常处理返回类型逻辑型
def 改变当前进程目录(路径):
    """修改当前进程的根目录（chroot）。成功返回 True。"""
    os.chroot(路径)
    return True


def 文件_检查权限(路径, 权限=os.F_OK):
    """
    检查路径的访问权限。

    Args:
        路径 (str): 文件或目录路径。
        权限 (int, 可选): os.F_OK|os.R_OK|os.W_OK|os.X_OK。默认 os.FOK。

    Returns:
        bool: 是否满足权限。
    """
    # {0: os.F_OK, 1: os.R_OK, 2: os.W_OK, 3: os.X_OK}
    return os.access(路径, 权限)


def 文件_是否为绝对路径(路径):
    """判断是否为绝对路径。"""
    return os.path.isabs(路径)


def 文件_是否为目录(路径):
    """判断路径是否为目录。"""
    return os.path.isdir(路径)


def 文件_是否为文件(路径):
    """判断路径是否为文件。"""
    return os.path.isfile(路径)


def 文件是否存在(路径):
    """判断文件或目录是否存在。"""
    return os.path.exists(路径)


def 文件_取文件大小(路径):
    """返回文件大小（字节）。"""
    return os.path.getsize(路径)


def 文件_获取文件信息(路径):
    """
    获取文件信息（时间戳与大小）。

    Returns:
        tuple: (上次访问时间, 修改时间, 文件大小)。时间为时间戳（秒）。
    """
    结果 = os.stat(路径)
    return (结果.st_atime, 结果.st_mtime, 结果.st_size)


def 文件_修改文件时间(路径, 时间):
    """
    修改文件的访问/修改时间。

    Args:
        路径 (str): 文件路径。
        时间 (tuple): (访问时间戳, 修改时间戳)。

    Returns:
        bool: 成功返回 True。
    """
    os.utime(路径, 时间)
    return True


# 调用格式： 〈日期时间型〉 取文件时间 （文本型 文件名） - 系统核心支持库->磁盘操作
# 英文名称：FileDateTime
# 返回指定文件被创建或最后修改后的日期和时间。如果该文件不存在，将返回100年1月1日。本命令为初级命令。
# 参数<1>的名称为“文件名”，类型为“文本型（text）”。
#
# 操作系统需求： Windows、Linux
def 取文件访问时间(路径):
    """返回文件上次访问时间戳。"""
    return os.path.getatime(路径)


def 取文件创建时间(路径):
    """返回文件创建时间戳。"""
    return os.path.getctime(路径)


def 取文件修改时间(路径):
    """返回文件修改时间戳。"""
    return os.path.getmtime(路径)


def 文件_修改权限(路径, 权限=stat.S_IRWXU):
    """
    修改路径权限。

    参考: http://www.runoob.com/python/os-chmod.html

    Returns:
        int: 返回 os.chmod 的结果。
    """
    # stat.S_IREAD 只读
    # stat.S_IWRITE 取消只读
    # stat.S_IRWXU 读写执行
    return os.chmod(路径, 权限)


def 文件_枚举(欲寻找的目录: str = ".", name: str = ".jpg", 递归子目录: bool = True) -> list:
    """
    枚举目录下指定模式的文件路径列表。

    Args:
        欲寻找的目录 (str, 可选): 起始目录。默认当前目录。
        name (str, 可选): 名称包含的子串（简单包含匹配）。默认 ".jpg"。
        递归子目录 (bool, 可选): 是否递归检索。默认 True。

    Returns:
        list[str]: 文件路径列表。
    """
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


def 目录_枚举(欲寻找的目录: str = ".", 递归子目录: bool = True) -> list:
    """
    枚举目录（返回所有目录路径）。

    Args:
        欲寻找的目录 (str, 可选): 起始目录。默认当前目录。
        递归子目录 (bool, 可选): 是否递归检索。默认 True。

    Returns:
        list[str]: 目录路径列表。
    """
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
    """删除文件（包装 删除文件）。"""
    return 删除文件(欲删除的文件名)


def 文件_取扩展名(路径: str) -> str:
    """返回去掉点的扩展名。"""
    return 子文本替换(文件_路径取扩展名(路径), ".", "")


def 文件_更名(原文件名, 新文件名) -> bool:
    """包装 文件更名。"""
    return 文件更名(原文件名, 新文件名)


def 文件_取父目录(路径) -> str:
    """返回父目录路径。"""
    return os.path.dirname(路径)


def 文件_写出(文件名: str, 欲写入文件的数据) -> bool:
    """
    将数据写出到文件（若目录不存在则自动创建）。

    Args:
        文件名 (str): 目标文件路径。
        欲写入文件的数据 (Any): 写入内容。

    Returns:
        bool: 成功返回 True。
    """
    dir = 文件_取父目录(文件名)
    if 文件是否存在(dir) == False:
        创建目录(dir)
    return 写到文件(文件名, 欲写入文件的数据)


@异常处理返回类型逻辑型
def 文件_追加文本(文件名: str, 欲追加的文本: str) -> bool:
    """
    在文件末尾追加一行文本并换行。

    Args:
        文件名 (str): 目标文件。
        欲追加的文本 (str): 文本内容。

    Returns:
        bool: 成功返回 True。
    """
    dir = 文件_取父目录(文件名)
    if 文件是否存在(dir) == False:
        创建目录(dir)
    with open(文件名, "a") as f:
        f.write(str(欲追加的文本) + "\n")
    return True


@异常处理返回类型逻辑型
def 读入文本(文件名: str) -> str:
    """以 UTF-8 解码读入文件全部文本。"""
    return 读入文件(文件名).decode('utf-8')


def 文件_保存(文件名: str, 欲写入文件的数据: bytes) -> str:
    """
    若内容发生变化则写出，否则跳过以减少 IO。

    Args:
        文件名 (str): 目标文件。
        欲写入文件的数据 (bytes): 新内容（字节串）。

    Returns:
        bool: 写出或无需写出时均返回 True。
    """
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
    按顺序返回第一个存在的文件路径。

    Args:
        路径列表 (Sequence[str]): 候选路径列表。

    Returns:
        str: 第一个存在的文件路径；若均不存在返回空字符串。

    Examples:
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


def 路径优化(path: str) -> str:
    """
    规范化路径分隔符，统一为系统标准形式。

    将出现的 \\ 与 // 进一步规整，再通过 os.path.normpath 处理重复分隔符与 .. 等。

    Args:
        path (str): 原始路径。

    Returns:
        str: 规整后的路径。
    """
    if 寻找文本(path, "\\") > -1:
        path = 子文本替换(path, "\\", "/")
    if 寻找文本(path, r"\\") > -1:
        path = 子文本替换(path, r"\\", "/")
    if 寻找文本(path, r"//") > -1:
        path = 子文本替换(path, r"//", "/")
    return os.path.normpath(path)


def 目录_取文件夹大小(path: str) -> str:
    """
    计算文件夹占用大小（MB/GB）。

    Args:
        path (str): 目录路径。

    Returns:
        str: 形如 "12.35-MB" 或 "1.23-GB" 的字符串。
    """
    size = 0.0
    for root, dirs, files in os.walk(path):
        size += sum([os.path.getsize(os.path.join(root, file)) for file in files])
    size = round(size / 1024 / 1024, 2)
    if size > 1000:
        size = round(size / 1024, 2)
        return str(size) + '-GB'
    return str(size) + '-MB'


def 路径_合并(*paths) -> str:
    """合并多个路径片段。"""
    return os.path.join(*paths)

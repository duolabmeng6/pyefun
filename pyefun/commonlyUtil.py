import random

import ubelt as ub
from collections import OrderedDict
import operator
from .dirkBase import *
from .stringUtil import *
import hashlib
import uuid


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


def 取sha1(data, 哈希算法='sha1'):
    return ub.hash_data(data, hasher=哈希算法)


def 取md5(内容, 编码="utf-8"):
    MD5 = hashlib.md5()
    MD5.update(内容.encode(encoding=编码))
    return MD5.hexdigest()


def 取哈希(data, 哈希算法='sha1'):
    return ub.hash_data(data, hasher=哈希算法)


def 取文件哈希(文件路径, 哈希算法='sha1'):
    return ub.hash_file(文件路径, hasher=哈希算法, base='hex')


def 运行命令(str,
         运行目录=None,
         环境变量=None,
         显示信息=0,
         后台运行=False,
         shell=False
         ):
    info = ub.cmd(str,
                  cwd=运行目录,
                  env=环境变量,
                  verbose=显示信息,
                  detach=后台运行,
                  shell=shell,
                  )
    return (info['out'])


def 取缓存目录(name):
    """
    # The resource root directory is
    # ~/AppData/Roaming on Windows,
    # ~/.config on Linux and ~/Library/Application Support on Mac.
    # The cache root directory is ~/AppData/Local on Windows,
    # ~/.config on Linux and ~/Library/Caches on Mac.
    """
    return ub.shrinkuser(ub.ensure_app_cache_dir(name))


def 下载文件(url, 保存文件路径=None):
    fpath = ub.download(url, fpath=保存文件路径, verbose=0)
    return ub.shrinkuser(fpath)


def 下载文件缓存(url, 保存文件路径=None):
    fpath = ub.grabdata(url, fpath=保存文件路径, verbose=0)
    return ub.shrinkuser(fpath)


def 字典_取最小值(indexable, key=None):
    """
    # assert argmin({'a': 3, 'b': 2, 'c': 100}) == 'b'
    # assert argmin(['a', 'c', 'b', 'z', 'f']) == 0
    # assert argmin([[0, 1], [2, 3, 4], [5]], key=len) == 2
    # assert argmin({'a': 3, 'b': 2, 3: 100, 4: 4}) == 'b'
    # assert argmin(iter(['a', 'c', 'A', 'z', 'f'])) == 2
    """
    return ub.argmin(indexable, key)


def 字典_分组(数组, 类别数组):
    groups = ub.group_items(数组, 类别数组)
    return groups


def 字典_统计(数组, weights=None, ordered=False, labels=None):
    data = ub.dict_hist(数组, weights, ordered, labels)
    return data


def 字典_取子集(数组, key, default=ub.util_const.NoParam, cls=OrderedDict):
    data = ub.dict_subset(数组, key, default, cls)
    return data


def 字典_取值(字典, key, default=None):
    return list(ub.dict_take(字典, key, default))


def 字典_合并(*args):
    # 字典_取值({'a': 1, 'b': 1}, {'b': 2, 'c': 2})
    data = ub.dict_union(*args)
    return data


def 字典_差集(*args):
    # 字典_差集({'a': 1, 'b': 1}, {'a'}, {'c'})
    data = ub.dict_diff(*args)
    return data


def 字典_根据值重建(func, dict_):
    data = ub.map_vals(func, dict_)
    return data


def 字典_根据健重建(func, dict_):
    data = ub.map_keys(func, dict_)
    return data


def 字典_根据值排序(dict_, key=None, reverse=False):
    # dict_ = {'spam': 2.62, 'eggs': 1.20, 'jam': 2.92}
    # newdict = 字典_排序(dict_)
    # print(ub.repr2(newdict, nl=0))
    # {'eggs': 1.2, 'spam': 2.62, 'jam': 2.92}
    # newdict = 字典_排序(dict_, reverse=True)
    # print(ub.repr2(newdict, nl=0))
    # {'jam': 2.92, 'spam': 2.62, 'eggs': 1.2}
    # newdict = 字典_排序(dict_, key=lambda x: x % 1.6)
    # print(ub.repr2(newdict, nl=0))
    # {'spam': 2.62, 'eggs': 1.2, 'jam': 2.92}
    data = ub.sorted_vals(dict_, key, reverse)
    return data


def 字典_根据键排序(dict_, key=None, reverse=False):
    # import ubelt as ub
    # dict_ = {'spam': 2.62, 'eggs': 1.20, 'jam': 2.92}
    # newdict = sorted_keys(dict_)
    # print(ub.repr2(newdict, nl=0))
    # {'eggs': 1.2, 'jam': 2.92, 'spam': 2.62}
    # newdict = sorted_keys(dict_, reverse=True)
    # print(ub.repr2(newdict, nl=0))
    # {'spam': 2.62, 'jam': 2.92, 'eggs': 1.2}
    # newdict = sorted_keys(dict_, key=lambda x: sum(map(ord, x)))
    # print(ub.repr2(newdict, nl=0))
    # {'jam': 2.92, 'eggs': 1.2, 'spam': 2.62}
    data = ub.sorted_keys(dict_, key, reverse)
    return data


def 字典_交换健值(dict_, 唯一值=True):
    data = ub.invert_dict(dict_, unique_vals=唯一值)
    return data


def 字典_查找重复项(items, 至少出现=2, key=None):
    data = ub.util_dict.find_duplicates(items, 至少出现, key)
    return data


def 灵活字典():
    return ub.AutoDict()


def 灵活有序字典():
    return ub.AutoOrderedDict()


def 数组_合并为字典(items1, items2, cls=dict):
    return ub.dzip(items1, items2, cls)


def 导入包_从路径(路径):
    return ub.import_module_from_path(路径)


def 创建连接(文件路径, 目标路径, 覆盖=False, 显示信息=0):
    return ub.symlink(文件路径, 目标路径, 覆盖, 显示信息)


def 数组_查找重复项(items, 至少出现=2):
    data = ub.find_duplicates(items, k=至少出现)
    return data


def 数组_随机排序(items):
    return random.shuffle(items)


def 命令行_获取参数(参数名, 默认值=ub.util_const.NoParam, argv=None):
    return ub.argval(参数名, 默认值, argv)


def 命令行_是否存在参数(参数名, argv=None):
    return ub.argflag(参数名, argv)


def 内存缓存(func):
    # 缓存函数结果
    return ub.memoize(func)


def 内存缓存方法(func):
    # 缓存方法函数结果
    return ub.memoize_method(func)


def 内存缓存属性(func):
    # 只会执行1次不可变更
    return ub.memoize_property(func)


def 路径_名字处理(路径, 末尾='', 前缀='', 扩展名=None, 名称=None, dpath=None,
            relative=None, 不包含点=False):
    return ub.augpath(路径, 末尾, 前缀, 扩展名, 名称, dpath, relative, 不包含点)


def 路径_取用户目录(用户名=None):
    # 返回某个用户主目录的路径。
    return ub.userhome(用户名)


def 路径_替换为用户路径(path, home='~'):
    # 返回某个用户主目录的路径。
    return ub.shrinkuser(path, home)


def 路径_展开路径(path):
    r"""

    :param path:  ~/foo
    :return: C:\Users\foo
    """

    return 路径_优化路径(ub.expandpath(path))


def 路径_优化路径(path):
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
    return ub.util_path.normpath(path)


def 路径_合并(*path):
    """
    a b c d 合并为 a/b/c/d 并且自动优化路径
    :param path:
    :return:
    """
    return 路径_优化路径(ub.util_path.join(*path))


def 目录_创建(路径, 权限=0o1777, 显示信息=None, 重建=False):
    return ub.ensuredir(路径, 权限, 显示信息, 重建)


class 临时目录(ub.TempDir):
    """
    用于创建和清理临时目录的上下文。

    #Example:
    #    with 临时目录() as self:
    #        dpath = self.dpath
    #        print(dpath)
    #        assert 文件是否存在(dpath)
    #    assert not 文件是否存在(dpath)

    #Example:
    #    self = 临时目录()
    #    dpath = self.ensure()
    #    assert exists(dpath)
    #    self.cleanup()
    #    assert not exists(dpath)
    """

    def 初始化(self):
        return self.ensure()

    def 清理(self):
        self.cleanup()

    def 取路径(self):
        return self.dpath


def 系统_取用户数据目录():
    return ub.platform_data_dir()


def 系统_取配置目录():
    return ub.platform_config_dir()


def 系统_缓存目录():
    return ub.platform_cache_dir()


def 系统_设置应用数据目录(appname, *args):
    return ub.ensure_app_data_dir(appname, *args)


def 系统_取应用配置目录(appname, *args):
    return ub.get_app_config_dir(appname, *args)


def 系统_设置应用配置目录(appname, *args):
    return ub.ensure_app_config_dir(appname, *args)


def 系统_取应用缓存目录(appname, *args):
    return ub.get_app_cache_dir(appname, *args)


def 系统_设置应用缓存目录(appname, *args):
    return ub.ensure_app_cache_dir(appname, *args)


def 查找可执行文件(名称, 匹配所有=False, 路径=None):
    """
    # 查找可执行文件('ls')
    # 查找可执行文件('ping')
    # assert 查找可执行文件('which') == 查找可执行文件(查找可执行文件('which'))
    # 查找可执行文件('which', 匹配所有=True)
    # 查找可执行文件('ping', 匹配所有=True)
    # 查找可执行文件('cmake', 匹配所有=True)
    # 查找可执行文件('nvcc', 匹配所有=True)
    # 查找可执行文件('noexist', 匹配所有=True)
    """
    return ub.find_exe(名称, 匹配所有, 路径)


def 查找文件或目录(名称, 路径=None, 精确=False):
    """
    # list(查找文件或目录('ping', exact=True))
    # list(查找文件或目录('bin'))
    # list(查找文件或目录('bin'))
    # list(查找文件或目录('*cc*'))
    # list(查找文件或目录('cmake*'))
    """
    return ub.find_path(名称, 路径, 精确)


def 文本_缩进(文本, 前缀='    '):
    return ub.util_str.indent(文本, 前缀)


def 文本_代码块(文本):
    return ub.util_str.codeblock(文本)


def 文本_段落(文本):
    return ub.util_str.paragraph(文本)


def 文本_水平合并(args, sep=''):
    """
    # import ubelt as ub
    # B = ub.repr2([[1, 2], [3, 457]], nl=1, cbr=True, trailsep=False)
    # C = ub.repr2([[5, 6], [7, 8]], nl=1, cbr=True, trailsep=False)
    # args = ['A = ', B, ' * ', C]
    # print(文本_水平合并(args))
    # A = [[1, 2],   * [[5, 6],
    #               [3, 457]]    [7, 8]]
    """
    return ub.util_str.hzcat(args, sep)


def 文本_转unicode(str):
    return ub.ensure_unicode(str)


class 控制台(ub.CaptureStdout):
    """
    控制台操作
    """

    def __init__(self, 获取内容=True, 是否启用=True):
        super().__init__(supress=获取内容, enabled=是否启用)

    def 停止(self):
        self.stop()

    def 开始(self):
        self.start()

    def 获取内容(self):
        return self.text.strip()


class 分块(ub.chunks):
    pass

    def __init__(self, items, 分块数量=None, 创建块数=None, 创建数量=None,
                 边界模式='none'):
        """
        # 边界模式（str）–确定输入的长度不能被块大小整除的最后一种情况，
        # 有效值为：{'none'，'cycle'，'replicate'}
"""
        super().__init__(
            items=items,
            chunksize=分块数量,
            nchunks=创建块数,
            total=创建数量,
            bordermode=边界模式,
        )


def 数组_索引取值(items, indices, default=ub.util_const.NoParam):
    return ub.util_list.take(items, indices, default)


def 数组_逻辑取值(items, flags):
    return ub.util_list.compress(items, flags)


def 数组_转平面(items):
    return ub.util_list.flatten(items)


def 数组_去重复(items, key=None):
    """
    # import ubelt as ub
    # import six
    # items = ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'D', 'E']
    # unique_items = list(ub.unique(items, key=six.text_type.lower))
    # assert unique_items == ['A', 'b', 'C', 'D', 'e']
    # unique_items = list(ub.unique(items))
    # assert unique_items == ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'E']
    """
    return ub.util_list.unique(items, key)


def 数组_取唯一值的索引(items, key=None):
    """
    # import ubelt as ub
    # import six
    # items = ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'D', 'E']
    # unique_items = list(ub.unique(items, key=six.text_type.lower))
    # assert unique_items == ['A', 'b', 'C', 'D', 'e']
    # unique_items = list(ub.unique(items))
    # assert unique_items == ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'E']
    """
    return ub.util_list.argunique(items, key)


def 数组_取唯一值的逻辑值(items, key=None):
    """
    # import ubelt as ub
    # import six
    # items = ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'D', 'E']
    # unique_items = list(ub.unique(items, key=six.text_type.lower))
    # assert unique_items == ['A', 'b', 'C', 'D', 'e']
    # unique_items = list(ub.unique(items))
    # assert unique_items == ['A', 'a', 'b', 'B', 'C', 'c', 'D', 'e', 'E']
    """
    return ub.util_list.unique_flags(items, key)


def 数组_构建逻辑值列表(indices, maxval=None):
    """
    #    import ubelt as ub
    #indices = [0, 1, 4]
    #mask = ub.boolmask(indices, maxval=6)
    #assert mask == [True, True, False, False, True, False]
    #mask = ub.boolmask(indices)
    #assert mask == [True, True, False, False, True]
    """
    return ub.util_list.boolmask(indices, maxval)


def 数组_是否全部相同(iterable, eq=operator.eq):
    """
    #allsame([1, 1, 1, 1])
    # True
    #allsame([])
    # True
    #allsame([0, 1])
    # False
    #iterable = iter([0, 1, 1, 1])
    #next(iterable)
    #allsame(iterable)
    # True
    #allsame(range(10))
    # False
    #allsame(range(10), lambda a, b: True)
    # True
    """
    return ub.allsame(iterable, eq)


def 数组_排序索引(indexable, key=None, reverse=False):
    return ub.argsort(indexable, key, reverse)


def 数组_取最小值(indexable, key=None):
    """


    # assert argmin({'a': 3, 'b': 2, 'c': 100}) == 'b'
    # assert argmin(['a', 'c', 'b', 'z', 'f']) == 0
    # assert argmin([[0, 1], [2, 3, 4], [5]], key=len) == 2
    # assert argmin({'a': 3, 'b': 2, 3: 100, 4: 4}) == 'b'
    # assert argmin(iter(['a', 'c', 'A', 'z', 'f'])) == 2
    """
    return ub.argmin(indexable, key)


def 数组_弹出(iterable):
    return ub.peek(iterable)


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
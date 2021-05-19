import ubelt as ub
from collections import OrderedDict


def 取sha1(data, 哈希算法='sha1'):
    return ub.hash_data(data, hasher=哈希算法)


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
    # Quickly inspect and parse output of a
    # print(ub.repr2(info))
    return (info['out'])


def 取缓存目录(name):
    # The resource root directory is
    # ~/AppData/Roaming on Windows,
    # ~/.config on Linux and ~/Library/Application Support on Mac.
    # The cache root directory is ~/AppData/Local on Windows,
    # ~/.config on Linux and ~/Library/Caches on Mac.
    return ub.shrinkuser(ub.ensure_app_cache_dir(name))


def 下载文件(url, 保存文件路径=None):
    fpath = ub.download(url, fpath=保存文件路径, verbose=0)
    return ub.shrinkuser(fpath)


def 下载文件缓存(url, 保存文件路径=None):
    fpath = ub.grabdata(url, fpath=保存文件路径, verbose=0)
    return ub.shrinkuser(fpath)


def 取最小值(indexable, key=None):
    # assert argmin({'a': 3, 'b': 2, 'c': 100}) == 'b'
    # assert argmin(['a', 'c', 'b', 'z', 'f']) == 0
    # assert argmin([[0, 1], [2, 3, 4], [5]], key=len) == 2
    # >>> assert argmin({'a': 3, 'b': 2, 3: 100, 4: 4}) == 'b'
    # >>> assert argmin(iter(['a', 'c', 'A', 'z', 'f'])) == 2
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
    # >>> dict_ = {'spam': 2.62, 'eggs': 1.20, 'jam': 2.92}
    # >>> newdict = 字典_排序(dict_)
    # >>> print(ub.repr2(newdict, nl=0))
    # {'eggs': 1.2, 'spam': 2.62, 'jam': 2.92}
    # >>> newdict = 字典_排序(dict_, reverse=True)
    # >>> print(ub.repr2(newdict, nl=0))
    # {'jam': 2.92, 'spam': 2.62, 'eggs': 1.2}
    # >>> newdict = 字典_排序(dict_, key=lambda x: x % 1.6)
    # >>> print(ub.repr2(newdict, nl=0))
    # {'spam': 2.62, 'eggs': 1.2, 'jam': 2.92}
    data = ub.sorted_vals(dict_, key, reverse)
    return data


def 字典_根据键排序(dict_, key=None, reverse=False):
    # >>> import ubelt as ub
    # >>> dict_ = {'spam': 2.62, 'eggs': 1.20, 'jam': 2.92}
    # >>> newdict = sorted_keys(dict_)
    # >>> print(ub.repr2(newdict, nl=0))
    # {'eggs': 1.2, 'jam': 2.92, 'spam': 2.62}
    # >>> newdict = sorted_keys(dict_, reverse=True)
    # >>> print(ub.repr2(newdict, nl=0))
    # {'spam': 2.62, 'jam': 2.92, 'eggs': 1.2}
    # >>> newdict = sorted_keys(dict_, key=lambda x: sum(map(ord, x)))
    # >>> print(ub.repr2(newdict, nl=0))
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


def 路径_扩展路径(path):
    return ub.expandpath(path)


def 路径_优化路径(path):
    return ub.util_path.normpath(path)


def 目录_创建(路径, 权限=0o1777, 显示信息=None, 重建=False):
    return ub.ensuredir(路径, 权限, 显示信息, 重建)


class 临时目录(ub.TempDir):
    """
    用于创建和清理临时目录的上下文。

    Example:
        with 临时目录() as self:
            dpath = self.dpath
            print(dpath)
            assert 文件是否存在(dpath)
        assert not 文件是否存在(dpath)

    Example:
        self = 临时目录()
        dpath = self.ensure()
        assert exists(dpath)
        self.cleanup()
        assert not exists(dpath)
    """
    def 初始化(self):
        return self.ensure()

    def 清理(self):
        self.cleanup()

    def 取路径(self):
        return self.dpath

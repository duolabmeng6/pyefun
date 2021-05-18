import ubelt as ub


def 取sha1(data, 哈希算法='sha1'):
    return ub.hash_data(data, hasher=哈希算法)


def 取哈希(data, 哈希算法='sha1'):
    return ub.hash_data(data, hasher=哈希算法)


def 取文件哈希(文件路径, 哈希算法='sha1'):
    return ub.hash_file(文件路径, hasher=哈希算法, base='hex')


def 运行命令(str):
    info = ub.cmd(str)
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


def 字典_分组(数组, 类别数组):
    groups = ub.group_items(数组, 类别数组)
    return groups


def 字典_统计(数组):
    data = ub.dict_hist(数组)
    return data


def 字典_取子集(数组, key):
    data = ub.dict_subset(数组, key)
    return data


def 字典_取值(字典, key, default=None):
    return list(ub.dict_take(字典, key, default))

def 字典_根据健重建值(func, dict_):
    data = ub.map_vals(func, dict_)
    return data



def 字典_健值交换( dict_,唯一值=True):
    data = ub.invert_dict(dict_, unique_vals=唯一值)
    return data

def 灵活字典():
    return ub.AutoDict()


def 导入包_从路径(路径):
    return ub.import_module_from_path(路径)


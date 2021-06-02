"""

.. Hint::
    缓存工具 用于快速缓存函数结果的

.. literalinclude:: ../../../pyefun/cacheUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""


import ubelt as ub
from os.path import basename


class 缓存(ub.Cacher):
    def __init__(self, 前缀='cache',
                 key="",
                 缓存目录="./cache/",
                 扩展名=".pkl",
                 启用=True,
                 信息级别=3,
                 哈希类型="sha1",
                 协议版本=4,
                 ):
        "显示 0 不显示 1结束显示 2概率显示 3全部显示"
        # ProgIter(iterable=迭代对象,total=总数, desc=描述, show_times=False, verbose=显示)
        super().__init__(
            fname=前缀,
            depends=ub.hash_data(key),
            dpath=缓存目录,
            # appname="my",
            ext=扩展名,
            verbose=信息级别,
            enabled=启用,
            hasher=哈希类型,
            protocol=协议版本,
        )

    def 取缓存文件路径(self, cfgstr=None):
        return self.get_fpath(cfgstr)

    def 是否存在(self, cfgstr=None):
        return self.exists(cfgstr)

    def 取缓存文件列表(self, cfgstr=None):
        exist_fnames = list(map(basename, self.existing_versions()))
        return exist_fnames

    def 清空(self, cfgstr=None):
        return self.clear(cfgstr)

    def 读入(self, cfgstr=None):
        return self.tryload(cfgstr)

    def 保存(self, data, cfgstr=None):
        self.save(data, cfgstr)


class 缓存标记(ub.CacheStamp):
    def __init__(self, 前缀='cache',
                 key="",
                 缓存目录="./cache/",
                 启用=True,
                 信息级别=3,
                 哈希类型="sha1",
                 ):
        "显示 0 不显示 1结束显示 2概率显示 3全部显示"
        # ProgIter(iterable=迭代对象,total=总数, desc=描述, show_times=False, verbose=显示)
        super().__init__(
            fname=前缀,
            depends=ub.hash_data(key),
            dpath=缓存目录,
            # appname="my",
            verbose=信息级别,
            enabled=启用,
            hasher=哈希类型,
        )

    def 检查标记(self, cfgstr=None):
        return self.expired(cfgstr)

    def 保存标记(self, cfgstr=None, product=None):
        return self.renew(cfgstr, product)

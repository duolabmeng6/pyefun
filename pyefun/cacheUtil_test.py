import unittest

from .dirkBase import *
from .cacheUtil import *
import ubelt as ub


@缓存('name', 'func')  # boilerplate:1
def func():  # boilerplate:2
    data = 'mydata'
    return data  # boilerplate:3


def compute_many_files(dpath):
    for i in range(0):
        fpath = '{}/file{}.txt'.format(dpath, i)
        open(fpath).write('foo' + str(i))


class TestCacheUtil(unittest.TestCase):

    def test_1(self):
        cacher = ub.Cacher(
            fname="mycache",
            depends=ub.hash_data('test'),
            dpath="./cache/",
            appname="my",
            ext=".pkl",
            verbose=3,
            enabled=True,
            hasher='sha1',
            protocol=3,
        )
        print(cacher.get_fpath())
        data = cacher.tryload()
        if data is None:
            myvar1 = 'result of expensive process'
            myvar2 = 'another result'
            data = myvar1, myvar2
            cacher.save(data)
        myvar1, myvar2 = data

        data = func()
        print(data)

        from ubelt.util_cache import Cacher
        from os.path import basename
        # Ensure that some data exists
        known_fpaths = set()
        # cacher = Cacher('versioned_data_v2', depends='1')
        # cacher.ensure(lambda: 'data1')
        # known_fpaths.add(cacher.get_fpath())
        # cacher = Cacher('versioned_data_v2', depends='2')
        # cacher.ensure(lambda: 'data2')
        # known_fpaths.add(cacher.get_fpath())
        # # List previously computed configs for this type
        # cacher = ub.Cacher('versioned_data_v2', depends='2')
        exist_fpaths = set(cacher.existing_versions())
        print('exist_fnames = {!r}'.format(exist_fpaths))

        exist_fnames = list(map(basename, exist_fpaths))
        print('exist_fnames = {!r}'.format(exist_fnames))
        # assert exist_fpaths.issubset(known_fpaths)

    def test_2(self):
        dpath = 取运行目录() + r"\cache"
        # You must specify a directory, unlike in Cacher where it is optional
        self = ub.CacheStamp('name', dpath=dpath, cfgstr='dependencies')
        if self.expired():
            compute_many_files(dpath)

            self.renew()
        assert not self.expired()

    def test_3(self):
        cacher = 缓存("pro", "test")
        data = cacher.读入()
        if data is None:
            myvar1 = 'result of expensive process'
            myvar2 = 'another result'
            data = myvar1, myvar2
            cacher.保存(data)
        myvar1, myvar2 = data
        print(myvar1, myvar2)

        data = func()
        print(data)

        # cacher.清空()

    def test_4(self):
        func标记 = 缓存标记('name2', key='dependencies')
        print("标记", func标记.检查标记())
        if func标记.检查标记():
            print("完成过程", 1)
            func标记.保存标记()
        print("标记", func标记.检查标记())

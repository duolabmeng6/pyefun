import unittest

from .commonlyUtil import *
from .dirkBase import *


class TestcommonlyUtil(unittest.TestCase):

    def test_1(self):
        pass
        data = 取哈希("abc")
        print(data)

        写到文件("sha1.txt", "abc")
        data = 取文件哈希("sha1.txt")
        print(data)

    def test_2(self):
        pass
        return 
        data = 运行命令("ipconfig")
        print(data)

    def test_3(self):
        pass
        data = 取缓存目录("app")
        print(data)

    def test_4(self):
        pass
        # data = 下载文件("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", 取运行目录() + "/1.png")
        # print(data)

        data = 下载文件缓存("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", 取运行目录() + "/1.png")
        print(data)

    def test_5(self):
        选项 = ['ham', 'jam', 'spam', 'eggs', 'cheese', 'bannana']
        分组 = ['protein', 'fruit', 'protein', 'protein', 'dairy', 'fruit']
        data = 字典_分组(选项, 分组)
        print(data)

        items = [1, 2, 39, 900, 1232, 900, 1232, 2, 2, 2, 900]
        data = 字典_统计(items)
        print(data)

        dict_ = {'K': 3, 'dcvs_clip_max': 0.2, 'p': 0.1}
        subdict_ = 字典_取子集(dict_, ['K', 'dcvs_clip_max'])
        print(subdict_)

        dict_ = {1: 'a', 2: 'b', 3: 'c'}
        print(字典_取值(dict_, [1, 2, 3, 4, 5]))

        dict_ = {'a': [1, 2, 3], 'b': [], 'c': [4, 5, 6]}
        newdict = 字典_根据值重建(len, dict_)
        print(newdict)

        mapping = {'a': 0, 'A': 1, 'b': 1, 'c': 2, 'C': 2, 'd': 3}
        data = 字典_交换健值(mapping)
        print(data)

        mapping = {'a': 0, 'A': 1, 'b': 1, 'c': 2, 'C': 2, 'd': 3}
        data = 字典_交换健值(mapping, False)
        print(data)

    def test2(self):
        auto = 灵活字典()
        print('auto = {!r}'.format(auto))
        auto[0][10][100] = None
        print('auto = {!r}'.format(auto))
        auto[0][1] = 'hello'
        print('auto = {!r}'.format(auto))
        auto[0][100][1] = 'hello'
        print('auto = {!r}'.format(auto))

    def test3(self):
        return
        写到文件(取运行目录() + r"/test/__init__.py", """
def test():
    print("动态导入的包")
        """)

        data = 导入包_从路径(取运行目录() + r"/test/")
        print(data)
        data.test()

    def test4(self):
        items = [0, 0, 0, 1, 2, 3, 3, 0, 12, 2, 9]
        data = 数组_查找重复项(items, 3)
        print(data)
        data = 数组_查找重复项(items, 2)
        print(data)

    def test5(self):
        data = func(1, 2)
        print(data)
        data = func(1, 2)
        print(data)
        data = func(2, 2)
        print(data)
        data = func(2, 2)
        print(data)

        func(1, 2)
        func(1, 2)
        a = MyClass()
        print(a.my_method(1, 2))
        print(a.my_method(1, 2))
        print(a.my_method(2, 2))
        print(a.my_method(2, 2))
        print(a.my_method(1, 2))
        print(a.my_property1)
        print(a.my_property1)
        print(a.my_property2())
        print(a.my_property2())

    def test6(self):
        data = 路径_名字处理('foo.bar')
        print(data)
        # 'foo.bar'
        data = 路径_名字处理('foo.bar', 扩展名='.BAZ')
        print(data)
        # 'foo.BAZ'
        data = 路径_名字处理('foo.bar', 末尾='_')
        print(data)
        # 'foo_.bar'
        data = 路径_名字处理('foo.bar', 前缀='_')
        print(data)
        # '_foo.bar'
        data = 路径_名字处理('foo.bar', 名称='baz')
        print(data)
        # 'baz.bar'
        data = 路径_名字处理('foo.tar.gz', 扩展名='.zip', 不包含点=True)
        print(data)
        # foo.zip
        data = 路径_名字处理('foo.tar.gz', 扩展名='.zip', 不包含点=False)
        print(data)
        # foo.tar.zip
        data = 路径_名字处理('foo.tar.gz', 末尾='_new', 不包含点=True)
        print(data)
        # foo_new.tar.gz

    def test7(self):
        data = 路径_取用户目录()
        print(data)
        # import getpass
        # username = getpass.getuser()
        # data = 路径_取用户目录(username)
        # print(data)

        path = ub.util_path.expanduser('~')
        print(path)

        data = 路径_替换为用户路径(path) == '~'
        print(data)

        data = 路径_替换为用户路径(path + '1')
        print(data)

        data = 路径_替换为用户路径(path + '/1')
        print(data)

        data = 路径_替换为用户路径(path + '/1', '$HOME')
        print(data)

        data = 路径_替换为用户路径('.')
        print(data)
        data = 路径_优化路径(路径_展开路径('~/foo'))
        print(data)
        data = 路径_优化路径(r'c:/123\abc\dbf/dddd')
        print(data)
        data = 路径_展开路径('foo')
        print(data)

    def test666(self):
        data = 路径_合并(r'c://', r"/bb/", r"//cc//", r"dd/aa")
        print(data)
        data = 路径_展开路径('~/foo')
        print(data)



    def test8(self):
        with 临时目录() as self:
            dpath = self.dpath
            print(dpath)
            assert 文件是否存在(dpath)
        assert not 文件是否存在(dpath)

        self = 临时目录()
        dpath = self.初始化()
        print(dpath)
        assert 文件是否存在(dpath)
        self.清理()
        assert not 文件是否存在(dpath)

    def test9(self):
        self = 控制台(获取内容=True)
        with self:
            print('I am captured and printed in stdout')
        print("test3", self.获取内容())

        self = 控制台(获取内容=False)
        with self:
            print('I am captured and printed in stdout')
        print("test2", self.获取内容())

    def test10(self):
        items = '1234567'
        genresult = 分块(items, 分块数量=2)
        print(list(genresult))
        items = '1234567890'
        genresult = 分块(items, 创建块数=1, 创建数量=4)
        print(list(genresult))




@内存缓存
def func(a, b):
    print("缓存了")
    return a + b


class MyClass:
    # Memoize a class method, the args are hashed
    @内存缓存方法
    def my_method(self, a, b):
        print("my_method", a, b)
        return a + b

    #
    # Memoize a property: there can be no args,
    @内存缓存属性
    def my_property1(self):
        print("my_property1")
        return 4

    #
    # The property decorator is optional
    def my_property2(self):
        print("my_property2")
        return 5
#

"""

.. Hint::
    数组操作

.. literalinclude:: ../../../pyefun/arrayActionBase_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""

class 数组:

    def __init__(self, data: list = []):
        self.val = list(data)

    def 加入成员(self, object):
        self.val.append(object)

    def 统计成员次数(self, object):
        return self.val.count(object)

    def 查找成员(self, object):
        return self.val.index(object)

    def 弹出成员(self, index: int = -1):
        return self.val.pop(index)

    def 插入成员(self, object, index: int = -1):
        self.val.insert(index, object)

    def 移除成员(self, object):
        self.val.remove(object)

    def 翻转(self):
        self.val.reverse()

    def 排序(self, **kwargs):
        # cmp=None, key=None, reverse=False
        # cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
        # key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
        # reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
        self.val.sort(**kwargs)

    def 从大到小(self, 下标=0):
        pass
        self.排序(reverse=True, key=lambda d: _func_key(d, 下标))

    def 从小到大(self, 下标=0):
        self.排序(reverse=False, key=lambda d: _func_key(d, 下标))

    def 取所有成员(self):
        return self.val

    def 清空(self):
        self.val = []


def _func_key(d, 下标=0):
    if (type(d) == tuple):
        return d[下标]
    return d


def 字典_取值并删除(字典, 键, 失败返回值=None):
    '如果查找键不存在则返回设置的失败返回值,该值可空'
    return 字典.pop(键, 失败返回值)


def 字典_取指定键值(字典, 键, 失败返回值=None):
    '如果查找键不存在则返回设置的失败返回值'
    return 字典.get(键, 失败返回值)


def 字典_清空(字典):
    '清空字典内的全部元素,成功返回True'
    字典.clear()
    return True


def 字典_拷贝(新字典, 原字典):
    '成功返回True 直接赋值拷贝值会跟着原字典改变,用copy不会'
    新字典 = 原字典.copy()
    return True


def 字典_生成(键值列表, 键值):
    '传入键值列表创建字典,字典内的值都为设置的键值'
    return dict.fromkeys(键值列表, 键值)


def 字典_转列表(字典):
    '返回列表格式[(1,2),(2,3),(3,4)]'
    return list(字典.items())


def 字典_取全部键(字典):
    return list(字典.keys())


def 字典_取全部值(字典):
    return list(字典.values())


def 字典_取出并删除最后键值(字典):
    '删除字典中最后一个键跟值并以元组格式返回删除的键跟值'
    return 字典.popitem()


def 字典_取值添加(字典, 键, 值=None):
    '如果查找键不存在则返回设置的失值且为字典新建该键值'
    return 字典.setdefault(键, 值)


def 列表_转字典(列表):
    '将[(1,2),(3,4)]转换成{1:2,3:4}'
    字典 = dict()
    for x in 列表: 字典[x[0]] = x[1]
    return 字典


def 列表_合并为字典(列表1, 列表2):
    '传入两个列表转换成字典 [1,2],[8,9]==>{1:8,2:9}'
    return dict(zip(列表1, 列表2))


def 列表_加入成员(列表, 值):
    '成功返回True'
    列表.append(值)
    return True


def 列表_插入成员(列表, 位置, 值):
    '成功返回True 在指定位置插入指定值'
    列表.insert(位置, 值)
    return True


def 列表_取出现次数(列表, 值):
    '搜索时 True 会当成1   False 是0'
    return 列表.count(值)


def 列表_合并列表(列表, 新列表):
    '成功返回True 在列表后面追加新的列表或元组成员进去'
    列表.extend(新列表)
    return True


def 列表_查找成员位置(列表, 值):
    return 列表.index(值)


def 列表_取值并删除(列表, 位置=None):
    '取出列表的一个成员值 并删除该成员,默认最后一个,位置为0则为第一个'
    if 位置 == None:
        return 列表.pop()
    else:
        return 列表.pop(位置)


def 列表_删除指定值(列表, 值):
    '成功返回True 删除列表中找到的第一个值'
    列表.remove(值)
    return True


def 列表_倒序排列(列表):
    '成功返回True 把列表的成员顺序到过来排序'
    列表.reverse()
    return True


def 列表_大小排序(列表, 排序方式=False):
    '成功返回True 排序的列表只能全为整数型的,排序方式True为从大到小,默认False从小到大'
    列表.sort(reverse=排序方式)
    return True


def 数组_按成员长度排序(数组):
    '传入一个序列，根据成员的长度排序 长的在前面'
    return sorted(数组, key=lambda i: len(i), reverse=True)


def 数组_按子成员大小排序(数组, 成员索引):
    '处理数组内包含数组需要排序的'
    return sorted(数组, key=lambda i: i[成员索引])


def 数组_取随机成员数组(数组, 数量):
    '失败返回False,在指定数组内随机取出指定数量的成员组成新数组返回'
    return random.sample(数组, 数量)


def 数组_取随机成员(数组):
    '可以传入字符 元组 列表登录,随机取出一个值'
    return random.choice(数组)

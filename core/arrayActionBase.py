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

    def 取所有成员(self):
        return self.val

    def 清空(self):
        self.val = []

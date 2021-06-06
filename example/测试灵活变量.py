from pyefun import *


class 灵活字典变量(AutoDict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

xx = 灵活字典变量()
xx.a.b = 1
xx.b = 1

print(xx)
print(xx["b"])
print(xx["a"]["b"])


# print(repr("a"))
class 人类:
    pass
    名字 = ""

    def __getattr__(self, name):
        print("定义当用户试图获取一个不存在的属性时的行为")
        print(name)

    def __getattribute__(self, name):
        print("定义当该类的属性被访问时的行为")
        print(name)
        if name == "内容":
            pass

    def __setattr__(self, name, value):
        print("定义当一个属性被设置时的行为")
        print(name, value)
        if name == "内容":
            pass

    def __delattr__(self, name):
        print("定义当一个属性被删除时的行为")
        print(name)

    def __dir__(self):
        print("被调用时的行为")

    def __get__(self, instance, owner):
        print("定义当描述符的值被取得时的行为")
        print(instance, owner)

    def __set__(self, instance, value):
        print("定义当描述符的值被改变时的行为")
        print(instance, value)

    def __delete__(self, instance):
        print("定义当描述符的值被删除时的行为")
        print(instance)


# ren = 人类()
# ren.年龄 = 10
# ren.年龄 = 22
# ren.名字 = "22"
# ren.内容 = "祖国你好"
# print(ren.aaa)
# print(ren.内容)

class 小猫():
    颜色 = ""

    def __init__(self):
        pass

    _颜色 = None
    @property
    def 颜色(self):
        print("颜色")
        return self._颜色

    @颜色.setter
    def 颜色(self, value):
        self._颜色 = value
        print("颜色", value)


猫猫 = 小猫()
猫猫.颜色 = "红色"
print(猫猫.颜色)


import wx.html2
import wx
from .wxControl import *

组件名称 = "浏览器"
组件创建代码 = """wx.浏览器(self.容器, size=({宽度}, {高度}), pos=({左边}, {顶边}))"""
界面设计器使用占位符创建 = True

class 浏览器(公用方法):
    pass

    def __init__(self, *args, **kw):
        self.浏览器对象 = wx.html2.WebView.New(*args, **kw)
        # self.__class__ = self.浏览器对象

    @property
    def 左边(self):
        return int(self.浏览器对象.GetPosition()[0])

    @左边.setter
    def 左边(self, value):
        return self.浏览器对象.Move(value, self.浏览器对象.GetPosition()[1])

    @property
    def 顶边(self):
        return int(self.浏览器对象.GetPosition()[1])

    @顶边.setter
    def 顶边(self, value):
        return self.浏览器对象.Move(self.浏览器对象.GetPosition()[0], value)

    @property
    def 宽度(self):
        return self.浏览器对象.GetSize()[0]

    @宽度.setter
    def 宽度(self, value):
        return self.浏览器对象.SetInitialSize((value, self.浏览器对象.GetSize()[1]))

    @property
    def 高度(self):
        return self.浏览器对象.GetSize()[1]

    @高度.setter
    def 高度(self, value):
        return self.浏览器对象.SetInitialSize((self.浏览器对象.GetSize()[0], value))

    def GetRect(self):
        return self.浏览器对象.GetRect()

    def GetId(self):
        return self.浏览器对象.GetId()

    def GetFont(self):
        return self.浏览器对象.GetFont()

    def IsShown(self):
        return self.浏览器对象.IsShown()

    def GetForegroundColour(self):
        return self.浏览器对象.GetForegroundColour()
    def GetLabel(self):
        return self.浏览器对象.GetLabel()

    def Raise(self):
        return self.浏览器对象.Raise()


    def GetBackgroundColour(self):
        return self.浏览器对象.GetBackgroundColour()

    def 绑定事件(self, *args, **kwargs):
        return self.浏览器对象.Bind(*args, **kwargs)

    def Bind(self, *args, **kwargs):
        return self.浏览器对象.Bind(*args, **kwargs)

    def Refresh(self, *args, **kwargs):
        return self.浏览器对象.Refresh(*args, **kwargs)

    def Move(self, *args, **kwargs):
        return self.浏览器对象.Move(*args, **kwargs)

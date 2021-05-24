import wx.adv
import wx
from .wxControl import *

class 进度条(wx.Gauge, 公用方法):
    pass

    def 取最大位置(self):
        return self.GetRange()

    def 取当前位置(self):
        return self.GetValue()

    def 是否为垂直进度条(self):
        return self.IsVertical()

    @组件_异常检测
    def 置最大位置(self,位置):
        return self.SetRange(位置)

    @组件_异常检测
    def 置当前位置(self,位置):
        return self.SetValue(位置)

    def 置加载模式(self):
        '使滚动条编程滚动加载状态,调用SetValue停止滚动加载'
        self.Pulse()

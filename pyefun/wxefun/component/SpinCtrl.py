
import wx
from .wxControl import *

class 整数微调框(wx.SpinCtrl, 公用方法):
    pass

    def 取数值进制类型(self):
        '返回10或16，十进制或16进制'
        return self.GetBase()

    @组件_异常检测
    def 置数值进制类型(self,类型):
        '类型：10或16，十进制或16进制'
        return self.SetBase(类型)

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    @组件_异常检测
    def 置最大值(self,数值):
        return self.SetMax(数值)

    @组件_异常检测
    def 置最小值(self,数值):
        return self.SetMin(数值)

    def 取数值范围(self):
        '获取微调的数值范围'
        return self.GetRange()

    @组件_异常检测
    def 置数值范围(self,最小值,最大值):
        '设置微调的数值范围'
        return self.SetRange(最小值,最大值)

    @组件_异常检测
    def 取当前数值(self):
        return self.GetValue()

    @组件_异常检测
    def 置当前数值(self,数值):
        return self.SetValue(数值)

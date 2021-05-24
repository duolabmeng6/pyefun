import wx.lib.agw.floatspin as floatspin
from .wxControl import *


class 小数微调框(floatspin.FloatSpin, 公用方法):
    pass

    def 取当前数值(self):
        return self.GetDefaultValue().GetValue()

    def 取当前数值2(self):
        return self.GetValue()

    def 取默认数值(self):
        return self.GetDefaultValue()

    def 取显示的位数(self):
        return self.GetDigits()

    def 取字符格式(self):
        return self.GetFormat()

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    @组件_异常检测
    def 置最大值(self,最大值):
        return self.SetMax(最大值)

    @组件_异常检测
    def 置最小值(self,最小值):
        return self.SetMin(最小值)

    @组件_异常检测
    def 置数值范围(self,最小值,最大值):
        return self.SetRange(最小值,最大值)

    @组件_异常检测
    def 置数值范围2(self,最小值,最大值):
        return self.SetRangeDontClampValue(最小值,最大值)

    def 是否设置数值范围(self):
        return self.HasRange()

    @组件_异常检测
    def 是否在数值范围内容(self,数值):
        '测试指定数值是否在允许的范围内'
        return self.InRange(数值)

    def 是否已设置默认值(self):
        return self.IsDefaultValue()

    @组件_异常检测
    def 置小数位数(self,位数):
        return self.SetDigits(位数)

    @组件_异常检测
    def 置字符格式(self,格式):
        return self.SetFormat(格式)

    @组件_异常检测
    def 置当前数值(self,数值):
        return self.SetValue(数值)

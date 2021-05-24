import wx.adv
import wx
from .wxControl import *

class 日期框(wx.adv.DatePickerCtrl, 公用方法):
    pass

    def 取可选日期范围(self):
        return self.GetRange()

    @组件_异常检测
    def 置可选日期范围(self,最早日期,最晚日期):
        return self.SetRange(最早日期,最晚日期)

    def 取当前日期(self):
        return self.GetValue()

    @组件_异常检测
    def 置当前日期(self,日期):
        return self.SetValue(日期)

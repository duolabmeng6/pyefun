import wx.adv
import wx
from .wxControl import *

class 时间框(wx.adv.TimePickerCtrl, 公用方法):
    pass

    def 取当前时间(self):
        '返回一个元组，(时,分,秒)'
        return self.GetTime()

    @组件_异常检测
    def 置当前时间(self,时,分,秒):
        return self.SetTime(时,分,秒)

    def 取当前时间_dt(self):
        '返回wx.DateTime'
        return self.GetValue()

    @组件_异常检测
    def 置当前时间_dt(self,时间):
        'wx.DateTime格式时间'
        return self.SetValue(时间)


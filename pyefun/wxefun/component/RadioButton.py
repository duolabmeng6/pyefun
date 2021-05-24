import wx
from .wxControl import *


class 单选框(wx.RadioButton, 公用方法):
    pass

    def 是否选中(self):
        return self.GetValue()

    @组件_异常检测
    def 置选中状态(self, 状态):
        'True/False'
        return self.SetValue(状态)

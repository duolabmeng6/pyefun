import wx
from .wxControl import *


class 复选框(wx.CheckBox, 公用方法):
    pass

    def 取三态多选框状态(self):
        '返回 0.未选中  1.选中  2.半选中'
        return self.Get3StateValue()

    @组件_异常检测
    def 置三态多选框状态(self, 状态):
        '0.未选中  1.选中  2.半选中'
        return self.Set3StateValue(状态)

    def 是否选中(self):
        return self.GetValue()

    @组件_异常检测
    def 置选中状态(self, 状态):
        'True/False'
        return self.SetValue(状态)

    def 是否为三态复选框(self):
        return self.Is3State()

    def 是否可设置为半选中(self):
        return self.Is3rdStateAllowedForUser()

    @property
    def 选中(self):
        return self.GetValue()

    @选中.setter
    def 选中(self, value):
        self.SetValue(value)

    @property
    def 标题居左(self):
        return self.GetValue()

    @标题居左.setter
    def 标题居左(self, value):
        if value:
            self.SetWindowStyle(wx.ALIGN_RIGHT)
        else:
            self.ToggleWindowStyle(wx.ALIGN_RIGHT)


class 选择框(复选框):
    pass

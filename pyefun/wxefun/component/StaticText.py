"""
标签组件

"""
import wx
from .wxControl import *
import pyefun.wxefun.evt as evt


class 标签(wx.StaticText, 公用方法):
    pass

    @property
    def 标题(self):
        return self.GetLabel()

    @标题.setter
    def 标题(self, value: str):
        return self.SetLabel(value)

    @property
    def 文字对齐方式(self):
        return ""

    @文字对齐方式.setter
    def 文字对齐方式(self, 标签样式: int):
        """
            wx.标签样式.文字在左边
            wx.标签样式.文字在右边
            wx.标签样式.文字在居中
        """
        self.SetWindowStyle(标签样式)
        self.Refresh()

    @property
    def 省略号位置(self):
        return ""

    @省略号位置.setter
    def 省略号位置(self, 标签样式: int):
        """
            wx.标签样式.省略号在开头
            wx.标签样式.省略号在中间
            wx.标签样式.省略号在末尾
        """
        self.SetWindowStyle(标签样式)
        self.Refresh()

    @property
    def 自动调整大小(self):
        return ""

    @自动调整大小.setter
    def 自动调整大小(self, 是否自动调整大小: bool):
        "默认是自动跳转大小的 如果设置 真 就是默认自动跳转大小 如果设置假就是禁用自动跳转代销"
        if 是否自动调整大小:
            self.ToggleWindowStyle(evt.标签样式.禁用自动调整大小)
        else:
            self.SetWindowStyle(evt.标签样式.禁用自动调整大小)
        self.Refresh()

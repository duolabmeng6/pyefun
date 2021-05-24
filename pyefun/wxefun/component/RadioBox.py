
import wx
from .wxControl import *

class 分组单选框(wx.RadioBox, 公用方法):
    pass
    @组件_异常检测
    def 启用某项(self,索引):
        return self.EnableItem(索引,True)

    @组件_异常检测
    def 禁用某项(self,索引):
        return self.EnableItem(索引,False)

    @组件_异常检测
    def 置指定项是否可用(self,索引,启用=True):
        return self.EnableItem(索引, 启用)

    @组件_异常检测
    def 查找选项(self,标题文本,区分大小写=False):
        return self.FindString(标题文本,区分大小写)

    def 取选项列数(self):
        '返回单选框中的列数。'
        return self.GetColumnCount()

    def 取选项行数(self):
        return self.GetRowCount()

    def 取选项数(self):
        return self.GetCount()

    def 取指定坐标处选项(self,x,y):
        return self.GetItemFromPoint((x,y))

    @组件_异常检测
    def 取选项帮助文本(self,索引):
        return self.GetItemHelpText(索引)

    @组件_异常检测
    def 取选项文本(self,索引):
        return self.GetItemLabel(索引)

    @组件_异常检测
    def 取选项文本2(self,索引):
        return self.GetString(索引)

    @组件_异常检测
    def 取选项提示工具(self,索引):
        '返回与指定项目关联的工具提示（ 如果有的话）None。返回类型 wx.ToolTip'
        return self.GetItemToolTip()

    @组件_异常检测
    def 取选项提示文本(self,索引):
        return self.GetItemToolTip(索引).GetTip()

    @组件_异常检测
    def 置选项提示文本(self, 索引,提示内容):
        return self.GetItemToolTip(索引).SetTip(提示内容)

    @组件_异常检测
    def 置选项提示时间(self,索引,时间=2000):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetAutoPop(时间)

    @组件_异常检测
    def 置选项提示延迟显示时间(self, 索引, 时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetDelay(时间)

    @组件_异常检测
    def 置选项提示最大宽度(self, 索引, 宽度):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetMaxWidth(宽度)

    @组件_异常检测
    def 置选项提示后续提示延时(self,索引,时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetReshow(时间)

    @组件_异常检测
    def 启用或禁用选项提示(self,索引,启用=True):
        return self.GetItemToolTip(索引).Enable(启用)

    def 取现行选中项(self):
        '返回所选项目的索引，或者NOT_FOUND 如果未选择任何项目，则返回该索引 。'
        return self.GetSelection()

    @组件_异常检测
    def 是否启用指定项(self,索引):
        '判断指定选项是否启用,是启用不是选中'
        return self.IsItemEnabled(索引)

    @组件_异常检测
    def 是否显示指定项(self,索引):
        '返回True当前是否显示该项目或False是否使用隐藏该项目Show。'
        return self.IsItemShown(索引)

    @组件_异常检测
    def 置选项帮助文本(self,索引,内容):
        return self.SetItemHelpText(索引,内容)

    @组件_异常检测
    def 置选项标题(self,索引,标题):
        return self.SetItemLabel(索引,标题)

    @组件_异常检测
    def 置选项提示文本(self,索引,提示内容):
        return self.SetItemToolTip(索引,提示内容)

    @组件_异常检测
    def 置选中项(self,索引):
        '指定选项设置为选中状态'
        return self.SetSelection(索引)

    @组件_异常检测
    def 置选项标题(self,索引,标题):
        '指定选项设置为选中状态'
        return self.SetSelection(索引,标题)

    @组件_异常检测
    def 显示某项(self,索引):
        return self.ShowItem(索引,True)

    @组件_异常检测
    def 隐藏某项(self,索引):
        return self.ShowItem(索引,False)

    @组件_异常检测
    def 显示或隐藏某项(self,索引,显示=True):
        return self.ShowItem(索引,显示)

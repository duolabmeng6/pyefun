
import wx
from .wxControl import *

class 组合框(wx.ComboBox, 公用方法):
    pass

    @组件_异常检测
    def 取指定项目索引(self,项目文本,是否区分大小写=False):
        return self.FindString(项目文本,是否区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项索引(self):
        return self.GetCurrentSelection()

    def 取选中项索引2(self):
        return self.GetSelection()

    def 取选中范围(self):
        return self.GetTextSelection()

    @组件_异常检测
    def 取指定项目文本(self,索引):
        return self.GetString(索引)

    def 取选中项文本(self):
        return self.GetStringSelection()

    def 列表项是否为空(self):
        return self.IsListEmpty()

    def 弹出列表(self):
        self.Popup()

    @组件_异常检测
    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    @组件_异常检测
    def 置默认文本(self,文本):
        self.SetValue(文本)

    @组件_异常检测
    def 置选中项(self,索引):
        self.SetSelection(索引)

    @组件_异常检测
    def 置选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    @组件_异常检测
    def 选中范围文本(self,开始位置,结束位置):
        '如果两个参数都等于-1，则选择控件中的所有文本'
        self.SetTextSelection(开始位置,结束位置)

    def 清空表项(self):
        self.Clear()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    @组件_异常检测
    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    @组件_异常检测
    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    @组件_异常检测
    def 删除指定项目(self,索引):
        self.Delete(索引)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)

    def 置列表项目(self,列表项目列表):
        self.Clear()
        for v in 列表项目列表:
            self.Append(v)
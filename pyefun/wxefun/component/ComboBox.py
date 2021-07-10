import wx
from .wxControl import *


class 组合框(wx.ComboBox, 公用方法):

    @property
    def 宽度(self):
        size = self.GetSize()
        return size[0]

    @宽度.setter
    def 宽度(self, value):
        size = self.GetSize()
        size[0] = value
        self.SetSize(-1, -1, value, size[1])

    @property
    def 高度(self):
        size = self.GetSize()
        return size[1]

    @高度.setter
    def 高度(self, value):
        size = self.GetSize()
        size[1] = value
        self.SetSize(-1, -1, size[0], value)

    @property
    def 现行选中项(self):
        return self.GetSelection()

    @现行选中项.setter
    def 现行选中项(self, value):
        self.SetSelection(value)

    @property
    def 列表项目(self):
        return []

    @列表项目.setter
    def 列表项目(self, value):
        print(value)
        self.Set(value)

    @property
    def 内容(self):
        return self.GetValue()

    @内容.setter
    def 内容(self, value):
        self.SetValue(value)

    @组件_异常检测
    def 取指定项目索引(self, 项目文本, 是否区分大小写=False):
        return self.FindString(项目文本, 是否区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项索引(self):
        return self.GetCurrentSelection()

    def 取选中项索引2(self):
        return self.GetSelection()

    def 取选中范围(self):
        return self.GetTextSelection()

    @组件_异常检测
    def 取项目文本(self, 索引):
        return self.GetString(索引)

    def 取选中项文本(self):
        return self.GetStringSelection()

    def 列表项是否为空(self):
        return self.IsListEmpty()

    def 文本是否为空(self):
        return self.IsTextEmpty()

    def 弹出列表(self):
        self.Popup()

    @组件_异常检测
    def 置项目文本(self, 索引, 文本):
        self.SetString(索引, 文本)

    @组件_异常检测
    def 置默认文本(self, 文本):
        self.SetValue(文本)

    @组件_异常检测
    def 置选中项(self, 索引):
        self.SetSelection(索引)

    @组件_异常检测
    def 置选中项_文本(self, 项目文本):
        return self.SetStringSelection(项目文本)

    @组件_异常检测
    def 选中范围文本(self, 开始位置, 结束位置):
        '如果两个参数都等于-1，则选择控件中的所有文本'
        self.SetTextSelection(开始位置, 结束位置)

    @组件_异常检测
    def 清空(self):
        """
            删除组合框列表部分中的所有项目。
        """
        self.Clear()

    @组件_异常检测
    def 置项目列表(self, 项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    @组件_异常检测
    def 加入项目(self, 项目文本: str):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目文本)

    @组件_异常检测
    def 删除项目(self, 项目索引):
        self.Delete(项目索引)

    @组件_异常检测
    def 插入项目(self, 欲插入的位置, 欲插入项目的文本):
        return self.Insert(欲插入项目的文本, 欲插入的位置)

    @组件_异常检测
    def 置列表项目(self, 列表项目列表):
        """
        用给定的项目替换当前控件内容。
        请注意，如果您需要添加大量项目，调用此方法通常比将它们一个一个地附加起来要快得多。
        """
        self.Clear()
        self.Set(列表项目列表)

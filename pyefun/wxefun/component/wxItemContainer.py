import wx
from .wxControl import *


class 列表项目操作类(wx.ItemContainer):
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
        self.SetItems(value)

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
    def 置列表项目(self, 项目列表: list):
        if type(项目列表) == list:
            self.Set(项目列表)

    @组件_异常检测
    def 清空(self):
        self.Clear()

    """
    ItemContainerImmutable()
    @组件_异常检测
    wxItemContainer defines an interface which is implemented by all
    controls which have string subitems each of which may be selected.
    """

    @组件_异常检测
    def 取指定项目索引(self, 项目文本, 是否区分大小写=False):
        """
        FindString(string, caseSensitive=False) -> int

        Finds an item whose label matches the given string.
        """
        return self.FindString(项目文本, 是否区分大小写)

    @组件_异常检测
    def 取项目数(self):  # real signature unknown; restored from __doc__
        """
        GetCount() -> unsignedint

        Returns the number of items in the control.
        """
        return self.GetCount()

    @组件_异常检测
    def 取选中项索引(self):  # real signature unknown; restored from __doc__
        """
        GetSelection() -> int

        Returns the index of the selected item or wxNOT_FOUND if no item is
        selected.
        """
        return self.GetSelection()

    @组件_异常检测
    def 取项目文本(self, n):  # real signature unknown; restored from __doc__
        """
        GetString(n) -> String

        Returns the label of the item with the given index.
        """
        return self.GetString(n)

    @组件_异常检测
    def 取所有项目文本(self):  # real signature unknown; restored from __doc__
        """
        GetStrings() -> ArrayString

        Returns the array of the labels of all items in the control.
        """
        return self.GetStrings()

    @组件_异常检测
    def 取现行选中项文本(self):  # real signature unknown; restored from __doc__
        """
        GetStringSelection() -> String

        Returns the label of the selected item or an empty string if no item
        is selected.
        """
        return self.GetStringSelection()

    @组件_异常检测
    def 是否为空(self):  # real signature unknown; restored from __doc__
        """
        IsEmpty() -> bool

        Returns true if the control is empty or false if it has some items.
        """
        return self.IsEmpty()

    @组件_异常检测
    def 选择项目(self, n):  # real signature unknown; restored from __doc__
        """
        Select(n)

        This is the same as SetSelection() and exists only because it is
        slightly more natural for controls which support multiple selection.
        """
        return self.Select(n)

    @组件_异常检测
    def 置现行选中项(self, n):  # real signature unknown; restored from __doc__
        """
        SetSelection(n)

        Sets the selection to the given item n or removes the selection
        entirely if n == wxNOT_FOUND.
        """
        return self.SetSelection(n)

    @组件_异常检测
    def 置项目文本(self, n, string):  # real signature unknown; restored from __doc__
        """
        SetString(n, string)

        Sets the label for the given item.
        """
        self.SetString(n, string)

    @组件_异常检测
    def 置现行选中项文本(self, string):  # real signature unknown; restored from __doc__
        """
        SetStringSelection(string) -> bool

        Selects the item with the specified string in the control.
        """
        return self.SetStringSelection(string)

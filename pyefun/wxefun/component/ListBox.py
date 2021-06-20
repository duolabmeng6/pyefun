
import wx
from .wxControl import *

class 列表框(wx.ListBox, 公用方法):
    pass
    @组件_异常检测
    def 取消指定选中项(self,索引):
        '在列表框中取消选择一个项目。'
        return self.Deselect(索引)

    @组件_异常检测
    def 保证显示(self,索引):
        '确保当前显示具有给定索引的项目。'
        return self.EnsureVisible(索引)

    @组件_异常检测
    def 取指定项目索引(self,查找的内容,区分大小写=False):
        '查找标签与给定字符串匹配的项目。返回项目索引'
        return self.FindString(查找的内容,区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取可见项目数(self):
        '返回可以垂直放入列表框可见区域的项目数。'
        return self.GetCountPerPage()

    def 取选中项索引(self):
        return self.GetSelection()

    def 取选中范围索引(self):
        '返回一个列表包含所有选中项索引,用当前所选项目的位置填充一个整数数组。'
        return self.GetSelections()

    @组件_异常检测
    def 取指定项目文本(self, 索引):
        return self.GetString(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    @组件_异常检测
    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.InsertItems(项目列表,插入位置)

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
    def 项目是否选中(self,索引):
        return self.InsertItems(索引)

    def 表项是否按字母排序(self):
        return self.IsSorted()

    @组件_异常检测
    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    @组件_异常检测
    def 置指定项目背景色(self,索引,颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引,颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目前景色(self,索引,颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引,颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目字体(self,索引,字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引,字体)
        self.Refresh()

    @组件_异常检测
    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    @组件_异常检测
    def 置现行选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    @组件_异常检测
    def 置现行选中项(self,索引):
        return self.SetSelection(索引)

    @组件_异常检测
    def 取选中项文本(self):
        return self.GetStringSelection()

    def 置列表项目(self,列表项目列表):
        self.Clear()
        for v in 列表项目列表:
            self.Append(v)

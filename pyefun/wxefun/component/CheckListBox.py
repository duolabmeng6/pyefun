import wx
from .wxControl import *

class 选择列表框(wx.CheckListBox, 公用方法):
    pass
    @组件_异常检测
    def 置选中状态(self,索引,选中=True):
        self.Check(索引,选中)

    @组件_异常检测
    def 选中项目(self,索引):
        self.Check(索引,True)

    @组件_异常检测
    def 取消选中项目(self,索引):
        self.Check(索引,False)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项(self):
        '返回一个元组,包含所有选中的表项索引'
        return self.GetCheckedItems()

    def 取选中项_文本(self):
        '返回一个元组,包含所有选中的表项文本'
        return self.GetCheckedStrings()

    @组件_异常检测
    def 是否选中(self,索引):
        return self.IsChecked(索引)

    @组件_异常检测
    def 置选中状态_批量(self,索引列表):
        '传入需要选中的索引列表,不存在的会报错'
        self.SetCheckedItems(索引列表)

    @组件_异常检测
    def 置选中状态_文本_批量(self,索引列表):
        '传入需要选中的项目文本列表,不存在的会报错'
        self.SetCheckedStrings(索引列表)

    @组件_异常检测
    def 置指定项目背景色(self, 索引, 颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引, 颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目前景色(self, 索引, 颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引, 颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目字体(self, 索引, 字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引, 字体)
        self.Refresh()

    @组件_异常检测
    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    @组件_异常检测
    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)

    @组件_异常检测
    def 插入项目2(self,插入位置,项目列表):
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

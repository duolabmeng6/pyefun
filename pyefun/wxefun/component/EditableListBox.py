import wx.adv
import wx
from .wxControl import *

组件名称 = "排序列表框"
组件创建代码 = """wx.排序列表框(self.容器, size=({宽度}, {高度}), pos=({左边}, {顶边}), name='editableListBox', label='', style=1792)"""
界面设计器使用占位符创建 = True

class 排序列表框(wx.adv.EditableListBox, 公用方法):
    pass

    def 取项目列表(self):
        return self.GetStrings()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        return self.SetStrings(项目列表)

import wx.adv
import wx
from .wxControl import *

class 排序列表框(wx.adv.EditableListBox, 公用方法):
    pass

    def 取项目列表(self):
        return self.GetStrings()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        return self.SetStrings(项目列表)

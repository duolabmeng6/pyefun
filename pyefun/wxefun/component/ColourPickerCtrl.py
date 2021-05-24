
import wx
from .wxControl import *

class 颜色选择器(wx.ColourPickerCtrl, 公用方法):
    pass

    def 取当前颜色(self):
        return self.GetColour()

    @组件_异常检测
    def 置当前颜色(self,颜色):
        return self.SetColour(颜色)

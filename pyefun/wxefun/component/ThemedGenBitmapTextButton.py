
import wx.lib.buttons as lib_button
from .wxControl import *


class 图文按钮(lib_button.ThemedGenBitmapTextButton, 公用方法):
    pass

    def 取禁用状态图片(self):
        return self.GetBitmapDisabled()

    def 取焦点状态图片(self):
        return self.GetBitmapFocus()

    def 取正常状态图片(self):
        return self.GetBitmapLabel()

    def 取按下状态图片(self):
        return self.GetBitmapSelected()

    @组件_异常检测
    def 置禁用状态图片(self,图片):
        return self.SetBitmapDisabled(图片)

    @组件_异常检测
    def 置焦点状态图片(self,图片):
        return self.SetBitmapFocus(图片)

    @组件_异常检测
    def 置正常状态图片(self,图片):
        return self.SetBitmapLabel(图片)

    @组件_异常检测
    def 置按下状态图片(self,图片):
        return self.SetBitmapSelected(图片)

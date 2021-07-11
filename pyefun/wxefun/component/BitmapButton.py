import wx
import wx.lib.buttons
from .wxControl import *
import pyefun as efun


class 图形按钮(wx.lib.buttons.ThemedGenBitmapTextButton, 公用方法):
    pass

    _正常图片 = ""  # 储存图片路径以便在改变属性时刷新显示
    _焦点图片 = ""  # 储存图片路径以便在改变属性时刷新显示
    _禁止图片 = ""  # 储存图片路径以便在改变属性时刷新显示
    _按下图片 = ""  # 储存图片路径以便在改变属性时刷新显示
    _显示方式 = "图片居左上"  # 图片居左上 缩放图片 图片居中
    _图片缩放大小 = (0, 0)  # 宽度,高度

    def _处理图片的显示方式(self, value):
        if False == efun.文件是否存在(value):
            raise Exception("文件不存在 {}".format(value))
        if type(value) == str:
            value = wx.Image(value)
            if self._显示方式 == "图片居左上":
                pass
            elif self._显示方式 == "缩放图片":
                pass
                w, h = self._图片缩放大小[0],self._图片缩放大小[1]
                if w == 0 or h == 0:
                    w, h = self.GetSize()
                value = value.Scale(w, h)

            elif self._显示方式 == "图片居中":
                pass

            value = value.ConvertToBitmap()
        return value

    @property
    def 正常图片(self):
        return ""

    @正常图片.setter
    @组件_异常检测
    def 正常图片(self, value):
        if value == "":
            return
        图片 = self._处理图片的显示方式(value)
        self.SetBitmapLabel(图片)
        self._正常图片 = value

    @property
    def 显示方式(self):
        return self._显示方式

    @显示方式.setter
    def 显示方式(self, value):
        self._显示方式 = value

    @property
    def 图片缩放大小(self):
        return self._图片缩放大小

    @图片缩放大小.setter
    def 图片缩放大小(self, value):
        """ (w,h)"""
        self._图片缩放大小 = value
        self.正常图片 = self._正常图片
        self.焦点图片 = self._焦点图片
        self.按下图片 = self._按下图片
        self.禁止图片 = self._禁止图片

    @property
    def 焦点图片(self):
        return ""

    @焦点图片.setter
    @组件_异常检测
    def 焦点图片(self, value):
        if value == "":
            return
        图片 = self._处理图片的显示方式(value)
        self.SetBitmapFocus(图片)
        self._焦点图片 = value

    @property
    def 按下图片(self):
        return ""

    @按下图片.setter
    @组件_异常检测
    def 按下图片(self, value):
        if value == "":
            return
        图片 = self._处理图片的显示方式(value)
        self.SetBitmapSelected(图片)
        self._按下图片 = value

    @property
    def 禁止图片(self):
        return ""

    @禁止图片.setter
    @组件_异常检测
    def 禁止图片(self, value):
        if value == "":
            return
        图片 = self._处理图片的显示方式(value)
        self.SetBitmapDisabled(图片)
        self._禁止图片 = value

    def 取禁用状态图片(self):
        return self.GetBitmapDisabled()

    def 取焦点状态图片(self):
        return self.GetBitmapFocus()

    def 取正常状态图片(self):
        return self.GetBitmapLabel()

    def 取按下状态图片(self):
        return self.GetBitmapSelected()

    @组件_异常检测
    def 置禁用状态图片(self, 图片):
        return self.SetBitmapDisabled(图片)

    @组件_异常检测
    def 置焦点状态图片(self, 图片):
        return self.SetBitmapFocus(图片)

    @组件_异常检测
    def 置正常状态图片(self, 图片):
        return self.SetBitmapLabel(图片)

    @组件_异常检测
    def 置按下状态图片(self, 图片):
        return self.SetBitmapSelected(图片)

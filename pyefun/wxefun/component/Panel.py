import wx
from .wxControl import *


class 容器(wx.Panel, 公用方法):
    底图方式 = "图片居左上"

    @property
    def 底图(self):
        return self.底图文件路径

    @底图.setter
    def 底图(self, value):
        if value == "":
            return
        self.底图文件路径 = value
        self.Bind(wx.EVT_ERASE_BACKGROUND, self._绘制底图)
        self.Bind(wx.EVT_SIZE, self._onSize)

    def _onSize(self, evt):
        self.Refresh()

    def _绘制底图(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        size = self.GetClientSize()

        bmp = wx.Image(self.底图文件路径, wx.BITMAP_TYPE_ANY)
        if self.底图方式 == "图片居左上":
            pass
        elif self.底图方式 == "缩放图片":
            bmp = bmp.Scale(size.x, size.y)
        elif self.底图方式 == "图片平铺":
            pass
            # todo:: 未完成的代码 图片平铺
        elif self.底图方式 == "图片居中":
            pass
            # todo:: 未完成的代码 图片居中

        dc.DrawBitmap(bmp.ConvertToBitmap(), 0, 0)

    _Esc键关闭 = False

    @property
    def Esc键关闭(self):
        return self._Esc键关闭

    @Esc键关闭.setter
    def Esc键关闭(self, value):
        self._Esc键关闭 = value
        if value:
            self.Bind(wx.EVT_KEY_DOWN, self._OnKeyDown)

    def _OnKeyDown(self, e):
        key = e.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            exit()


class 面板(容器):
    pass

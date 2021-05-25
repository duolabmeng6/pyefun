import wx.lib.agw.floatspin as floatspin
from .wxControl import *


class 图片操作(wx.Image, 公用方法):
    pass

    def 设置宽度高度(self, width, height, quality=0):
        return 图片操作(self.Scale(width, height, quality))

    def 取位图(self, depth=-1):
        return self.ConvertToBitmap(depth)

import wx
from .wxControl import *


class 图片框(wx.StaticBitmap, 公用方法):
    pass

    @property
    def 图片(self):
        return self.取图片()

    @图片.setter
    def 图片(self, value):
        return self.置图片(value)

    @property
    def 图标(self):
        return self.取图标()

    @图标.setter
    def 图标(self, value):
        return self.置图标(value)


    def 取图片(self):
        '返回控件中当前使用的位图。'
        return self.GetBitmap()

    def 取图标(self):
        '返回控件中当前使用的图标。'
        return self.GetIcon()

    def 取缩放模式(self):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.GetScaleMode()

    @组件_异常检测
    def 置图片(self, 图片):
        return self.SetBitmap(图片)

    @组件_异常检测
    def 置图标(self, 图标):
        return self.SetIcon(图标)

    @组件_异常检测
    def 置缩放模式(self, 模式):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.SetScaleMode(模式)

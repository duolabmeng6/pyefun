import wx
from .wxControl import *


class 按钮(wx.Button, 公用方法):
    pass
    @组件_异常检测
    def 置认证图标(self,显示=True):
        return self.SetAuthNeeded(显示)
    def 显示认证图标(self):
        return self.SetAuthNeeded()
    def 隐藏认证图标(self):
        return self.SetAuthNeeded(False)
    def 置顶层默认项(self):
        '设置后再窗口中按回车即可触发按钮点击事件'
        return self.SetDefault()

class Button(按钮, 公用方法):
    pass


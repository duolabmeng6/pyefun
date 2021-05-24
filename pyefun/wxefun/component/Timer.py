import wx.adv
import wx
from .wxControl import *


class 时钟(wx.Timer, 公用方法):
    pass

    def 启动(self, milliseconds=-1, oneShot=False):
        self.Start(milliseconds, oneShot)

    def 停止(self):
        self.Stop()

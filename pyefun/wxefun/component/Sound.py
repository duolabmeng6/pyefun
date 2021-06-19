"""
播放器组件

https://www.wxpython.org/Phoenix/docs/html/wx.adv.Sound.html

"""

import wx
from .wxControl import *


class 播放器(wx.adv.Sound, 公用方法):
    def __init__(self, 文件路径):
        super(播放器, self).__init__(文件路径)

    def 从音乐文件中加载(self, 文件路径):
        return self.Create(文件路径)

    def 从音乐数据中加载(self, data):
        return self.CreateFromData(data)

    def 是否已加载(self):
        return self.IsOk()

    def 播放音乐(self, 播放次数):
        """
        wx.播放次数.仅播放一次
        wx.播放次数.循环播放

        """
        return self.Play(播放次数)

    def 播放音乐文件(self, 文件路径, 播放次数):
        """
        播放声音文件。

        如果正在播放另一种声音，它将被中断。

        True成功返回，False否则返回。请注意，通常可以在调用此函数后随时删除正在异步播放的对象，声音将继续播放，但是对于从内存数据加载的声音对象，这在 Windows 下目前不起作用。
        """
        return self.PlaySound(文件路径, 播放次数)

    def 停止播放(self,):
        return self.Stop()
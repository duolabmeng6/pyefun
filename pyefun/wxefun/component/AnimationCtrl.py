
import wx.adv
import wx
from .wxControl import *

class 动画框(wx.adv.AnimationCtrl, 公用方法):
    pass

    def 创建控件动画对象(self):
        return self.CreateCompatibleAnimation()

    def 创建控件动画对象2(self):
        return self.CreateAnimation()

    def 取当前动画(self):
        return self.GetAnimation()

    def 取当前图片(self):
        '返回当此控件显示的非活动位图；查看SetInactiveBitmap 更多信息'
        return self.GetInactiveBitmap()

    def 是否正在播放动画(self):
        return self.IsPlaying()

    @组件_异常检测
    def 载入动画_流(self,文件):
        '从给定的流中加载动画并调用SetAnimation'
        return self.Load(文件)

    @组件_异常检测
    def 载入动画_文件(self,文件):
        '从给定的文件加载动画并调用SetAnimation。'
        return self.LoadFile(文件)

    def 播放动画(self):
        return self.Play()

    def 停止播放(self):
        return self.Stop()

    @组件_异常检测
    def 载入动画(self,动画):
        '设置动画在此控件中播放'
        return self.SetAnimation(动画)

    @组件_异常检测
    def 置默认显示图片(self,图片):
        '设置位图在不播放动画时显示在控件上。'
        return self.SetInactiveBitmap(图片)

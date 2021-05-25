# -*- coding:utf-8 -*-
import wx
import pyefun.wxefun as wx
from pyefun import *


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='测试组件属性', size=(529, 390), name='frame', style=541072384)
        self.启动窗口 = wx.容器(self)
        self.Centre()
        self.按钮_测试 = wx.Button(self.启动窗口, size=(100, 48), pos=(128, 31), label='测试', name='button')
        self.按钮_测试.绑定事件(wx.事件.按钮被点击, self.按钮_测试_按钮被单击)

        self.按钮_测试.鼠标指针 = wx.鼠标指针.指向右的

        self.编辑框1 = wx.编辑框(self.启动窗口, size=(100, 48), pos=(23, 30), value='', name='text', style=0)
        self.编辑框1.边框 = wx.边框.无边框  # 不清楚为什么没效果... 还是带有默认样式的

        图片框1_图片 = wx.Image(r'./1.jpg').Scale(200, 200).ConvertToBitmap()
        self.图片框1 = wx.图片框(self.启动窗口, bitmap=图片框1_图片, size=(200, 200), pos=(19, 87), name='staticBitmap', style=0)

        self.图片框1.图片 = wx.图片操作(r'./2.png').设置宽度高度(200, 200).取位图()
        # self.图片框1.图标 = wx.Icon(r'./2.png')

        self.进度条1 = wx.进度条(self.启动窗口, range=100, size=(259, 37), pos=(243, 88), name='gauge', style=4)
        self.进度条1.SetValue(10)
        self.进度条1.位置 = 1

        self.列表框1 = wx.列表框(self.启动窗口, size=(257, 162), pos=(243, 133), name='listBox', choices=[], style=32)
        self.列表框1.Bind(wx.EVT_CHECKLISTBOX, self.列表框1_表项被单击)
        self.按钮_测试进度条 = wx.Button(self.启动窗口, size=(100, 48), pos=(244, 31), label='测试进度条', name='button',
                                  style=wx.按钮样式.文字在顶部)
        self.按钮_测试进度条.Bind(wx.EVT_BUTTON, self.按钮_测试进度条_按钮被单击)
        self.按钮_测试列表框 = wx.Button(self.启动窗口, size=(100, 48), pos=(241, 297), label='测试_列表框', name='button')
        self.按钮_测试列表框.Bind(wx.EVT_BUTTON, self.按钮_测试列表框_按钮被单击)
        self.按钮_测试图片加载 = wx.Button(self.启动窗口, size=(100, 48), pos=(23, 299), label='测试图片加载', name='button')
        self.按钮_测试图片加载.Bind(wx.EVT_BUTTON, self.按钮_测试图片加载_按钮被单击)

        self.标签1 = wx.标签(self.启动窗口, size=(111, 46), pos=(360, 30), label='标签', name='staticText', style=wx.ALIGN_RIGHT)
        self.标签2 = wx.标签(self.启动窗口, size=(111, 46), pos=(360, 60), label='标签标签标签标签标签标签标签标签标签标签', name='staticText',
                         style=wx.标签样式.省略号在开头
                         )


    def 按钮_测试_按钮被单击(self, event):
        print('按钮_测试,按钮被单击')

    def 列表框1_表项被单击(self, event):
        print('列表框1,表项被单击')

    def 按钮_测试进度条_按钮被单击(self, event):
        print('按钮_测试进度条,按钮被单击')

        def 调整进度条():
            for i in range(100):
                self.进度条1.位置 = i
                延时(0.1)

        启动线程(调整进度条)

    def 按钮_测试列表框_按钮被单击(self, event):
        print('按钮_测试列表框,按钮被单击')

        项目索引 = []
        for i in range(100):
            y = self.列表框1.加入项目(str(i))
            项目索引.append(y)

        # 延时(10)
        # print(项目索引)

        # for i in 项目索引:
        #     self.列表框1.删除指定项目(0)


    def 按钮_测试图片加载_按钮被单击(self, event):
        print('按钮_测试图片加载,按钮被单击')


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

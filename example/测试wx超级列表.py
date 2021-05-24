# -*- coding:utf-8 -*-
import wx
import pyefun.wxefun as wx
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='', size=(400, 250),name='frame',style=541072384)
        self.启动窗口 = wx.Panel(self)
        self.启动窗口.SetOwnBackgroundColour((231, 231, 231, 255))
        self.Centre()
        self.超级列表框1 = wx.ListCtrl(self.启动窗口,size=(400, 400),pos=(0, 0),name='listCtrl',style=8227)
        self.超级列表框1.SetForegroundColour((0, 0, 0, 216))
        self.超级列表框1.插入列(0,"标题",0,100)
        self.超级列表框1.插入列(0,"一列",0,100)
        for i in range(10):
            x=self.超级列表框1.插入行(0, str(i))
            self.超级列表框1.置标题(x,1, str(i))


class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
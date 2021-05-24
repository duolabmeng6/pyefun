import wx

import pyefun.wxefun as wxefun

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='aaa', size=(839, 626), name='frame', style=541072384)
        self.启动窗口 = wx.Panel(self)

        self.Centre()
        self.按钮3 = wxefun.按钮(self.启动窗口, size=(80, 32), pos=(16, 13), label='按钮', name='button')
        self.按钮3.绑定事件(wxefun.事件_按钮_被点击, self.按钮3_按钮被单击)
        self.标签1 = wxefun.标签(self.启动窗口, size=(80, 24), pos=(17, 61), label='标签', name='staticText', style=2321)
        self.标签1.绑定事件(wxefun.事件_鼠标左键按下, self.标签1_鼠标左键按下)

        self.编辑框2 = wxefun.编辑框(self.启动窗口, size=(80, 22), pos=(22, 111), value='', name='text', style=0)
        self.编辑框2.Bind(wx.EVT_TEXT, self.编辑框2_内容被改变)
        self.单选框1 = wxefun.单选框(self.启动窗口, size=(80, 24), pos=(38, 152), name='radioButton', label='单选框')
        self.单选框1.SetValue(True)
        self.多选框1 = wxefun.复选框(self.启动窗口, size=(80, 24), pos=(30, 190), name='check', label='多选框', style=12288)
        self.图片框1 = wxefun.图片框(self.启动窗口, size=(110, 70), pos=(29, 225), name='staticBitmap', style=0)

        self.组合框1 = wxefun.组合框(self.启动窗口, value='', pos=(33, 28), name='comboBox', choices=[], style=16)
        self.组合框1.SetSize((100, 22))
        self.进度条1 = wxefun.进度条(self.启动窗口, range=100, size=(120, 24), pos=(35, 71), name='gauge', style=4)
        self.进度条1.SetValue(0)
        self.滑块条1 = wxefun.滑块条(self.启动窗口, size=(120, 22), pos=(44, 110), name='slider', minValue=1, maxValue=100,
                               value=1, style=4)
        self.滑块条1.SetTickFreq(10)
        self.滑块条1.SetPageSize(5)
        self.整数微调框1 = wxefun.整数微调框(self.启动窗口, size=(60, 24), pos=(41, 146), name='wxSpinCtrl', min=0, max=100,
                                   initial=0, style=0)
        self.整数微调框1.SetBase(10)
        self.动画框1 = wxefun.动画框(self.启动窗口, size=(64, 64), pos=(194, 21), name='animationctrl', style=2097152)
        self.列表框1 = wxefun.列表框(self.启动窗口, size=(100, 50), pos=(220, 108), name='listBox', choices=[], style=32)
        self.选择列表框1 = wxefun.选择列表框(self.启动窗口, size=(100, 50), pos=(221, 174), name='listBox', choices=[], style=0)

        self.图形按钮1 = wxefun.图形按钮(self.启动窗口, size=(80, 32), pos=(3, 20), name='button')
        self.超级链接框2 = wxefun.超级链接框(self.启动窗口, size=(60, 22), pos=(122, 27), name='hyperlink', label='易起玩',
                                   url='www.012.plus', style=1)
        self.排序列表框1 = wxefun.排序列表框(self.启动窗口, size=(170, 140), pos=(25, 77), name='editableListBox', label='',
                                   style=1792)
        self.排序列表框1.SetStrings([])
        self.引导按钮1 = wxefun.引导按钮(self.启动窗口, size=(110, 50), pos=(271, 113), name='button', mainLabel='标签内容',
                                 note='描述内容')
        self.日历框1 = wxefun.日历框(self.启动窗口, size=(246, 163), pos=(9, 59), name='CalendarCtrl', style=1)
        self.日期框1 = wxefun.日期框(self.启动窗口, size=(100, 24), pos=(274, 22), name='datectrl', style=2)
        self.时间框1 = wxefun.时间框(self.启动窗口, size=(70, 24), pos=(279, 59), name='timectrl')
        self.时间框1.SetTime(13, 59, 29)
        self.超级列表框1 = wxefun.超级列表框(self.启动窗口, size=(100, 80), pos=(178, 9), name='listCtrl', style=8227)
        self.横向滚动条1 = wxefun.滚动条(self.启动窗口, size=(60, 20), pos=(192, 311), name='scrollBar', style=4)
        self.横向滚动条1.SetScrollbar(0, 1, 2, 1, True)
        self.纵向滚动条1 = wxefun.滚动条(self.启动窗口, size=(20, 60), pos=(295, 424), name='scrollBar', style=8)
        self.纵向滚动条1.SetScrollbar(0, 1, 2, 1, True)
        self.分组单选框1 = wxefun.分组单选框(self.启动窗口, size=(120, 60), pos=(476, 340), label='单选项', choices=['示例1', '示例2'],
                                   majorDimension=0, name='radioBox', style=4)
        self.颜色选择器1 = wxefun.颜色选择器(self.启动窗口, size=(80, 28), pos=(531, 241), colour=(0, 0, 0, 255), name='colourpicker',
                                   style=0)
        self.图文按钮1 = wxefun.图文按钮(self.启动窗口, size=(100, 32), pos=(517, 284), bitmap=None, label='图文按钮', name='genbutton')
        self.图文按钮L1 = wxefun.图文按钮L(self.启动窗口, size=(100, 32), pos=(380, 277), bitmap=None, label='图文按钮L',
                                   name='gradientbutton')
        self.图文按钮L1.SetForegroundColour((255, 255, 255, 255))
        self.超级链接框L1 = wxefun.超级链接框L(self.启动窗口, size=(80, 22), pos=(328, 214), name='staticText', label='易起玩',
                                     URL='www.012.plus')
        超级链接框L1_字体 = wx.Font(9, 70, 90, 400, True, 'Microsoft YaHei UI', -1)
        self.超级链接框L1.SetFont(超级链接框L1_字体)
        self.超级链接框L1.SetForegroundColour((0, 0, 255, 255))
        self.小数微调框1 = wxefun.小数微调框(self.启动窗口, size=(80, -1), pos=(50, 387), name='FloatSpin', min_val=0, max_val=5.0,
                                   increment=0.1, value=1.1, agwStyle=4)
        self.小数微调框1.SetDigits(1)

        self.按钮4 = wxefun.按钮(self.启动窗口, size=(129, 52), pos=(12, 505), label='按钮', name='button')
        self.编辑框4 = wxefun.编辑框(self.启动窗口, size=(159, 45), pos=(154, 508), value='', name='text', style=0)
        self.按钮4.绑定事件(wxefun.事件_按钮_被点击, self.按钮4_按钮_被点击)

    def 按钮4_按钮_被点击(self, event):
        print('按钮4_按钮_被点击')
        self.编辑框4.置内容("祖国你好")
        self.按钮4.置标题("你好")
        self.编辑框4.加入文本("祖国你好")
        print(wxefun.窗口_取窗口句柄(self.启动窗口))


    def 标签1_鼠标左键按下(self, event):
        print('标签1,鼠标左键按下')

    def 按钮3_按钮被单击(self, event):
        print('按钮3,按钮被单击')
        self.编辑框2.SetValue("aa")

    def 编辑框2_内容被改变(self, event):
        print('编辑框2,内容被改变')


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

# -*- coding:utf-8 -*-
import wx.lib.agw.floatspin as lib_fs
import wx.lib.agw.hyperlink as lib_hyperlink
import wx.lib.agw.gradientbutton as lib_gb
import wx.lib.buttons as lib_button
import wx.adv
# import wx
import pyefun.wxefun as wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='aaa', size=(839, 626), name='frame', style=541072384)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.按钮4 = wx.Button(self.启动窗口, size=(129, 52), pos=(12, 505), label='按钮', name='button')
        self.按钮4.Bind(wx.事件_按钮_被点击, self.按钮4_按钮被单击)
        self.编辑框4 = wx.TextCtrl(self.启动窗口, size=(159, 45), pos=(155, 508), value='1234567890', name='text', style=0)
        self.编辑框4.Bind(wx.EVT_TEXT, self.编辑框4_内容被改变)
        self.按钮5 = wx.Button(self.启动窗口, size=(80, 32), pos=(21, 9), label='按钮', name='button')
        self.标签2 = wx.StaticText(self.启动窗口, size=(80, 24), pos=(118, 9), label='标签', name='staticText', style=2321)
        self.编辑框5 = wx.TextCtrl(self.启动窗口, size=(80, 22), pos=(269, 12), value='', name='text', style=0)
        self.单选框2 = wx.RadioButton(self.启动窗口, size=(80, 24), pos=(378, 22), name='radioButton', label='单选框')
        self.多选框2 = wx.CheckBox(self.启动窗口, size=(80, 24), pos=(488, 15), name='check', label='多选框', style=12288)
        self.图片框3 = wx.StaticBitmap(self.启动窗口, size=(64, 64), pos=(596, 20), name='staticBitmap', style=0)
        self.组合框2 = wx.ComboBox(self.启动窗口, value='', pos=(17, 76), name='comboBox', choices=[], style=16)
        self.组合框2.SetSize((100, 22))
        self.进度条2 = wx.Gauge(self.启动窗口, range=100, size=(120, 24), pos=(141, 73), name='gauge', style=4)
        self.进度条2.SetValue(0)
        self.滑块条2 = wx.Slider(self.启动窗口, size=(120, 22), pos=(292, 83), name='slider', minValue=1, maxValue=100,
                              value=1, style=4)
        self.滑块条2.SetTickFreq(10)
        self.滑块条2.SetPageSize(5)
        self.整数微调框2 = wx.SpinCtrl(self.启动窗口, size=(60, 24), pos=(458, 78), name='wxSpinCtrl', min=0, max=100, initial=0,
                                  style=0)
        self.整数微调框2.SetBase(10)
        self.动画框2 = wx.adv.AnimationCtrl(self.启动窗口, size=(64, 64), pos=(26, 138), name='animationctrl', style=2097152)
        self.列表框2 = wx.ListBox(self.启动窗口, size=(100, 50), pos=(137, 152), name='listBox', choices=[], style=32)
        self.选择列表框2 = wx.CheckListBox(self.启动窗口, size=(100, 50), pos=(288, 155), name='listBox', choices=[], style=0)
        self.图形按钮2 = wx.BitmapButton(self.启动窗口, size=(80, 32), pos=(416, 155), name='button')
        self.超级链接框4 = wx.adv.HyperlinkCtrl(self.启动窗口, size=(60, 22), pos=(541, 167), name='hyperlink', label='易起玩',
                                           url='www.012.plus', style=1)
        self.排序列表框2 = wx.adv.EditableListBox(self.启动窗口, size=(170, 140), pos=(638, 138), name='editableListBox',
                                             label='', style=1792)
        self.排序列表框2.SetStrings([])
        self.引导按钮2 = wx.adv.CommandLinkButton(self.启动窗口, size=(110, 50), pos=(55, 260), name='button', mainLabel='标签内容',
                                              note='描述内容')
        self.日历框2 = wx.adv.CalendarCtrl(self.启动窗口, size=(246, 163), pos=(232, 271), name='CalendarCtrl', style=1)
        self.日期框2 = wx.adv.DatePickerCtrl(self.启动窗口, size=(100, 24), pos=(505, 286), name='datectrl', style=2)
        self.时间框2 = wx.adv.TimePickerCtrl(self.启动窗口, size=(70, 24), pos=(499, 340), name='timectrl')
        self.时间框2.SetTime(17, 2, 43)
        self.超级列表框2 = wx.ListCtrl(self.启动窗口, size=(100, 80), pos=(516, 391), name='listCtrl', style=8227)
        self.横向滚动条2 = wx.ScrollBar(self.启动窗口, size=(60, 20), pos=(389, 474), name='scrollBar', style=4)
        self.横向滚动条2.SetScrollbar(0, 1, 2, 1, True)
        self.纵向滚动条2 = wx.ScrollBar(self.启动窗口, size=(20, 60), pos=(463, 458), name='scrollBar', style=8)
        self.纵向滚动条2.SetScrollbar(0, 1, 2, 1, True)
        self.分组单选框2 = wx.RadioBox(self.启动窗口, size=(120, 60), pos=(52, 365), label='单选项', choices=['示例1', '示例2'],
                                  majorDimension=0, name='radioBox', style=4)
        self.颜色选择器2 = wx.ColourPickerCtrl(self.启动窗口, size=(80, 28), pos=(76, 207), colour=(0, 0, 0, 255),
                                          name='colourpicker', style=0)
        self.图文按钮2 = lib_button.ThemedGenBitmapTextButton(self.启动窗口, size=(100, 32), pos=(208, 230), bitmap=None,
                                                          label='图文按钮', name='genbutton')
        self.图文按钮L2 = lib_gb.GradientButton(self.启动窗口, size=(100, 32), pos=(359, 228), bitmap=None, label='图文按钮L',
                                            name='gradientbutton')
        self.图文按钮L2.SetForegroundColour((255, 255, 255, 255))
        self.超级链接框L2 = lib_hyperlink.HyperLinkCtrl(self.启动窗口, size=(80, 22), pos=(503, 234), name='staticText',
                                                   label='易起玩', URL='www.012.plus')
        超级链接框L2_字体 = wx.Font(9, 70, 90, 400, True, 'Microsoft YaHei UI', -1)
        self.超级链接框L2.SetFont(超级链接框L2_字体)
        self.超级链接框L2.SetForegroundColour((0, 0, 255, 255))
        self.小数微调框2 = lib_fs.FloatSpin(self.启动窗口, size=(80, -1), pos=(631, 310), name='FloatSpin', min_val=0,
                                       max_val=5.0, increment=0.1, value=1.1, agwStyle=4)
        self.小数微调框2.SetDigits(1)

        self.时钟2 = wx.时钟(self)
        self.时钟2.启动(1000)
        self.Bind(wx.EVT_TIMER, self.时钟2_周期事件, self.时钟2)

    def 时钟2_周期事件(self, event):
        print('时钟2,周期事件')
        print(self.编辑框4.内容)

    def 按钮4_按钮被单击(self, event):
        print('按钮4_按钮_被点击')
        self.编辑框4.内容 = "祖国你好"
        print(self.编辑框4.内容)
        self.编辑框4.高度 = 100
        self.编辑框4.宽度 = 100
        self.编辑框4.左边 = 100
        self.编辑框4.顶边 = 100
        # self.编辑框4.可视 = False
        # self.编辑框4.禁止 = True
        self.编辑框4.鼠标指针 = 5
        self.编辑框4.边框 = wx.BORDER_NONE
        print(self.编辑框4.可视)

        # self.编辑框4.置内容("祖国你好")
        self.按钮4.置标题("你好")
        # self.编辑框4.加入文本("祖国你好")
        print(wx.窗口_取窗口句柄(self.启动窗口))
        # self.时钟2.停止()

    def 编辑框4_内容被改变(self, event):
        print('编辑框4,内容被改变')


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

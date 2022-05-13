import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(823, 537), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.窗口样式.最大化按钮))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.窗口1.背景颜色 = (171, 171, 171, 255)
        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.绑定事件(wx.事件.鼠标左键被按下, self.窗口1_鼠标左键被按下)
        self.按钮2 = wx.按钮(self.容器, size=(111, 36), pos=(11, 20), label='按钮')
        self.编辑框1 = wx.编辑框(self.容器, size=(121, 42), pos=(173, 12), value='', style=wx.TE_LEFT)
        self.编辑框1.背景颜色 = (255, 255, 255, 255)
        self.标签2 = wx.标签(self.容器, size=(121, 41), pos=(338, 19), label='标签', style=wx.ALIGN_CENTER)
        self.单选框1 = wx.单选框(self.容器, size=(58, 36), pos=(497, 14), label='单选框', style=0)
        self.单选框1.选中 = False
        self.选择框1 = wx.选择框(self.容器, size=(54, 43), pos=(584, 16), label='选择框', style=wx.CHK_2STATE)
        self.选择框1.标题居左 = False
        self.选择框1.选中 = False
        self.图片框1 = wx.图片框(self.容器, size=(71, 44), pos=(665, 26), style=0)
        self.组合框1 = wx.组合框(self.容器, value='', pos=(21, 78), choices=[], style=wx.组合框样式.可编辑列表式)
        self.组合框1.SetSize((70, 29))
        self.组合框1.背景颜色 = (255, 255, 255, 255)
        self.组合框1.置列表项目([])
        self.列表框1 = wx.列表框(self.容器, size=(84, 83), pos=(120, 82), choices=[], style=wx.列表框样式.单选列表 | wx.列表框样式.禁用垂直滚动条)
        self.列表框1.背景颜色 = (255, 255, 255, 255)
        self.列表框1.置列表项目({})
        self.选择列表框1 = wx.选择列表框(self.容器, size=(76, 86), pos=(237, 79), choices=[], style=0)
        self.选择列表框1.背景颜色 = (255, 255, 255, 255)
        self.横向滚动条1 = wx.滚动条(self.容器, size=(80, 36), pos=(334, 91), name='scrollBar', style=4)
        self.纵向滚动条1 = wx.滚动条(self.容器, size=(65, 69), pos=(438, 82), name='scrollBar', style=8)
        self.进度条1 = wx.进度条(self.容器, range=100, size=(172, 48), pos=(542, 81), style=4)
        self.滑块条2 = wx.滑块条(self.容器, size=(111, 32), pos=(21, 189), minValue=1, maxValue=100, value=1, style=4)
        self.日期框1 = wx.日期框(self.容器, size=(108, 55), pos=(180, 202), name='datectrl', style=2)
        self.日历框1 = wx.日历框(self.容器, size=(81, 71), pos=(333, 193), name='CalendarCtrl', style=1)
        self.时间框1 = wx.时间框(self.容器, size=(147, 103), pos=(445, 196), name='timectrl')
        self.颜色选择器1 = wx.颜色选择器(self.容器, size=(115, 56), pos=(648, 210), colour=(0, 0, 0, 255), name='colourpicker', style=0)
        self.图形按钮1 = wx.图形按钮(self.容器, size=(95, 67), pos=(44, 296), bitmap=None, label='图形按钮')
        self.图形按钮1.正常图片 = r''
        self.图形按钮1.焦点图片 = r''
        self.图形按钮1.按下图片 = r''
        self.图形按钮1.禁止图片 = r''
        self.图形按钮1.图片缩放大小 = (32, 32)
        self.动画框1 = wx.动画框(self.容器, size=(53, 68), pos=(185, 312), style=2097152)
        self.排序列表框1 = wx.排序列表框(self.容器, size=(126, 112), pos=(289, 341), name='editableListBox', label='', style=1792)
        self.排序列表框1.背景颜色 = (255, 255, 255, 255)
        self.引导按钮1 = wx.引导按钮(self.容器, size=(120, 61), pos=(464, 360), name='button', mainLabel='标签内容', note='描述内容')
        self.超级列表框1 = wx.超级列表框(self.容器, size=(141, 96), pos=(628, 344), style=wx.超级列表框样式.大图标列表框 | wx.超级列表框样式.图标顶部对齐)
        self.超级列表框1.背景颜色 = (255, 255, 255, 255)
        self.分组单选框1 = wx.分组单选框(self.容器, size=(136, 55), pos=(5, 417), label='单选项', choices=['示例1', '示例2'], majorDimension=0,name='radioBox', style=4)
        self.整数微调框1 = wx.整数微调框(self.容器, size=(75, -1), pos=(168, 401), min=0, max=100, initial=0, style=0)
        self.整数微调框1.背景颜色 = (255, 255, 255, 255)
        self.属性表格1 = wx.属性表格(self.容器, size=(113, 116), pos=(592, 189))
        self.浏览器1 = wx.浏览器(self.容器, size=(114, 72), pos=(236, 288))
        self.浏览器1.背景颜色 = (255, 255, 255, 255)
		#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
    def 窗口1_鼠标左键被按下(self,event):
        print("窗口1_鼠标左键被按下")
                        
	
    def 窗口1_创建完毕(self,event):
        print("窗口1_创建完毕")
                        	
    def 按钮1_被单击(self,event):
        print("按钮1_被单击")
                        	#########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

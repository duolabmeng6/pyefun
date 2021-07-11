import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码##########
        
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.列表框1 = wx.列表框(self.容器, size=(159, 180), pos=(16, 9), name='listBox', choices=[], style=32)
        self.列表框1.置列表项目({})
        self.按钮1 = wx.按钮(self.容器, size=(114, 28), pos=(209, 13), label='按钮')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
		#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
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

import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.单选框1 = wx.单选框(self.容器, size=(124, 31), pos=(31, 29), label='单选框', style=0)
        self.单选框1.选中 = False
        self.选择框1 = wx.选择框(self.容器, size=(127, 29), pos=(34, 105), label='选择框', style=wx.CHK_2STATE)
        self.选择框1.标题居左 = False
        self.选择框1.选中 = False
        self.按钮1 = wx.按钮(self.容器, size=(88, 52), pos=(248, 37), label='测试')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.单选框2 = wx.单选框(self.容器, size=(90, 24), pos=(31, 67), label='单选框', style=0)
        self.单选框2.字体 = wx.Font(9, 70, 90, 400, False, 'Microsoft YaHei UI', -1)
        self.单选框2.选中 = False
#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
	
    def 按钮1_被单击(self,event):
        print("按钮1_被单击")
        self.单选框1.选中 = True
        self.选择框1.选中 = True
        self.选择框1.标题居左 = True


	#########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(600, 369), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.图形按钮1 = wx.图形按钮(self.容器, size=(330, 97), pos=(237, 93), bitmap=None, label='图形按钮')
        self.图形按钮1.正常图片 = r'.\resources\hh1.png'
        self.图形按钮1.焦点图片 = r'.\resources\hh2.png'
        self.图形按钮1.按下图片 = r'.\resources\hh3.png'
        self.图形按钮1.禁止图片 = r'.\resources\hh4.png'
        self.图形按钮1.显示方式 = r'缩放图片'
        self.图形按钮1.图片缩放大小 = (32, 32)
        self.图形按钮1.绑定事件(wx.事件.被单击, self.图形按钮1_被单击)
        self.按钮1 = wx.按钮(self.容器, size=(161, 44), pos=(35, 197), label='按钮')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.编辑框1 = wx.编辑框(self.容器, size=(149, 43), pos=(26, 21), value='', style=wx.TE_LEFT)
#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
    def 图形按钮1_被单击(self,event):
        print("图形按钮1_被单击")
                        
	
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

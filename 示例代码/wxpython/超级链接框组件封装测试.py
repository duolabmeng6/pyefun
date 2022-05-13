import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.窗口样式.最大化按钮))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.窗口1.背景颜色 = (171, 171, 171, 255)
        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.超级链接框1 = wx.超级链接框(self.容器, size=(130, 40), pos=(67, 81), label='超级链接框', url='https://wxpython.org/Phoenix/docs/html/wx.adv.HyperlinkCtrl.html',style=wx.adv.HL_DEFAULT_STYLE)
        self.超级链接框1.文本颜色 = (179, 255, 0, 255)
        self.超级链接框1.未访问颜色 = (179, 255, 0, 255)
        self.超级链接框1.焦点颜色 = (255, 0, 0, 255)
        self.标签1 = wx.标签(self.容器, size=(89, 27), pos=(208, 71), label='标签', style=wx.ALIGN_CENTER)
        self.标签1.文本颜色 = (255, 0, 0, 255)
		#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
	
    def 窗口1_创建完毕(self,event):
        print("窗口1_创建完毕")
                        
	#########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

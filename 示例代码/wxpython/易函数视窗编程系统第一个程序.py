import pyefun.wxefun as wx

class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame', style=wx.窗口边框.普通可调边框)
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.编辑框1 = wx.编辑框(self.容器, size=(321, 42), pos=(18, 39), value='易函数，你好', style=wx.TE_CENTRE)
        self.编辑框1.字体 = wx.Font(12, 74, 90, 400, False, '微软雅黑', 28)
        self.编辑框1.文本颜色 = (255, 0, 0, 255)
        self.按钮1 = wx.按钮(self.容器, size=(193, 40), pos=(76, 116), label='祖国，您好')
        self.按钮1.字体 = wx.Font(12, 74, 90, 400, False, '微软雅黑', 28)
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)

        #########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        self.编辑框1.内容 = "祖国，您好！"
        wx.信息框("祖国，您好！", "温馨提示")

    def 窗口1_创建完毕(self, event):
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

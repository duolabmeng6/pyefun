import wx.html2
import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码##########

        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(1163, 770), name='frame',
                       style=wx.窗口边框.普通可调边框 & ~(wx.窗口样式.最大化按钮))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.按钮1 = wx.按钮(self.容器, size=(78, 36), pos=(1014, 30), label='按钮')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        #########以上是创建的组件代码##########

        self.浏览器 = wx.浏览器(self.容器, size=(500, 500), pos=(0, 0), url="about:blank", style=0, name="")
        # print(self.浏览器.__bases__)
        self.浏览器.__bases__ = (wx.html2.WebView, wx.公用方法)

        # self.浏览器 = wx.html2.WebView.New(self.容器, size=(500, 500), pos=(0, 0),url="about:blank",style=0,name="")

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击22222222")
        # self.浏览器.LoadURL("https://www.baidu.com")

        self.浏览器.左边 = 100
        self.浏览器.顶边 = 100
        # self.浏览器.置组件名称("1")

    #########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

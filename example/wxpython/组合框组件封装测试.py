import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame',
                       style=wx.窗口边框.普通可调边框 & ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.窗口1.播放次数 = wx.播放次数.循环播放
        self.窗口1.位置 = wx.窗口位置.通常
        self.按钮1 = wx.按钮(self.容器, size=(97, 30), pos=(241, 63), label='测试')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.组合框样式.可编辑下拉式 | wx.组合框样式.自动排序)
        self.组合框1.SetSize((179, 36))
        self.组合框1.置列表项目([])
        self.组合框1.绑定事件(wx.事件.列表项被选择, self.组合框1_列表项被选择)
        self.组合框1.绑定事件(wx.事件.编辑内容被改变, self.组合框1_编辑内容被改变)
        self.组合框1.绑定事件(wx.事件.将弹出列表, self.组合框1_将弹出列表)
        self.组合框1.绑定事件(wx.事件.列表被关闭, self.组合框1_列表被关闭)
        self.按钮2 = wx.按钮(self.容器, size=(97, 30), pos=(243, 22), label='清空')
        self.按钮2.绑定事件(wx.事件.被单击, self.按钮2_被单击)
        self.按钮3 = wx.按钮(self.容器, size=(97, 30), pos=(236, 117), label='加入项目测试')
        self.按钮3.绑定事件(wx.事件.被单击, self.按钮3_被单击)
        self.按钮4 = wx.按钮(self.容器, size=(97, 30), pos=(245, 169), label='遍历所有项目')
        self.按钮4.绑定事件(wx.事件.被单击, self.按钮4_被单击)
        #########以上是创建的组件代码##########
        # self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.CB_SIMPLE)
        # self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.CB_DROPDOWN)
        # self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.CB_READONLY)
        # self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.CB_SORT)
        # self.组合框1 = wx.组合框(self.容器, value='', pos=(23, 20), choices=[], style=wx.TE_PROCESS_ENTER)
        self.组合框1.列表项目 = ["a", "b", "c", "d", "apple", "e"]
        self.组合框1.现行选中项 = 0
        self.组合框1.内容 = "aaaaaaaaaaaaaaa"

        # self.组合框1.置列表项目(["a", "b", "c", "d", "e"])

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        print(self.组合框1.内容)
        self.组合框1.内容 = "aaaaaaaaa"

    def 组合框1_列表项被选择(self, event):
        print("组合框1_列表项被选择")
        print(self.组合框1.现行选中项)
        print(self.组合框1.取项目文本(self.组合框1.现行选中项))

    def 组合框1_编辑内容被改变(self, event):
        print("组合框1_编辑内容被改变")

    def 组合框1_将弹出列表(self, event):
        print("组合框1_将弹出列表")

    def 组合框1_列表被关闭(self, event):
        print("组合框1_列表被关闭")
        print(self.组合框1.现行选中项)
        print(self.组合框1.取项目文本(self.组合框1.现行选中项))

    def 按钮2_被单击(self, event):
        print("按钮2_被单击")
        self.组合框1.清空()

    def 按钮3_被单击(self, event):
        print("按钮3_被单击")
        for i in range(100):
            self.组合框1.加入项目(str(i))

    def 按钮4_被单击(self, event):
        print("按钮4_被单击")
        for i in range(self.组合框1.取项目数()):
            print(i, self.组合框1.取项目文本(i))

    #########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

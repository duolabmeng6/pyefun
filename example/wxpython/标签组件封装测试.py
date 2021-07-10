import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码##########

        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame',
                       style=wx.窗口边框.普通可调边框 & ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.窗口1.播放次数 = wx.播放次数.循环播放
        self.窗口1.位置 = wx.窗口位置.通常
        self.标签1 = wx.标签(self.容器, size=(200, 111), pos=(42, 24),
                         label='标签1111111111111111111111111111111111111111111111111111111111',
                         style=wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE | wx.ST_ELLIPSIZE_START)
        self.按钮1 = wx.按钮(self.容器, size=(82, 30), pos=(26, 155), label='按钮')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)

    #########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        # self.标签1.ToggleWindowStyle(wx.标签样式.文字在右边)
        # self.标签1.SetWindowStyle(wx.标签样式.文字在右边)
        # self.标签1.SetWindowStyle(wx.标签样式.省略号在开头)
        # self.标签1.SetWindowStyle(wx.标签样式.省略号在末尾)
        # self.标签1.SetWindowStyle(wx.标签样式.省略号在中间)
        # self.标签1.Refresh()
        self.标签1.标题 = "测试标题属性的设置"
        print("测试获取标题属性", self.标签1.标题)

    #########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

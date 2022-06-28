import pyefun.wxefun as wx
import pyefun as efun


class 窗口1(wx.窗口):
    停止工作 = False
    完成数量 = 0

    def __init__(self):
        self.初始化界面()
        self.导入数据到表格(r"C:\123\tikcpy\产品信息.txt")

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='库存监控软件', size=(1200, 550), name='frame', style=wx.窗口边框.普通固定边框& ~(wx.窗口样式.最大化按钮))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.窗口1.背景颜色 = (171, 171, 171, 255)
        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.超级列表框1 = wx.超级列表框(self.容器, size=(1170, 400), pos=(7, 8), style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.显示水平表格线 | wx.超级列表框样式.显示垂直表格线 | wx.超级列表框样式.单一选择)
        self.超级列表框1.背景颜色 = (255, 255, 255, 255)
        self.按钮1 = wx.按钮(self.容器, size=(116, 54), pos=(10, 431), label='导入产品信息')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.按钮2 = wx.按钮(self.容器, size=(116, 54), pos=(161, 432), label='开始工作')
        self.按钮2.字体 = wx.Font(9, 74, 90, 400, False, 'Microsoft YaHei UI', -1)
        self.按钮2.绑定事件(wx.事件.被单击, self.按钮2_被单击)
        self.标签1 = wx.标签(self.容器, size=(385, 36), pos=(325, 443), label='进度:', style=wx.ALIGN_CENTER)
        self.编辑框1 = wx.编辑框(self.容器, size=(85, 24), pos=(1039, 445), value='5', style=wx.TE_CENTRE)
        self.编辑框1.背景颜色 = (255, 255, 255, 255)
        self.标签2 = wx.标签(self.容器, size=(64, 16), pos=(972, 450), label='工作线程', style=wx.ALIGN_CENTER)
		#########以上是创建的组件代码##########

        self.超级列表框1.插入列(0, "序号", 2, 60)
        self.超级列表框1.插入列(1, "监控id", 0, 200)
        self.超级列表框1.插入列(2, "库存", 2, 100)
        self.超级列表框1.插入列(3, "监控状态", 2, 200)
        self.超级列表框1.插入列(4, "备注", 2, 200)
        self.超级列表框1.行高 = 32


    #########以下是组件绑定的事件代码#########

    def 按钮2_被单击(self, event):
        print("按钮2_被单击")
        self.按钮2.禁止 = True

        if self.按钮2.标题 == "开始工作":
            self.停止工作 = False

            self.按钮2.标题 = "停止工作"
            efun.启动线程(self.开始工作)
        else:
            self.停止工作 = True
        efun.延时(1)
        self.按钮2.禁止 = False

    def 任务完成(self, 返回结果):
        print("任务完成 {}".format(返回结果))
        self.完成数量 = self.完成数量 + 1

    def 开始工作(self):
        pool = efun.线程池(efun.到整数(self.编辑框1.内容), 投递任务时阻塞=True)
        任务数量 = self.超级列表框1.取表项数()
        进度 = 0
        self.完成数量 = 0
        for i in range(self.超级列表框1.取表项数()):
            if self.停止工作:
                break

            self.超级列表框1.选择(i)
            self.超级列表框1.保证显示(i)
            task = pool.投递任务(self.工作任务, i)
            pool.设置任务结束回调函数(task, self.任务完成)
            进度 = efun.四舍五入((self.完成数量 / 任务数量) * 100, 2)
            self.标签1.标题 = "进度 {}% 任务总数 {} 完成数量 {}".format(进度, 任务数量, self.完成数量)

        pool.等待()
        进度 = efun.四舍五入((self.完成数量 / 任务数量) * 100, 2)
        self.标签1.标题 = "进度 {}% 任务总数 {} 完成数量 {}".format(进度, 任务数量, self.完成数量)
        # for i in range(self.超级列表框1.取表项数()):
        #     self.工作任务(i)

        self.按钮2.标题 = "开始工作"

    def 工作任务(self, i):
        监控id = self.超级列表框1.取标题(i, 1)

        print(i, 监控id)
        self.超级列表框1.置标题(i, 3, "查询中")
        efun.延时(efun.取随机数(1, 3))

        self.超级列表框1.置标题(i, 2, str(efun.取随机数(1, 9999)))
        self.超级列表框1.置标题(i, 3, "查询成功")

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        文件路径 = wx.通用对话框_打开文件(标题="请选择文件", 初始路径=efun.取运行目录(), 默认文件名="", 过滤器="所有文件|*.*", 父窗口=None)
        if 文件路径 == "":
            return

        print(文件路径)
        self.导入数据到表格(文件路径)

    def 导入数据到表格(self, 文件路径):
        self.超级列表框1.删除所有项目()

        内容 = efun.到文本(efun.读入文件(文件路径))
        arr = efun.分割文本(内容, "\r\n")
        i = 0
        for v in arr:
            # print(v)
            if v == "":
                continue
            self.超级列表框1.插入表项(i, "{}".format(i + 1))
            self.超级列表框1.置单元格文本(i, 1, v)
            i = i + 1

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

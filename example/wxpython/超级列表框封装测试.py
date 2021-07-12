import pyefun.wxefun as wx
import pyefun as efun


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(765, 472), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13), style=wx.超级列表框样式.大图标列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.按钮1 = wx.按钮(self.容器, size=(125, 35), pos=(33, 359), label='增加')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.按钮2 = wx.按钮(self.容器, size=(125, 35), pos=(172, 359), label='删除')
        self.按钮3 = wx.按钮(self.容器, size=(125, 35), pos=(314, 359), label='加图标')
        self.按钮4 = wx.按钮(self.容器, size=(125, 35), pos=(455, 359), label='遍历')
#########以上是创建的组件代码##########

        self.超级列表框1.插入列(0, heading="基本组件")  # mac
        self.超级列表框1.置列宽(0, 130)
        组件名称列表 = ["指针", "按钮", "编辑框", "标签", "单选框", "选择框", "图片框", "组合框", "列表框", "选择列表框", "横向滚动条", "纵向滚动条", "进度条",
                  "滑块条", "日期框", "日历框", "时间框", "颜色选择器", "图形按钮", "动画框", "排序列表框", "引导按钮", "超级列表框", "分组单选框", "超级链接框",
                  "整数微调框",
                  "小数微调框", "属性表格", "选择夹"]
        self.图片组 = wx.图片组类(64, 64, True)  # 设置所有图片宽高
        k = 0
        for v in 组件名称列表:
            filepath = efun.路径优化(r"C:\pyefun\wxview\resources\images\组件图标/" + v + ".png")
            if efun.文件是否存在(filepath) == False:
                filepath = efun.路径优化(r"C:\pyefun\wxview\resources\images\组件图标/默认.png")
            il_max = self.图片组.加入图片(filepath,64,64)
            k = k + 1

        self.超级列表框1.置图片组(self.图片组, wx.IMAGE_LIST_NORMAL)  # 加入图片组
        k = 0
        for v in 组件名称列表:
            self.超级列表框1.插入项目(k,v, k)
            k = k + 1


    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        self.超级列表框1.取表项数()


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

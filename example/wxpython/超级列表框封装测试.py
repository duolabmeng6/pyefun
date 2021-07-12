import pyefun.wxefun as wx
import pyefun as efun


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(765, 536), name='frame', style=wx.窗口边框.普通可调边框& ~(wx.MAXIMIZE_BOX))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.绑定事件(wx.事件.创建完毕, self.窗口1_创建完毕)
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13), style=wx.超级列表框样式.普通列表框 | wx.超级列表框样式.图标顶部对齐)
        self.超级列表框1.绑定事件(wx.事件.当前表项被改变, self.超级列表框1_当前表项被改变)
        self.按钮1 = wx.按钮(self.容器, size=(125, 35), pos=(33, 359), label='增加')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.按钮2 = wx.按钮(self.容器, size=(125, 35), pos=(172, 359), label='删除')
        self.按钮2.绑定事件(wx.事件.被单击, self.按钮2_被单击)
        self.按钮3 = wx.按钮(self.容器, size=(125, 35), pos=(315, 359), label='设置行高')
        self.按钮3.字体 = wx.Font(18, 74, 90, 700, False, '微软雅黑', 28)
        self.按钮3.绑定事件(wx.事件.被单击, self.按钮3_被单击)
        self.按钮4 = wx.按钮(self.容器, size=(125, 35), pos=(455, 359), label='遍历')
        self.按钮4.绑定事件(wx.事件.被单击, self.按钮4_被单击)
        self.按钮6 = wx.按钮(self.容器, size=(108, 38), pos=(638, 21), label='报表模式用法')
        self.按钮6.绑定事件(wx.事件.被单击, self.按钮6_被单击)
        self.按钮7 = wx.按钮(self.容器, size=(108, 38), pos=(638, 74), label='大图标列表框用法')
        self.按钮7.绑定事件(wx.事件.被单击, self.按钮7_被单击)
        self.按钮8 = wx.按钮(self.容器, size=(108, 38), pos=(638, 128), label='小图标列表框用法')
        self.按钮8.绑定事件(wx.事件.被单击, self.按钮8_被单击)
        self.按钮9 = wx.按钮(self.容器, size=(108, 38), pos=(638, 182), label='普通列表框用法')
        self.按钮9.绑定事件(wx.事件.被单击, self.按钮9_被单击)
        self.按钮10 = wx.按钮(self.容器, size=(108, 38), pos=(638, 235), label='带有选择框的列表')
        self.按钮10.绑定事件(wx.事件.被单击, self.按钮10_被单击)
        self.按钮11 = wx.按钮(self.容器, size=(108, 38), pos=(638, 289), label='取现行选中项')
        self.按钮11.绑定事件(wx.事件.被单击, self.按钮11_被单击)
        self.按钮12 = wx.按钮(self.容器, size=(108, 38), pos=(638, 350), label='取选中的项目')
        self.按钮12.绑定事件(wx.事件.被单击, self.按钮12_被单击)
        self.按钮13 = wx.按钮(self.容器, size=(118, 32), pos=(34, 425), label='选择项目')
        self.按钮13.绑定事件(wx.事件.被单击, self.按钮13_被单击)
        self.按钮14 = wx.按钮(self.容器, size=(108, 38), pos=(637, 411), label='单列带图标')
        self.按钮14.绑定事件(wx.事件.被单击, self.按钮14_被单击)
#########以上是创建的组件代码##########
        self.按钮10_被单击(self)

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        self.超级列表框1.取表项数()

    def 窗口1_创建完毕(self, event):
        print("窗口1_创建完毕")

    def 按钮2_被单击(self, event):
        print("按钮2_被单击")
        self.超级列表框1.清空()

    def 按钮6_被单击(self, event):
        print("按钮6_被单击")
        ########### 易语言中超级列表框的用法 ##############
        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13),
                               style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, "第0列")
        self.超级列表框1.插入列(1, "第1列")
        self.超级列表框1.插入列(2, "第2列")
        self.超级列表框1.插入列(3, "第3列")
        self.超级列表框1.插入列(4, "第4列")
        for i in range(100):
            self.超级列表框1.插入表项(i, "{}{}".format("第0列", i))
            self.超级列表框1.置标题(i, 1, "{}{}".format("第1列", i))
            self.超级列表框1.置标题(i, 2, "{}{}".format("第2列", i))
            self.超级列表框1.置标题(i, 3, "{}{}".format("第3列", i))
            self.超级列表框1.置标题(i, 4, "{}{}".format("第4列", i))
            if i % 2 == 0:
                self.超级列表框1.设置项目背景颜色(i, (240, 240, 240))
                self.超级列表框1.设置项目文本颜色(i, (0, 0, 255))

    def 按钮7_被单击(self, event):
        print("按钮7_被单击")
        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(13, 13),
                               style=wx.超级列表框样式.大图标列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, heading="基本组件")  # mac
        self.超级列表框1.置列宽(0, 130)
        组件名称列表 = ["指针", "按钮", "编辑框", "标签", "单选框", "选择框", "图片框", "组合框", "列表框", "选择列表框", "横向滚动条", "纵向滚动条", "进度条",
                  "滑块条", "日期框", "日历框", "时间框", "颜色选择器", "图形按钮", "动画框", "排序列表框", "引导按钮", "超级列表框", "分组单选框", "超级链接框",
                  "整数微调框",
                  "小数微调框", "属性表格", "选择夹"]
        self.图片组 = wx.图片组类(64, 64, True)  # 设置所有图片宽高
        k = 0
        for v in 组件名称列表:
            filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/" + v + ".png")
            if efun.文件是否存在(filepath) == False:
                filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/默认.png")
            il_max = self.图片组.加入图片(filepath, 32, 32)
            k = k + 1
        self.超级列表框1.置图片组(self.图片组, wx.IMAGE_LIST_NORMAL)  # 加入图片组
        k = 0
        for v in 组件名称列表:
            self.超级列表框1.插入项目(k, v, k)
            k = k + 1

    def 按钮8_被单击(self, event):
        print("按钮8_被单击")
        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(13, 13),
                               style=wx.超级列表框样式.小图标列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, heading="基本组件")  # mac
        self.超级列表框1.置列宽(0, 130)
        组件名称列表 = ["指针", "按钮", "编辑框", "标签", "单选框", "选择框", "图片框", "组合框", "列表框", "选择列表框", "横向滚动条", "纵向滚动条", "进度条",
                  "滑块条", "日期框", "日历框", "时间框", "颜色选择器", "图形按钮", "动画框", "排序列表框", "引导按钮", "超级列表框", "分组单选框", "超级链接框",
                  "整数微调框",
                  "小数微调框", "属性表格", "选择夹"]
        self.图片组 = wx.图片组类(64, 64, True)  # 设置所有图片宽高
        k = 0
        for v in 组件名称列表:
            filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/" + v + ".png")
            if efun.文件是否存在(filepath) == False:
                filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/默认.png")
            il_max = self.图片组.加入图片(filepath, 32, 32)
            k = k + 1
        self.超级列表框1.置图片组(self.图片组, wx.IMAGE_LIST_SMALL)  # 加入图片组
        k = 0
        for v in 组件名称列表:
            self.超级列表框1.插入项目(k, v, k)
            k = k + 1

    def 按钮9_被单击(self, event):
        print("按钮9_被单击")
        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13),
                               style=wx.超级列表框样式.普通列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, heading="基本组件")  # mac
        self.超级列表框1.置列宽(0, 130)
        组件名称列表 = ["指针", "按钮", "编辑框", "标签", "单选框", "选择框", "图片框", "组合框", "列表框", "选择列表框", "横向滚动条", "纵向滚动条", "进度条",
                  "滑块条", "日期框", "日历框", "时间框", "颜色选择器", "图形按钮", "动画框", "排序列表框", "引导按钮", "超级列表框", "分组单选框", "超级链接框",
                  "整数微调框",
                  "小数微调框", "属性表格", "选择夹"]
        self.图片组 = wx.图片组类(64, 64, True)  # 设置所有图片宽高
        k = 0
        for v in 组件名称列表:
            filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/" + v + ".png")
            if efun.文件是否存在(filepath) == False:
                filepath = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/默认.png")
            il_max = self.图片组.加入图片(filepath, 32, 32)
            k = k + 1
        self.超级列表框1.置图片组(self.图片组, wx.IMAGE_LIST_SMALL)  # 加入图片组
        k = 0
        for v in 组件名称列表:
            self.超级列表框1.插入项目(k, v, k)
            k = k + 1

    def 按钮4_被单击(self, event):
        print("按钮4_被单击")
        print("self.超级列表框1.取表项数()", self.超级列表框1.取表项数())
        for i in range(self.超级列表框1.取表项数()):
            print("{} {} {} {}".format(self.超级列表框1.取标题(i, 0), self.超级列表框1.取标题(i, 1), self.超级列表框1.取标题(i, 2),
                                       self.超级列表框1.取标题(i, 3)))

    def 按钮3_被单击(self, event):
        print("按钮3_被单击")
        # self.超级列表框1.设置项目背景颜色(3, (240, 240, 240))
        # self.超级列表框1.设置项目文本颜色(1, (0, 0, 255))
        # self.超级列表框1.设置项目字体(1, wx.Font(18, 74, 90, 700, False, '微软雅黑', 28))

        # self.超级列表框1.SetItemColumnImage(1 , wx.Image(1, 48, clear=True).SetBackgroundColour((255,255,255)).ConvertToBitmap())

        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13),
                               style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, "第0列")
        self.超级列表框1.插入列(1, "第1列")
        self.超级列表框1.插入列(2, "第2列")
        self.超级列表框1.插入列(3, "第3列")
        self.超级列表框1.插入列(4, "第4列")
        self.超级列表框1.行高 = 100

        for i in range(10):
            self.超级列表框1.插入表项(i, "{}{}".format("第0列", i))
            self.超级列表框1.置标题(i, 1, "{}{}".format("第1列", i))
            self.超级列表框1.置标题(i, 2, "{}{}".format("第2列", i))
            self.超级列表框1.置标题(i, 3, "{}{}".format("第3列", i))
            self.超级列表框1.置标题(i, 4, "{}{}".format("第4列", i))
            if i % 2 == 0:
                self.超级列表框1.设置项目背景颜色(i, (240, 240, 240))
                self.超级列表框1.设置项目文本颜色(i, (0, 0, 255))

        # 想设置一下行高....
        # self.图片组 = wx.图片组类(1, 32, True)  # 设置所有图片宽高
        # self.超级列表框1.置图片组(self.图片组, wx.图片组样式.小图标)  # 加入图片组

        # self.图片组 = wx.图片组类(1, 64, True)  # 设置所有图片宽高
        # self.超级列表框1.置图片组(self.图片组, wx.图片组样式.小图标)  # 加入图片组

    def 按钮10_被单击(self, event):
        print("按钮6_被单击")
        ########### 易语言中超级列表框的用法 ##############
        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(14, 13),
                               style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标顶部对齐)
        self.超级列表框1.启用选择框(True)
        self.超级列表框1.插入列(0, "第0列")
        self.超级列表框1.插入列(1, "第1列")
        self.超级列表框1.插入列(2, "第2列")
        self.超级列表框1.插入列(3, "第3列")
        self.超级列表框1.插入列(4, "第4列")
        for i in range(100):
            self.超级列表框1.插入表项(i, "{}{}".format("第0列", i))
            self.超级列表框1.置单元格文本(i, 1, "{}{}".format("第1列", i))
            self.超级列表框1.置单元格文本(i, 2, "{}{}".format("第2列", i))
            self.超级列表框1.置单元格文本(i, 3, "{}{}".format("第3列", i))
            self.超级列表框1.置单元格文本(i, 4, "{}{}".format("第4列", i))
            if i % 2 == 0:
                self.超级列表框1.设置项目背景颜色(i, (240, 240, 240))
                self.超级列表框1.设置项目文本颜色(i, (0, 0, 255))

    def 超级列表框1_当前表项被改变(self, event):
        print("超级列表框1_当前表项被改变")

    def 按钮11_被单击(self, event):
        print("按钮11_被单击")
        print(self.超级列表框1.取现行选中项(), "self.超级列表框1.取现行选中项()")
        print(self.超级列表框1.取选中项目数量(), "self.超级列表框1.取选中项目数量()")
        print(self.超级列表框1.取选中的项目索引(), "self.超级列表框1.取选中的项目索引()")
        for i in self.超级列表框1.取选中的项目索引():
            print("{} {} {} {}".format(self.超级列表框1.取标题(i, 0), self.超级列表框1.取标题(i, 1), self.超级列表框1.取标题(i, 2),
                                       self.超级列表框1.取标题(i, 3)))

    def 按钮12_被单击(self, event):
        print("按钮12_被单击")
        # self.超级列表框1.选择框全选()
        # self.超级列表框1.重画()
        # efun.延时(2)
        # self.超级列表框1.选择框全不选()
        # self.超级列表框1.重画()
        # efun.延时(2)
        # self.超级列表框1.选择框取反()
        print("选择框取选中项目索引", self.超级列表框1.选择框取选中项目索引())
        for i in self.超级列表框1.选择框取选中项目索引():
            print("{} {} {} {}".format(self.超级列表框1.取标题(i, 0), self.超级列表框1.取标题(i, 1), self.超级列表框1.取标题(i, 2),
                                       self.超级列表框1.取标题(i, 3)))

    def 按钮13_被单击(self, event):
        print("按钮13_被单击")
        # self.超级列表框1.选择(2)
        # self.超级列表框1.选择(4)
        # self.超级列表框1.取消选择(5)
        self.超级列表框1.选择(50)
        self.超级列表框1.保证显示(50)

    def 按钮14_被单击(self, event):
        print("按钮14_被单击")

        self.超级列表框1.销毁()
        self.超级列表框1 = wx.超级列表框(self.容器, size=(617, 327), pos=(13, 13),
                               style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标左边对齐 | wx.超级列表框样式.单一选择)
        self.超级列表框1.插入列(0, heading="基本组件")  # mac
        self.超级列表框1.置列宽(0, 130)
        组件名称列表 = ["指针", "按钮", "编辑框", "标签", "单选框", "选择框", "图片框", "组合框", "列表框", "选择列表框", "横向滚动条", "纵向滚动条", "进度条",
                  "滑块条", "日期框", "日历框", "时间框", "颜色选择器", "图形按钮", "动画框", "排序列表框", "引导按钮", "超级列表框", "分组单选框", "超级链接框",
                  "整数微调框",
                  "小数微调框", "属性表格", "选择夹"]

        self.图片组 = wx.图片组类(24, 24, True)  # 设置所有图片宽高
        k = 0
        for v in 组件名称列表:
            文件路径 = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/" + v + ".png")
            if efun.文件是否存在(文件路径) == False:
                文件路径 = efun.路径优化(r"C:\efun_view_system\resources\images\组件图标/默认.png")
            il_max = self.图片组.加入图片(文件路径, 24, 24)
            k = k + 1
        self.超级列表框1.置图片组(self.图片组, wx.图片组样式.小图标)  # 加入图片组
        k = 0
        for v in 组件名称列表:
            self.超级列表框1.插入项目(k, v, k)
            k = k + 1

    #########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

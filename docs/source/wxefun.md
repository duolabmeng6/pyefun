# 易函数视窗编程系统

易函数视窗编程系统是一款为中国人入门编程的产品

易函数视窗编程系统由三个主要部分组成
* pycharm插件`易函数视窗编程系统`
* 易函数视窗设计器
* 易函数ui组件库

[易函数视窗编程系统快速入门文字版](https://www.kancloud.cn/duolabmeng/pyefundoc/2310056)
[易函数视窗编程系统快速入门视频教程](https://www.bilibili.com/video/BV1rV411W7KN/)


## 优势

* 中文编程的得天独厚
* 可视化视窗设计器
* 最强的 `python` 开发工具 `Pycharm` 的加持
* `pyefun` 易函数全中文函数库以及专门为 `wxPython` 封装的中文组件属性及组件事件
* 以易语言核心支持库组件库为标准封装的界面库
* 易函数提供了国人熟悉的组件属性和组件事件命名
* 易函数支持跨平台的可视化窗口程序开发 `window` ，`mac OS`， `ubuntu` 实现一套代码多端运行
* 易函数为 `wxPython` 插上中文函数的翅膀  `import wx`  可替代为 `import pyefun.wxefun as wx` 即可提供中文函数支持对原有项目没有任何影响
* 易函数提供一键编译功能将任意python代码转换为c编译为可执行程序

代码风格展示

```python
import pyefun.wxefun as wx


class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='易函数视窗编程系统', size=(380, 250), name='frame', style=541072896)
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self

        self.按钮1 = wx.按钮(self.容器, size=(106, 42), pos=(28, 25), label='易函数您好', name='button')
        self.按钮1.鼠标指针 = wx.鼠标指针.手型
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.编辑框1 = wx.编辑框(self.容器, size=(182, 42), pos=(153, 25), value='', name='text', style=0)
        self.编辑框1.背景颜色 = (255, 255, 255, 255)
        self.按钮2 = wx.按钮(self.容器, size=(301, 39), pos=(31, 90), label='禁止状态的按钮', name='button')
        self.按钮2.禁止 = True
        self.按钮2.字体 = wx.Font(16, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.按钮2.文本颜色 = (255, 0, 0, 255)
        self.按钮2.绑定事件(wx.事件.被单击, self.按钮2_被单击)
    #########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########

    def 按钮1_被单击(self, event):
        print("按钮1_被单击")
        self.编辑框1.内容 = "祖国您好"


    def 按钮2_被单击(self,event):
        print("按钮2_被单击")

    #########以上是组件绑定的事件代码#########


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()

```

![从 Pycharm 中打开易函数视窗设计器](./_static/efun_view_system/5.png)
![从 Pycharm 中打开易函数视窗设计器 mac](./_static/efun_view_system/10.png)


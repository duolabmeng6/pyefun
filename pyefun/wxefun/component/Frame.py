import wx
from .wxControl import *
from .Sound import *


class 窗口(wx.Frame, 公用方法):

    def 关闭(self):
        self.Close(True)

    @组件_异常检测
    def 置图标(self, 图标路径):
        icon = wx.Icon(图标路径)
        self.SetIcon(icon)

    def 居中(self):
        '将窗口调整到屏幕中间'
        self.Centre()

    @组件_异常检测
    def 创建状态栏(self, 项目, 抓取器=True):  # 只能创建一个
        "项目格式为list，每个成员为tuple 格式(项目名,宽度)，如[('项目1',-1),('项目2',-1)],负数表示按比例分配"
        try:
            if self.状态栏:
                return False
        except:
            pass

        样式 = wx.STB_SHOW_TIPS | wx.STB_ELLIPSIZE_END | wx.FULL_REPAINT_ON_RESIZE
        样式 += wx.STB_SIZEGRIP if 抓取器 else 0
        self.状态栏 = self.CreateStatusBar(style=样式)
        self.状态栏.SetFieldsCount(len(项目))
        self.状态栏.SetStatusWidths([x[1] for x in 项目])
        for x in range(len(项目)):
            self.状态栏.SetStatusText(项目[x][0], x)

    @组件_异常检测
    def 置状态栏项目宽度(self, 宽度列表):
        '需要传入一个整数列表设置全部项目宽度'
        self.状态栏.SetStatusWidths(宽度列表)

    @组件_异常检测
    def 置状态栏项目文本(self, 索引, 文本):
        self.状态栏.SetStatusText(文本, 索引)

    @组件_异常检测
    def 取状态栏项目数(self):
        return self.状态栏.GetFieldsCount()

    @组件_异常检测
    def 取状态栏项目文本(self, 索引):
        return self.状态栏.GetStatusText(索引)

    @组件_异常检测
    def 取状态栏项目宽度(self, 索引):
        return self.状态栏.GetStatusWidth(索引)

    @组件_异常检测
    def 取状态栏项目样式(self, 索引):
        return self.状态栏.GetStatusStyle(索引)

    @组件_异常检测
    def 置状态栏最小宽度(self, 宽度):
        return self.状态栏.SetMinHeight(宽度)

    @组件_异常检测
    def 置状态栏项目数(self, 项目数, 宽度列表=[]):
        宽度列表 = 宽度列表 if 宽度列表 else [-1 for x in range(项目数)]
        return self.状态栏.SetFieldsCount(项目数, 宽度列表)

    音乐播放次数 = "仅播放一次"
    sound = None

    @property
    def 播放次数(self):
        return self.音乐播放次数

    @播放次数.setter
    def 播放次数(self, value):
        self.音乐播放次数 = value
        if self.sound:
            self.背景音乐 = self.背景音乐路径

    @property
    def 背景音乐(self):
        return self.背景音乐路径

    @背景音乐.setter
    def 背景音乐(self, value):
        self.背景音乐路径 = value
        if self.背景音乐路径 == "":
            return

        if not self.sound:
            self.sound = 播放器(self.背景音乐路径)
        if self.sound.IsOk():
            if self.音乐播放次数 == "循环播放":
                flag = wx.adv.SOUND_ASYNC | wx.adv.SOUND_LOOP
                self.sound.Play(flag)
            elif self.音乐播放次数 == "仅播放一次":
                flag = wx.adv.SOUND_ASYNC
                self.sound.Play(flag)
            elif self.音乐播放次数 == "不播放":
                pass
        else:
            print("音乐文件加载失败 %s" % self.背景音乐路径)

    _窗口位置 = "居中"

    @property
    def 位置(self):
        return self._窗口位置

    @播放次数.setter
    def 位置(self, value):
        self._窗口位置 = value
        if self._窗口位置 == "通常":
            self.Centre()
        elif self._窗口位置 == "居中":
            self.Centre()
        elif self._窗口位置 == "最小化":
            self.Iconize(True)
        elif self._窗口位置 == "最大化":
            self.Maximize()
        elif self._窗口位置 == "全屏":
            self.ShowFullScreen(True)

    _图标 = ""

    @property
    def 图标(self):
        return self._图标

    @播放次数.setter
    def 图标(self, value):
        self._图标 = value
        if value == "":
            return
        self.置图标(value)

    _总在最前 = False

    @property
    def 总在最前(self):
        return self._总在最前

    @播放次数.setter
    def 总在最前(self, value=True):
        self._总在最前 = value
        if value:
            style = self.GetWindowStyle()
            self.SetWindowStyle(style | wx.STAY_ON_TOP)
        else:
            self.ToggleWindowStyle(wx.STAY_ON_TOP)

    def 置菜单栏(self, 菜单栏):
        self.SetMenuBar(菜单栏)

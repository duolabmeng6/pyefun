
import wx
from .wxControl import *

class 滚动条(wx.ScrollBar, 公用方法):
    pass

    def 取页面大小(self):
        return self.GetPageSize()

    def 取最大位置(self):
        return self.GetRange()

    def 取当前位置(self):
        return self.GetThumbPosition()

    def 取滑块大小(self):
        return self.GetThumbSize()

    def 是否为垂直滚动条(self):
        return self.IsVertical()

    @组件_异常检测
    def 置当前位置(self,位置):
        return self.SetThumbPosition()

    def 置滚动条属性(self,当前位置,滑块大小,最大位置,页面大小,是否重绘=True):
        """
        假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
        scrollbar.SetScrollbar(0, 16, 50, 15)

        页面大小比拇指大小小1，因此上一页的最后一行将在下一页可见，以帮助定向用户
        """
        return self.SetScrollbar(当前位置,滑块大小,最大位置,页面大小,是否重绘)


import wx
from .wxControl import *

class 滑块条(wx.Slider, 公用方法):
    pass

    def 清除刻度线(self):
        self.ClearTicks()

    def 取行大小(self):
        return self.GetLineSize()

    def 取最大位置(self):
        return self.GetMax()

    def 取最小位置(self):
        return self.GetMin()

    def 取页面间隔(self):
        return self.GetPageSize()

    def 取滑块数值范围(self):
        '返回一个元组，包含滑块的最小值跟最大值'
        return self.GetRange()

    def 取选中终点(self):
        return self.GetSelEnd()

    def 取选中起点(self):
        return self.GetSelStart()

    def 取滑块大小(self):
        return self.GetThumbLength()

    def 取刻线间隔(self):
        return self.GetTickFreq()

    def 取滑块位置(self):
        return self.GetValue()

    @组件_异常检测
    def 置滑块大小(self,数值):
        return self.SetThumbLength(数值)

    @组件_异常检测
    def 置行大小(self,数值):
        return self.SetLineSize(数值)

    @组件_异常检测
    def 置最大位置(self,数值):
        return self.SetMax(数值)

    @组件_异常检测
    def 置最小位置(self,数值):
        return self.SetMin(数值)

    @组件_异常检测
    def 置页面间隔(self,数值):
        return self.SetPageSize(数值)

    @组件_异常检测
    def 置滑块范围(self,最小值,最大值):
        return self.SetRange(最小值,最大值)

    @组件_异常检测
    def 置选中范围(self,起点值,结束值):
        return self.SetSelection(起点值,结束值)

    @组件_异常检测
    def 置刻线位置(self,位置):
        '在指定位置上标注刻线'
        return self.SetTick(位置)

    @组件_异常检测
    def 置刻线间隔(self,间隔):
        return self.SetTickFreq(间隔)

    @组件_异常检测
    def 置滑块位置(self,位置):
        return self.SetValue()

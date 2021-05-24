import wx.adv
import wx
from .wxControl import *

class 日历框(wx.adv.CalendarCtrl, 公用方法):
    pass
    @组件_异常检测
    def 突显周末(self,突显=True):
        return self.EnableHolidayDisplay(突显)

    @组件_异常检测
    def 允许修改月份(self,允许=True):
        return self.EnableMonthChange(允许)

    def 取当前日期(self):
        '返回格式：2020/9/26 0:00:00'
        return self.GetDate()

    def 取可选日期范围(self):
        return self.GetDateRange()

    def 取标题背景色(self):
        return self.GetHeaderColourBg()

    def 取标题前景色(self):
        return self.GetHeaderColourFg()

    def 取背景高光颜色(self):
        return self.GetHighlightColourBg()

    def 取前景高光颜色(self):
        return self.GetHighlightColourFg()

    def 取周末突显背景色(self):
        return self.GetHolidayColourBg()

    def 取周末突显前景色(self):
        return self.GetHolidayColourFg()

    @组件_异常检测
    def 标记日期(self,日期,标记=True):
        '日期：0-31'
        self.Mark(日期,标记)

    @组件_异常检测
    def 清除指定日期属性(self,日期):
        '清除与给定日期相关联的所有属性（范围为1…31）。'
        self.ResetAttr(日期)

    @组件_异常检测
    def 置日期属性(self,日期,属性):
        '将属性与指定的日期关联（范围为1…31）'
        return self.SetAttr(日期,属性)

    @组件_异常检测
    def 置当前日期(self,日期):
        '设置当前日期。日期（wx.DateTime）'
        return self.SetDate(日期)

    @组件_异常检测
    def 置可选日期范围(self,最早日期,最晚日期):
        '将可以在控件中选择的日期限制为指定的范围。如果设置了任一日期，则将强制执行并True返回相应的限制。如果未设置，则现有限制将被删除并False返回。日期（wx.DateTime）'
        return self.SetDateRange(最早日期,最晚日期)

    @组件_异常检测
    def 置顶部颜色(self,前景色,背景色):
        '在控件顶部设置用于平日绘画的颜色。该方法当前仅在通用 wx.adv.CalendarCtrl中实现， 在本机版本中不执行任何操作。'
        return self.SetHeaderColours(前景色,背景色)

    @组件_异常检测
    def 置选中日期颜色(self,前景色,背景色):
        '设置用于突出显示当前所选日期的颜色。该方法当前仅在通用 wx.adv.CalendarCtrl中实现， 在本机版本中不执行任何操作。'
        return self.SetHighlightColours(前景色,背景色)

    @组件_异常检测
    def 某天标记为假日(self,日期):
        '将指定的日期标记为当前月份的假日。此方法仅在控件的通用版本中实现，而在本机控件中不执行任何操作。'
        return self.SetHoliday(日期)

    @组件_异常检测
    def 置假日突显颜色(self,前景色,背景色):
        '设置用于假日突出显示的颜色。此方法仅在控件的通用版本中实现，而在本机控件中不执行任何操作。仅当窗口样式包含 CAL_SHOW_HOLIDAYS flag或 EnableHolidayDisplay 已被调用时，才应调用它。'
        return self.SetHolidayColours(前景色,背景色)

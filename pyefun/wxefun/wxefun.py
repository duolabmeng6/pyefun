"""
组件的私有方法

"""

import wx.lib.agw.floatspin as floatspin
import wx.lib.agw.hyperlink as hyperlink
import wx.lib.agw.gradientbutton as gradientbutton
import wx.lib.buttons as lib_button
import wx.adv
import wx
from wx import *
from .wxFunc import *
from .wxEvt import *
from .wxControl import *



class 窗口(wx.Frame, 公用方法):

    def 关闭(self):
        self.Close(True)

    @组件_异常检测
    def 置图标(self,图标路径):
        icon = wx.Icon(图标路径)
        self.SetIcon(icon)

    def 居中(self):
        '将窗口调整到屏幕中间'
        self.Centre()

    @组件_异常检测
    def 创建状态栏(self,项目,抓取器=True):#只能创建一个
        "项目格式为list，每个成员为tuple 格式(项目名,宽度)，如[('项目1',-1),('项目2',-1)],负数表示按比例分配"
        try:
            if self.状态栏:
                return False
        except:
            pass

        样式 = wx.STB_SHOW_TIPS|wx.STB_ELLIPSIZE_END|wx.FULL_REPAINT_ON_RESIZE
        样式 += wx.STB_SIZEGRIP  if 抓取器 else 0
        self.状态栏 = self.CreateStatusBar(style=样式)
        self.状态栏.SetFieldsCount(len(项目))
        self.状态栏.SetStatusWidths([x[1] for x in 项目])
        for x in range(len(项目)):
            self.状态栏.SetStatusText(项目[x][0], x)

    @组件_异常检测
    def 置状态栏项目宽度(self,宽度列表):
        '需要传入一个整数列表设置全部项目宽度'
        self.状态栏.SetStatusWidths(宽度列表)

    @组件_异常检测
    def 置状态栏项目文本(self,索引,文本):
        self.状态栏.SetStatusText(文本, 索引)

    @组件_异常检测
    def 取状态栏项目数(self):
        return self.状态栏.GetFieldsCount()

    @组件_异常检测
    def 取状态栏项目文本(self,索引):
        return self.状态栏.GetStatusText(索引)

    @组件_异常检测
    def 取状态栏项目宽度(self,索引):
        return self.状态栏.GetStatusWidth(索引)

    @组件_异常检测
    def 取状态栏项目样式(self,索引):
        return self.状态栏.GetStatusStyle(索引)

    @组件_异常检测
    def 置状态栏最小宽度(self,宽度):
        return self.状态栏.SetMinHeight(宽度)

    @组件_异常检测
    def 置状态栏项目数(self,项目数,宽度列表=[]):
        宽度列表 = 宽度列表 if 宽度列表 else [-1 for x in range(项目数)]
        return self.状态栏.SetFieldsCount(项目数,宽度列表)


class 按钮(wx.Button, 公用方法):
    pass
    @组件_异常检测
    def 置认证图标(self,显示=True):
        return self.SetAuthNeeded(显示)
    def 显示认证图标(self):
        return self.SetAuthNeeded()
    def 隐藏认证图标(self):
        return self.SetAuthNeeded(False)
    def 置顶层默认项(self):
        '设置后再窗口中按回车即可触发按钮点击事件'
        return self.SetDefault()


class 标签(wx.StaticText, 公用方法):
    pass


class 编辑框(wx.TextCtrl, 公用方法):
    pass

    def 置内容(self, 内容):
        self.SetValue(内容)

    def 取新文本样式(self):
        '返回当前用于新文本的样式。'
        return self.GetDefaultStyle()

    @组件_异常检测
    def 取指定行长度(self,行号):
        '获取指定行的长度，不包括任何尾随换行符。'
        return self.GetLineLength(行号)

    @组件_异常检测
    def 取指定行内容(self,行号):
        '返回文本控件中给定行的内容，不包括任何结尾的换行符。'
        return self.GetLineText(行号)

    def 取缓冲区行数(self):
        return self.GetNumberOfLines()

    def 内容是否被修改(self):
        '返回True文本是否已被用户修改。调用SetValue 不会使控件修改。'
        return self.IsModified()

    def 是否为多行编辑框(self):
        return self.IsMultiLine()

    def 是否为单行编辑框(self):
        return self.IsSingleLine()

    @组件_异常检测
    def 载入指定文件内容(self,路径):
        '从指定文件加载内容到编辑框'
        return self.LoadFile(路径)

    @组件_异常检测
    def 内容写到指定文件(self,路径):
        '将编辑框的内容写到指定文件内'
        return self.SaveFile(路径)

    def 标记为已修改2(self):
        '将文本标记为已修改'
        return self.MarkDirty()

    @组件_异常检测
    def 指定位置转像素位置(self,位置):
        '取指定位置处的文本的像素坐标'
        return self.PositionToCoords(位置)

    @组件_异常检测
    def 指定位置转行列位置(self,位置):
        '取指定位置处的文本所在行跟列,返回一个元组,(是否存在,行,列)'
        return self.PositionToXY(位置)

    @组件_异常检测
    def 置新文本样式(self,样式):
        '更改要用于要添加到控件的新文本的默认样式。'
        return self.SetDefaultStyle(样式)

    @组件_异常检测
    def 置修改状态(self,修改=True):
        '将控件标记为是否被用户修改'
        return self.SetModified(修改)

    def 标记为已修改(self):
        '将控件标记为已被用户修改'
        return self.SetModified(True)

    def 标记为未修改(self):
        '将控件标记为未被用户修改'
        return self.SetModified(False)

    @组件_异常检测
    def 置指定范围样式(self,开始位置,结束位置,样式):
        return self.SetStyle(开始位置,结束位置,样式)

    @组件_异常检测
    def 置指定位置可见(self,位置):
        '使指定位置的字符显示在编辑框可见范围内'
        return self.ShowPosition(位置)

    @组件_异常检测
    def 指定行列转位置(self,行,列):
        '将给定的从零开始的列和行号转换为位置'
        return self.XYToPosition(行,列)

    @组件_异常检测
    def 加入文本(self,内容):
        return self.write(内容)

    def 清空内容(self):
        self.Clear()

class 单选框(wx.RadioButton, 公用方法):
    pass
    def 是否选中(self):
        return self.GetValue()

    @组件_异常检测
    def 置选中状态(self,状态):
        'True/False'
        return self.SetValue(状态)


class 复选框(wx.CheckBox, 公用方法):
    pass

    def 取三态多选框状态(self):
        '返回 0.未选中  1.选中  2.半选中'
        return self.Get3StateValue()

    @组件_异常检测
    def 置三态多选框状态(self,状态):
        '0.未选中  1.选中  2.半选中'
        return self.Set3StateValue(状态)

    def 是否选中(self):
        return self.GetValue()

    @组件_异常检测
    def 置选中状态(self,状态):
        'True/False'
        return self.SetValue(状态)

    def 是否为三态复选框(self):
        return self.Is3State()

    def 是否可设置为半选中(self):
        return self.Is3rdStateAllowedForUser()


class 图片框(wx.StaticBitmap, 公用方法):
    pass

    def 取图片(self):
        '返回控件中当前使用的位图。'
        return self.GetBitmap()

    def 取图标(self):
        '返回控件中当前使用的图标。'
        return self.GetIcon()

    def 取缩放模式(self):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.GetScaleMode()

    @组件_异常检测
    def 置图片(self,图片):
        return self.SetBitmap(图片)

    @组件_异常检测
    def 置图标(self,图标):
        return self.SetIcon(图标)

    @组件_异常检测
    def 置缩放模式(self,模式):
        '模式： 0.以原始大小显示 1.比例填充  2.通过保持纵横比，缩放位图以适合控件的大小。  3.缩放位图以填充控件的大小。'
        return self.SetScaleMode(模式)

class 组合框(wx.ComboBox, 公用方法):
    pass

    @组件_异常检测
    def 取指定项目索引(self,项目文本,是否区分大小写=False):
        return self.FindString(项目文本,是否区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项索引(self):
        return self.GetCurrentSelection()

    def 取选中项索引2(self):
        return self.GetSelection()

    def 取选中范围(self):
        return self.GetTextSelection()

    @组件_异常检测
    def 取指定项目文本(self,索引):
        return self.GetString(索引)

    def 取选中项文本(self):
        return self.GetStringSelection()

    def 列表项是否为空(self):
        return self.IsListEmpty()

    def 弹出列表(self):
        self.Popup()

    @组件_异常检测
    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    @组件_异常检测
    def 置默认文本(self,文本):
        self.SetValue(文本)

    @组件_异常检测
    def 置选中项(self,索引):
        self.SetSelection(索引)

    @组件_异常检测
    def 置选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    @组件_异常检测
    def 选中范围文本(self,开始位置,结束位置):
        '如果两个参数都等于-1，则选择控件中的所有文本'
        self.SetTextSelection(开始位置,结束位置)

    def 清空表项(self):
        self.Clear()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    @组件_异常检测
    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    @组件_异常检测
    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    @组件_异常检测
    def 删除指定项目(self,索引):
        self.Delete(索引)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)


class 进度条(wx.Gauge, 公用方法):
    pass

    def 取最大位置(self):
        return self.GetRange()

    def 取当前位置(self):
        return self.GetValue()

    def 是否为垂直进度条(self):
        return self.IsVertical()

    @组件_异常检测
    def 置最大位置(self,位置):
        return self.SetRange(位置)

    @组件_异常检测
    def 置当前位置(self,位置):
        return self.SetValue(位置)

    def 置加载模式(self):
        '使滚动条编程滚动加载状态,调用SetValue停止滚动加载'
        self.Pulse()


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

class 整数微调框(wx.SpinCtrl, 公用方法):
    pass

    def 取数值进制类型(self):
        '返回10或16，十进制或16进制'
        return self.GetBase()

    @组件_异常检测
    def 置数值进制类型(self,类型):
        '类型：10或16，十进制或16进制'
        return self.SetBase(类型)

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    @组件_异常检测
    def 置最大值(self,数值):
        return self.SetMax(数值)

    @组件_异常检测
    def 置最小值(self,数值):
        return self.SetMin(数值)

    def 取数值范围(self):
        '获取微调的数值范围'
        return self.GetRange()

    @组件_异常检测
    def 置数值范围(self,最小值,最大值):
        '设置微调的数值范围'
        return self.SetRange(最小值,最大值)

    @组件_异常检测
    def 取当前数值(self):
        return self.GetValue()

    @组件_异常检测
    def 置当前数值(self,数值):
        return self.SetValue(数值)

class 动画框(wx.adv.AnimationCtrl, 公用方法):
    pass

    def 创建控件动画对象(self):
        return self.CreateCompatibleAnimation()

    def 创建控件动画对象2(self):
        return self.CreateAnimation()

    def 取当前动画(self):
        return self.GetAnimation()

    def 取当前图片(self):
        '返回当此控件显示的非活动位图；查看SetInactiveBitmap 更多信息'
        return self.GetInactiveBitmap()

    def 是否正在播放动画(self):
        return self.IsPlaying()

    @组件_异常检测
    def 载入动画_流(self,文件):
        '从给定的流中加载动画并调用SetAnimation'
        return self.Load(文件)

    @组件_异常检测
    def 载入动画_文件(self,文件):
        '从给定的文件加载动画并调用SetAnimation。'
        return self.LoadFile(文件)

    def 播放动画(self):
        return self.Play()

    def 停止播放(self):
        return self.Stop()

    @组件_异常检测
    def 载入动画(self,动画):
        '设置动画在此控件中播放'
        return self.SetAnimation(动画)

    @组件_异常检测
    def 置默认显示图片(self,图片):
        '设置位图在不播放动画时显示在控件上。'
        return self.SetInactiveBitmap(图片)


class 列表框(wx.ListBox, 公用方法):
    pass
    @组件_异常检测
    def 取消指定选中项(self,索引):
        '在列表框中取消选择一个项目。'
        return self.Deselect(索引)

    @组件_异常检测
    def 保证显示(self,索引):
        '确保当前显示具有给定索引的项目。'
        return self.EnsureVisible(索引)

    @组件_异常检测
    def 取指定项目索引(self,查找的内容,区分大小写=False):
        '查找标签与给定字符串匹配的项目。返回项目索引'
        return self.FindString(查找的内容,区分大小写)

    def 取项目数(self):
        return self.GetCount()

    def 取可见项目数(self):
        '返回可以垂直放入列表框可见区域的项目数。'
        return self.GetCountPerPage()

    def 取选中项索引(self):
        return self.GetSelection()

    def 取选中范围索引(self):
        '返回一个列表包含所有选中项索引,用当前所选项目的位置填充一个整数数组。'
        return self.GetSelections()

    @组件_异常检测
    def 取指定项目文本(self, 索引):
        return self.GetString(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    @组件_异常检测
    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.InsertItems(项目列表,插入位置)

    def 清空表项(self):
        self.Clear()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    @组件_异常检测
    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    @组件_异常检测
    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    @组件_异常检测
    def 删除指定项目(self,索引):
        self.Delete(索引)

    @组件_异常检测
    def 项目是否选中(self,索引):
        return self.InsertItems(索引)

    def 表项是否按字母排序(self):
        return self.IsSorted()

    @组件_异常检测
    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    @组件_异常检测
    def 置指定项目背景色(self,索引,颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引,颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目前景色(self,索引,颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引,颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目字体(self,索引,字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引,字体)
        self.Refresh()

    @组件_异常检测
    def 置指定项目文本(self,索引,文本):
        self.SetString(索引,文本)

    @组件_异常检测
    def 置现行选中项_文本(self,项目文本):
        return self.SetStringSelection(项目文本)

    @组件_异常检测
    def 置现行选中项(self,索引):
        return self.SetSelection(索引)

    @组件_异常检测
    def 取选中项文本(self):
        return self.GetStringSelection()



class 选择列表框(wx.CheckListBox, 公用方法):
    pass
    @组件_异常检测
    def 置选中状态(self,索引,选中=True):
        self.Check(索引,选中)

    @组件_异常检测
    def 选中项目(self,索引):
        self.Check(索引,True)

    @组件_异常检测
    def 取消选中项目(self,索引):
        self.Check(索引,False)

    def 取项目数(self):
        return self.GetCount()

    def 取选中项(self):
        '返回一个元组,包含所有选中的表项索引'
        return self.GetCheckedItems()

    def 取选中项_文本(self):
        '返回一个元组,包含所有选中的表项文本'
        return self.GetCheckedStrings()

    @组件_异常检测
    def 是否选中(self,索引):
        return self.IsChecked(索引)

    @组件_异常检测
    def 置选中状态_批量(self,索引列表):
        '传入需要选中的索引列表,不存在的会报错'
        self.SetCheckedItems(索引列表)

    @组件_异常检测
    def 置选中状态_文本_批量(self,索引列表):
        '传入需要选中的项目文本列表,不存在的会报错'
        self.SetCheckedStrings(索引列表)

    @组件_异常检测
    def 置指定项目背景色(self, 索引, 颜色):
        '在列表框中设置项目的背景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemBackgroundColour(索引, 颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目前景色(self, 索引, 颜色):
        '在列表框中设置项目的前景色。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemForegroundColour(索引, 颜色)
        self.Refresh()

    @组件_异常检测
    def 置指定项目字体(self, 索引, 字体):
        '在列表框中设置项目的字体。仅在MSW上且wx.LB_OWNERDRAW设置了标志时有效。'
        self.SetItemFont(索引, 字体)
        self.Refresh()

    @组件_异常检测
    def 置顶指定项(self,索引):
        '将指定的项目设置为第一个可见项目。'
        self.SetFirstItem(索引)

    def 取首个可见项索引(self):
        '返回最顶部可见项目的索引。'
        return self.GetTopItem()

    @组件_异常检测
    def 取指定坐标索引(self,左边,顶边):
        '返回列表框内指定坐标处项目索引'
        return self.HitTest(左边,顶边)

    @组件_异常检测
    def 插入项目(self,插入位置,项目列表):
        return self.Insert(项目列表,插入位置)

    @组件_异常检测
    def 插入项目2(self,插入位置,项目列表):
        return self.InsertItems(项目列表,插入位置)

    def 清空表项(self):
        self.Clear()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        '会覆盖原有的项目列表'
        self.SetItems(项目列表)

    @组件_异常检测
    def 加入项目(self,项目):
        '支持单个或多个项目,多个项目使用列表传入，加入后会返回最后一个项目索引'
        return self.Append(项目)

    @组件_异常检测
    def 加入项目2(self,项目):
        '支持单个或多个项目,多个项目使用列表传入'
        self.AppendItems(项目)

    @组件_异常检测
    def 删除指定项目(self,索引):
        self.Delete(索引)


class 图形按钮(wx.BitmapButton, 公用方法):
    pass


class 超级链接框(wx.adv.HyperlinkCtrl, 公用方法):
    pass

    def 取单击前焦点颜色(self):
        '返回鼠标悬停在控件上时用于打印超链接标签的颜色。'
        return self.GetHoverColour()

    def 取初始颜色(self):
        '返回以前从未单击过链接（即尚未访问链接）并且鼠标不在控件上时用于打印标签的颜色。'
        return self.GetNormalColour()

    def 取URL(self):
        '返回与超链接关联的URL。'
        return self.GetURL()

    def 是否已点击(self):
        '返回True超链接是否已被用户至少单击一次。'
        return self.GetVisited()

    def 取单击后焦点颜色(self):
        '返回鼠标悬停在控件上且之前已单击链接（即已访问链接）时用于打印标签的颜色。'
        return self.GetVisitedColour()

    @组件_异常检测
    def 置焦点颜色(self,颜色):
        '设置鼠标悬停在控件上时用于打印超链接标签的颜色。'
        return self.SetHoverColour(颜色)

    @组件_异常检测
    def 置初始颜色(self,颜色):
        '设置以前从未单击过链接（即未访问链接）并且鼠标不在控件上时用于打印标签的颜色。'
        return self.SetNormalColour(颜色)

    @组件_异常检测
    def 置URL(self,url):
        '设置与超链接关联的URL。'
        return self.SetURL(url)

    @组件_异常检测
    def 置访问状态(self,已访问=True):
        '将超链接标记为已访问/未访问'
        return self.SetVisited(已访问)

    @组件_异常检测
    def 置已点击颜色(self,颜色):
        return self.SetVisitedColour(颜色)


class 排序列表框(wx.adv.EditableListBox, 公用方法):
    pass

    def 取项目列表(self):
        return self.GetStrings()

    @组件_异常检测
    def 置项目列表(self,项目列表):
        return self.SetStrings(项目列表)

class 引导按钮(wx.adv.CommandLinkButton, 公用方法):
    pass

    def 取主标题(self):
        return self.GetMainLabel()

    def 取描述内容(self):
        return self.GetNote()

    @组件_异常检测
    def 置标题(self,标题,描述):
        '要设置的标签和注释，两者之间用第一个换行符分隔，或者不设置空白注释'
        return self.SetLabel("{}\n{}".format(标题,描述))

    @组件_异常检测
    def 置标题2(self,标题,描述):
        return self.SetMainLabelAndNote(标题,描述)

    @组件_异常检测
    def 置主标题(self,标题):
        return self.SetMainLabel(标题)

    @组件_异常检测
    def 置描述内容(self,描述):
        return self.SetNote(描述)

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


class 日期框(wx.adv.DatePickerCtrl, 公用方法):
    pass

    def 取可选日期范围(self):
        return self.GetRange()

    @组件_异常检测
    def 置可选日期范围(self,最早日期,最晚日期):
        return self.SetRange(最早日期,最晚日期)

    def 取当前日期(self):
        return self.GetValue()

    @组件_异常检测
    def 置当前日期(self,日期):
        return self.SetValue(日期)


class 时间框(wx.adv.TimePickerCtrl, 公用方法):
    pass

    def 取当前时间(self):
        '返回一个元组，(时,分,秒)'
        return self.GetTime()

    @组件_异常检测
    def 置当前时间(self,时,分,秒):
        return self.SetTime(时,分,秒)

    def 取当前时间_dt(self):
        '返回wx.DateTime'
        return self.GetValue()

    @组件_异常检测
    def 置当前时间_dt(self,时间):
        'wx.DateTime格式时间'
        return self.SetValue(时间)



class 超级列表框(wx.ListCtrl, 公用方法):
    pass

    @组件_异常检测
    def 加入行(self,内容列表):
        '在末尾加入新一行数据，返回加入的行索引'
        return self.Append(内容列表)

    @组件_异常检测
    def 加入列(self,标题,对齐方式=2,宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.AppendColumn(标题,对齐方式,宽度)

    @组件_异常检测
    def 排列项目(self,排列方式=0):
        """
        在图标或小图标视图中排列项目
        :param 排列方式: 0.默认对齐方式  1.与控件的左侧对齐 2.与控件的顶部对齐 3.对齐网格
        :return:
        """
        return self.Arrange(排列方式)

    @组件_异常检测
    def 置选中状态(self,索引,选中=True):
        '使用复选框选中或取消选中 控件中的wx.ListItem'
        return self.CheckItem(索引,选中)

    def 全部删除(self):
        '删除所有项目和所有列'
        return self.ClearAll()

    def 删除所有列(self):
        return self.DeleteAllColumns()

    def 删除所有行(self):
        return self.DeleteAllItems()

    @组件_异常检测
    def 删除指定列(self,列索引):
        return self.DeleteColumn(列索引)

    @组件_异常检测
    def 删除指定行(self,行索引):
        return self.DeleteItem(行索引)

    @组件_异常检测
    def 开始编辑(self,行索引):
        '需要设置了 wx.LC_EDIT_LABELS 样式才能使用,开始编辑指定行的第一列'
        return self.EditLabel(行索引)

    @组件_异常检测
    def 启用或禁用交替行背景色(self,启用=True):
        '启用交替的行背景色（也称为斑马条纹）,该方法只能在虚拟报表模式（即具有LC_REPORT 和LC_VIRTUAL 样式）中为控件调用。'
        return self.EnableAlternateRowColours(启用)

    @组件_异常检测
    def 启用或禁用按键搜索(self,启用):
        '只匹配第一列，从键盘搜索项目时，如果当前输入的文本不匹配，则启用或禁用蜂鸣声。'
        return self.EnableBellOnNoMatch(启用)

    @组件_异常检测
    def 启用或禁用选择框(self,启用=True):
        '启用或禁用列表项的复选框'
        return self.EnableCheckBoxes(启用)

    @组件_异常检测
    def 启用或禁用系统主题样式(self,启用=True):
        return self.EnableSystemTheme(启用)

    @组件_异常检测
    def 保证显示(self,行索引):
        return self.EnsureVisible(行索引)

    @组件_异常检测
    def 保证显示2(self,行索引):
        return self.Focus(行索引)

    @组件_异常检测
    def 查找表项(self,查找的内容,开始索引=-1,模糊查找=False):
        '只查找第一列'
        return self.FindItem(开始索引,查找的内容,模糊查找)

    @组件_异常检测
    def 取交替行背景色(self):
        return self.GetAlternateRowColour()

    @组件_异常检测
    def 取列对象(self,列索引):
        return self.GetColumn(列索引)

    @组件_异常检测
    def 取列标题(self,列索引):
        return self.GetColumn(列索引).GetText()

    @组件_异常检测
    def 取列对齐方式(self,列索引):
        "对齐方式：0.左对齐 1.右对齐 2.居中"
        return self.GetColumn(列索引).GetAlign()

    @组件_异常检测
    def 取列宽(self,列索引):
        return self.GetColumnWidth(列索引)

    @组件_异常检测
    def 取列宽2(self,列索引):
        return self.GetColumn(列索引).GetWidth()

    def 取列数(self):
        return self.GetColumnCount()

    @组件_异常检测
    def 取可视列索引(self,索引):
        '一般用不上，除非你调整了列排序啥的我也没用过'
        return self.GetColumnOrder(索引)

    def 取列顺序索引(self):
        '一般用不上除非你改动了列，返回一个列表，包含列索引数值'
        return self.GetColumnsOrder()

    def 取可见行数(self):
        '返回列表框完全可见的行数'
        return self.GetCountPerPage()

    def 取编辑控件对象(self):
        '返回当前用于编辑标签的编辑控件。None如果没有标签被编辑，则返回'
        return self.GetEditControl()

    def 取现行选中项(self):
        '返回第一个选定的项目；如果未选择任何项目，则返回-1。'
        return self.GetFirstSelected()

    def 取现行焦点项(self):
        '获取当前焦点的项目；如果没有焦点，则返回-1。'
        return self.GetFocusedItem()

    @组件_异常检测
    def 取图片组列表(self,类型):
        '图片组类型：0.普通(大图列表)  1.小图列表  2.自定义列表  返回类型wx.ImageList'
        return self.GetImageList(类型)

    def 取行数(self):
        return self.GetItemCount()

    @组件_异常检测
    def 取行对象(self,行索引):
        return self.GetItem(行索引)

    @组件_异常检测
    def 取行背景色(self,行索引):
        return self.GetItemBackgroundColour(行索引)

    @组件_异常检测
    def 取行背景色2(self,行索引):
        return self.GetItem(行索引).GetBackgroundColour()

    @组件_异常检测
    def 取行字体(self,行索引):
        return self.GetItemFont(行索引)

    @组件_异常检测
    def 取行坐标(self,行索引):
        '返回指定行所在的x,y坐标'
        return self.GetItemPosition(行索引)

    @组件_异常检测
    def 取行矩形(self,行索引):
        '返回指定行的矩形'
        return self.GetItemRect(行索引)

    def 取图标间距(self):
        return self.GetItemSpacing()

    @组件_异常检测
    def 取行状态(self,行索引,类型=wx.LIST_STATE_SELECTED):
        '默认返回是否为现行选中项'
        return bool(self.GetItemState(行索引,类型))

    @组件_异常检测
    def 取标题(self,行索引,列索引):
        return self.GetItemText(行索引,列索引)

    @组件_异常检测
    def 取行文本颜色(self,行索引):
        '如果项目没有特定的颜色，则返回无效的颜色（而不是控件本身的默认前景色控件，因为这不允许区分与当前控件前景色相同颜色的项目和默认颜色的项目，因此，与控件始终具有相同的颜色）。'
        return self.GetItemTextColour(行索引)

    @组件_异常检测
    def 取下一选中项(self,当前索引):
        '返回指定行下面的现行选中项 没有就返回-1'
        return self.GetNextSelected(当前索引)

    def 取选中表项数(self):
        return self.GetSelectedItemCount()

    def 取文本颜色(self):
        return self.GetTextColour()

    def 取首个可见索引(self):
        '在列表或报表视图中获取最顶部可见项目的索引。'
        return self.GetTopItem()

    def 取最大尺寸(self):
        '''
        请注意，此功能仅在图标视图和小图标视图中有效，而在列表视图或报表视图中则无效（这是本机Win32控件的限制）。
        返回控件中所有项目采用的矩形。
        换句话说，如果控件客户端的大小等于此矩形的大小，则不需要滚动条，也不会留下可用空间。
        '''
        return self.GetViewRect()

    def 是否启用选择框(self):
        return self.HasCheckBoxes()

    def 是否带LC_REPORT样式(self):
        '单列或多列报表视图，带有可选标题。'
        return self.InReportView()

    @组件_异常检测
    def 插入列(self,插入位置,标题,对齐方式=2,宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.InsertColumn(插入位置,标题,对齐方式,宽度)

    @组件_异常检测
    def 插入行(self,插入位置,标题):
        '只能插入第一个标题'
        return self.InsertItem(插入位置,标题)

    @组件_异常检测
    def 插入图片(self,插入位置,图片索引):
        '与此控件和视图样式关联的图像列表的索引'
        return self.InsertItem(插入位置,图片索引)

    @组件_异常检测
    def 插入图文(self,插入位置,标题,图片索引):
        '插入图像/字符串项目。'
        return self.InsertItem(插入位置, 标题,图片索引)

    def 是否无表项(self):
        '具有某些列的控件如果没有行，则仍被认为是空的。'
        return self.IsEmpty()

    @组件_异常检测
    def 是否选中(self,行索引):
        '判断该行选择框是否勾选'
        return self.IsItemChecked(行索引)

    @组件_异常检测
    def 是否为选择项(self,索引):
        '返回True是否选择了该项目,不是选中'
        return self.IsSelected(索引)

    def 是否为虚拟报表(self):
        '返回True该控件当前是否在虚拟报表视图中。'
        return self.IsVirtual()

    @组件_异常检测
    def 表项是否可见(self,行索引):
        '检查项目是否可见。'
        return self.IsVisible(行索引)

    @组件_异常检测
    def 取指定行图片索引(self,行索引):
        '它应返回控件图像列表中项目图像的索引，如果没有图像，则返回-1'
        return self.OnGetItemImage(行索引)

    @组件_异常检测
    def 是否选中2(self,行索引):
        '它应该返回是否选中了指定 item 复选框。对于具有 使用复选框的样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemIsChecked(行索引)

    @组件_异常检测
    def 取标题2(self,行索引,列索引):
        '它应返回包含 指定 的给定列文本的字符串item。对于具有 样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemText(行索引,列索引)

    @组件_异常检测
    def 重画指定项目(self,行索引):
        return self.RefreshItem(行索引)

    @组件_异常检测
    def 重画指定范围项目(self,起始行,结束行):
        '正如RefreshItem 这仅对虚拟列表控件有用。起始项必须小于或等于结束项。重绘itemFrom 和itemTo之间的项目。'
        return self.RefreshItems(起始行,结束行)

    @组件_异常检测
    def 滚动滚动条(self,dx,dy):
        '如果处于图标，小图标或报告查看模式，则dx 指定要滚动的像素数。如果处于列表视图模式，则dx 指定要滚动的列数。dy 始终指定要垂直滚动的像素数。'
        return self.ScrollList(dx,dy)

    @组件_异常检测
    def 选择某项(self,行索引):
        '选择不是选中'
        return self.Select(行索引)

    @组件_异常检测
    def 置备用行背景色(self,颜色):
        '将备用行背景色设置为特定颜色。与一样EnableAlternateRowColours，此方法只能与具有LC_REPORT 和LC_VIRTUAL 样式的控件一起使用'
        return self.SetAlternateRowColour(颜色)

    @组件_异常检测
    def 置列标题(self,列索引,标题):
        Item = self.GetColumn(列索引)
        Item.SetText(标题)
        return self.SetColumn(列索引,Item)

    @组件_异常检测
    def 置列宽(self,列索引,宽度):
        return self.SetColumnWidth(列索引,宽度)

    @组件_异常检测
    def 置列宽2(self,列索引,宽度):
        Item = self.GetColumn(列索引)
        Item.SetWidth(宽度)
        return self.SetColumn(列索引,Item)

    @组件_异常检测
    def 置列对齐方式(self,列索引,对齐方式):
        '对齐方式: 0.左对齐  1.右对齐 2.居中'
        Item = self.GetColumn(列索引)
        Item.SetAlign(对齐方式)
        return self.SetColumn(列索引,Item)

    @组件_异常检测
    def 置列图片(self,列索引,图片):
        return self.SetColumnImage(列索引,图片)

    @组件_异常检测
    def 置列排序位置(self,排序列表):
        '修改列的位置'
        return self.SetColumnsOrder(排序列表)

    @组件_异常检测
    def 置列标题字体颜色(self,attr):
        '更改用于列表控件标题的字体和颜色。'
        return self.SetHeaderAttr(attr)

    @组件_异常检测
    def 置关联图片列表(self,图片列表):
        return self.SetImageList(图片列表)

    @组件_异常检测
    def 置标题(self,行索引,列索引,标题):
        return self.SetItem(行索引,列索引,标题)

    @组件_异常检测
    def 置图文(self,行索引,列索引,标题,图片索引):
        return self.SetItem(行索引,列索引,标题,图片索引)

    @组件_异常检测
    def 置行色(self,行索引,颜色):
        return self.SetItemBackgroundColour(行索引,颜色)

    @组件_异常检测
    def 置图片(self,行索引,列索引,图片索引):
        return self.SetItemColumnImage(行索引,列索引,图片索引)

    @组件_异常检测
    def 置行数(self,行数):
        '此方法只能与虚拟列表控件一起使用。 没用过'
        return self.SetItemCount(行数)

    @组件_异常检测
    def 置行字体(self,行索引,字体):
        return self.SetItemFont(行索引,字体)

    @组件_异常检测
    def 置选中状态图片(self,行索引,选中图索引,未选中图索引):
        '设置与项目关联的未选择和选择的图像。'
        return self.SetItemImage(行索引,选中图索引,未选中图索引)

    @组件_异常检测
    def 置项目坐标(self,项目索引,x,y):
        '在图标或小图标视图中设置项目的位置。'
        return self.SetItemPosition(项目索引,(x,y))

    @组件_异常检测
    def 置选择状态(self,行索引,是否选择):
        状态 = 4 if 是否选择 else 0
        return self.SetItemState(行索引, 状态, wx.LIST_STATE_SELECTED)

    @组件_异常检测
    def 置标题_首列(self,行索引,标题):
        return self.SetItemText(行索引,标题)

    @组件_异常检测
    def 置行文本颜色(self,行索引,颜色):
        return self.SetItemTextColour(行索引,颜色)

    @组件_异常检测
    def 添加列表样式(self,样式):
        return self.SetSingleStyle(样式,True)

    @组件_异常检测
    def 删除列表样式(self,样式):
        return self.SetSingleStyle(样式,False)

    @组件_异常检测
    def 置全部文本颜色(self,颜色):
        return self.SetTextColour(颜色)

    @组件_异常检测
    def 置窗口新样式(self,样式):
        return self.SetWindowStyleFlag(样式)

class 滚动条(wx.ScrollBar, 公用方法):
    pass


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


class 分组单选框(wx.RadioBox, 公用方法):
    pass
    @组件_异常检测
    def 启用某项(self,索引):
        return self.EnableItem(索引,True)

    @组件_异常检测
    def 禁用某项(self,索引):
        return self.EnableItem(索引,False)

    @组件_异常检测
    def 置指定项是否可用(self,索引,启用=True):
        return self.EnableItem(索引, 启用)

    @组件_异常检测
    def 查找选项(self,标题文本,区分大小写=False):
        return self.FindString(标题文本,区分大小写)

    def 取选项列数(self):
        '返回单选框中的列数。'
        return self.GetColumnCount()

    def 取选项行数(self):
        return self.GetRowCount()

    def 取选项数(self):
        return self.GetCount()

    def 取指定坐标处选项(self,x,y):
        return self.GetItemFromPoint((x,y))

    @组件_异常检测
    def 取选项帮助文本(self,索引):
        return self.GetItemHelpText(索引)

    @组件_异常检测
    def 取选项文本(self,索引):
        return self.GetItemLabel(索引)

    @组件_异常检测
    def 取选项文本2(self,索引):
        return self.GetString(索引)

    @组件_异常检测
    def 取选项提示工具(self,索引):
        '返回与指定项目关联的工具提示（ 如果有的话）None。返回类型 wx.ToolTip'
        return self.GetItemToolTip()

    @组件_异常检测
    def 取选项提示文本(self,索引):
        return self.GetItemToolTip(索引).GetTip()

    @组件_异常检测
    def 置选项提示文本(self, 索引,提示内容):
        return self.GetItemToolTip(索引).SetTip(提示内容)

    @组件_异常检测
    def 置选项提示时间(self,索引,时间=2000):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetAutoPop(时间)

    @组件_异常检测
    def 置选项提示延迟显示时间(self, 索引, 时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetDelay(时间)

    @组件_异常检测
    def 置选项提示最大宽度(self, 索引, 宽度):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetMaxWidth(宽度)

    @组件_异常检测
    def 置选项提示后续提示延时(self,索引,时间):
        '时间为毫秒'
        return self.GetItemToolTip(索引).SetReshow(时间)

    @组件_异常检测
    def 启用或禁用选项提示(self,索引,启用=True):
        return self.GetItemToolTip(索引).Enable(启用)

    def 取现行选中项(self):
        '返回所选项目的索引，或者NOT_FOUND 如果未选择任何项目，则返回该索引 。'
        return self.GetSelection()

    @组件_异常检测
    def 是否启用指定项(self,索引):
        '判断指定选项是否启用,是启用不是选中'
        return self.IsItemEnabled(索引)

    @组件_异常检测
    def 是否显示指定项(self,索引):
        '返回True当前是否显示该项目或False是否使用隐藏该项目Show。'
        return self.IsItemShown(索引)

    @组件_异常检测
    def 置选项帮助文本(self,索引,内容):
        return self.SetItemHelpText(索引,内容)

    @组件_异常检测
    def 置选项标题(self,索引,标题):
        return self.SetItemLabel(索引,标题)

    @组件_异常检测
    def 置选项提示文本(self,索引,提示内容):
        return self.SetItemToolTip(索引,提示内容)

    @组件_异常检测
    def 置选中项(self,索引):
        '指定选项设置为选中状态'
        return self.SetSelection(索引)

    @组件_异常检测
    def 置选项标题(self,索引,标题):
        '指定选项设置为选中状态'
        return self.SetSelection(索引,标题)

    @组件_异常检测
    def 显示某项(self,索引):
        return self.ShowItem(索引,True)

    @组件_异常检测
    def 隐藏某项(self,索引):
        return self.ShowItem(索引,False)

    @组件_异常检测
    def 显示或隐藏某项(self,索引,显示=True):
        return self.ShowItem(索引,显示)


class 颜色选择器(wx.ColourPickerCtrl, 公用方法):
    pass

    def 取当前颜色(self):
        return self.GetColour()

    @组件_异常检测
    def 置当前颜色(self,颜色):
        return self.SetColour(颜色)


class 图文按钮(lib_button.ThemedGenBitmapTextButton, 公用方法):
    pass

    def 取禁用状态图片(self):
        return self.GetBitmapDisabled()

    def 取焦点状态图片(self):
        return self.GetBitmapFocus()

    def 取正常状态图片(self):
        return self.GetBitmapLabel()

    def 取按下状态图片(self):
        return self.GetBitmapSelected()

    @组件_异常检测
    def 置禁用状态图片(self,图片):
        return self.SetBitmapDisabled(图片)

    @组件_异常检测
    def 置焦点状态图片(self,图片):
        return self.SetBitmapFocus(图片)

    @组件_异常检测
    def 置正常状态图片(self,图片):
        return self.SetBitmapLabel(图片)

    @组件_异常检测
    def 置按下状态图片(self,图片):
        return self.SetBitmapSelected(图片)


class 图文按钮L(gradientbutton.GradientButton, 公用方法):
    pass

    def 是否允许通过单击获取焦点(self):
        return self.AcceptsFocus()

    def 取最佳尺寸(self):
        '返回一个元组,(宽，高),覆盖基类虚拟。根据标签和边框尺寸确定按钮的最佳尺寸。'
        return self.DoGetBestSize()

    def 取渐变底纹底端颜色(self):
        return self.GetBottomEndColour()

    def 取渐变底纹顶端颜色(self):
        return self.GetTopEndColour()

    def 取渐变底纹底部起始颜色(self):
        return self.GetBottomStartColour()

    def 取渐变底纹按下底部起始颜色(self):
        return self.GetPressedBottomColour()

    def 取渐变底纹按下顶部起始颜色(self):
        return self.GetPressedTopColour()

    def 取渐变阴影顶部起始颜色(self):
        return self.GetTopStartColour()

    @组件_异常检测
    def 置各状态颜色(self,起始色,前景色):
        '设置底部，顶部，按下和前景色,起始色–用于底部，顶部和压制的基础颜色,前景色 –用于文本的颜色'
        return self.SetBaseColours(起始色,前景色)

    @组件_异常检测
    def 置图片(self,图片):
        return self.SetBitmapLabel(图片)

    @组件_异常检测
    def 置渐变底纹底端颜色(self,颜色):
        return self.SetBottomEndColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶部底部颜色(self,颜色):
        return self.SetBottomStartColour(颜色)

    @组件_异常检测
    def 置默认按钮(self):
        return self.SetDefault()

    @组件_异常检测
    def 置最佳尺寸(self):
        '将按钮调整为最佳尺寸'
        self.SetInitialSize()

    @组件_异常检测
    def 置渐变阴影下底部开始颜色(self,颜色):
        return self.SetPressedBottomColour(颜色)

    @组件_异常检测
    def 置渐变阴影设置按下顶部起始颜色(self,颜色):
        return self.SetPressedTopColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶端颜色(self,颜色):
        return self.SetTopEndColour(颜色)

    @组件_异常检测
    def 置渐变底纹顶部起始颜色(self,颜色):
        return self.SetTopStartColour(颜色)


class 超级链接框L(hyperlink.HyperLinkCtrl, 公用方法):
    pass
    @组件_异常检测
    def 允许打开链接(self,打开=True):
        '单击后自动浏览到URL。'
        return self.AutoBrowse(True)

    @组件_异常检测
    def 弹出错误提示(self,提示内容):
        return self.DisplayError(提示内容)

    @组件_异常检测
    def 允许右键弹出菜单(self,弹出=True):
        return self.DoPopup(弹出)

    @组件_异常检测
    def 允许翻转(self,允许=False):
        '干啥用的'
        return self.EnableRollover(允许)

    def 标题是否为粗体(self):
        return self.GetBold()

    def 取默认字体颜色(self):
        return self.GetColours()[0]

    def 取访问后字体颜色(self):
        return self.GetColours()[1]

    def 取焦点字体颜色(self):
        return self.GetColours()[2]

    def 取各种字体颜色(self):
        '返回一个元组,(默认颜色,点击后颜色,焦点颜色)'
        return self.GetColours()

    def 默认标题是否带下划线(self):
        return self.GetUnderlines()[0]

    def 焦点标题是否带下划线(self):
        return self.GetUnderlines()[1]

    def 点击后标题是否带下划线(self):
        return self.GetUnderlines()[2]

    def 标题是否带各状态下划线(self):
        '返回一个元组，显示各状态下标题是否带下划线,（默认标题，焦点状态标题，点击后标题）'
        return self.GetUnderlines()

    def 取鼠标光标(self):
        return self.GetLinkCursor()

    def 取URL(self):
        return self.GetURL()

    def 是否已访问过(self):
        return self.GetVisited()

    @组件_异常检测
    def 打开指定链接(self,链接):
        return self.GotoURL(链接)

    @组件_异常检测
    def 置标题字体粗细(self,粗体=True):
        return self.SetBold(粗体)

    @组件_异常检测
    def 置各状态标题颜色(self,默认,访问后,焦点):
        '设置链接，访问的链接和鼠标悬停的颜色。'
        return self.SetColours(默认,访问后,焦点)

    @组件_异常检测
    def 置默认标题颜色(self,颜色):
        return self.SetColours(颜色,None,None)

    @组件_异常检测
    def 置访问后标题颜色(self,颜色):
        return self.SetColours(None,颜色,None)

    @组件_异常检测
    def 置焦点标题颜色(self, 颜色):
        return self.SetColours(None, None, 颜色)

    @组件_异常检测
    def 置各状态标题下划线(self,默认=False,已访问=False,焦点=False):
        '设置是否应为新链接，访问的链接和过渡文本加下划线。'
        return self.SetUnderlines(默认,已访问,焦点)

    @组件_异常检测
    def 置默认标题下划线(self,下划线=True):
        return self.SetUnderlines(下划线,None,None)

    @组件_异常检测
    def 置访问猴标题下划线(self,下划线=True):
        return self.SetUnderlines(None,下划线,None)

    @组件_异常检测
    def 置焦点标题下划线(self,下划线=True):
        return self.SetUnderlines(None,None,下划线)

    @组件_异常检测
    def 置URL(self,url):
        return self.SetURL(url)

    @组件_异常检测
    def 置访问状态(self,状态=True):
        '设置链接访问状态是否已访问郭'
        return self.SetVisited(状态)

    @组件_异常检测
    def 更新链接(self,刷新控件=True):
        self.UpdateLink(刷新控件)


class 小数微调框(floatspin.FloatSpin, 公用方法):
    pass

    def 取当前数值(self):
        return self.GetDefaultValue().GetValue()

    def 取当前数值2(self):
        return self.GetValue()

    def 取默认数值(self):
        return self.GetDefaultValue()

    def 取显示的位数(self):
        return self.GetDigits()

    def 取字符格式(self):
        return self.GetFormat()

    def 取最大值(self):
        return self.GetMax()

    def 取最小值(self):
        return self.GetMin()

    @组件_异常检测
    def 置最大值(self,最大值):
        return self.SetMax(最大值)

    @组件_异常检测
    def 置最小值(self,最小值):
        return self.SetMin(最小值)

    @组件_异常检测
    def 置数值范围(self,最小值,最大值):
        return self.SetRange(最小值,最大值)

    @组件_异常检测
    def 置数值范围2(self,最小值,最大值):
        return self.SetRangeDontClampValue(最小值,最大值)

    def 是否设置数值范围(self):
        return self.HasRange()

    @组件_异常检测
    def 是否在数值范围内容(self,数值):
        '测试指定数值是否在允许的范围内'
        return self.InRange(数值)

    def 是否已设置默认值(self):
        return self.IsDefaultValue()

    @组件_异常检测
    def 置小数位数(self,位数):
        return self.SetDigits(位数)

    @组件_异常检测
    def 置字符格式(self,格式):
        return self.SetFormat(格式)

    @组件_异常检测
    def 置当前数值(self,数值):
        return self.SetValue(数值)

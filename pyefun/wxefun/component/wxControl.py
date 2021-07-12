"""
组件公用方法

"""
import wx.lib.agw.floatspin as floatspin
import wx.lib.agw.hyperlink as hyperlink
import wx.lib.agw.gradientbutton as gradientbutton
import wx.lib.buttons as lib_button
import wx.adv
import wx
import datetime
import traceback


def 组件_异常检测(function):
    '装饰器'

    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__, "函数发生异常")
            print("错误发生时间：", str(datetime.datetime.now()))
            print("错误的详细情况：", traceback.format_exc())

    return box


class 公用方法(wx.Control):
    def 绑定事件(self, event, handler, source=None, id=-1, id2=-1):  # reliably restored by inspect
        self.Bind(event, handler, source=source, id=id, id2=id2)

    def 置标题(self, 内容):
        self.SetName(内容)

    def 取窗口句柄(self):
        return self.GetHandle()

    @组件_异常检测
    def 取组件名称(self):
        return self.GetName()

    @组件_异常检测
    def 取标记ID(self):
        return self.GetId()

    @组件_异常检测
    def 取左边顶边(self):
        return self.GetPosition()

    @组件_异常检测
    def 取左边(self):
        return self.GetPosition()[0]

    @组件_异常检测
    def 取顶边(self):
        return self.GetPosition()[1]

    @组件_异常检测
    def 取宽度高度(self):
        return self.GetSize()

    @组件_异常检测
    def 取宽度高度2(self):
        return self.GetClientSize()

    @组件_异常检测
    def 取宽高3(self):
        '将窗口的最佳大小合并为最小大小'
        return self.GetEffectiveMinSize()

    @组件_异常检测
    def 取宽度(self):
        return self.GetSize()[0]

    @组件_异常检测
    def 取高度(self):
        return self.GetSize()[1]

    @组件_异常检测
    def 取祖组件(self):
        return self.GetGrandParent()

    @组件_异常检测
    def 取桌面相对坐标(self):
        "取组件左边跟顶边相对于桌面的坐标位置"
        return self.GetScreenPosition()

    @组件_异常检测
    def 取桌面相对坐标2(self):
        "取组件左边跟顶边相对于桌面的坐标位置"
        return self.ClientToScreen(0, 0)

    @组件_异常检测
    def 取窗口相对屏幕矩形(self):
        '出错返回False,返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边,组件宽度,组件高度)'
        return self.GetScreenRect()

    @组件_异常检测
    def 取背景颜色(self):
        '返回窗口的背景色,格式:(240, 240, 240, 255)'
        return self.GetBackgroundColour()

    @组件_异常检测
    def 取可设置的最小尺寸(self):
        '返回窗口的最佳可接受最小尺寸, 返回格式: (宽度, 高度)，高度不包含标题栏高度'
        return self.GetBestSize()

    @组件_异常检测
    def 取可设置的最大尺寸(self):
        '返回窗口的最佳可接受最大尺寸, 返回格式: (宽度, 高度)，高度不包含标题栏高度'
        return self.GetBestVirtualSize()

    @组件_异常检测
    def 取主题样式(self):
        '样式：0.默认背景样式值,1.使用由系统或当前主题确定的默认背景,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.无介绍,4.表示未擦除窗口背景，从而使父窗口得以显示'
        return self.GetBackgroundStyle()

    @组件_异常检测
    def 取边框样式(self):
        return self.GetBorder()

    @组件_异常检测
    def 取额外样式(self):
        return self.GetExtraStyle()

    @组件_异常检测
    def 取字体及颜色(self):
        '返回: 字体,背景颜色,前景颜色，#(<wx._core.Font object at 0x000002140997DB88>, wx.Colour(240, 240, 240, 255), wx.Colour(0, 0, 0, 255))'
        结果 = self.GetClassDefaultAttributes()
        return 结果.font, 结果.colBg, 结果.colFg

    @组件_异常检测
    def 取矩形(self):
        '返回窗口矩形：(左边,顶边,宽度,高度)'
        return self.GetRect()

    @组件_异常检测
    def 取工作区矩形(self):
        return self.GetClientRect()

    @组件_异常检测
    def 取字体(self):
        return self.GetFont()

    @组件_异常检测
    def 取字体高度(self):
        '返回此窗口的字符高度'
        return self.GetCharHeight()

    @组件_异常检测
    def 取字体平均宽度(self):
        '返回此窗口的平均字符宽度'
        return self.GetCharWidth()

    @组件_异常检测
    def 取前景色(self):
        return self.GetForegroundColour()

    @组件_异常检测
    def 取标题(self):
        return self.GetLabel()

    @组件_异常检测
    def 取标题T(self):
        return self.GetTitle()

    @组件_异常检测
    def 取内容(self):
        return self.GetValue()

    @组件_异常检测
    def 取工作区最小宽高(self):
        '返回窗口的工作区的最小大小，这向sizer布局机制指示这是其工作区的最小所需大小'
        return self.GetMinClientSize()

    @组件_异常检测
    def 取最小宽高(self):
        '返回窗口的最小大小，这向sizer布局机制指示这是最小所需大小'
        return self.GetMinSize()

    @组件_异常检测
    def 取下一个组件(self):
        '返回下一个组件的对象，即按TAB键切换到的下一个组件'
        return self.GetNextSibling()

    @组件_异常检测
    def 取下上一个组件(self):
        '返回上一个组件的对象，即按TAB键切换到的上一个组件'
        return self.GetPrevSibling()

    @组件_异常检测
    def 取父窗口(self):
        '返回父窗口对象'
        return self.GetParent()

    @组件_异常检测
    def 取顶级窗口(self):
        return self.GetTopLevelParent()

    @组件_异常检测
    def 取虚拟宽高(self):
        '这将获取窗口的虚拟大小,它返回窗口的客户端大小，但是在调用SetVirtualSize 它之后，将返回使用该方法设置的大小'
        return self.GetVirtualSize()

    @组件_异常检测
    def 取内置滚动条缩略图大小(self, 方向):
        '返回内置滚动条的缩略图大小,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollThumb(方向)

    @组件_异常检测
    def 取内置滚动条范围(self, 方向):
        '返回内置滚动条范围,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollRange(方向)

    @组件_异常检测
    def 取内置滚动条位置(self, 方向):
        '返回内置滚动条的位置,方向：4.横向滚动条 8.纵向滚动条'
        return self.GetScrollPos(方向)

    @组件_异常检测
    def 置组件名称(self, 名称):
        return self.SetName(名称)

    def 置标记ID(self):
        return self.SetId()

    @组件_异常检测
    def 置左边顶边(self, 左边, 顶边):
        return self.Move(左边, 顶边)

    @组件_异常检测
    def 置左边顶边2(self, 左边, 顶边):
        return self.SetPosition(左边, 顶边)

    @组件_异常检测
    def 置左边(self, 左边):
        return self.Move(左边, self.GetPosition()[1])

    @组件_异常检测
    def 置顶边(self, 顶边):
        return self.Move(self.GetPosition()[0], 顶边)

    @组件_异常检测
    def 置左边2(self, 左边):
        return self.SetPosition(左边, self.GetPosition()[1])

    @组件_异常检测
    def 置顶边2(self, 顶边):
        return self.SetPosition(self.GetPosition()[0], 顶边)

    @组件_异常检测
    def 置宽度高度(self, 宽度, 高度):
        return self.GetSize((宽度, 高度))

    @组件_异常检测
    def 置宽度高度2(self, 宽度, 高度):
        return self.SetInitialSize((宽度, 高度))

    @组件_异常检测
    def 置宽度(self, 宽度):
        return self.SetInitialSize((宽度, self.GetSize()[1]))

    @组件_异常检测
    def 置高度(self, 高度):
        return self.SetInitialSize((self.GetSize()[0], 高度))

    @组件_异常检测
    def 置标题(self, 标题):
        return self.SetLabel(标题)

    @组件_异常检测
    def 置标题T(self, 标题):
        return self.SetTitle(标题)

    @组件_异常检测
    def 置内容(self, 内容):
        return self.SetValue(内容)

    @组件_异常检测
    def 置拖放权限(self, 拖放=True):
        "设置是否允许接收拖放文件"
        return self.DragAcceptFiles(拖放)

    @组件_异常检测
    def 置工作区宽高(self, 宽度, 高度):
        '出设置组件工作区的宽高(不包含边框,标题栏的宽高)'
        return self.SetClientSize(宽度, 高度)

    @组件_异常检测
    def 置背景颜色(self, 颜色):
        return self.SetBackgroundColour(颜色)

    @组件_异常检测
    def 单独置背景颜色(self, 颜色):
        '设置窗口的背景色，但防止其被该窗口的子级继承'
        return self.SetOwnBackgroundColour(颜色)

    @组件_异常检测
    def 置前景颜色(self, 颜色):
        return self.SetForegroundColour(颜色)

    @组件_异常检测
    def 单独置前景颜色(self, 颜色):
        '设置窗口的前景色，但防止其被该窗口的子级继承'
        return self.SetOwnForegroundColour(颜色)

    @组件_异常检测
    def 置最大宽高(self, 宽度, 高度):
        '设置整个窗口最大可设置的尺寸'
        return self.SetMaxSize((宽度, 高度))

    @组件_异常检测
    def 置最小宽高(self, 宽度, 高度):
        '设置整个窗口最小可设置的尺寸'
        return self.SetMinSize((宽度, 高度))

    @组件_异常检测
    def 置工作区最大宽高(self, 宽度, 高度):
        '设置工作区最大可设置的尺寸'
        return self.SetMaxClientSize((宽度, 高度))

    @组件_异常检测
    def 置工作区最小宽高(self, 宽度, 高度):
        '设置工作区最小可设置的尺寸'
        return self.SetMinClientSize((宽度, 高度))

    @组件_异常检测
    def 置虚拟宽高(self, 宽度, 高度):
        '设置窗口的虚拟大小（以像素为单位）'
        return self.SetVirtualSize((宽度, 高度))

    @组件_异常检测
    def 置透明度(self, 透明度):
        '设置窗口与透明度,范围0-255(0.完全透明,255完全不透明)'
        return self.SetTransparent(透明度)

    @组件_异常检测
    def 置主题样式(self, 样式):
        '窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
        return self.SetBackgroundStyle(样式)

    @组件_异常检测
    def 置窗口样式(self, 样式):
        return self.SetWindowStyleFlag(样式)

    @组件_异常检测
    def 置鼠标样式(self, 样式):
        '''

        出错返回False,样式:
        0:无描述
        1:标准箭头光标。
        2:指向右侧的标准箭头光标。
        3:靶心光标。
        4:矩形字符光标。
        5:十字光标。
        6:手形光标。
        7:工字梁光标（垂直线）。
        8:表示鼠标左键按下。
        9:放大镜图标。
        10:表示按下中间按钮的鼠标。
        11:不可输入的符号光标。
        12:画笔光标。
        13:铅笔光标。
        14:指向左的光标。
        15:指向右的光标。
        16:箭头和问号。
        17:表示按下了右键的鼠标。
        18:调整大小的光标指向NE-SW。
        19:调整大小的光标指向N-S。
        20:调整大小的光标指向NW-SE。
        21:调整大小的光标指向W-E。
        22:一般大小的游标。
        23:Spraycan游标。
        24:等待光标。
        25:监视光标。
        26:透明光标。
        27:带有标准箭头的等待光标。
        28:无描述。

        '''
        return self.SetCursor(wx.Cursor(样式))

    @组件_异常检测
    def 取鼠标样式(self):
        return self.GetCursor()

    @组件_异常检测
    def 置字体(self, 字体):
        return self.SetFont(字体)

    @组件_异常检测
    def 置字体2(self, 字体名, 大小, 粗细, 下划线):
        return self.SetFont(wx.Font(大小, wx.DEFAULT, wx.NORMAL, 粗细, 下划线, 字体名))

    @组件_异常检测
    def 置文本颜色(self, 颜色):
        return self.SetForegroundColour(颜色)

    @组件_异常检测
    def 置组件顺序_上(self, 上一个组件):
        '设置使用TAB键切换组件时的切换顺序，从上一个组件按下TAB键后跳转到单前组件'
        return self.MoveAfterInTabOrder(上一个组件)

    @组件_异常检测
    def 置组件顺序_下(self, 下一个组件):
        '设置使用TAB键切换组件时的切换顺序，从在单前组件按下TAB键后切换到下一个组件'
        return self.MoveBeforeInTabOrder(下一个组件)

    @组件_异常检测
    def 置滚动条属性(self, 方向, 位置, 可见大小, 最大位置, 重绘):
        '''
        设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)
        假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
        self.SetScrollbar(wx.VERTICAL, 0, 16, 50)
        '''
        return self.SetScrollbar(方向, 位置, 可见大小, 最大位置, 重绘)

    @组件_异常检测
    def 置滚动条位置(self, 方向, 位置, 重绘):
        '设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)'
        return self.SetScrollPos(方向, 位置, 重绘)

    @组件_异常检测
    def 销毁(self):
        return self.Destroy()

    @组件_异常检测
    def 销毁2(self):
        '官方解释：计划在不久的将来销毁该窗口,每当销毁可能发生得太早时（例如，当该窗口或其子级仍在事件队列中等待时），都应使用此方法'
        return self.DestroyLater()

    @组件_异常检测
    def 销毁子窗口(self):
        return self.DestroyChildren()

    @组件_异常检测
    def 禁用2(self):
        return self.Disable()



    @组件_异常检测
    def 禁止重画(self):
        return self.Freeze()

    @组件_异常检测
    def 允许重画(self):
        return self.Thaw()

    @组件_异常检测
    def 移动(self, 左边=-1, 顶边=-1, 宽度=-1, 高度=-1):
        '调整移动窗口的左边跟顶边位置并重新设置宽度跟高度,不想调整的填-1'
        return self.SetSize(左边, 顶边, 宽度, 高度)

    @组件_异常检测
    def 刷新重绘(self, 删除背景=False):
        '导致GTK1重新绘制此窗口及其所有子级（除非未实现此子级）'
        return self.Refresh(删除背景)

    @组件_异常检测
    def 刷新重绘2(self):
        '调用此方法将立即重新绘制窗口的无效区域及其所有子级的对象（通常仅在控制流返回事件循环时才发生）'
        return self.Update()

    def 重画(self):
        self.Refresh()
        self.Update()

    @组件_异常检测
    def 遍历下级组件(self):
        '遍历组件下的子级组件,返回在WindowList 列表里'
        return self.GetChildren()

    @组件_异常检测
    def 弹出菜单(self, 菜单, 左边=0, 顶边=0):
        '此函数在此窗口中的给定位置显示一个弹出菜单，并返回所选的ID'
        return self.GetPopupMenuSelectionFromUser(菜单, 左边, 顶边)

    @组件_异常检测
    def 移动鼠标(self, x, y):
        '移动鼠标到组件内的指定位置'
        return self.WarpPointer(x, y)

    @组件_异常检测
    def 是否有焦点(self):
        return self.HasFocus()

    @组件_异常检测
    def 是否有滚动条(self, 方向):
        '返回此窗口当前是否具有该方向的滚动条,方向：4.横向滚动条 8.纵向滚动条'
        return self.HasScrollbar(方向)

    @组件_异常检测
    def 是否透明(self):
        return self.HasTransparentBackground()

    @组件_异常检测
    def 显示或隐藏(self, 是否显示=True):
        '显示或隐藏窗口'
        return self.Show(是否显示)

    @组件_异常检测
    def 隐藏(self):
        return self.Show(False)

    @组件_异常检测
    def 隐藏2(self):
        return self.Hide()

    @组件_异常检测
    def 隐藏_带特效(self, 效果, 效果时长):
        '''
        出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
        效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
        效果时长：单位毫秒
        '''
        return self.HideWithEffect(效果, 效果时长)

    @组件_异常检测
    def 显示(self):
        return self.Show(True)

    @组件_异常检测
    def 显示_带特效(self, 效果, 效果时长):
        '''
        出错返回False,此功能可隐藏一个窗口并使用特殊的视觉效果
        效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
        效果时长：单位毫秒
        '''
        return self.ShowWithEffect(效果, 效果时长)

    @组件_异常检测
    def 是否继承父窗口背景色(self):
        return self.InheritsBackgroundColour()

    @组件_异常检测
    def 是否继承父窗口前景色(self):
        return self.InheritsForegroundColour()

    @组件_异常检测
    def 重置缓存最佳大小(self):
        '出错返回False,重置缓存的最佳大小值，以便下次需要时重新计算'
        return self.InvalidateBestSize()

    @组件_异常检测
    def 是否正在销毁(self):
        '出错返回False,此窗口是否正在销毁中'
        return self.IsBeingDeleted()

    @组件_异常检测
    def 是否禁用(self):
        return not self.IsEnabled()

    @组件_异常检测
    def 是否可获取焦点(self):
        return self.IsFocusable()

    @组件_异常检测
    def 是否为上级窗口(self, 待判断组件):
        return self.IsDescendant(待判断组件)

    @组件_异常检测
    def 是否禁止重画(self):
        return self.IsFrozen()

    @组件_异常检测
    def 是否隐藏(self):
        '判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
        return self.IsShown()

    @组件_异常检测
    def 是否允许透明(self):
        return self.CanSetTransparent()

    @组件_异常检测
    def 是否显示在屏幕上(self):
        return self.IsShownOnScreen()

    @组件_异常检测
    def 是否启用(self):
        '是否从本质上启用了此窗口，False否则返回'
        return self.IsThisEnabled()

    @组件_异常检测
    def 是否为顶级窗口(self):
        return self.IsTopLevel()

    @组件_异常检测
    def 重绘指定区域(self, 矩形=(0, 0, 0, 0), 擦除背景=True):
        '重绘指定矩形的内容：仅对其内部的区域进行重绘'
        return self.RefreshRect(矩形, 擦除背景)

    @组件_异常检测
    def 修改父级窗口(self, 新父级组件):
        '即该窗口将从其当前父窗口中移除加入到新的父级窗口下'
        return self.Reparent(新父级组件)

    @组件_异常检测
    def 桌面坐标转窗口内坐标(self, x, y):
        '从屏幕转换为客户端窗口内工作区坐标,'
        return self.ScreenToClient(x, y)

    @组件_异常检测
    def 到最顶层(self):
        '调整显示顺序'
        self.Raise()

    @组件_异常检测
    def 到最底层(self):
        '调整显示顺序'
        self.Lower()

    @组件_异常检测
    def 是否已设置背景色(self):
        return self.UseBackgroundColour()

    @组件_异常检测
    def 是否已设置前景色(self):
        return self.UseForegroundColour()

    @组件_异常检测
    def 向上滚动(self):
        '与ScrollLines （-1）相同,返回True是否滚动窗口，False如果窗口已经在顶部，则什么也不做'
        return self.LineUp()

    @组件_异常检测
    def 向下滚动(self):
        '与ScrollLines （1）相同，返回True是否滚动窗口，False如果窗口已经在底部，则什么也不做'
        return self.LineDown()

    @组件_异常检测
    def 是否始终显示滚动条(self, 方向):
        '判断滚动条是否始终显示,方向：4.横向滚动条 8.纵向滚动条'
        return self.IsScrollbarAlwaysShown(方向)

    @组件_异常检测
    def 滚动_页(self, 滚动页数=1):
        '滚动页数:向上滚动1次为-1,向下为1'
        return self.ScrollPages(滚动页数)

    @组件_异常检测
    def 滚动_行(self, 滚动行数=1):
        '出错返回False,滚动行数:向上滚动1次为-1,向下为1'
        return self.ScrollLines(滚动行数)

    @组件_异常检测
    def 是否使用系统主题设置背景(self):
        '窗口是否使用系统主题绘制其背景'
        return self.GetThemeEnabled()

    @property
    def 高度(self):
        return self.取高度()

    @property
    def 左边(self):
        return int(self.取左边())

    @property
    def 宽度(self):
        return self.取宽度()

    @property
    def 顶边(self):
        return int(self.取顶边())

    @高度.setter
    def 高度(self, value):
        self.置高度(value)

    @宽度.setter
    def 宽度(self, value):
        self.置宽度(value)

    @左边.setter
    def 左边(self, value):
        self.置左边(value)

    @顶边.setter
    def 顶边(self, value):
        self.置顶边(value)

    @property
    def 可视(self):
        return self.是否隐藏()

    @可视.setter
    def 可视(self, value):
        self.显示或隐藏(value)

    @property
    def 禁止(self):
        return self.是否禁用()

    @禁止.setter
    def 禁止(self, value):
        self.禁用 = value

    @property
    def 鼠标指针(self):
        return self.取鼠标样式()

    @鼠标指针.setter
    def 鼠标指针(self, value):
        '''
        鼠标指针_

        wx.StockCursor(鼠标样式)
        详细文档：https://wxpython.org/Phoenix/docs/html/wx.StockCursor.enumeration.html


        出错返回False,样式:
        0:无描述
        1:标准箭头光标。
        2:指向右侧的标准箭头光标。
        3:靶心光标。
        4:矩形字符光标。
        5:十字光标。
        6:手形光标。
        7:工字梁光标（垂直线）。
        8:表示鼠标左键按下。
        9:放大镜图标。
        10:表示按下中间按钮的鼠标。
        11:不可输入的符号光标。
        12:画笔光标。
        13:铅笔光标。
        14:指向左的光标。
        15:指向右的光标。
        16:箭头和问号。
        17:表示按下了右键的鼠标。
        18:调整大小的光标指向NE-SW。
        19:调整大小的光标指向N-S。
        20:调整大小的光标指向NW-SE。
        21:调整大小的光标指向W-E。
        22:一般大小的游标。
        23:Spraycan游标。
        24:等待光标。
        25:监视光标。
        26:透明光标。
        27:带有标准箭头的等待光标。
        28:无描述。

        '''
        return self.置鼠标样式(value)

    @property
    def 边框(self):
        return self.取边框样式()

    @边框.setter
    @组件_异常检测
    def 边框(self, value):
        pass
        # 等待编写
        return self.SetWindowStyle(value)

    @property
    def 标题(self):
        return self.取标题()

    @标题.setter
    def 标题(self, value):
        return self.置标题(value)

    @property
    def 名称(self):
        return self.取组件名称()

    @名称.setter
    def 名称(self, value):
        return self.置组件名称(value)

    @property
    def 备注(self):
        return self.备注

    @备注.setter
    def 备注(self, value):
        self.备注 = value

    @property
    def 标记(self):
        return self.标记

    @标记.setter
    def 标记(self, value):
        self.标记 = value

    @property
    def 文本颜色(self):
        return self.GetForegroundColour()

    @文本颜色.setter
    def 文本颜色(self, value):
        self.SetForegroundColour(value)


    @property
    def 字体(self):
        return self.GetFont()

    @字体.setter
    def 字体(self, value):
        self.SetFont(value)

    @property
    def 背景颜色(self):
        return self.取背景颜色()

    @背景颜色.setter
    def 背景颜色(self, value):
        return self.置背景颜色(value)

    @property
    def 底色(self):
        return self.取背景颜色()

    @底色.setter
    def 底色(self, value):
        return self.置背景颜色(value)

    @property
    def 窗口样式(self):
        return self.取主题样式()

    @窗口样式.setter
    def 窗口样式(self, value):
        return self.置主题样式(value)

    @property
    def 禁用(self):
        return self.是否禁用()

    @禁用.setter
    def 禁用(self, value):
        "True为禁用组件，False为恢复组件使用"
        return self.Enable(not value)

    @property
    def 提示文本(self):
        return self.GetToolTipText()

    @提示文本.setter
    def 提示文本(self, value):
        return self.置提示文本(value)

    def 置提示文本(self,value):
        return self.SetToolTip(value)

    def 取提示文本(self):
        return self.GetToolTipText()

    def 删除提示文本(self):
        self.UnsetToolTip()
"""
一些ui界面的函数

"""
import datetime
import traceback
import wx


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


@组件_异常检测
def 窗口_取窗口句柄(组件):
    '取wxpython组件的窗口句柄'
    return 组件.GetHandle()


@组件_异常检测
def 窗口_取组件祖组件(组件):
    '取wxpython组件的上上层组件,[当前-父组件-祖组件]'
    return 组件.GetGrandParent()


@组件_异常检测
def 窗口_对齐(组件, 方向=12):
    '默认居中,使组件在父组件内对齐,主窗口则在屏幕中间,1.左上 4/5.顶边 8/9.左边 12/13.居中'
    return 组件.Center(方向)


@组件_异常检测
def 窗口_取桌面相对坐标(组件, x=0, y=0):
    '返回相对于此组件的坐标转换为屏幕坐标,x,y为偏移位置,0为当前'
    return 组件.ClientToScreen(x, y)


@组件_异常检测
def 窗口_关闭(窗口, 关闭=True):
    '用来关闭窗口'
    return 窗口.Close(关闭)


@组件_异常检测
def 窗口_销毁(窗口):
    '备注写的这个方法不会立即销毁窗口,会等事件执行后才安全的销毁'
    return 窗口.Destroy()


@组件_异常检测
def 窗口_销毁所有子窗口(组件):
    '销毁窗口下所有的子窗口,组件'
    return 组件.DestroyChildren()


@组件_异常检测
def 窗口_销毁2(窗口):
    '官方解释：计划在不久的将来销毁该窗口,每当销毁可能发生得太早时（例如，当该窗口或其子级仍在事件队列中等待时），都应使用此方法'
    return 窗口.DestroyLater()


@组件_异常检测
def 窗口_禁用(组件):
    '组件禁用后连同子级组件也无法点击移动'
    return 组件.Disable()


@组件_异常检测
def 窗口_禁用2(组件):
    '启用或禁用用于用户输入的窗口'
    return 组件.Enable(False)


@组件_异常检测
def 窗口_允许拖放文件(组件, 允许=True):
    '允许接收拖放文件'
    return 组件.DragAcceptFiles(允许)


@组件_异常检测
def 窗口_ID匹配组件(父窗口, id):
    '在父窗口下查找返回该ID的组件'
    return 父窗口.FindWindow(id)


@组件_异常检测
def 窗口_ID匹配组件2(父窗口, id):
    '在父窗口下查找返回匹配到的第一个该ID的组件,可使用wx.FindWindowById全程序查找'
    return 父窗口.FindWindowById(id)


@组件_异常检测
def 窗口_取键盘焦点组件(父窗口):
    '在父窗口下查找当前具有键盘焦点的窗口或控件'
    return 父窗口.FindFocus()


@组件_异常检测
def 窗口_标题匹配组件(父窗口, 标题):
    '通过组件标题查找返回匹配到的第一个组件,可使用wx.FindWindowByLabel全程序查找'
    return 父窗口.FindWindowByLabel(标题)


@组件_异常检测
def 窗口_名称匹配组件(父窗口, 组件名):
    '通过组件标题查找返回匹配到的第一个组件,可使用wx.FindWindowByName全程序查找'
    return 父窗口.FindWindowByName(组件名)


@组件_异常检测
def 窗口_自动调整尺寸(组件):
    '调整窗口大小以适合其最佳大小。'
    return 组件.Fit()


@组件_异常检测
def 窗口_自动调整内部尺寸(组件):
    '与相似Fit，但是调整窗户的内部（虚拟）尺寸,主要用于滚动窗口，以在调整大小而不会触发大小事件的情况下重置滚动条，和/或不带内部大小调整器的滚动窗口。如果没有子窗口，此功能同样不会执行任何操作。'
    return 组件.FitInside()


@组件_异常检测
def 窗口_禁止重画(组件):
    '冻结窗口，换句话说，阻止任何更新在屏幕上发生，窗口根本不会重绘'
    return 组件.Freeze()


@组件_异常检测
def 窗口_允许重画(组件):
    '重新启用窗口更新'
    return 组件.Thaw()


@组件_异常检测
def 窗口_取背景颜色(组件):
    '返回窗口的背景色,格式:(240, 240, 240, 255)'
    return 组件.GetBackgroundColour()


@组件_异常检测
def 窗口_取样式(组件):
    '样式：0.默认背景样式值,1.使用由系统或当前主题确定的默认背景,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.无介绍,4.表示未擦除窗口背景，从而使父窗口得以显示'
    return 组件.GetBackgroundStyle()


@组件_异常检测
def 窗口_取最小可接受尺寸(组件):
    '回窗口的最佳可接受最小尺寸,返回格式:(宽度,高度)，高度不包含标题栏高度'
    return 组件.GetBestSize()


@组件_异常检测
def 窗口_取最大可接受尺寸(组件):
    '回窗口的最佳可接受最小尺寸,返回格式:(宽度,高度)，高度不包含标题栏高度'
    return 组件.GetBestVirtualSize()


@组件_异常检测
def 窗口_取边框样式(组件):
    '获取此窗口的标志的边框'
    return 组件.GetBorder()


@组件_异常检测
def 窗口_取额外样式(组件):
    '窗口的额外样式位'
    return 组件.GetExtraStyle()


@组件_异常检测
def 窗口_取字体高度(组件):
    '返回此窗口的字符高度'
    return 组件.GetCharHeight()


@组件_异常检测
def 窗口_取平均字符宽度(组件):
    '返回此窗口的平均字符宽度'
    return 组件.GetCharWidth()


@组件_异常检测
def 窗口_遍历下级组件(组件):
    '遍历组件下的子级组件,返回在WindowList 列表里'
    return 组件.GetChildren()


@组件_异常检测
def 窗口_取字体及颜色(组件):
    '返回字体,背景颜色,前景颜色，#(<wx._core.Font object at 0x000002140997DB88>, wx.Colour(240, 240, 240, 255), wx.Colour(0, 0, 0, 255))'
    结果 = 组件.GetClassDefaultAttributes()
    return 结果.font, 结果.colBg, 结果.colFg


@组件_异常检测
def 窗口_取矩形(组件):
    '返回窗口矩形：(左边,顶边,宽度,高度)'
    return 组件.GetRect()


@组件_异常检测
def 窗口_取矩形2(组件):
    '返回窗口矩形：(0,0,宽度,高度)'
    return 组件.GetClientRect()


@组件_异常检测
def 窗口_取宽高(组件):
    '返回窗口实际宽高：(宽度,高度)'
    return 组件.GetClientSize()


@组件_异常检测
def 窗口_取宽高2(组件):
    '将窗口的最佳大小合并为最小大小，然后返回结果,返回宽高：(宽度,高度)'
    return 组件.GetEffectiveMinSize()


@组件_异常检测
def 窗口_取字体(组件):
    '返回此窗口的字体'
    return 组件.GetFont()


@组件_异常检测
def 窗口_取前景色(组件):
    '返回窗口的前景色'
    return 组件.GetForegroundColour()


@组件_异常检测
def 窗口_取标记ID(组件):
    '返回窗口的标识符'
    return 组件.GetId()


@组件_异常检测
def 窗口_取标题(组件):
    '返回窗口的标题'
    return 组件.GetLabel()


@组件_异常检测
def 窗口_置工作区宽高(组件, 宽度, 高度):
    '设置组件工作区的宽高(不包含边框,标题栏的宽高)'
    return 组件.SetClientSize(宽度, 高度)


@组件_异常检测
def 窗口_取工作区最小宽高(组件):
    '返回窗口的工作区的最小大小，这向sizer布局机制指示这是其工作区的最小所需大小'
    return 组件.GetMinClientSize()


@组件_异常检测
def 窗口_取最小宽高(组件):
    '返回窗口的最小大小，这向sizer布局机制指示这是最小所需大小'
    return 组件.GetMinSize()


@组件_异常检测
def 窗口_取组件名称(组件):
    '返回窗口的名称'
    return 组件.GetName()


@组件_异常检测
def 窗口_取下一窗口(组件):
    '返回此窗口之后的下一个窗口(同一级窗口里)'
    return 组件.GetNextSibling()


@组件_异常检测
def 窗口_取上一窗口(组件):
    '返回父级的子级中前一个的前一个窗口'
    return 组件.GetPrevSibling()


@组件_异常检测
def 窗口_取父级窗口(组件):
    '返回窗口的父级，或者返回没有父级的窗口None'
    return 组件.GetParent()


@组件_异常检测
def 窗口_弹出菜单(组件, 菜单, 左边, 顶边):
    '此函数在此窗口中的给定位置显示一个弹出菜单，并返回所选的ID'
    return 组件.GetPopupMenuSelectionFromUser(菜单, 左边, 顶边)


@组件_异常检测
def 窗口_取左边顶边(组件):
    '这将获得相对于子窗口的父窗口或相对于顶级窗口的显示原点的窗口位置（以像素为单位）,格式：(左边,顶边)'
    return 组件.DirDialog()


@组件_异常检测
def 窗口_取窗口相对屏幕坐标(组件):
    '返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边)'
    return 组件.GetScreenPosition()


@组件_异常检测
def 窗口_取窗口相对屏幕矩形(组件):
    '返回窗口在屏幕坐标中的位置，无论该窗口是子窗口还是顶级窗口,格式:(相对于屏幕的左边,相对于屏幕的顶边,组件宽度,组件高度)'
    return 组件.GetScreenRect()


@组件_异常检测
def 窗口_取内置滚动条位置(组件, 方向):
    '返回内置滚动条的位置,方向：4.横向滚动条 8.纵向滚动条'
    return 组件.GetScrollPos(方向)


@组件_异常检测
def 窗口_取内置滚动条范围(组件, 方向):
    '返回内置滚动条范围,方向：4.横向滚动条 8.纵向滚动条'
    return 组件.GetScrollRange(方向)


@组件_异常检测
def 窗口_取内置滚动条缩略图大小(组件, 方向):
    '返回内置滚动条的缩略图大小,方向：4.横向滚动条 8.纵向滚动条'
    return 组件.GetScrollThumb(方向)


@组件_异常检测
def 窗口_置滚动条位置(组件, 方向, 位置, 重绘):
    '设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)'
    return 组件.SetScrollPos(方向, 位置, 重绘)


@组件_异常检测
def 窗口_置滚动条属性(组件, 方向, 位置, 可见大小, 最大位置, 重绘):
    '''
    设置滚动条位置,方向可选4或8,重绘True或False(设置内置滚动条之一的位置)
    假设您希望使用相同的字体显示50行文本。窗口的大小设置为一次只能看到16行。您将使用：
    self.SetScrollbar(wx.VERTICAL, 0, 16, 50)
    '''
    return 组件.SetScrollbar(方向, 位置, 可见大小, 最大位置, 重绘)


@组件_异常检测
def 窗口_取完整窗口宽高(组件):
    '返回整个窗口的大小（以像素为单位），包括标题栏，边框，滚动条等。如果此窗口是顶级窗口，并且当前已最小化，则返回的大小是还原的窗口大小，而不是窗口图标的大小'
    return 组件.GetSize()


@组件_异常检测
def 窗口_是否使用系统主题设置背景(组件):
    '窗口是否使用系统主题绘制其背景'
    return 组件.GetThemeEnabled()


@组件_异常检测
def 窗口_取顶级窗口(组件):
    '返回此窗口（顶级窗口）的第一个祖先'
    return 组件.GetTopLevelParent()


@组件_异常检测
def 窗口_取虚拟宽高(组件):
    '出错返回False,这将获取窗口的虚拟大小,它返回窗口的客户端大小，但是在调用SetVirtualSize 它之后，将返回使用该方法设置的大小'
    return 组件.GetVirtualSize()


@组件_异常检测
def 窗口_是否有焦点(组件):
    '窗口（或在复合控件的情况下，其主子窗口）是否具有焦点'
    return 组件.HasFocus()


@组件_异常检测
def 窗口_是否有滚动条(组件, 方向):
    '返回此窗口当前是否具有该方向的滚动条,方向：4.横向滚动条 8.纵向滚动条'
    return 组件.HasScrollbar(方向)


@组件_异常检测
def 窗口_是否透明(组件):
    '返回此窗口背景是否透明（例如，对于 wx.StaticText），并应显示父窗口背景'
    return 组件.HasTransparentBackground()


@组件_异常检测
def 窗口_隐藏(组件):
    '此功能可隐藏一个窗口'
    return 组件.Hide()


@组件_异常检测
def 窗口_隐藏带特效(组件, 效果, 效果时长):
    '''
    此功能可隐藏一个窗口并使用特殊的视觉效果
    效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
    效果时长：单位毫秒
    '''
    return 组件.HideWithEffect(效果, 效果时长)


@组件_异常检测
def 窗口_显示带特效(组件, 效果, 效果时长):
    '''
    此功能可隐藏一个窗口并使用特殊的视觉效果
    效果：0.无效果，1.向左滚动窗口，2.向右滚动窗口，3.将窗口滚动到顶部，4.将窗口滚动到底部，5.向左滑动窗口，6.向右滑动窗口，7.将窗口滑动到顶部，8.将窗口滑动到底部，9.淡入或淡出效果，10.扩大或崩溃的作用
    效果时长：单位毫秒
    '''
    return 组件.ShowWithEffect(效果, 效果时长)


@组件_异常检测
def 窗口_是否继承父级背景色(组件):
    '如果此窗口从其父级继承背景色，则返回True'
    return 组件.InheritsBackgroundColour()


@组件_异常检测
def 窗口_是否继承父级前景色(组件):
    '如果此窗口从其父级继承前景色，则返回True'
    return 组件.InheritsForegroundColour()


@组件_异常检测
def 窗口_重置缓存最佳大小(组件):
    '重置缓存的最佳大小值，以便下次需要时重新计算'
    return 组件.InvalidateBestSize()


@组件_异常检测
def 窗口_是否正在销毁(组件):
    '此窗口是否正在销毁中'
    return 组件.IsBeingDeleted()


@组件_异常检测
def 窗口_是否为下级窗口(组件, 对比组件):
    '检查指定的窗口是否是该窗口的后代,窗口是否为该窗口的后代（例如，子代或孙代或子孙或……）返回True'
    return 组件.IsDescendant(对比组件)


@组件_异常检测
def 窗口_是否禁用(组件):
    '是否启用了窗口，即是否接受用户输入'
    return 组件.IsEnabled()


@组件_异常检测
def 窗口_是否可获取焦点(组件):
    '判断窗口是否可以获取焦点'
    return 组件.IsFocusable()


@组件_异常检测
def 窗口_是否禁止重画(组件):
    '判断窗口是否可已经禁止重画'
    return 组件.IsFrozen()


@组件_异常检测
def 窗口_是否始终显示滚动条(组件, 方向):
    '判断滚动条是否始终显示,方向：4.横向滚动条 8.纵向滚动条'
    return 组件.IsScrollbarAlwaysShown(方向)


@组件_异常检测
def 窗口_是否隐藏(组件):
    '判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
    return 组件.IsShown()


@组件_异常检测
def 窗口_是否显示在屏幕上(组件):
    '判断是否调用命令隐藏了窗口,最小化,遮挡,不算隐藏'
    return 组件.IsShownOnScreen()


@组件_异常检测
def 窗口_是否启用(组件):
    '是否从本质上启用了此窗口，False否则返回'
    return 组件.IsThisEnabled()


@组件_异常检测
def 窗口_是否为顶级窗口(组件):
    '窗口是否为顶级窗口'
    return 组件.IsTopLevel()


@组件_异常检测
def 窗口_向下滚动(组件):
    '与ScrollLines （1）相同，返回True是否滚动窗口，False如果窗口已经在底部，则什么也不做'
    return 组件.LineDown()


@组件_异常检测
def 窗口_向上滚动(组件):
    '与ScrollLines （-1）相同,返回True是否滚动窗口，False如果窗口已经在顶部，则什么也不做'
    return 组件.LineUp()


@组件_异常检测
def 窗口_滚动_页(组件, 滚动页数=1):
    '滚动页数:向上滚动1次为-1,向下为1'
    return 组件.ScrollPages(滚动页数)


@组件_异常检测
def 窗口_滚动_行(组件, 滚动行数=1):
    '滚动行数:向上滚动1次为-1,向下为1'
    return 组件.ScrollLines(滚动行数)


@组件_异常检测
def 窗口_移动左边顶边(组件, 左边, 顶边):
    '调整移动窗口的左边跟顶边位置'
    return 组件.Move(左边, 顶边)


@组件_异常检测
def 窗口_移动左边顶边2(组件, 左边, 顶边):
    '调整移动窗口的左边跟顶边位置'
    return 组件.SetPosition((左边, 顶边))


@组件_异常检测
def 窗口_移动(组件, 左边=-1, 顶边=-1, 宽度=-1, 高度=-1):
    '调整移动窗口的左边跟顶边位置并重新设置宽度跟高度,不想调整的填-1'
    return 组件.SetSize(左边, 顶边, 宽度, 高度)


@组件_异常检测
def 窗口_设置切换顺序_上(组件, 上一个组件):
    '调整TAB切换的顺序,当上一个组件按TAB后焦点就会到当前组件上'
    return 组件.MoveAfterInTabOrder(上一个组件)


@组件_异常检测
def 窗口_设置切换顺序_下(组件, 下一个组件):
    '调整TAB切换的顺序,当前组件按TAB后焦点会切换到下一个组件'
    return 组件.MoveBeforeInTabOrder(下一个组件)


@组件_异常检测
def 窗口_生成组件ID(组件):
    '创建一个新的ID或当前未使用的ID范围,格式:-31987'
    return 组件.NewControlId()


@组件_异常检测
def 窗口_重绘指定区域(组件, 矩形=(0, 0, 0, 0), 擦除背景=True):
    '重绘指定矩形的内容：仅对其内部的区域进行重绘'
    return 组件.RefreshRect(矩形, 擦除背景)


@组件_异常检测
def 窗口_修改父级窗口(组件, 新父级组件):
    '即该窗口将从其当前父窗口中移除加入到新的父级窗口下'
    return 组件.Reparent(新父级组件)


@组件_异常检测
def 窗口_桌面坐标转窗口内坐标(组件, x, y):
    '从屏幕转换为客户端窗口内工作区坐标,'
    return 组件.ScreenToClient(x, y)


@组件_异常检测
def 窗口_到最顶层(组件):
    return 组件.Raise()


@组件_异常检测
def 窗口_到最底层(组件):
    return 组件.Lower()


@组件_异常检测
def 窗口_是否已设置背景色(组件):
    return 组件.UseBackgroundColour()


@组件_异常检测
def 窗口_是否已设置前景色(组件):
    return 组件.UseForegroundColour()


@组件_异常检测
def 窗口_置背景颜色(组件, 颜色):
    return 组件.SetBackgroundColour(颜色)


@组件_异常检测
def 窗口_单独置背景颜色(组件, 颜色):
    '设置窗口的背景色，但防止其被该窗口的子级继承'
    return 组件.SetOwnBackgroundColour(颜色)


@组件_异常检测
def 窗口_置前景颜色(组件, 颜色):
    return 组件.SetForegroundColour(颜色)


@组件_异常检测
def 窗口_单独置前景颜色(组件, 颜色):
    '设置窗口的前景色，但防止其被该窗口的子代继承'
    return 组件.SetOwnForegroundColour(颜色)


@组件_异常检测
def 窗口_置标识ID(组件, ID):
    return 组件.SetId(ID)


@组件_异常检测
def 窗口_置宽高(组件, 宽度, 高度):
    return 组件.SetInitialSize((宽度, 高度))


@组件_异常检测
def 窗口_置最大宽高(组件, 宽度, 高度):
    '设置整个窗口最大尺寸范围'
    return 组件.SetMaxSize((宽度, 高度))


@组件_异常检测
def 窗口_置最小宽高(组件, 宽度, 高度):
    '设置整个窗口最大尺寸范围'
    return 组件.SetMinSize((宽度, 高度))


@组件_异常检测
def 窗口_置工作区最大宽高(组件, 宽度, 高度):
    '设置窗口的最大客户端大小(不包含标题栏菜单栏状态栏的尺寸)，以向sizer布局机制指示这是其客户端区域的最大可能大小'
    return 组件.SetMaxClientSize((宽度, 高度))


@组件_异常检测
def 窗口_置工作区最小宽高(组件, 宽度, 高度):
    '设置窗口的最大客户端大小(不包含标题栏菜单栏状态栏的尺寸)，以向sizer布局机制指示这是其客户端区域的最大可能大小'
    return 组件.SetMinClientSize((宽度, 高度))


@组件_异常检测
def 窗口_置虚拟宽高(组件, 宽度, 高度):
    '设置窗口的虚拟大小（以像素为单位）'
    return 组件.SetVirtualSize((宽度, 高度))


@组件_异常检测
def 窗口_置标题(组件, 标题):
    return 组件.SetLabel(标题)


@组件_异常检测
def 窗口_置名称(组件, 名称):
    return 组件.SetName(名称)


@组件_异常检测
def 窗口_是否允许透明(组件):
    return 组件.CanSetTransparent()


@组件_异常检测
def 窗口_置透明度(组件, 透明度):
    '设置窗口与透明度,范围0-255(0.完全透明,255完全不透明)'
    return 组件.SetTransparent(透明度)


@组件_异常检测
def 窗口_置主题样式(组件, 样式):
    '窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
    return 组件.SetBackgroundStyle(样式)


@组件_异常检测
def 窗口_置窗口样式(组件, 样式):
    '样式:0.无边框,536870912.右上角无按钮,更多样式百度'
    return 组件.SetWindowStyleFlag(样式)


@组件_异常检测
def 窗口_刷新重绘(组件, 删除背景=False):
    '导致GTK1重新绘制此窗口及其所有子级（除非未实现此子级）'
    return 组件.Refresh(删除背景)


@组件_异常检测
def 窗口_刷新重绘2(组件):
    '调用此方法将立即重新绘制窗口的无效区域及其所有子级的对象（通常仅在控制流返回事件循环时才发生）'
    return 组件.Update()


@组件_异常检测
def 窗口_显示或隐藏(组件, 是否显示=True):
    '显示或隐藏窗口'
    return 组件.Show(是否显示)


@组件_异常检测
def 窗口_移动鼠标(组件, x, y):
    '将指针移动到窗口上的指定位置'
    return 组件.WarpPointer(x, y)


@组件_异常检测
def 窗口_置鼠标光标样式(组件, 样式):
    '''样式:
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
    return 组件.SetCursor(wx.Cursor(样式))


@组件_异常检测
def 窗口_设置字体(组件, 字体名, 大小, 粗细, 下划线):
    '窗口样式:0.默认(可擦除背景),1.跟随系统主题,2.指示仅在用户定义的EVT_PAINT处理程序中擦除背景,3.表示未擦除窗口背景，从而使父窗口得以显示,4.无描述。'
    return 组件.SetFont(wx.Font(大小, wx.DEFAULT, wx.NORMAL, 粗细, 下划线, 字体名))


@组件_异常检测
def 程序_取指定坐标处组件(x, y):
    '传入桌面上坐标'
    return wx.FindWindowAtPoint((x, y))


@组件_异常检测
def 程序_取鼠标处组件跟坐标():
    '取当前鼠标下面的组件及坐标,返回格式:(组件,(x,y)),返回的坐标是相对于桌面的坐标'
    return wx.FindWindowAtPointer()


@组件_异常检测
def 程序_取屏幕工作区矩形():
    '取屏幕工作区矩形(不包含任务栏宽高),格式：(0,0,1920,1040) 任务栏占了40'
    return wx.GetClientDisplayRect()


@组件_异常检测
def 程序_取屏幕分辨率():
    '返回格式:(1920,1080)'
    return wx.GetDisplaySize()


@组件_异常检测
def 程序_取屏幕尺寸():
    '返回以毫米为单位的显示尺寸，格式:(508,286)'
    return wx.GetDisplaySizeMM()


@组件_异常检测
def 程序_恢复默认鼠标光标():
    '对于应用程序中的所有窗口，将光标更改回原始光标'
    return wx.EndBusyCursor()


@组件_异常检测
def 程序_重置所有鼠标光标(光标类型):
    '''将光标更改为应用程序中所有窗口的给定光标
    光标类型:
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
    return wx.BeginBusyCursor(wx.Cursor(光标类型))


@组件_异常检测
def 程序_关闭2():
    "立即结束程序"
    wx.Abort()


@组件_异常检测
def 程序_关闭():
    "立即结束程序,会卡顿下"
    wx.Exit()


@组件_异常检测
def 程序_系统错误代码转提示文本(code):
    "返回与给定系统错误代码对应的错误消息,示例：code=3 返回:系统找不到指定的路径。"
    return wx.SysErrorMsgStr(3)


@组件_异常检测
def 程序_电脑关机():
    "立即结束程序,会卡顿下"
    wx.Shutdown(2)


@组件_异常检测
def 程序_电脑重启():
    "立即结束程序,会卡顿下"
    wx.Shutdown(4)


@组件_异常检测
def 程序_延时_微秒(时间):
    "延时单位(微秒)1秒=1000000微秒"
    wx.MicroSleep(时间)


@组件_异常检测
def 程序_延时_毫秒(时间):
    "延时单位(毫秒)1秒=1000毫秒"
    wx.MilliSleep(时间)


@组件_异常检测
def 程序_延时_秒(时间):
    wx.Sleep(时间)


@组件_异常检测
def 程序_取本地英文时间():
    "返回时间示例：Sun Aug 16 15:57:41 2020"
    return wx.Now()


@组件_异常检测
def 程序_取程序对象():
    "返回当前应用程序对象"
    return wx.GetApp()


@组件_异常检测
def 程序_取程序顶级窗口列表():
    "返回应用程序顶级窗口的类似列表的对象(返回顶级窗口的对象列表)"
    return wx.GetTopLevelWindows()


@组件_异常检测
def 程序_取计算机名():
    "返回当前应用程序对象"
    return wx.GetHostName()


@组件_异常检测
def 程序_取系统版本信息():
    "返回示例: Windows 10 (build 18363)，64位版"
    return wx.GetOsDescription()


@组件_异常检测
def 程序_取系统用户名():
    "返回示例: Administrator"
    return wx.GetUserName()


@组件_异常检测
def 程序_系统是否64位():
    "返回True程序运行所在的操作系统是否为64位。"
    return wx.IsPlatform64Bit()


@组件_异常检测
def 程序_打开指定网址或目录(地址):
    "可以打开电脑目录或使用默认浏览器打开指定网址"
    return wx.LaunchDefaultBrowser(地址)


@组件_异常检测
def 程序_打开指定网址(url):
    import webbrowser
    return webbrowser.open(url)


@组件_异常检测
def 程序_取鼠标坐标():
    "返回鼠标坐标(x,y)"
    return wx.GetMouseState().GetPosition()


@组件_异常检测
def 程序_鼠标侧键1是否按下():
    "返回当前应用程序对象,判断鼠标侧边附加的按键是否按下"
    return wx.GetMouseState().Aux1IsDown()


@组件_异常检测
def 程序_鼠标侧键2是否按下():
    "返回True或False,判断鼠标侧边附加的按键是否按下"
    return wx.GetMouseState().Aux2IsDown()


@组件_异常检测
def 程序_鼠标左键是否按下():
    "返回True或False,判断鼠标左键是否按下"
    return wx.GetMouseState().LeftIsDown()


@组件_异常检测
def 程序_鼠标中键是否按下():
    "返回True或False,判断鼠标中键是否按下"
    return wx.GetMouseState().MiddleIsDown()


@组件_异常检测
def 程序_鼠标右键是否按下():
    "返回True或False,判断鼠标右键是否按下"
    return wx.GetMouseState().RightIsDown()


@组件_异常检测
def 程序_取当前进程ID():
    "返回当前程序进程PID"
    return wx.GetProcessId()


@组件_异常检测
def 程序_系统环境是否支持中文():
    "返回True或False    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Language.enumeration.html#wx-language"
    return wx.GetLocale().IsAvailable(wx.LANGUAGE_CHINESE)


@组件_异常检测
def 程序_取环境语言名称():
    "返回示例: Chinese (Simplified)    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Locale.html#wx-locale"
    return wx.GetLocale().GetLocale()


@组件_异常检测
def 程序_取环境语言缩写():
    "返回实力: zh_CN    更多环境语言方法参考:https://wxpython.org/Phoenix/docs/html/wx.Locale.html#wx-locale"
    return wx.GetLocale().GetName()


@组件_异常检测
def 程序_系统是否已激活():
    "返回True或False,不太确定是不是这个命令,获取更多电脑描述信息参考:https://wxpython.org/Phoenix/docs/html/wx.VersionInfo.html#wx-versioninfo"
    return wx.GetLibraryVersionInfo().HasCopyright()


@组件_异常检测
def 程序_执行Dos(命令):
    '运行cmd内的命令,只返回True跟False'
    return wx.Shell(命令)


@组件_异常检测
def 组件_信息框(提示="", 标题="提示", 类型=0, 父窗口=None):
    """
    类型:
    0.无图标信息框
    1.带取消键普通信息框
    2.带是/否键普通信息框
    3.带帮助键普通信息框
    4.带红色错误图标信息框
    5.带黄色感叹标题信息框
    6.带盾牌(类似权限验证)图标信息框

    返回值:2.是   4.确定   8.否   16.取消/关闭   4096.帮助
    """
    字典 = {0: 262144, 1: 16, 2: 10, 3: 4096, 4: 512, 5: 256, 6: 524288}
    return wx.MessageBox(提示, 标题, 字典[类型], 父窗口)


@组件_异常检测
def 信息框(提示信息="", 标题="提示", 类型=0, 父窗口=None):
    """
    类型:
    0.无图标信息框
    1.带取消键普通信息框
    2.带是/否键普通信息框
    3.带帮助键普通信息框
    4.带红色错误图标信息框
    5.带黄色感叹标题信息框
    6.带盾牌(类似权限验证)图标信息框

    返回值:2.是   4.确定   8.否   16.取消/关闭   4096.帮助
    """
    字典 = {0: 262144, 1: 16, 2: 10, 3: 4096, 4: 512, 5: 256, 6: 524288}
    return wx.MessageBox(提示信息, 标题, 字典[类型], 父窗口)


@组件_异常检测
def 组件_提示信息框(内容):
    "弹出一个带蓝色反向感叹号图标的信息框"
    return wx.LogMessage(内容)


@组件_异常检测
def 组件_警告信息框(内容):
    "弹出一个带黄色三角形感叹号图标的信息框"
    return wx.LogWarning(内容)


@组件_异常检测
def 组件_报错信息框(内容):
    "弹出一个带红叉图标的信息框"
    return wx.LogError(内容)


@组件_异常检测
def 组件_文件选择器(标题="请选择文件", 初始路径="", 默认文件名="", 过滤器="所有文件|*.*", 父窗口=None):
    "选择文件后返回完整文件路径,没选择返回空文本,可添加参数,flags(标识),parent(父窗口),x,y"
    return wx.FileSelector(标题, 初始路径, 默认文件名, wildcard=过滤器)


@组件_异常检测
def 组件_保存文件对话框(提示="", 后缀="*", 默认文件名="", 父窗口=None):
    "设置文件后返回完整文件路径,没选择返回空文本"
    return wx.SaveFileSelector(提示, 后缀, 默认文件名, 父窗口)


@组件_异常检测
def 组件_目录选择器(提示="", 初始路径="", 父窗口=None):
    "选择目录后返回完整路径,没选择返回空文本,返回示例:c:\\user"
    return wx.DirSelector(message=提示, default_path=初始路径, parent=父窗口)


@组件_异常检测
def 组件_颜色选择器(初始颜色=None, 标题="请选择颜色", 父窗口=None):
    "选择颜色后返回颜色值(0,0,0,255),可添加参数,flags(标识),parent(父窗口),x,y"
    return wx.GetColourFromUser(父窗口, 初始颜色, 标题)


@组件_异常检测
def 组件_字体选择器(父窗口, 默认字体=None, 标题="请选择字体"):
    "选择字体后返回字体类型"
    return wx.GetFontFromUser(父窗口, 默认字体 if 默认字体 else 父窗口.GetFont(), 标题)


@组件_异常检测
def 组件_数值对话框(标题="请设置数值", 提示="", 参数提示="", 默认值=1, 最小值=1, 最大值=100, 父窗口=None):
    "不能在线程里调用,弹出一个设置数值的对话框"
    return wx.GetNumberFromUser(提示, 参数提示, 标题, 默认值, 最小值, 最大值, 父窗口)


@组件_异常检测
def 组件_密码对话框(提示="", 标题="请输入密码", 默认文本="", 父窗口=None):
    "弹出一个文本对话框,输入的内容会被替换成圆点,适合密码等输入使用,确认后返回输入的内容,取消返回空文本"
    return wx.GetPasswordFromUser(message=提示, caption=标题, default_value=默认文本, parent=父窗口)


@组件_异常检测
def 组件_单选列表对话框(提示="", 标题="请选择", 选择项=['未设置'], 初始选中=0, 父窗口=None):
    "弹出一个单选列表对话框,选择后返回选中的文本内容,取消返回空,选择项必须是文本型列表,初始选中从0开始"
    return wx.GetSingleChoice(message=提示, caption=标题, choices=选择项, initialSelection=初始选中, parent=父窗口)


@组件_异常检测
def 组件_普通对话框(提示="", 标题="请输入", 默认文本='', 父窗口=None):
    "弹出一个对话框输入文本,确认后返回输入的文本,取消返回空"
    return wx.GetTextFromUser(message=提示, caption=标题, default_value=默认文本, parent=父窗口)


@组件_异常检测
def 组件_气泡提示框(父窗口, 提示="", 标题="", 超时时间=3000, x=0, y=0):
    "弹出一个气泡提示框,默认在组件中间,可通过设置x,y调整"
    气泡 = wx.adv.RichToolTip(标题, 提示)
    气泡.SetTimeout(超时时间)
    气泡.ShowFor(父窗口, (0, 0, x * 2, y * 2))


@组件_异常检测
def 组件_系统弹窗(父窗口=None, 提示="", 标题=""):
    "电脑右下角弹出一个提示框,可以绑定提示框点击事件,详细操作：https://wxpython.org/Phoenix/docs/html/wx.adv.NotificationMessage.html#wx.adv.NotificationMessage.Show"
    提示框 = wx.adv.NotificationMessage(标题, 提示, 父窗口)
    提示框.Show()

"""
********
组件的事件
********


- 事件.按钮_被点击 = wx.EVT_BUTTON
- 事件.复选框_被点击 = wx.EVT_CHECKBOX
- 事件.选择_被点击 = wx.EVT_CHOICE
- 事件.列表框_被点击 = wx.EVT_LISTBOX
- 事件.列表框_被双击 = wx.EVT_LISTBOX_DCLICK
- 事件.菜单_被点击 = wx.EVT_MENU
- 事件.菜单范围_被点击 = wx.EVT_MENU_RANGE
- 事件.滑块_被点击 = wx.EVT_SLIDER
- 事件.无线电箱_被点击 = wx.EVT_RADIOBOX
- 事件.单选按钮_被点击 = wx.EVT_RADIOBUTTON

- 事件.鼠标左键按下 = wx.EVT_LEFT_DOWN
- 事件.鼠标左键松开 = wx.EVT_LEFT_UP
- 事件.鼠标左键双击 = wx.EVT_LEFT_DCLICK
- 事件.鼠标右键按下 = wx.EVT_RIGHT_DOWN
- 事件.鼠标右键松开 = wx.EVT_RIGHT_UP
- 事件.鼠标右键双击 = wx.EVT_RIGHT_DCLICK
- 事件.鼠标中键按下 = wx.EVT_MIDDLE_DOWN
- 事件.鼠标中键松开 = wx.EVT_MIDDLE_UP
- 事件.鼠标中键双击 = wx.EVT_MIDDLE_DCLICK
- 事件.鼠标中键滚动 = wx.EVT_MOUSEWHEEL
- 事件.鼠标移动 = wx.EVT_MOTION
- 事件.鼠标进入 = wx.EVT_ENTER_WINDOW
- 事件.鼠标离开 = wx.EVT_LEAVE_WINDOW
- 事件.点击某键 = wx.EVT_CHAR_HOOK
- 事件.按下某键 = wx.EVT_KEY_DOWN
- 事件.松开某键 = wx.EVT_KEY_UP
- 事件.获得焦点 = wx.EVT_SET_FOCUS
- 事件.失去焦点 = wx.EVT_KILL_FOCUS
- 事件.按钮被单击 = wx.EVT_BUTTON
- 事件.创建完毕 = wx.EVT_WINDOW_CREATE
- 事件.尺寸被改变 = wx.EVT_SIZE
- 事件.位置被移动 = wx.EVT_MOVE
- 事件.将被关闭 = wx.EVT_CLOSE
- 事件.内容被改变 = wx.EVT_TEXT
- 事件.按下Enter键 = wx.EVT_TEXT_ENTER
- 事件.达到限制长度 = wx.EVT_TEXT_MAXLEN
- 事件.状态被改变 = wx.EVT_RADIOBUTTON
- 事件.狀态被改变 = wx.EVT_CHECKBOX
- 事件.选中列表项 = wx.EVT_COMBOBOX
- 事件.文本发生变化 = wx.EVT_TEXT
- 事件.弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
- 事件.收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
- 事件.被拖动 = wx.EVT_SLIDER
- 事件.向小拖动 = wx.EVT_SCROLL_PAGEUP
- 事件.向大拖动 = wx.EVT_SCROLL_PAGEDOWN
- 事件.正在拖动 = wx.EVT_SCROLL_THUMBTRACK
- 事件.停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
- 事件.数值被调整 = wx.EVT_SPINCTRL
- 事件.周期事件 = wx.EVT_TIMER
- 事件.表项被单击 = wx.EVT_CHECKLISTBOX
- 事件.表项被双击 = wx.EVT_LISTBOX_DCLICK
- 事件.链接被单击 = wx.adv.EVT_HYPERLINK
- 事件.双击某一天 = wx.adv.EVT_CALENDAR
- 事件.日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
- 事件.年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
- 事件.内容被更改 = wx.adv.EVT_DATE_CHANGED
- 事件.内容被修改 = wx.adv.EVT_TIME_CHANGED
- 事件.左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
- 事件.右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
- 事件.开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
- 事件.编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
- 事件.表项被删除 = wx.EVT_LIST_DELETE_ITEM
- 事件.表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
- 事件.选中表项 = wx.EVT_LIST_ITEM_SELECTED
- 事件.取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
- 事件.表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
- 事件.中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
- 事件.右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
- 事件.表项按下某键 = wx.EVT_LIST_KEY_DOWN
- 事件.插入新表项 = wx.EVT_LIST_INSERT_ITEM
- 事件.左键单击某列 = wx.EVT_LIST_COL_CLICK
- 事件.右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
- 事件.开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
- 事件.分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
- 事件.列宽被修改 = wx.EVT_LIST_COL_END_DRAG
- 事件.表项被选中 = wx.EVT_LIST_ITEM_CHECKED
- 事件.表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
- 事件.滚动事件 = wx.EVT_SCROLL
- 事件.滚到最小位置 = wx.EVT_SCROLL_TOP
- 事件.滚到最大位置 = wx.EVT_SCROLL_BOTTOM
- 事件.向小滚动 = wx.EVT_SCROLL_PAGEUP
- 事件.向大滚动 = wx.EVT_SCROLL_PAGEDOWN
- 事件.停止滚动 = wx.EVT_SCROLL_CHANGED
- 事件.选项被单击 = wx.EVT_RADIOBOX
- 事件.颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
- 事件.点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
- 事件.取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
- 事件.点击链接 = wx.EVT_TEXT_URL
- 事件.响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
- 事件.响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
- 事件.响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
- 事件.数字被调整 = floatspin.EVT_FLOATSPIN

"""
import wx.lib.agw.floatspin as floatspin
import wx.lib.agw.hyperlink as hyperlink

import wx
import wx.adv
from wx import *


class 事件:
    被单击 = wx.EVT_LEFT_DOWN

    按钮被点击 = wx.EVT_BUTTON
    复选框被点击 = wx.EVT_CHECKBOX
    选择被点击 = wx.EVT_CHOICE
    列表框被点击 = wx.EVT_LISTBOX
    列表框被双击 = wx.EVT_LISTBOX_DCLICK
    菜单被点击 = wx.EVT_MENU
    菜单范围被点击 = wx.EVT_MENU_RANGE
    滑块被点击 = wx.EVT_SLIDER
    单选框被点击 = wx.EVT_RADIOBOX
    单选框按钮被点击 = wx.EVT_RADIOBUTTON

    鼠标左键被按下 = wx.EVT_LEFT_DOWN
    鼠标左键被放开 = wx.EVT_LEFT_UP
    鼠标左键被双击 = wx.EVT_LEFT_DCLICK
    被双击 = wx.EVT_LEFT_DCLICK
    鼠标右键被按下 = wx.EVT_RIGHT_DOWN
    鼠标右键被放开 = wx.EVT_RIGHT_UP
    鼠标右键被双击 = wx.EVT_RIGHT_DCLICK
    鼠标中键被按下 = wx.EVT_MIDDLE_DOWN
    鼠标中键被松开 = wx.EVT_MIDDLE_UP
    鼠标中键被双击 = wx.EVT_MIDDLE_DCLICK
    鼠标中键被滚动 = wx.EVT_MOUSEWHEEL
    滚轮被滚动 = wx.EVT_MOUSEWHEEL
    鼠标位置被移动 = wx.EVT_MOTION
    鼠标进入 = wx.EVT_ENTER_WINDOW
    鼠标离开 = wx.EVT_LEAVE_WINDOW
    点击某键 = wx.EVT_CHAR_HOOK
    按下某键 = wx.EVT_KEY_DOWN
    字符输入 = wx.EVT_KEY_DOWN  # 可能有误
    放开某键 = wx.EVT_KEY_UP
    获得焦点 = wx.EVT_SET_FOCUS
    失去焦点 = wx.EVT_KILL_FOCUS
    按钮被单击 = wx.EVT_BUTTON
    创建完毕 = wx.EVT_WINDOW_CREATE
    尺寸被改变 = wx.EVT_SIZE
    位置被改变 = wx.EVT_MOVE
    可否被关闭 = wx.EVT_CLOSE
    窗口可否被关闭 = wx.EVT_CLOSE
    将被销毁 = wx.EVT_CLOSE
    被激活 = wx.EVT_ACTIVATE
    被取消激活 = wx.EVT_ACTIVATE
    空闲 = wx.IdleEvent  # 不知道
    首次激活 = wx.EVT_ACTIVATE
    托盘事件 = wx.EVT_MENU
    被显示 = wx.EVT_SHOW
    被隐藏 = wx.EVT_SHOW  # 不知道

    内容被改变 = wx.EVT_TEXT
    按下Enter键 = wx.EVT_TEXT_ENTER
    达到限制长度 = wx.EVT_TEXT_MAXLEN
    状态被改变 = wx.EVT_RADIOBUTTON
    狀态被改变 = wx.EVT_CHECKBOX
    选中列表项 = wx.EVT_COMBOBOX
    列表项被选择 = wx.EVT_COMBOBOX
    编辑内容被改变 = wx.EVT_TEXT
    编辑框按下回车 = wx.EVT_TEXT_ENTER
    将弹出列表 = wx.EVT_COMBOBOX_DROPDOWN
    列表被关闭 = wx.EVT_COMBOBOX_CLOSEUP
    双击选择 = wx.EVT_RIGHT_DCLICK
    文本发生变化 = wx.EVT_TEXT
    弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
    收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
    被拖动 = wx.EVT_SLIDER
    向小拖动 = wx.EVT_SCROLL_PAGEUP
    向大拖动 = wx.EVT_SCROLL_PAGEDOWN
    正在拖动 = wx.EVT_SCROLL_THUMBTRACK
    停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
    数值被调整 = wx.EVT_SPINCTRL
    周期事件 = wx.EVT_TIMER
    表项被单击 = wx.EVT_CHECKLISTBOX
    表项被双击 = wx.EVT_LISTBOX_DCLICK
    链接被单击 = wx.adv.EVT_HYPERLINK
    双击某一天 = wx.adv.EVT_CALENDAR
    日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
    年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
    内容被更改 = wx.adv.EVT_DATE_CHANGED
    内容被修改 = wx.adv.EVT_TIME_CHANGED
    左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
    右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
    开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
    编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
    表项被删除 = wx.EVT_LIST_DELETE_ITEM
    表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
    # 超级列表框
    当前表项被改变 = wx.EVT_LIST_ITEM_SELECTED
    表项被激活 = wx.EVT_LIST_ITEM_ACTIVATED
    表头被单击 = wx.EVT_LIST_COL_CLICK
    表项跟踪 = wx.EVT_LIST_COL_CLICK
    左键单击表项 = wx.EVT_LIST_COL_CLICK
    右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
    开始编辑 = wx.EVT_LIST_BEGIN_LABEL_EDIT
    结束编辑 = wx.EVT_LIST_END_LABEL_EDIT
    检查框状态被改变 = wx.EVT_LIST_COL_CLICK
    # todo 有很多都不知道是啥 待补充
    选中表项 = wx.EVT_LIST_ITEM_SELECTED
    取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
    表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
    中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
    右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
    表项按下某键 = wx.EVT_LIST_KEY_DOWN
    插入新表项 = wx.EVT_LIST_INSERT_ITEM
    左键单击某列 = wx.EVT_LIST_COL_CLICK
    右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
    开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
    分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
    列宽被修改 = wx.EVT_LIST_COL_END_DRAG
    表项被选中 = wx.EVT_LIST_ITEM_CHECKED
    表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
    滚动事件 = wx.EVT_SCROLL
    滚到最小位置 = wx.EVT_SCROLL_TOP
    滚到最大位置 = wx.EVT_SCROLL_BOTTOM
    向小滚动 = wx.EVT_SCROLL_PAGEUP
    向大滚动 = wx.EVT_SCROLL_PAGEDOWN
    停止滚动 = wx.EVT_SCROLL_CHANGED
    选项被单击 = wx.EVT_RADIOBOX
    颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
    点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
    取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
    点击链接 = wx.EVT_TEXT_URL
    响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
    响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
    响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
    数字被调整 = floatspin.EVT_FLOATSPIN


# 鼠标指针
# https://wxpython.org/Phoenix/docs/html/wx.StockCursor.enumeration.html
class 鼠标指针:
    无 = wx.CURSOR_NONE
    最大 = wx.CURSOR_MAX
    默认型 = wx.CURSOR_ARROW
    标准箭头型 = wx.CURSOR_ARROW
    指向右侧的箭头 = wx.CURSOR_RIGHT_ARROW
    靶心 = wx.CURSOR_BULLSEYE
    矩形字符 = wx.CURSOR_CHAR
    十字型 = wx.CURSOR_CROSS
    手型 = wx.CURSOR_HAND
    文本编辑型 = wx.CURSOR_IBEAM  # 工字梁垂直线
    表示鼠标左键按下 = wx.CURSOR_LEFT_BUTTON
    放大镜 = wx.CURSOR_MAGNIFIER
    表示按下中间按钮的鼠标 = wx.CURSOR_MIDDLE_BUTTON
    禁止符型 = wx.CURSOR_NO_ENTRY
    画笔 = wx.CURSOR_PAINT_BRUSH
    铅笔 = wx.CURSOR_PENCIL
    向上箭头 = wx.CURSOR_ARROW  # 这个好像没有啊
    指向左的 = wx.CURSOR_POINT_LEFT
    指向右的 = wx.CURSOR_POINT_RIGHT
    箭头及问号型 = wx.CURSOR_QUESTION_ARROW
    表示按下右键的鼠标 = wx.CURSOR_RIGHT_BUTTON
    四向箭头型 = wx.CURSOR_SIZENESW
    北东箭头型 = wx.CURSOR_SIZENESW  # 这个好像没有啊
    北南箭头型 = wx.CURSOR_SIZENS
    北西箭头型 = wx.CURSOR_SIZENWSE
    西东箭头型 = wx.CURSOR_SIZEWE
    一般大小的游标 = wx.CURSOR_SIZING
    Spraycan游标 = wx.CURSOR_SPRAYCAN
    沙漏型 = wx.CURSOR_WAIT
    监视沙漏 = wx.CURSOR_WATCH
    透明 = wx.CURSOR_BLANK
    标准X11_wxGTK = wx.CURSOR_DEFAULT
    MacOS_Theme_Plus箭头 = wx.CURSOR_COPY_ARROW
    箭头及沙漏型 = wx.CURSOR_ARROWWAIT


# 边框
# https://wxpython.org/Phoenix/docs/html/wx.Window.html
class 边框:
    窗口边框 = wx.BORDER_DEFAULT  # 窗口类将决定要显示的边框类型（如果有）。

    细边框 = wx.BORDER_SIMPLE  # 在窗口周围显示细边框。wx.SIMPLE_BORDER是此样式的旧名称。

    下陷边框 = wx.BORDER_SUNKEN  # 显示下陷的边框。wx.SUNKEN_BORDER是此样式的旧名称。

    凸起边框 = wx.BORDER_RAISED  # 显示凸起的边框。wx.RAISED_BORDER是此样式的旧名称。

    静态控件边框 = wx.BORDER_STATIC  # 显示适合静态控件的边框。wx.STATIC_BORDER是此样式的旧名称。仅Windows。

    系统边框 = wx.BORDER_THEME  # 在当前平台上显示适合控件的本机边框。在Windows上，这将是一个主题边框；在大多数其他平台上，将使用凹陷的边框。有关Windows主题边框的更多信息，请参见Windows主题边框。

    无边框 = wx.BORDER_NONE  # 不显示任何边框，覆盖窗口的默认边框样式。wx.NO_BORDER是此样式的旧名称。

    # todo:: 边框样式我也不知道尽量对得上吧
    # 无边框 = wx.BORDER_NONE,
    凹入式 = wx.BORDER_SUNKEN,
    凸出式 = wx.BORDER_RAISED,
    浅凹入式 = wx.BORDER_SIMPLE,
    镜框式 = wx.BORDER_STATIC,
    单线边框式 = wx.BORDER_THEME


class 窗口边框:
    无边框 = wx.BORDER_NONE
    普通可调边框 = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
    普通固定边框 = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN


class 底图方式:
    图片居左上 = "图片居左上"
    图片平铺 = "图片平铺"
    图片居中 = "图片居中"
    缩放图片 = "缩放图片"


class 窗口位置:
    通常 = "通常"
    居中 = "最小化"
    最小化 = "最小化"
    最大化 = "最大化"
    全屏 = "全屏"


class 播放次数:
    仅播放一次同步模式 = wx.adv.SOUND_SYNC  # Play 将阻塞并等待声音重放。
    仅播放一次 = wx.adv.SOUND_ASYNC  # 声音异步播放， Play 立即返回。
    循环播放 = wx.adv.SOUND_ASYNC | wx.adv.SOUND_LOOP  # 声音异步播放并循环播放，直到另一个声音被播放、Stop 调用或程序终止。


class 窗口样式:
    透明 = wx.TRANSPARENT_WINDOW  # 窗口是透明的，即它将不接收绘画事件。仅Windows。
    tab导航 = wx.TAB_TRAVERSAL  # wxWidgets使用此样式的窗口支持TAB其子级之间的导航，例如 wx.Dialog 和 wx.Panel。几乎不应在应用程序代码中使用它。
    支持导航键 = wx.WANTS_CHARS  # 使用它来指示窗口希望获取所有键的所有char / key事件-甚至对于通常用于对话框导航的键，例如TAB或ENTER，如果没有这种样式就不会生成这些键。如果您需要使用此样式来获取箭头等，但仍希望进行正常的键盘导航，则应调用“导航”以响应Tab和Shift-Tab的键事件。
    #  = wx.NO_FULL_REPAINT_ON_RESIZE #在Windows上，此样式用于在更改大小后完全禁用重新绘制窗口。由于现在是默认行为，因此样式现在已过时，不再起作用。
    垂直滚动条 = wx.VSCROLL  # 使用此样式可以启用垂直滚动条。请注意，此样式不能与不支持滚动条的本机控件一起使用，也不能与大多数端口中的顶级窗口一起使用。
    水平滚动条 = wx.HSCROLL  # 使用此样式启用水平滚动条。与wx.VSCROLL适用于此样式的限制相同。
    自动显示滚动条 = wx.ALWAYS_SHOW_SB  # 如果窗口具有滚动条，请在不需要滚动条时将其禁用，而不是隐藏它们（例如，当窗口的大小足够大而无需滚动条进行导航时）。目前，此样式已针对wxMSW，wxGTK和wxUniversal实现，并且在其他平台上不起作用。
    清除绘制闪烁 = wx.CLIP_CHILDREN  # 使用此样式可以消除由于重新绘制背景而在其上绘制子级而引起的闪烁。仅Windows。
    强制重绘窗口 = wx.FULL_REPAINT_ON_RESIZE  # 注意使用此样式可以在重新调整窗口大小时强制完全重绘窗口，而不是仅重绘受调整大小影响的窗口部分。请注意，默认情况下是2.5.1发行版之前的行为，并且如果您遇到以前使用过的代码重绘问题，则可能需要尝试此操作。目前，此样式仅适用于GTK + 2和Windows，并且始终在其他平台上进行完整的重新绘制。

    最小化按钮 = wx.MINIMIZE_BOX
    最大化按钮 = wx.MAXIMIZE_BOX
    可调边框 = wx.RESIZE_BORDER
    系统菜单 = wx.SYSTEM_MENU
    标题 = wx.CAPTION
    关闭按钮 = wx.CLOSE_BOX
    # wx.CLIP_CHILDREN 似乎是一个用于加速父窗口绘制的

    图标 = wx.ICONIZE  # ：显示图标化（最小化）的框架。仅限 Windows。
    # wx.CAPTION  # ：在框架上放置标题。请注意，该标志是wx.MINIMIZE_BOX,wx.MAXIMIZE_BOX并且wx.CLOSE_BOX在大多数系统上是必需的，因为如果窗口根本没有标题栏，则无法显示相应的按钮。即如果wx.CAPTION没有指定那些样式将被简单地忽略。
    # wx.MINIMIZE  #: 一样wx.ICONIZE。仅限 Windows。
    # wx.MINIMIZE_BOX  # ：在框架上显示最小化框。
    # wx.MAXIMIZE  #: 最大化显示帧。仅限 Windows 和 GTK+。
    # wx.MAXIMIZE_BOX  # ：在框架上显示最大化框。请注意，在 wxGTK 下也wx.RESIZE_BORDER必须使用，否则此样式将被忽略。
    # wx.CLOSE_BOX  # ：在框架上显示一个关闭框。
    总在最前 = wx.STAY_ON_TOP  # ：留在所有其他窗口的顶部，另请参见wx.FRAME_FLOAT_ON_PARENT。
    # wx.SYSTEM_MENU  #: 在窗口标题栏中显示包含各种窗口命令列表的系统菜单。与wx.MINIMIZE_BOX,wx.MAXIMIZE_BOX和wx.CLOSE_BOX样式不同，这种样式wx.CAPTION至少在 Windows 下可以不使用，并且在这种情况下使系统菜单可用而无需在屏幕上显示。但是，建议仅将其与wx.CAPTION所有平台下的一致行为一起使用。
    # wx.RESIZE_BORDER  # ：在窗口周围显示可调整大小的边框。
    不显示在任务栏 = wx.FRAME_TOOL_WINDOW  #: 导致创建一个带有小标题栏的框架；在 Windows 或 GTK+ 下，该框架不会出现在任务栏中。
    正常窗口 = wx.FRAME_NO_TASKBAR  #: 创建一个其他正常的框架，但它不会出现在 Windows 或 GTK+ 下的任务栏中（请注意，它会最小化到 Windows 下的桌面窗口，这对用户来说可能看起来很奇怪，因此最好只使用这种样式而不使用wx.MINIMIZE_BOX样式）。在 wxGTK 中，仅当窗口管理器支持_NET_WM_STATE_SKIP_TASKBAR提示时才考虑该标志。
    始终在父窗口前面 = wx.FRAME_FLOAT_ON_PARENT  #: 框架将始终位于其父级之上（与 不同wx.STAY_ON_TOP）。使用此样式创建的框架必须具有非None父项。
    改变形状 = wx.FRAME_SHAPED  #: 允许使用此样式的窗口使用该SetShape 方法更改其形状。


class 按钮样式:
    文字左对齐 = wx.BU_LEFT  # 左对齐标签。仅Windows和GTK +。
    文字在顶部 = wx.BU_TOP  # 将标签对准按钮的顶部。仅Windows和GTK +。
    文字右对齐 = wx.BU_RIGHT  # 右对齐位图标签。仅Windows和GTK +。
    文字在底部 = wx.BU_BOTTOM  # 将标签对准按钮的底部。仅Windows和GTK +。
    精准贴合 = wx.BU_EXACTFIT  # 默认情况下，即使所有按钮的内容足够小以适合较小的尺寸，它们也至少由标准按钮尺寸制成。这样做是为了保持一致性，因为大多数平台在本机对话框中使用大小相同的按钮，但可以通过指定此标志来覆盖它们。如果指定了该按钮，则其大小将刚好足以容纳其内容。请注意，在MSW下，即使按钮具有非空标签，即使采用这种样式，该按钮仍将至少具有标准高度。
    不显示标签 = wx.BU_NOTEXT  # 即使按钮具有一个或其id是带有关联标签的标准库存ID之一，也无法在按钮中显示文本标签#如果不使用此样式，则仅应显示位图但使用标准ID的按钮也会显示标签。
    无边框 = wx.BORDER_NONE  # 创建一个无边框的按钮。目前已在MSW，GTK2和OSX / Cocoa中实现

    文字在左上角 = wx.BU_LEFT | wx.BU_TOP
    文字在顶部 = wx.BU_TOP
    文字在右上角 = wx.BU_RIGHT | wx.BU_TOP
    文字在左边 = wx.BU_LEFT
    文字在居中 = 0
    文字在右边 = wx.BU_RIGHT
    文字在左下角 = wx.BU_RIGHT | wx.BU_BOTTOM
    文字在底部 = wx.BU_RIGHT
    文字在右下角 = wx.BU_RIGHT | wx.BU_BOTTOM


# 文字方向
class 文本样式:
    左对齐 = wx.ALIGN_LEFT  # 将文本向左对齐。
    右对齐 = wx.ALIGN_RIGHT  # 将文本向右对齐。
    居中 = wx.ALIGN_CENTRE_HORIZONTAL  # 将文本居中（水平）。


class 标签样式:
    文字在左边 = wx.ALIGN_LEFT  # 将文本向左对齐。
    文字在右边 = wx.ALIGN_RIGHT  # 将文本向右对齐。
    文字在居中 = wx.ALIGN_CENTRE_HORIZONTAL  # 将文本居中（水平）。
    禁用自动调整大小 = wx.ST_NO_AUTORESIZE  # ：默认情况下，控件将调整其大小以使其完全适合SetLabel 被调用时文本的大小。如果提供了此样式标志，则控件将不会更改其大小（此样式对于也具有ALIGN_RIGHT 或 ALIGN_CENTRE_HORIZONTAL 样式的控件特别有用， 因为否则在调用以后它们将不再有意义 SetLabel）。
    省略号在开头 = wx.ST_ELLIPSIZE_START  # ：如果labeltext宽度超过控件宽度，则用省略号替换标签的开头；用途wx.Control.Ellipsize。
    省略号在中间 = wx.ST_ELLIPSIZE_MIDDLE  # ：如果标签文本的宽度超过控件的宽度，则用省略号替换标签的中间；用途wx.Control.Ellipsize。
    省略号在末尾 = wx.ST_ELLIPSIZE_END  # ：如果标签文本的宽度超过控件的宽度，请用省略号替换标签的末尾；用途wx.Control.Ellipsize。


class 组合框样式:
    可编辑列表式 = wx.CB_SIMPLE  # ：创建一个带有永久显示列表的组合框。仅限 Windows。
    可编辑下拉式 = wx.CB_DROPDOWN  # ：创建一个带有下拉列表的组合框。仅 MSW 和 Motif。
    不可编辑下拉式 = wx.CB_READONLY  # ：具有这种样式的组合框的行为类似于wx .Choice （并且可能看起来也相同，尽管这取决于平台），即它允许用户从选项列表中进行选择但不允许输入列表中不存在的值。
    自动排序 = wx.CB_SORT  # ：按字母顺序对列表中的条目进行排序。
    接收按下回车事件 = wx.TE_PROCESS_ENTER  #: 控件会产生 程序可以处理的事件 。否则，即如果根本没有指定此样式，或者使用它，但没有此事件的事件处理程序或调用的事件处理程序 以避免覆盖默认处理，则按 Enter 键要么由控件内部处理，要么使用激活对话框的默认按钮（如果有）。wxEVT_TEXT_ENTERwx.Event.Skip


class 列表框样式:
    单选列表 = wx.LB_SINGLE  # ：单选列表。
    多选列表 = wx.LB_MULTIPLE  # ：多选列表 #：用户可以打开和关闭多个项目。这与wx.LB_EXTENDEDwxGTK2 端口相同。
    扩展选择列表 = wx.LB_EXTENDED  # ：扩展选择列表 #：用户可以使用SHIFT 或 CTRL 键与光标移动键或鼠标一起使用来扩展选择 。
    自动显示水平滚动条 = wx.LB_HSCROLL  # ：如果内容太宽，则创建水平滚动条（仅限 Windows）。
    始终显示垂直滚动条 = wx.LB_ALWAYS_SB  # ：始终显示垂直滚动条。
    自动显示垂直滚动条 = wx.LB_NEEDED_SB  # ：仅在需要时创建垂直滚动条。
    禁用垂直滚动条 = wx.LB_NO_SB  #: 不要创建垂直滚动条（仅限 wxMSW 和 wxGTK）。
    自动排序 = wx.LB_SORT  # ：列表框内容按字母顺序排序。
    # 注意
    # LB_SINGLE, LB_MULTIPLE 和 LB_EXTENDED 样式是互斥的，您最多可以指定其中之一（默认为单选）。另请参阅 窗口样式。


class 超级列表框样式:
    普通列表框 = wx.LC_LIST  # ：多列列表视图，带有可选的小图标。列是自动计算的，即您没有像 in 那样设置列 LC_REPORT。换句话说，与 wx.ListBox不同，列表会自动换 行。
    报表列表框 = wx.LC_REPORT  # ：单列或多列报表视图，带有可选标题。
    报表列表下项目文本 = wx.LC_VIRTUAL  # ：该应用程序按需提供项目文本。只能与 LC_REPORT.
    大图标列表框 = wx.LC_ICON  # ：大图标视图，带有可选标签。
    小图标列表框 = wx.LC_SMALL_ICON  # ：小图标视图，带有可选标签。
    图标顶部对齐 = wx.LC_ALIGN_TOP  # ：图标与顶部对齐。Win32 默认，仅 Win32。
    图标左边对齐 = wx.LC_ALIGN_LEFT  # ：图标向左对齐。
    自动排列图标 = wx.LC_AUTOARRANGE  #: 图标自行排列。仅限 Win32。
    允许编辑 = wx.LC_EDIT_LABELS  # ：标签可编辑 #：编辑开始时将通知应用程序。
    报表列表无表头 = wx.LC_NO_HEADER  #: 报表模式下没有标题。
    单一选择 = wx.LC_SINGLE_SEL  # ：单选（默认为多选）。
    正向排序 = wx.LC_SORT_ASCENDING  #: 按升序排列。（您仍然必须在wx.ListCtrl.SortItems. 中提供比较回调。）
    逆向排序 = wx.LC_SORT_DESCENDING  #: 降序排列。（您仍然必须在wx.ListCtrl.SortItems. 中提供比较回调。）
    显示水平表格线 = wx.LC_HRULES  # ：在报表模式下在行之间绘制浅色水平线。
    显示垂直表格线 = wx.LC_VRULES  # ：在报表模式下在列之间绘制浅色垂直线。


class 图片组样式:
    正常图标 = wx.IMAGE_LIST_NORMAL
    小图标 = wx.IMAGE_LIST_SMALL
    状态图标 = wx.IMAGE_LIST_STATE

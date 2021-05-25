"""
组件的事件


事件_按钮_被点击 = wx.EVT_BUTTON
事件_复选框_被点击 = wx.EVT_CHECKBOX
事件_选择_被点击 = wx.EVT_CHOICE
事件_列表框_被点击 = wx.EVT_LISTBOX
事件_列表框_被双击 = wx.EVT_LISTBOX_DCLICK
事件_菜单_被点击 = wx.EVT_MENU
事件_菜单范围_被点击 = wx.EVT_MENU_RANGE
事件_滑块_被点击 = wx.EVT_SLIDER
事件_无线电箱_被点击 = wx.EVT_RADIOBOX
事件_单选按钮_被点击 = wx.EVT_RADIOBUTTON

事件_鼠标左键按下 = wx.EVT_LEFT_DOWN
事件_鼠标左键松开 = wx.EVT_LEFT_UP
事件_鼠标左键双击 = wx.EVT_LEFT_DCLICK
事件_鼠标右键按下 = wx.EVT_RIGHT_DOWN
事件_鼠标右键松开 = wx.EVT_RIGHT_UP
事件_鼠标右键双击 = wx.EVT_RIGHT_DCLICK
事件_鼠标中键按下 = wx.EVT_MIDDLE_DOWN
事件_鼠标中键松开 = wx.EVT_MIDDLE_UP
事件_鼠标中键双击 = wx.EVT_MIDDLE_DCLICK
事件_鼠标中键滚动 = wx.EVT_MOUSEWHEEL
事件_鼠标移动 = wx.EVT_MOTION
事件_鼠标进入 = wx.EVT_ENTER_WINDOW
事件_鼠标离开 = wx.EVT_LEAVE_WINDOW
事件_点击某键 = wx.EVT_CHAR_HOOK
事件_按下某键 = wx.EVT_KEY_DOWN
事件_松开某键 = wx.EVT_KEY_UP
事件_获得焦点 = wx.EVT_SET_FOCUS
事件_失去焦点 = wx.EVT_KILL_FOCUS
事件_按钮被单击 = wx.EVT_BUTTON
事件_创建完毕 = wx.EVT_WINDOW_CREATE
事件_尺寸被改变 = wx.EVT_SIZE
事件_位置被移动 = wx.EVT_MOVE
事件_将被关闭 = wx.EVT_CLOSE
事件_内容被改变 = wx.EVT_TEXT
事件_按下Enter键 = wx.EVT_TEXT_ENTER
事件_达到限制长度 = wx.EVT_TEXT_MAXLEN
事件_状态被改变 = wx.EVT_RADIOBUTTON
事件_狀态被改变 = wx.EVT_CHECKBOX
事件_选中列表项 = wx.EVT_COMBOBOX
事件_文本发生变化 = wx.EVT_TEXT
事件_弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
事件_收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
事件_被拖动 = wx.EVT_SLIDER
事件_向小拖动 = wx.EVT_SCROLL_PAGEUP
事件_向大拖动 = wx.EVT_SCROLL_PAGEDOWN
事件_正在拖动 = wx.EVT_SCROLL_THUMBTRACK
事件_停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
事件_数值被调整 = wx.EVT_SPINCTRL
事件_周期事件 = wx.EVT_TIMER
事件_表项被单击 = wx.EVT_CHECKLISTBOX
事件_表项被双击 = wx.EVT_LISTBOX_DCLICK
事件_链接被单击 = wx.adv.EVT_HYPERLINK
事件_双击某一天 = wx.adv.EVT_CALENDAR
事件_日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
事件_年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
事件_内容被更改 = wx.adv.EVT_DATE_CHANGED
事件_内容被修改 = wx.adv.EVT_TIME_CHANGED
事件_左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
事件_右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
事件_开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
事件_编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
事件_表项被删除 = wx.EVT_LIST_DELETE_ITEM
事件_表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
事件_选中表项 = wx.EVT_LIST_ITEM_SELECTED
事件_取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
事件_表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
事件_中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
事件_右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
事件_表项按下某键 = wx.EVT_LIST_KEY_DOWN
事件_插入新表项 = wx.EVT_LIST_INSERT_ITEM
事件_左键单击某列 = wx.EVT_LIST_COL_CLICK
事件_右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
事件_开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
事件_分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
事件_列宽被修改 = wx.EVT_LIST_COL_END_DRAG
事件_表项被选中 = wx.EVT_LIST_ITEM_CHECKED
事件_表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
事件_滚动事件 = wx.EVT_SCROLL
事件_滚到最小位置 = wx.EVT_SCROLL_TOP
事件_滚到最大位置 = wx.EVT_SCROLL_BOTTOM
事件_向小滚动 = wx.EVT_SCROLL_PAGEUP
事件_向大滚动 = wx.EVT_SCROLL_PAGEDOWN
事件_停止滚动 = wx.EVT_SCROLL_CHANGED
事件_选项被单击 = wx.EVT_RADIOBOX
事件_颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
事件_点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
事件_取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
事件_点击链接 = wx.EVT_TEXT_URL
事件_响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
事件_响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
事件_响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
事件_数字被调整 = floatspin.EVT_FLOATSPIN

"""
import wx.lib.agw.floatspin as floatspin
import wx.lib.agw.hyperlink as hyperlink

import wx
import wx.adv
from wx import *

事件_按钮_被点击 = wx.EVT_BUTTON
事件_复选框_被点击 = wx.EVT_CHECKBOX
事件_选择_被点击 = wx.EVT_CHOICE
事件_列表框_被点击 = wx.EVT_LISTBOX
事件_列表框_被双击 = wx.EVT_LISTBOX_DCLICK
事件_菜单_被点击 = wx.EVT_MENU
事件_菜单范围_被点击 = wx.EVT_MENU_RANGE
事件_滑块_被点击 = wx.EVT_SLIDER
事件_无线电箱_被点击 = wx.EVT_RADIOBOX
事件_单选按钮_被点击 = wx.EVT_RADIOBUTTON

事件_鼠标左键按下 = wx.EVT_LEFT_DOWN
事件_鼠标左键松开 = wx.EVT_LEFT_UP
事件_鼠标左键双击 = wx.EVT_LEFT_DCLICK
事件_鼠标右键按下 = wx.EVT_RIGHT_DOWN
事件_鼠标右键松开 = wx.EVT_RIGHT_UP
事件_鼠标右键双击 = wx.EVT_RIGHT_DCLICK
事件_鼠标中键按下 = wx.EVT_MIDDLE_DOWN
事件_鼠标中键松开 = wx.EVT_MIDDLE_UP
事件_鼠标中键双击 = wx.EVT_MIDDLE_DCLICK
事件_鼠标中键滚动 = wx.EVT_MOUSEWHEEL
事件_鼠标移动 = wx.EVT_MOTION
事件_鼠标进入 = wx.EVT_ENTER_WINDOW
事件_鼠标离开 = wx.EVT_LEAVE_WINDOW
事件_点击某键 = wx.EVT_CHAR_HOOK
事件_按下某键 = wx.EVT_KEY_DOWN
事件_松开某键 = wx.EVT_KEY_UP
事件_获得焦点 = wx.EVT_SET_FOCUS
事件_失去焦点 = wx.EVT_KILL_FOCUS
事件_按钮被单击 = wx.EVT_BUTTON
事件_创建完毕 = wx.EVT_WINDOW_CREATE
事件_尺寸被改变 = wx.EVT_SIZE
事件_位置被移动 = wx.EVT_MOVE
事件_将被关闭 = wx.EVT_CLOSE
事件_内容被改变 = wx.EVT_TEXT
事件_按下Enter键 = wx.EVT_TEXT_ENTER
事件_达到限制长度 = wx.EVT_TEXT_MAXLEN
事件_状态被改变 = wx.EVT_RADIOBUTTON
事件_狀态被改变 = wx.EVT_CHECKBOX
事件_选中列表项 = wx.EVT_COMBOBOX
事件_文本发生变化 = wx.EVT_TEXT
事件_弹出列表项 = wx.EVT_COMBOBOX_DROPDOWN
事件_收起列表项 = wx.EVT_COMBOBOX_CLOSEUP
事件_被拖动 = wx.EVT_SLIDER
事件_向小拖动 = wx.EVT_SCROLL_PAGEUP
事件_向大拖动 = wx.EVT_SCROLL_PAGEDOWN
事件_正在拖动 = wx.EVT_SCROLL_THUMBTRACK
事件_停止拖动 = wx.EVT_SCROLL_THUMBRELEASE
事件_数值被调整 = wx.EVT_SPINCTRL
事件_周期事件 = wx.EVT_TIMER
事件_表项被单击 = wx.EVT_CHECKLISTBOX
事件_表项被双击 = wx.EVT_LISTBOX_DCLICK
事件_链接被单击 = wx.adv.EVT_HYPERLINK
事件_双击某一天 = wx.adv.EVT_CALENDAR
事件_日期已更改 = wx.adv.EVT_CALENDAR_SEL_CHANGED
事件_年月已更改 = wx.adv.EVT_CALENDAR_PAGE_CHANGED
事件_内容被更改 = wx.adv.EVT_DATE_CHANGED
事件_内容被修改 = wx.adv.EVT_TIME_CHANGED
事件_左键开始拖动 = wx.EVT_LIST_BEGIN_DRAG
事件_右键开始拖动 = wx.EVT_LIST_BEGIN_RDRAG
事件_开始编辑标签 = wx.EVT_LIST_BEGIN_LABEL_EDIT
事件_编辑标签结束 = wx.EVT_LIST_END_LABEL_EDIT
事件_表项被删除 = wx.EVT_LIST_DELETE_ITEM
事件_表项全部被删 = wx.EVT_LIST_DELETE_ALL_ITEMS
事件_选中表项 = wx.EVT_LIST_ITEM_SELECTED
事件_取消选中表项 = wx.EVT_LIST_ITEM_DESELECTED
事件_表项已激活 = wx.EVT_LIST_ITEM_ACTIVATED
事件_中键单击表项 = wx.EVT_LIST_ITEM_MIDDLE_CLICK
事件_右键单击表项 = wx.EVT_LIST_ITEM_RIGHT_CLICK
事件_表项按下某键 = wx.EVT_LIST_KEY_DOWN
事件_插入新表项 = wx.EVT_LIST_INSERT_ITEM
事件_左键单击某列 = wx.EVT_LIST_COL_CLICK
事件_右键单击某列 = wx.EVT_LIST_COL_RIGHT_CLICK
事件_开始调整列宽 = wx.EVT_LIST_COL_BEGIN_DRAG
事件_分隔线在拖动 = wx.EVT_LIST_COL_DRAGGING
事件_列宽被修改 = wx.EVT_LIST_COL_END_DRAG
事件_表项被选中 = wx.EVT_LIST_ITEM_CHECKED
事件_表项未选中 = wx.EVT_LIST_ITEM_UNCHECKED
事件_滚动事件 = wx.EVT_SCROLL
事件_滚到最小位置 = wx.EVT_SCROLL_TOP
事件_滚到最大位置 = wx.EVT_SCROLL_BOTTOM
事件_向小滚动 = wx.EVT_SCROLL_PAGEUP
事件_向大滚动 = wx.EVT_SCROLL_PAGEDOWN
事件_停止滚动 = wx.EVT_SCROLL_CHANGED
事件_选项被单击 = wx.EVT_RADIOBOX
事件_颜色被更改 = wx.EVT_COLOURPICKER_CHANGED
事件_点击某颜色 = wx.EVT_COLOURPICKER_CURRENT_CHANGED
事件_取消更改颜色 = wx.EVT_COLOURPICKER_DIALOG_CANCELLED
事件_点击链接 = wx.EVT_TEXT_URL
事件_响应左键事件 = hyperlink.EVT_HYPERLINK_LEFT
事件_响应中键事件 = hyperlink.EVT_HYPERLINK_MIDDLE
事件_响应右键事件 = hyperlink.EVT_HYPERLINK_RIGHT
事件_数字被调整 = floatspin.EVT_FLOATSPIN

# 鼠标指针
# https://wxpython.org/Phoenix/docs/html/wx.StockCursor.enumeration.html
鼠标指针_无 = wx.CURSOR_NONE
鼠标指针_最大光标 = wx.CURSOR_MAX
鼠标指针_标准箭头光标 = wx.CURSOR_ARROW
鼠标指针_指向右侧的标准箭头光标 = wx.CURSOR_RIGHT_ARROW
鼠标指针_靶心光标 = wx.CURSOR_BULLSEYE
鼠标指针_矩形字符光标 = wx.CURSOR_CHAR
鼠标指针_十字光标 = wx.CURSOR_CROSS
鼠标指针_手形光标 = wx.CURSOR_HAND
鼠标指针_工字梁光标垂直线 = wx.CURSOR_IBEAM
鼠标指针_表示鼠标左键按下 = wx.CURSOR_LEFT_BUTTON
鼠标指针_放大镜图标 = wx.CURSOR_MAGNIFIER
鼠标指针_表示按下中间按钮的鼠标 = wx.CURSOR_MIDDLE_BUTTON
鼠标指针_不可输入的符号光标 = wx.CURSOR_NO_ENTRY
鼠标指针_画笔光标 = wx.CURSOR_PAINT_BRUSH
鼠标指针_铅笔光标 = wx.CURSOR_PENCIL
鼠标指针_指向左的光标 = wx.CURSOR_POINT_LEFT
鼠标指针_指向右的光标 = wx.CURSOR_POINT_RIGHT
鼠标指针_箭头和问号 = wx.CURSOR_QUESTION_ARROW
鼠标指针_表示按下了右键的鼠标 = wx.CURSOR_RIGHT_BUTTON
鼠标指针_调整大小的光标指向NE_SW = wx.CURSOR_SIZENESW
鼠标指针_调整大小的光标指向N_S = wx.CURSOR_SIZENS
鼠标指针_调整大小的光标指向NW_SE = wx.CURSOR_SIZENWSE
鼠标指针_调整大小的光标指向W_E = wx.CURSOR_SIZEWE
鼠标指针_一般大小的游标 = wx.CURSOR_SIZING
鼠标指针_Spraycan游标 = wx.CURSOR_SPRAYCAN
鼠标指针_等待光标 = wx.CURSOR_WAIT
鼠标指针_监视光标 = wx.CURSOR_WATCH
鼠标指针_透明光标 = wx.CURSOR_BLANK
鼠标指针_标准X11光标仅在wxGTK中 = wx.CURSOR_DEFAULT
鼠标指针_MacOS_Theme_Plus箭头 = wx.CURSOR_COPY_ARROW
鼠标指针_带有标准箭头的等待光标 = wx.CURSOR_ARROWWAIT

# 边框
# https://wxpython.org/Phoenix/docs/html/wx.Window.html
边框_窗口边框 = wx.BORDER_DEFAULT  # 窗口类将决定要显示的边框类型（如果有）。

边框_细边框 = wx.BORDER_SIMPLE  # 在窗口周围显示细边框。wx.SIMPLE_BORDER是此样式的旧名称。

边框_下陷边框 = wx.BORDER_SUNKEN  # 显示下陷的边框。wx.SUNKEN_BORDER是此样式的旧名称。

边框_凸起边框 = wx.BORDER_RAISED  # 显示凸起的边框。wx.RAISED_BORDER是此样式的旧名称。

边框_静态控件边框 = wx.BORDER_STATIC  # 显示适合静态控件的边框。wx.STATIC_BORDER是此样式的旧名称。仅Windows。

边框_系统边框 = wx.BORDER_THEME  # 在当前平台上显示适合控件的本机边框。在Windows上，这将是一个主题边框；在大多数其他平台上，将使用凹陷的边框。有关Windows主题边框的更多信息，请参见Windows主题边框。

边框_无边框 = wx.BORDER_NONE  # 不显示任何边框，覆盖窗口的默认边框样式。wx.NO_BORDER是此样式的旧名称。

# 边框_ = wx.BORDER_DOUBLE #此样式已过时，不应使用。

窗口样式_透明 = wx.TRANSPARENT_WINDOW  # 窗口是透明的，即它将不接收绘画事件。仅Windows。

窗口样式_tab导航 = wx.TAB_TRAVERSAL  # wxWidgets使用此样式的窗口支持TAB其子级之间的导航，例如 wx.Dialog 和 wx.Panel。几乎不应在应用程序代码中使用它。

窗口样式_支持导航键 = wx.WANTS_CHARS  # 使用它来指示窗口希望获取所有键的所有char / key事件-甚至对于通常用于对话框导航的键，例如TAB或ENTER，如果没有这种样式就不会生成这些键。如果您需要使用此样式来获取箭头等，但仍希望进行正常的键盘导航，则应调用“导航”以响应Tab和Shift-Tab的键事件。

# 窗口样式_ = wx.NO_FULL_REPAINT_ON_RESIZE #在Windows上，此样式用于在更改大小后完全禁用重新绘制窗口。由于现在是默认行为，因此样式现在已过时，不再起作用。

窗口样式_垂直滚动条 = wx.VSCROLL  # 使用此样式可以启用垂直滚动条。请注意，此样式不能与不支持滚动条的本机控件一起使用，也不能与大多数端口中的顶级窗口一起使用。

窗口样式_水平滚动条 = wx.HSCROLL  # 使用此样式启用水平滚动条。与wx.VSCROLL适用于此样式的限制相同。

窗口样式_自动显示滚动条 = wx.ALWAYS_SHOW_SB  # 如果窗口具有滚动条，请在不需要滚动条时将其禁用，而不是隐藏它们（例如，当窗口的大小足够大而无需滚动条进行导航时）。目前，此样式已针对wxMSW，wxGTK和wxUniversal实现，并且在其他平台上不起作用。

窗口样式_清除绘制闪烁 = wx.CLIP_CHILDREN  # 使用此样式可以消除由于重新绘制背景而在其上绘制子级而引起的闪烁。仅Windows。

窗口样式_强制重绘窗口 = wx.FULL_REPAINT_ON_RESIZE  # 注意使用此样式可以在重新调整窗口大小时强制完全重绘窗口，而不是仅重绘受调整大小影响的窗口部分。请注意，默认情况下是2.5.1发行版之前的行为，并且如果您遇到以前使用过的代码重绘问题，则可能需要尝试此操作。目前，此样式仅适用于GTK + 2和Windows，并且始终在其他平台上进行完整的重新绘制。

# 按钮文字方向
按钮样式_文字左对齐 = wx.BU_LEFT  # 左对齐标签。仅Windows和GTK +。
按钮样式_文字在顶部 = wx.BU_TOP  # 将标签对准按钮的顶部。仅Windows和GTK +。
按钮样式_文字右对齐 = wx.BU_RIGHT  # 右对齐位图标签。仅Windows和GTK +。
按钮样式_文字在底部 = wx.BU_BOTTOM  # 将标签对准按钮的底部。仅Windows和GTK +。
按钮样式_精准贴合 = wx.BU_EXACTFIT  # 默认情况下，即使所有按钮的内容足够小以适合较小的尺寸，它们也至少由标准按钮尺寸制成。这样做是为了保持一致性，因为大多数平台在本机对话框中使用大小相同的按钮，但可以通过指定此标志来覆盖它们。如果指定了该按钮，则其大小将刚好足以容纳其内容。请注意，在MSW下，即使按钮具有非空标签，即使采用这种样式，该按钮仍将至少具有标准高度。
按钮样式_不显示标签 = wx.BU_NOTEXT  # 即使按钮具有一个或其id是带有关联标签的标准库存ID之一，也无法在按钮中显示文本标签#如果不使用此样式，则仅应显示位图但使用标准ID的按钮也会显示标签。
按钮样式_无边框 = wx.BORDER_NONE  # 创建一个无边框的按钮。目前已在MSW，GTK2和OSX / Cocoa中实现

# 文字方向
文本样式_左对齐 = wx.ALIGN_LEFT  # 将文本向左对齐。
文本样式_右对齐 = wx.ALIGN_RIGHT  # 将文本向右对齐。
文本样式_居中 = wx.ALIGN_CENTRE_HORIZONTAL  # 将文本居中（水平）。
标签样式_自动调整大小 = wx.ST_NO_AUTORESIZE  # ：默认情况下，控件将调整其大小以使其完全适合SetLabel 被调用时文本的大小。如果提供了此样式标志，则控件将不会更改其大小（此样式对于也具有ALIGN_RIGHT 或 ALIGN_CENTRE_HORIZONTAL 样式的控件特别有用， 因为否则在调用以后它们将不再有意义 SetLabel）。
标签样式_省略号在开头 = wx.ST_ELLIPSIZE_START  # ：如果labeltext宽度超过控件宽度，则用省略号替换标签的开头；用途wx.Control.Ellipsize。
标签样式_省略号在中间 = wx.ST_ELLIPSIZE_MIDDLE  # ：如果标签文本的宽度超过控件的宽度，则用省略号替换标签的中间；用途wx.Control.Ellipsize。
标签样式_省略号在末尾 = wx.ST_ELLIPSIZE_END  # ：如果标签文本的宽度超过控件的宽度，请用省略号替换标签的末尾；用途wx.Control.Ellipsize。

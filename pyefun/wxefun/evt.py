"""
组件的事件

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

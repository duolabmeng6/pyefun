import wx.adv
import wx
from .wxControl import *


class 超级列表框(wx.ListCtrl, 公用方法):
    pass
    @property
    def 行数(self):
        return self.取行数()

    @行数.setter
    def 行数(self, value):
        self.SetItemCount(value)

    @property
    def 列数(self):
        return self.GetColumnCount()

    @列数.setter
    def 列数(self, value):
        pass

    @property
    def 行高(self):
        return self.GetColumnCount()

    @行高.setter
    def 行高(self, value):
        pass
        图片组 = wx.ImageList(1, value, True)
        self.置图片组(图片组, wx.IMAGE_LIST_SMALL)


    def 选择框全选(self):
        for i in range(self.取项目数量()):
            self.选择框置选中状态(i, True)

    def 选择框全不选(self):
        for i in range(self.取项目数量()):
            self.选择框置选中状态(i, False)

    def 选择框取反(self):
        for i in range(self.取项目数量()):
            if self.选择框取选中状态(i):
                self.选择框置选中状态(i, False)
            else:
                self.选择框置选中状态(i, True)

    def 选择框取选中项目索引(self):
        indexs = []
        for i in range(self.取项目数量()):
            if self.选择框取选中状态(i):
                indexs.append(i)
        return indexs

    def 取选中的项目索引(self):
        indexs = []
        for i in range(self.取项目数量()):
            if self.IsSelected(i):
                indexs.append(i)
        return indexs

    def 取表项数(self):
        return self.取项目数量()
    def 取行数(self):
        return self.取项目数量()

    def 插入表项(self, 索引, 项目文本="", 图片索引=0):
        return self.插入项目(索引, 项目文本, 图片索引)

    @组件_异常检测
    def 加入行(self, 内容列表):
        '在末尾加入新一行数据，返回加入的行索引'
        return self.Append(内容列表)

    @组件_异常检测
    def 加入列(self, 标题, 对齐方式=2, 宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.AppendColumn(标题, 对齐方式, 宽度)

    @组件_异常检测
    def 排列项目(self, 排列方式=0):
        """
        在图标或小图标视图中排列项目
        :param 排列方式: 0.默认对齐方式  1.与控件的左侧对齐 2.与控件的顶部对齐 3.对齐网格
        :return:
        """
        return self.Arrange(排列方式)

    @组件_异常检测
    def 置选中状态(self, 索引, 选中=True):
        '使用复选框选中或取消选中 控件中的wx.ListItem'
        return self.CheckItem(索引, 选中)

    def 全部删除(self):
        '删除所有项目和所有列'
        return self.ClearAll()

    def 删除所有列(self):
        return self.DeleteAllColumns()

    def 删除所有行(self):
        return self.DeleteAllItems()

    @组件_异常检测
    def 删除指定列(self, 列索引):
        return self.DeleteColumn(列索引)

    @组件_异常检测
    def 删除指定行(self, 行索引):
        return self.DeleteItem(行索引)

    @组件_异常检测
    def 开始编辑(self, 行索引):
        '需要设置了 wx.LC_EDIT_LABELS 样式才能使用,开始编辑指定行的第一列'
        return self.EditLabel(行索引)

    @组件_异常检测
    def 启用或禁用交替行背景色(self, 启用=True):
        '启用交替的行背景色（也称为斑马条纹）,该方法只能在虚拟报表模式（即具有LC_REPORT 和LC_VIRTUAL 样式）中为控件调用。'
        return self.EnableAlternateRowColours(启用)

    @组件_异常检测
    def 启用或禁用按键搜索(self, 启用):
        '只匹配第一列，从键盘搜索项目时，如果当前输入的文本不匹配，则启用或禁用蜂鸣声。'
        return self.EnableBellOnNoMatch(启用)

    @组件_异常检测
    def 启用或禁用系统主题样式(self, 启用=True):
        return self.EnableSystemTheme(启用)

    @组件_异常检测
    def 保证显示(self, 行索引):
        return self.EnsureVisible(行索引)

    @组件_异常检测
    def 保证显示2(self, 行索引):
        return self.Focus(行索引)

    @组件_异常检测
    def 查找表项(self, 查找的内容, 开始索引=-1, 模糊查找=False):
        '只查找第一列'
        return self.FindItem(开始索引, 查找的内容, 模糊查找)

    @组件_异常检测
    def 取交替行背景色(self):
        return self.GetAlternateRowColour()

    @组件_异常检测
    def 取列对象(self, 列索引):
        return self.GetColumn(列索引)

    @组件_异常检测
    def 取列标题(self, 列索引):
        return self.GetColumn(列索引).GetText()

    @组件_异常检测
    def 取列对齐方式(self, 列索引):
        "对齐方式：0.左对齐 1.右对齐 2.居中"
        return self.GetColumn(列索引).GetAlign()

    @组件_异常检测
    def 取列宽(self, 列索引):
        return self.GetColumnWidth(列索引)

    @组件_异常检测
    def 取列宽2(self, 列索引):
        return self.GetColumn(列索引).GetWidth()

    def 取列数(self):
        return self.GetColumnCount()

    @组件_异常检测
    def 取可视列索引(self, 索引):
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
    def 取图片组列表(self, 类型):
        '图片组类型：0.普通(大图列表)  1.小图列表  2.自定义列表  返回类型wx.ImageList'
        return self.GetImageList(类型)

    def 取行数(self):
        return self.GetItemCount()

    @组件_异常检测
    def 取行对象(self, 行索引):
        return self.GetItem(行索引)

    @组件_异常检测
    def 取行背景色(self, 行索引):
        return self.GetItemBackgroundColour(行索引)

    @组件_异常检测
    def 取行背景色2(self, 行索引):
        return self.GetItem(行索引).GetBackgroundColour()

    @组件_异常检测
    def 取行字体(self, 行索引):
        return self.GetItemFont(行索引)

    @组件_异常检测
    def 取行坐标(self, 行索引):
        '返回指定行所在的x,y坐标'
        return self.GetItemPosition(行索引)

    @组件_异常检测
    def 取行矩形(self, 行索引):
        '返回指定行的矩形'
        return self.GetItemRect(行索引)

    def 取图标间距(self):
        return self.GetItemSpacing()

    @组件_异常检测
    def 取行状态(self, 行索引, 类型=wx.LIST_STATE_SELECTED):
        '默认返回是否为现行选中项'
        return bool(self.GetItemState(行索引, 类型))

    @组件_异常检测
    def 取标题(self, 行索引, 列索引):
        return self.GetItemText(行索引, 列索引)

    @组件_异常检测
    def 取行文本颜色(self, 行索引):
        '如果项目没有特定的颜色，则返回无效的颜色（而不是控件本身的默认前景色控件，因为这不允许区分与当前控件前景色相同颜色的项目和默认颜色的项目，因此，与控件始终具有相同的颜色）。'
        return self.GetItemTextColour(行索引)

    @组件_异常检测
    def 取下一选中项(self, 当前索引):
        '返回指定行下面的现行选中项 没有就返回-1'
        return self.GetNextSelected(当前索引)

    def 取选中项目数量(self):
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

    def 选择框是否启用(self):
        return self.HasCheckBoxes()

    def 是否带LC_REPORT样式(self):
        '单列或多列报表视图，带有可选标题。'
        return self.InReportView()

    @组件_异常检测
    def 插入列(self, 插入位置, 标题, 对齐方式=2, 宽度=-1):
        """
        在末尾加入新一列
        :param 标题: 自己定
        :param 对齐方式: 0.左对齐  1.右对齐 2.居中
        :param 宽度: 自己定
        :return:加入的列索引
        """
        return self.InsertColumn(插入位置, 标题, 对齐方式, 宽度)

    @组件_异常检测
    def 插入行(self, 插入位置, 标题):
        '只能插入第一个标题'
        return self.InsertItem(插入位置, 标题)

    @组件_异常检测
    def 插入图片(self, 插入位置, 图片索引):
        '与此控件和视图样式关联的图像列表的索引'
        return self.InsertItem(插入位置, 图片索引)

    @组件_异常检测
    def 插入图文(self, 插入位置, 标题, 图片索引):
        '插入图像/字符串项目。'
        return self.InsertItem(插入位置, 标题, 图片索引)

    def 是否无表项(self):
        '具有某些列的控件如果没有行，则仍被认为是空的。'
        return self.IsEmpty()

    @组件_异常检测
    def 是否选中(self, 行索引):
        '判断该行选择框是否勾选'
        return self.IsItemChecked(行索引)

    @组件_异常检测
    def 是否为选择项(self, 索引):
        '返回True是否选择了该项目,不是选中'
        return self.IsSelected(索引)

    def 是否为虚拟报表(self):
        '返回True该控件当前是否在虚拟报表视图中。'
        return self.IsVirtual()

    @组件_异常检测
    def 表项是否可见(self, 行索引):
        '检查项目是否可见。'
        return self.IsVisible(行索引)

    @组件_异常检测
    def 取指定行图片索引(self, 行索引):
        '它应返回控件图像列表中项目图像的索引，如果没有图像，则返回-1'
        return self.OnGetItemImage(行索引)

    @组件_异常检测
    def 是否选中2(self, 行索引):
        '它应该返回是否选中了指定 item 复选框。对于具有 使用复选框的样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemIsChecked(行索引)

    @组件_异常检测
    def 取标题2(self, 行索引, 列索引):
        '它应返回包含 指定 的给定列文本的字符串item。对于具有 样式的控件，必须在派生类中重写 此函数LC_VIRTUAL。'
        return self.OnGetItemText(行索引, 列索引)

    @组件_异常检测
    def 重画指定项目(self, 行索引):
        return self.RefreshItem(行索引)

    @组件_异常检测
    def 重画指定范围项目(self, 起始行, 结束行):
        '正如RefreshItem 这仅对虚拟列表控件有用。起始项必须小于或等于结束项。重绘itemFrom 和itemTo之间的项目。'
        return self.RefreshItems(起始行, 结束行)

    @组件_异常检测
    def 滚动滚动条(self, dx, dy):
        '如果处于图标，小图标或报告查看模式，则dx 指定要滚动的像素数。如果处于列表视图模式，则dx 指定要滚动的列数。dy 始终指定要垂直滚动的像素数。'
        return self.ScrollList(dx, dy)

    @组件_异常检测
    def 选择某项(self, 行索引):
        '选择不是选中'
        return self.Select(行索引)

    @组件_异常检测
    def 置备用行背景色(self, 颜色):
        '将备用行背景色设置为特定颜色。与一样EnableAlternateRowColours，此方法只能与具有LC_REPORT 和LC_VIRTUAL 样式的控件一起使用'
        return self.SetAlternateRowColour(颜色)

    @组件_异常检测
    def 置列标题(self, 列索引, 标题):
        Item = self.GetColumn(列索引)
        Item.SetText(标题)
        return self.SetColumn(列索引, Item)

    @组件_异常检测
    def 置列宽(self, 列索引, 宽度):
        return self.SetColumnWidth(列索引, 宽度)

    @组件_异常检测
    def 置列宽2(self, 列索引, 宽度):
        Item = self.GetColumn(列索引)
        Item.SetWidth(宽度)
        return self.SetColumn(列索引, Item)

    @组件_异常检测
    def 置列对齐方式(self, 列索引, 对齐方式):
        '对齐方式: 0.左对齐  1.右对齐 2.居中'
        Item = self.GetColumn(列索引)
        Item.SetAlign(对齐方式)
        return self.SetColumn(列索引, Item)

    @组件_异常检测
    def 置列图片(self, 列索引, 图片):
        return self.SetColumnImage(列索引, 图片)

    @组件_异常检测
    def 置列排序位置(self, 排序列表):
        '修改列的位置'
        return self.SetColumnsOrder(排序列表)

    @组件_异常检测
    def 置列标题字体颜色(self, attr):
        '更改用于列表控件标题的字体和颜色。'
        return self.SetHeaderAttr(attr)

    @组件_异常检测
    def 置关联图片列表(self, 图片列表):
        return self.SetImageList(图片列表)

    @组件_异常检测
    def 置标题(self, 行索引, 列索引, 标题):
        return self.SetItem(行索引, 列索引, 标题)

    @组件_异常检测
    def 置图文(self, 行索引, 列索引, 标题, 图片索引):
        return self.SetItem(行索引, 列索引, 标题, 图片索引)

    @组件_异常检测
    def 置行色(self, 行索引, 颜色):
        return self.SetItemBackgroundColour(行索引, 颜色)

    @组件_异常检测
    def 置图片(self, 行索引, 列索引, 图片索引):
        return self.SetItemColumnImage(行索引, 列索引, 图片索引)

    @组件_异常检测
    def 置行数(self, 行数):
        '此方法只能与虚拟列表控件一起使用。 没用过'
        return self.SetItemCount(行数)

    @组件_异常检测
    def 置行字体(self, 行索引, 字体):
        return self.SetItemFont(行索引, 字体)

    @组件_异常检测
    def 置选中状态图片(self, 行索引, 选中图索引, 未选中图索引):
        '设置与项目关联的未选择和选择的图像。'
        return self.SetItemImage(行索引, 选中图索引, 未选中图索引)

    @组件_异常检测
    def 置项目坐标(self, 项目索引, x, y):
        '在图标或小图标视图中设置项目的位置。'
        return self.SetItemPosition(项目索引, (x, y))

    @组件_异常检测
    def 置选择状态(self, 行索引, 是否选择):
        状态 = 4 if 是否选择 else 0
        return self.SetItemState(行索引, 状态, wx.LIST_STATE_SELECTED)

    @组件_异常检测
    def 置标题_首列(self, 行索引, 标题):
        return self.SetItemText(行索引, 标题)

    @组件_异常检测
    def 置行文本颜色(self, 行索引, 颜色):
        return self.SetItemTextColour(行索引, 颜色)

    @组件_异常检测
    def 添加列表样式(self, 样式):
        return self.SetSingleStyle(样式, True)

    @组件_异常检测
    def 删除列表样式(self, 样式):
        return self.SetSingleStyle(样式, False)

    @组件_异常检测
    def 置全部文本颜色(self, 颜色):
        return self.SetTextColour(颜色)

    @组件_异常检测
    def 置窗口新样式(self, 样式):
        return self.SetWindowStyleFlag(样式)

    def 获取焦点(self):
        """
AcceptsFocus(self) -> bool
        """

        return super().AcceptsFocus()

    def 获取输入焦点(self):
        """
AcceptsFocusFromKeyboard(self) -> bool
        """

        return super().AcceptsFocusFromKeyboard()

    def 添加(self, entry):
        """

    Append an item to the list control.  The `entry` parameter should be a
    sequence with an item for each column

        """

        return super().Append(entry)

    def 添加列(self, heading, format=None, width=-1):
        """
AppendColumn(heading, format=LIST_FORMAT_LEFT, width=-1) -> long

Adds a new column to the list control in report view mode.
        """

        return super().AppendColumn(heading, format, width)

    def 图标排列方式(self, flag=None):
        """
Arrange(flag=LIST_ALIGN_DEFAULT) -> bool

Arranges the items in icon or small icon view.
在图标或小图标视图中排列项目。

这仅对 Win32 有效。标志 是以下之一：

wx.LIST_ALIGN_DEFAULT：默认对齐方式。

wx.LIST_ALIGN_LEFT：与控件左侧对齐。

wx.LIST_ALIGN_TOP：与控件的顶部对齐。

wx.LIST_ALIGN_SNAP_TO_GRID：对齐网格。
        """

        return super().Arrange(flag)

    def 置图片组(self, imageList, 图片组样式=0):
        """
AssignImageList(imageList, which)

Sets the image list associated with the control and takes ownership of
it (i.e.
        """

        return super().AssignImageList(imageList, 图片组样式)

    def 选择框置选中状态(self, item, check=True):
        """
CheckItem(item, check=True)

Check or uncheck a wxListItem in a control using checkboxes.
        """

        return super().CheckItem(item, check)

    def 清空(self):
        """
ClearAll()

Deletes all items and all columns.
        """

        return super().ClearAll()

    def 删除列图片(self, col):
        """
None
        """

        return super().ClearColumnImage(col)

    def 创建(self, parent, id=None, pos=None, size=None, style=None, validator=None, name=None):
        """
Create(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=LC_ICON, validator=DefaultValidator, name=ListCtrlNameStr) -> bool

Creates the list control.
        """

        return super().Create(parent, id, pos, size, style, validator, name)

    def 删除所有列(self):
        """
DeleteAllColumns() -> bool

Delete all columns in the list control.
        """

        return super().DeleteAllColumns()

    def 删除所有项目(self):
        """
DeleteAllItems() -> bool

Deletes all items in the list control.
        """

        return super().DeleteAllItems()

    def 删除列(self, col):
        """
DeleteColumn(col) -> bool

Deletes a column.
        """

        return super().DeleteColumn(col)

    def 删除项目(self, item):
        """
DeleteItem(item) -> bool

Deletes the specified item.
        """

        return super().DeleteItem(item)

    def 销毁(self):
        """
Destroy(self) -> bool
        """

        return super().Destroy()

    def 编辑项目标签(self, item):
        """
EditLabel(item) -> TextCtrl

Starts editing the label of the given item.
        """

        return super().EditLabel(item)

    def 启用行交替颜色(self, enable=True):
        """
EnableAlternateRowColours(enable=True)

Enable alternating row background colours (also called zebra
striping).
        """

        return super().EnableAlternateRowColours(enable)

    def 启用输入匹配(self, on=True):
        """
EnableBellOnNoMatch(on=True)

Enable or disable a beep if there is no match for the currently
entered text when searching for the item from keyboard.
        """

        return super().EnableBellOnNoMatch(on)

    def 启用选择框(self, enable=True):
        """
EnableCheckBoxes(enable=True) -> bool

Enable or disable checkboxes for list items.
        """

        return super().EnableCheckBoxes(enable)

    def 启用系统主题(self, enable=True):
        """
EnableSystemTheme(enable=True)

Can be used to disable the system theme of controls using it by
default.
        """

        return super().EnableSystemTheme(enable)

    def 启用获得焦点(self, enabled):
        """
EnableVisibleFocus(self, enabled: bool)
        """

        return super().EnableVisibleFocus(enabled)

    def 保证显示(self, item):
        """
EnsureVisible(item) -> bool

Ensures this item is visible.
        """

        return super().EnsureVisible(item)

    def 设置扩展规则和颜色(self, extend=True):
        """
ExtendRulesAndAlternateColour(extend=True)

Extend rules and alternate rows background to the entire client area.
        """

        return super().ExtendRulesAndAlternateColour(extend)

    def 查找项目(self, start, *args, **kw):
        """
FindItem(start, str, partial=False) -> long
FindItem(start, data) -> long
FindItem(start, pt, direction) -> long

Find an item whose label matches this string, starting from start or
the beginning if start is -1.


        """

        return super().FindItem(start, *args, **kw)

    def 查找项目位置(*args, **kw):
        """
FindItem(start, str, partial=False) -> long
FindItem(start, data) -> long
FindItem(start, pt, direction) -> long

Find an item whose label matches this string, starting from start or
the beginning if start is -1.


        """

        return super().FindItemAtPos(*args, **kw)

    def 查找项目数据(*args, **kw):
        """
FindItem(start, str, partial=False) -> long
FindItem(start, data) -> long
FindItem(start, pt, direction) -> long

Find an item whose label matches this string, starting from start or
the beginning if start is -1.


        """

        return super().FindItemData(*args, **kw)

    def 置项目焦点(self, idx):
        """

    Focus and show the given item.

        """

        return super().Focus(idx)

    def 取列(self, col):
        """
GetColumn(col) -> ListItem

Gets information about this column. See SetItem() for more
information.
        """

        return super().GetColumn(col)

    def 取列数量(self):
        """
GetColumnCount() -> int

Returns the number of columns.
        """

        return super().GetColumnCount()

    def 取列索引从视觉顺序(self, pos):
        """
GetColumnIndexFromOrder(pos) -> int

Gets the column index from its position in visual order.
        """

        return super().GetColumnIndexFromOrder(pos)

    def 取列视觉顺序(self, col):
        """
GetColumnOrder(col) -> int

Gets the column visual order position.
        """

        return super().GetColumnOrder(col)

    def 取所有列顺序(self):
        """
GetColumnsOrder() -> ArrayInt

Returns the array containing the orders of all columns.
        """

        return super().GetColumnsOrder()

    def 取列宽(self, col):
        """
GetColumnWidth(col) -> int

Gets the column width (report view only).
        """

        return super().GetColumnWidth(col)

    def 取列表页数量(self):
        """
GetCountPerPage() -> int

Gets the number of items that can fit vertically in the visible area
of the list control (list or report view) or the total number of items
in the list control (icon or small icon view).
        """

        return super().GetCountPerPage()

    def 取当前编辑的标签(self):
        """
GetEditControl() -> TextCtrl

Returns the edit control being currently used to edit a label.
        """

        return super().GetEditControl()

    def 取选中项目中第一个(self, *args):
        """

    Returns the first selected item, or -1 when none is selected.

        """

        return super().GetFirstSelected(*args)

    def 置项目焦点(self):
        """

    Gets the currently focused item or -1 if none is focused.

        """

        return super().GetFocusedItem()

    def 取图片组(self, which):
        """
GetImageList(which) -> ImageList

Returns the specified image list.
        """

        return super().GetImageList(which)

    def 取项目(self, itemIdx, col=0):
        """
GetItem(itemIdx, col=0) -> ListItem

Gets information about the item. See SetItem() for more information.
        """

        return super().GetItem(itemIdx, col)

    def 取项目数量(self):
        """
GetItemCount() -> int

Returns the number of items in the list control.
        """

        return super().GetItemCount()

    def 取项目数据(self, item):
        """
GetItemData(item) -> long

Gets the application-defined data associated with this item.
        """

        return super().GetItemData(item)

    def 取项目字体(self, item):
        """
GetItemFont(item) -> Font

Returns the item's font.
        """

        return super().GetItemFont(item)

    def 取项目位置(self, item):
        """
GetItemPosition(item) -> Point

Returns the position of the item, in icon or small icon view.
        """

        return super().GetItemPosition(item)

    def 取项目矩形(self, item, code=None):
        """
GetItemRect(item, code=LIST_RECT_BOUNDS) -> Rect

Returns the rectangle representing the item's size and position, in
physical coordinates.
code is one of wx.LIST_RECT_BOUNDS, wx.LIST_RECT_ICON,
wx.LIST_RECT_LABEL.
        """

        return super().GetItemRect(item, code)

    def 取项目间距(self):
        """
GetItemSpacing() -> Size

Retrieves the spacing between icons in pixels: horizontal spacing is
returned as x component of the wxSize object and the vertical spacing
as its y component.
        """

        return super().GetItemSpacing()

    def 取项目状态(self, item, stateMask):
        """
GetItemState(item, stateMask) -> int

Gets the item state.
        """

        return super().GetItemState(item, stateMask)

    def 取项目文本(self, item, col=0):
        """
GetItemText(item, col=0) -> String

Gets the item text for this item.
        """

        return super().GetItemText(item, col)

    def 取单元格文本(self, 行索引, 列索引=0):
        """
GetItemText(item, col=0) -> String

Gets the item text for this item.
        """

        return super().GetItemText(行索引, 列索引)

    def 取项目文本颜色(self, item):
        """
GetItemTextColour(item) -> Colour

Returns the colour for this item.
        """

        return super().GetItemTextColour(item)

    def 取下一个项目(self, item, geometry=None, state=None):
        """
GetNextItem(item, geometry=LIST_NEXT_ALL, state=LIST_STATE_DONTCARE) -> long

Searches for an item with the given geometry or state, starting from
item but excluding the item itself.
        """

        return super().GetNextItem(item, geometry, state)

    def 取当前选择项目的下一个(self, item):
        """

    Returns subsequent selected items, or -1 when no more are selected.

        """

        return super().GetNextSelected(item)

    def 取选中项目数量(self):
        """
GetSelectedItemCount() -> int

Returns the number of selected items in the list control.
        """

        return super().GetSelectedItemCount()

    def 取子项目矩形(self, item, subItem, rect, code=None):
        """
GetSubItemRect(item, subItem, rect, code=LIST_RECT_BOUNDS) -> bool

Returns the rectangle representing the size and position, in physical
coordinates, of the given subitem, i.e.
        """

        return super().GetSubItemRect(item, subItem, rect, code)

    def 取头部项目(self):
        """
GetTopItem() -> long

Gets the index of the topmost visible item when in list or report
view.
        """

        return super().GetTopItem()

    def 取视图矩形(self):
        """
GetViewRect() -> Rect

Returns the rectangle taken by all items in the control.
        """

        return super().GetViewRect()

    def 是否有复选框(self):
        """
HasCheckBoxes() -> bool

Returns true if checkboxes are enabled for list items.
        """

        return super().HasCheckBoxes()

    def 是否为报表列表框样式(self):
        """
InReportView() -> bool

Returns true if the control is currently using wxLC_REPORT style.
        """

        return super().InReportView()

    def 插入列(self, col, *args, **kw):
        """
InsertColumn(col, info) -> long
InsertColumn(col, heading, format=LIST_FORMAT_LEFT, width=LIST_AUTOSIZE) -> long

For report view mode (only), inserts a column.

        """

        return super().InsertColumn(col, *args, **kw)

    def 插入图片项目(*args, **kw):
        """
InsertItem(info) -> long
InsertItem(index, label) -> long
InsertItem(index, imageIndex) -> long
InsertItem(index, label, imageIndex) -> long

Inserts an item, returning the index of the new item if successful, -1
otherwise.



        """

        return super().InsertImageItem(*args, **kw)

    def 插入图片文本项目(*args, **kw):
        """
InsertItem(info) -> long
InsertItem(index, label) -> long
InsertItem(index, imageIndex) -> long
InsertItem(index, label, imageIndex) -> long

Inserts an item, returning the index of the new item if successful, -1
otherwise.



        """

        return super().InsertImageStringItem(*args, **kw)

    def 插入项目(self, *args, **kw):
        """
InsertItem(info) -> long
InsertItem(index, label) -> long
InsertItem(index, imageIndex) -> long
InsertItem(index, label, imageIndex) -> long

Inserts an item, returning the index of the new item if successful, -1
otherwise.



        """

        return super().InsertItem(*args, **kw)

    def 插入文本项目(*args, **kw):
        """
InsertItem(info) -> long
InsertItem(index, label) -> long
InsertItem(index, imageIndex) -> long
InsertItem(index, label, imageIndex) -> long

Inserts an item, returning the index of the new item if successful, -1
otherwise.



        """

        return super().InsertStringItem(*args, **kw)

    def 选择框取选中状态(self, item):
        """
IsItemChecked(item) -> bool

Return true if the checkbox for the given wxListItem is checked.
        """

        return super().IsItemChecked(item)

    def 是否被选中(self, idx):
        """

    Returns ``True`` if the item is selected.

        """

        return super().IsSelected(idx)

    def 项目是否可见(self, item):
        """
IsVisible(item) -> bool

Check if the item is visible.
        """

        return super().IsVisible(item)

    def 刷新项目(self, item):
        """
RefreshItem(item)

Redraws the given item.
        """

        return super().RefreshItem(item)

    def 刷新多个项目(self, itemFrom, itemTo):
        """
RefreshItems(itemFrom, itemTo)

Redraws the items between itemFrom and itemTo.
        """

        return super().RefreshItems(itemFrom, itemTo)

    def 滚动条(self, dx, dy):
        """
ScrollList(dx, dy) -> bool

Scrolls the list control.
        """

        return super().ScrollList(dx, dy)

    def 选择项目(self, idx, on=1):
        """

    Selects/deselects an item.

        """

        return super().Select(idx, on)

    def 选择(self, idx):
        return super().Select(idx, 1)

    def 取消选择(self, idx):
        return super().Select(idx, 0)

    def 设置行交替颜色(self, colour):
        """
SetAlternateRowColour(colour)

Set the alternative row background colour to a specific colour.
        """

        return super().SetAlternateRowColour(colour)

    def 设置背景颜色(self, col):
        """
SetBackgroundColour(col) -> bool

Sets the background colour.
        """

        return super().SetBackgroundColour(col)

    def 设置可以获取焦点(self, canFocus):
        """
SetCanFocus(self, canFocus: bool)
        """

        return super().SetCanFocus(canFocus)

    def 设置列(self, col, item):
        """
SetColumn(col, item) -> bool

Sets information about this column.
        """

        return super().SetColumn(col, item)

    def 设置列图片(self, col, image):
        """
None
        """

        return super().SetColumnImage(col, image)

    def 设置列顺序(self, orders):
        """
SetColumnsOrder(orders) -> bool

Changes the order in which the columns are shown.
        """

        return super().SetColumnsOrder(orders)

    def 设置列宽(self, col, width):
        """
SetColumnWidth(col, width) -> bool

Sets the column width.
        """

        return super().SetColumnWidth(col, width)

    def 设置图片列表(self, imageList, which):
        """
SetImageList(imageList, which)

Sets the image list associated with the control.
        """

        return super().SetImageList(imageList, which)

    def 设置项目(self, *args, **kw):
        """
SetItem(info) -> bool
SetItem(index, column, label, imageId=-1) -> bool

Sets the data of an item.

        """

        return super().SetItem(*args, **kw)

    def 置单元格文本(self, 行索引, 列索引, 文本内容, 图片索引=-1):
        """
SetItem(info) -> bool
SetItem(index, column, label, imageId=-1) -> bool

Sets the data of an item.

        """

        return super().SetItem(index=行索引, column=列索引, label=文本内容, imageId=图片索引)


    def 设置项目背景颜色(self, item, 颜色值=(240, 240, 240)):
        """
SetItemBackgroundColour(item, col)

Sets the background colour for this item.
        """

        return super().SetItemBackgroundColour(item, 颜色值)

    def 设置项目列图片(self, item, column, image):
        """
SetItemColumnImage(item, column, image) -> bool

Sets the image associated with the item.
        """

        return super().SetItemColumnImage(item, column, image)

    def 设置项目数量(self, count):
        """
SetItemCount(count)

This method can only be used with virtual list controls.
        """

        return super().SetItemCount(count)

    def 设置项目数据(self, item, data):
        """
SetItemData(item, data) -> bool

Associates application-defined data with this item.
        """

        return super().SetItemData(item, data)

    def 设置项目字体(self, item, font):
        """
SetItemFont(item, font)

Sets the item's font.
        """

        return super().SetItemFont(item, font)

    def 设置项目图片(self, item, image, selImage=-1):
        """
SetItemImage(item, image, selImage=-1) -> bool

Sets the unselected and selected images associated with the item.
        """

        return super().SetItemImage(item, image, selImage)

    def 设置项目位置(self, item, pos):
        """
SetItemPosition(item, pos) -> bool

Sets the position of the item, in icon or small icon view.
        """

        return super().SetItemPosition(item, pos)

    def 设置项目状态(self, item, state, stateMask):
        """
SetItemState(item, state, stateMask) -> bool

Sets the item state.
        """

        return super().SetItemState(item, state, stateMask)

    def 设置项目文本(self, item, text):
        """
SetItemText(item, text)

Sets the item text for this item.
        """

        return super().SetItemText(item, text)

    def 设置项目文本颜色(self, item, 颜色值=(0, 0, 255)):
        """
SetItemTextColour(item, col)

Sets the colour for this item.
        """

        return super().SetItemTextColour(item, 颜色值)

    def 设置文本项目(*args, **kw):
        """
SetItem(info) -> bool
SetItem(index, column, label, imageId=-1) -> bool

Sets the data of an item.

        """

        return super().SetStringItem(*args, **kw)

    def 设置文本颜色(self, col):
        """
SetTextColour(col)

Sets the text colour of the list control.
        """

        return super().SetTextColour(col)

    def 项目排序(self, fnSortCallBack):
        """
SortItems(fnSortCallBack) -> bool

Call this function to sort the items in the list control.
        """

        return super().SortItems(fnSortCallBack)

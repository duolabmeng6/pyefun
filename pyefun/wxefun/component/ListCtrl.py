import wx.adv
import wx
from .wxControl import *


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

"""
编辑框

https://wxpython.org/Phoenix/docs/html/wx.TextCtrl.html
"""
import wx
from .wxControl import *


class 编辑框(wx.TextCtrl, 公用方法):
    pass

    @property
    def 内容(self):
        return self.取内容()

    @内容.setter
    def 内容(self, value):
        self.置内容(value)

    _最大允许长度 = None
    @property
    def 最大允许长度(self):
        return self._最大允许长度

    @最大允许长度.setter
    def 最大允许长度(self, value):
        self._最大允许长度 = value
        self.SetMaxLength(value)

    def 置内容(self, 内容):
        self.SetValue(内容)

    def 取新文本样式(self):
        '返回当前用于新文本的样式。'
        return self.GetDefaultStyle()

    @组件_异常检测
    def 取指定行长度(self, 行号):
        '获取指定行的长度，不包括任何尾随换行符。'
        return self.GetLineLength(行号)

    @组件_异常检测
    def 取指定行内容(self, 行号):
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
    def 载入指定文件内容(self, 路径):
        '从指定文件加载内容到编辑框'
        return self.LoadFile(路径)

    @组件_异常检测
    def 内容写到指定文件(self, 路径):
        '将编辑框的内容写到指定文件内'
        return self.SaveFile(路径)

    def 标记为已修改2(self):
        '将文本标记为已修改'
        return self.MarkDirty()

    @组件_异常检测
    def 指定位置转像素位置(self, 位置):
        '取指定位置处的文本的像素坐标'
        return self.PositionToCoords(位置)

    @组件_异常检测
    def 指定位置转行列位置(self, 位置):
        '取指定位置处的文本所在行跟列,返回一个元组,(是否存在,行,列)'
        return self.PositionToXY(位置)

    @组件_异常检测
    def 置新文本样式(self, 样式):
        '更改要用于要添加到控件的新文本的默认样式。'
        return self.SetDefaultStyle(样式)

    @组件_异常检测
    def 置修改状态(self, 修改=True):
        '将控件标记为是否被用户修改'
        return self.SetModified(修改)

    def 标记为已修改(self):
        '将控件标记为已被用户修改'
        return self.SetModified(True)

    def 标记为未修改(self):
        '将控件标记为未被用户修改'
        return self.SetModified(False)

    @组件_异常检测
    def 置指定范围样式(self, 开始位置, 结束位置, 样式):
        return self.SetStyle(开始位置, 结束位置, 样式)

    @组件_异常检测
    def 置指定位置可见(self, 位置):
        '使指定位置的字符显示在编辑框可见范围内'
        return self.ShowPosition(位置)

    @组件_异常检测
    def 指定行列转位置(self, 行, 列):
        '将给定的从零开始的列和行号转换为位置'
        return self.XYToPosition(行, 列)

    @组件_异常检测
    def 加入文本(self, 内容):
        return self.write(内容)

    def 清空内容(self):
        self.Clear()

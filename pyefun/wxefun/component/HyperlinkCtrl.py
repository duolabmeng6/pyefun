import wx
import wx.lib.agw.hyperlink
import wx.adv
from .wxControl import *


class 超级链接框(wx.adv.HyperlinkCtrl, 公用方法):
    pass

    @property
    def 链接地址(self):
        return self.GetURL()

    @链接地址.setter
    def 链接地址(self, url):
        self.SetURL(url)

    @property
    def 焦点颜色(self):
        return self.GetHoverColour()

    @焦点颜色.setter
    def 焦点颜色(self, value):
        self.SetHoverColour(value)

    @property
    def 未访问颜色(self):
        return self.GetNormalColour()

    @未访问颜色.setter
    def 未访问颜色(self, value):
        self.SetNormalColour(value)

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
    def 置焦点颜色(self, 颜色):
        '设置鼠标悬停在控件上时用于打印超链接标签的颜色。'
        return self.SetHoverColour(颜色)

    @组件_异常检测
    def 置初始颜色(self, 颜色):
        '设置以前从未单击过链接（即未访问链接）并且鼠标不在控件上时用于打印标签的颜色。'
        return self.SetNormalColour(颜色)

    @组件_异常检测
    def 置URL(self, url):
        '设置与超链接关联的URL。'
        return self.SetURL(url)

    @组件_异常检测
    def 置访问状态(self, 已访问=True):
        '将超链接标记为已访问/未访问'
        return self.SetVisited(已访问)

    @组件_异常检测
    def 置已点击颜色(self, 颜色):
        return self.SetVisitedColour(颜色)


class 超级链接框L(wx.lib.agw.hyperlink.HyperLinkCtrl, 公用方法):
    pass

    @组件_异常检测
    def 允许打开链接(self, 打开=True):
        '单击后自动浏览到URL。'
        return self.AutoBrowse(True)

    @组件_异常检测
    def 弹出错误提示(self, 提示内容):
        return self.DisplayError(提示内容)

    @组件_异常检测
    def 允许右键弹出菜单(self, 弹出=True):
        return self.DoPopup(弹出)

    @组件_异常检测
    def 允许翻转(self, 允许=False):
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
    def 打开指定链接(self, 链接):
        return self.GotoURL(链接)

    @组件_异常检测
    def 置标题字体粗细(self, 粗体=True):
        return self.SetBold(粗体)

    @组件_异常检测
    def 置各状态标题颜色(self, 默认, 访问后, 焦点):
        '设置链接，访问的链接和鼠标悬停的颜色。'
        return self.SetColours(默认, 访问后, 焦点)

    @组件_异常检测
    def 置默认标题颜色(self, 颜色):
        return self.SetColours(颜色, None, None)

    @组件_异常检测
    def 置访问后标题颜色(self, 颜色):
        return self.SetColours(None, 颜色, None)

    @组件_异常检测
    def 置焦点标题颜色(self, 颜色):
        return self.SetColours(None, None, 颜色)

    @组件_异常检测
    def 置各状态标题下划线(self, 默认=False, 已访问=False, 焦点=False):
        '设置是否应为新链接，访问的链接和过渡文本加下划线。'
        return self.SetUnderlines(默认, 已访问, 焦点)

    @组件_异常检测
    def 置默认标题下划线(self, 下划线=True):
        return self.SetUnderlines(下划线, None, None)

    @组件_异常检测
    def 置访问猴标题下划线(self, 下划线=True):
        return self.SetUnderlines(None, 下划线, None)

    @组件_异常检测
    def 置焦点标题下划线(self, 下划线=True):
        return self.SetUnderlines(None, None, 下划线)

    @组件_异常检测
    def 置URL(self, url):
        return self.SetURL(url)

    @组件_异常检测
    def 置访问状态(self, 状态=True):
        '设置链接访问状态是否已访问郭'
        return self.SetVisited(状态)

    @组件_异常检测
    def 更新链接(self, 刷新控件=True):
        self.UpdateLink(刷新控件)

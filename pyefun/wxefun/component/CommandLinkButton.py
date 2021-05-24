import wx.adv
import wx
from .wxControl import *

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

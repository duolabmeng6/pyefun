"""
工具条

[
  {
    "名称": "文件",
    "子菜单": [
      {
        "名称": "新建",
        "图标": "C:/pyefun/wxview/images/工具条/新建.png",
        "绑定事件": "菜单_新建_被点击"
      },
      {
        "名称": "打开",
        "图标": "C:/pyefun/wxview/images/工具条/打开.png"
      },
      {
        "名称": "关闭",
        "图标": "C:/pyefun/wxview/images/工具条/关闭.png"
      },
      {
        "名称": "退出\tCtrl+S",
        "图标": "C:/pyefun/wxview/images/工具条/保存.png"
      },
      {
        "名称": "另存为",
        "图标": "C:/pyefun/wxview/images/工具条/另存为.png",
        "隐藏": true
      },
      {
        "名称": "自动保存2",
        "选中": false,
        "类型": "单选框"
      },
      {
        "名称": "自动保存1",
        "选中": true,
        "类型": "单选框"
      },
      {
        "名称": "自动保存",
        "选中": true,
        "类型": "选择框"
      },
      {
        "名称": "退出\tCtrl+Q",
        "id": "wx.ID_EDIT",
        "图标": "C:/pyefun/wxview/images/工具条/关闭.png",
        "绑定事件": "菜单_退出_被点击",
        "帮助文本": "退出系统"
      }
    ]
  },
  {
    "名称": "其他",
    "子菜单": [
      {
        "名称": "其他",
        "子菜单": [
          {
            "名称": "其他11"
          },
          {
            "名称": "其他22"
          },
          {
            "名称": "其他33"
          },
          {
            "名称": "其他44"
          }
        ]
      },
      {
        "名称": "其他2"
      },
      {
        "名称": "其他3"
      },
      {
        "名称": "其他4"
      }
    ]
  }
]


"""

import wx
import json
import pyefun as efun
from .wxControl import *

ID_START = 2000


def _getMenuId():
    global ID_START
    ID_START += 1
    return ID_START


class 工具条(wx.ToolBar, 公用方法):
    pass

    def 设置图标大小(self, 宽度, 高度):
        self.SetToolBitmapSize((宽度, 高度))

    def 设置边距(self, 左边距, 上边距):
        self.SetMargins(x=左边距, y=上边距)

    def 设置间距(self, 间距=1):
        """如果工具栏是水平的，则用于垂直方向的间距，如果工具栏是垂直的，则用于水平方向的间距。"""
        self.SetToolPacking(间距)

    def 设置分割线大小(self, 间隔=5):
        self.SetToolSeparation(间隔)

    def 取工具对象(self, id):
        return self.FindById(id)

    def 取帮助文本(self, toolId):
        """传入对象或者传入工具按钮的id都可以"""
        if type(toolId) == int:
            return self.GetToolShortHelp(toolId)
        else:
            return self.GetToolShortHelp(toolId.GetId())

    def 取工具名称(self, item对象):
        return item对象.GetLabel()

    def 刷新显示(self):
        self.Realize()

    def 从工具条数据中创建(self, 工具条数据, 图标宽度=32, 图标高度=32):
        toolJson = json.loads(工具条数据)
        for 第一层的值 in toolJson:
            id = 第一层的值.get("id")
            名称 = 第一层的值.get("名称")
            图标 = 第一层的值.get("图标")
            帮助文本 = 第一层的值.get("帮助文本")
            if 名称 == "-":
                self.AddSeparator()
                continue

            if 帮助文本 is None:
                帮助文本 = 名称

            if id is None:
                id = _getMenuId()
            else:
                id = eval(id)
            if 图标 is not None:
                图标 = efun.子文本替换(图标, "./", efun.取运行目录() + "/")
                图标 = efun.路径优化(图标)
                if efun.文件是否存在(图标):
                    image = wx.Image(图标).Scale(图标宽度, 图标高度).ConvertToBitmap()
                    self.AddTool(id, 名称, image, shortHelp=帮助文本)
                else:
                    print("工具条图标文件不存在无法创建[{}]文件路径[{}]".format(名称, 图标, ))

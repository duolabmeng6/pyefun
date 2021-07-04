"""
菜单栏

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

    菜单数据 = 读入文本("C:\pyefun\wxview\menu.json")
    菜单栏 = wx.菜单栏()
    菜单栏.从菜单数据中创建(菜单数据, self)
    self.置菜单栏(菜单栏)


"""
import wx
from .wxControl import *
import pyefun as efun
import json

ID_START = 1000


def _getMenuId():
    global ID_START
    ID_START += 1
    return ID_START


class 菜单栏(wx.MenuBar, 公用方法):
    pass

    def 从菜单数据中创建(self, 创建菜单的json数据, winframe=wx.Frame):
        menuJson = json.loads(创建菜单的json数据)
        menuBar = self
        for 第一层的值 in menuJson:
            print(第一层的值.get("名称"))
            print(第一层的值.get("子菜单"))
            menu = menuBar.创建多级菜单(第一层的值.get("子菜单"), winframe)
            menuBar.Append(menu, 第一层的值.get("名称"))

    def 创建多级菜单(self, 创建菜单的json数据, winframe=wx.Frame):
        menu = wx.Menu()
        for 菜单值 in 创建菜单的json数据:
            k = 菜单值.get("名称")
            v = 菜单值.get("子菜单")
            图标 = 菜单值.get("图标")
            禁用 = 菜单值.get("禁用")
            隐藏 = 菜单值.get("隐藏")
            id = 菜单值.get("id")
            绑定事件 = 菜单值.get("绑定事件")
            选中 = 菜单值.get("选中")
            类型 = 菜单值.get("类型")
            帮助文本 = 菜单值.get("帮助文本")
            print(菜单值.get("名称"))
            print(菜单值.get("子菜单"))
            # 分隔符
            if k == '-':
                menu.AppendSeparator()
                continue
            # 子菜单
            if type(v) is list:
                submenu = self.创建多级菜单(v, winframe)
                menu.AppendSubMenu(submenu, k)
                return menu

            # 创建一个菜单的过程
            if id is None:
                id = _getMenuId()
            else:
                try:
                    if (type(id) == str):
                        id = eval(id)
                except:
                    print("建立菜单[{}]失败,无法获取菜单id[{}]".format(k, id))
                    id = _getMenuId()

            kind = wx.ITEM_NORMAL
            if 类型 is not None:
                if 类型 == "单选框":
                    kind = wx.ITEM_RADIO
                if 类型 == "选择框":
                    kind = wx.ITEM_CHECK

            if 帮助文本 is None:
                帮助文本 = ""

            item = wx.MenuItem(menu, id, k, 帮助文本, kind)

            if 图标 is not None and 图标 != "":
                图标 = efun.子文本替换(图标, "./", efun.取运行目录() + "/")
                图标 = efun.路径优化(图标)
                if efun.文件是否存在(图标):
                    item.SetBitmap(wx.Image(图标).Scale(16, 16).ConvertToBitmap())
            if 禁用 is True:
                item.Enable(False)
            if 隐藏 is True:
                continue
            if 绑定事件 is not None:
                try:
                    fc = "winframe.{}".format(绑定事件)
                    winframe.Bind(wx.EVT_MENU, eval(fc), item)
                except:
                    print("未定义菜单被点击事件[{}]函数  菜单名[{}]".format(fc, k))
            menu.Append(item)
            if 选中 is not None:
                item.Check(选中)
        return menu

"""
用于将一个类的代码复制下来 方便将代码进行汉化

"""
import pyefun as efun
from pyefun.正则表达式 import *  # 正则表达式
from pyefun.剪切板操作 import *  # 正则表达式
import wx

print(wx.ImageList.__init__.__doc__)
#
# 命令 = "文档 = wx.ImageList.__init__.__doc__"
# okok = locals()
# exec(命令,okok)
# print(okok['文档'])
#
# exit()

source = efun.读入文本(
    r"C:\Users\\AppData\Local\JetBrains\PyCharm2021.1\python_stubs\-1544258003\wx\_core\ListCtrl.py")
str = ""
for v in 正则表达式(r"def (.*?):", 正则.多行模式 | 正则.忽略大小写).搜索(source):
    # print(v)
    参数 = v
    参数 = efun.子文本替换(参数, "self, ", "")
    test = 正则表达式(r"[ \(]([A-Za-z].*?)[=\)]", 正则.多行模式 | 正则.忽略大小写).搜索(参数)
    if len(test) == 0:
        test = [efun.strCut(参数, "($)")]
    if test[0] == 'self':
        test = False

    # print(test)
    # print(参数)
    函数名字 = efun.strCut(v, "$(")
    if test == False:
        参数 = 函数名字 + "()"
    else:
        参数 = 函数名字 + "(" + ", ".join(test) + ")"
    # 参数 = efun.子文本替换(参数,"*","")

    文档 = ""
    try:
        命令 = "文档 = wx.ListCtrl.{参数}.__doc__".format(参数=函数名字)
        okok = locals()
        exec(命令, okok)
        文档 = okok['文档']

        # print(命令,文档)
    except:
        pass
        print("没文档", 命令)

    v = efun.子文本替换(v, "*__args", "*args, **kw")
    参数 = efun.子文本替换(参数, "*__args", "*args, **kw")
    if efun.判断文本(v, "__init__"):
        continue

    if 文档 != "":
        文档 = """\"\"\"
{0}
        \"\"\"
""".format(文档)

    str = str + """
    def ____{0}:
        {2}
        return super().{1}
            
    """.format(v, 参数, 文档)

print(str)
置剪辑板文本(str)

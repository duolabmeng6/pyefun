"""
用于将一个类的代码复制下来 方便将代码进行汉化

"""
import pyefun as efun
from pyefun.regexpUtil import *  # 正则表达式
from pyefun.clipBoard import *  # 正则表达式

source = efun.读入文本(
    r"wx\_core\ListCtrl.py")
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

    v = efun.子文本替换(v, "*__args", "*args, **kw")
    参数 = efun.子文本替换(参数, "*__args", "*args, **kw")
    if efun.判断文本(v,"__init__"):
        continue

    str = str + """
    def ____{0}:
        return super().{1}
            
    """.format(v, 参数)

print(str)
置剪辑板文本(str)

# 系统处理
import time
import os
import pyperclip
from win32api import GetSystemMetrics
# import pyautogui
from ubelt.util_format import *
import ubelt as ub


def 调试输出(obj):
    # data = repr2(obj, nl=2, precision=2)
    data = repr2(obj)
    print(data)


class 进度显示(ub.ProgIter):
    def __init__(self, 迭代对象=None,
                 描述="",
                 总数=None,
                 信息级别=3,
                 显示速率=False,
                 显示时间=False,
                 起始索引=0,
                 进度大小=None,
                 启用=True,
                 输出在同一行=True
                 ):
        "显示 0 不显示 1结束显示 2概率显示 3全部显示"
        # ProgIter(iterable=迭代对象,total=总数, desc=描述, show_times=False, verbose=显示)
        super().__init__(iterable=迭代对象,
                         total=总数,
                         desc=描述,
                         show_times=显示速率,
                         show_wall=显示时间,
                         verbose=信息级别,
                         initial=起始索引,
                         chunksize=进度大小,
                         enabled=启用,
                         clearline=输出在同一行
                         )


    def 下一步(self, 步数=1, 强制显示=False):
        self.step(inc=步数, force=强制显示)

    def 完成(self, 步数=1, 强制显示=False):
        self.end()

    def 开始(self):
        self.begin()

    def 取进度(self):
        data = self.format_message()
        return data

    def 换行(self):
        self.ensure_newline()

    def 输出(self, obj):
        self.ensure_newline()
        print(obj)

    def 附加输出(self, obj):
        self.set_extra(obj)


# 运行
# 打开内存文件
# 取剪辑板文本
# 置剪辑板文本
# 剪辑板中可有文本
# 清除剪辑板
# 取屏幕宽度
# 取屏幕高度
# 取鼠标水平位置
# 取鼠标垂直位置
# 取颜色数
# 输入框
# 信息框
# 取文本注册项
# 取数值注册项
# 取字节集注册
# 写注册项
# 删除注册项
# 注册项是否存在
# 取默认底色
# 快照
# 读配置项
# 写配置项
# 取配置节名
# 取操作系统类别
# 多文件对话框

def 延时(秒: int):
    time.sleep(秒)


def 运行(cmd):
    p = os.popen(cmd)
    x = p.read()
    p.close()
    return x


def 取剪辑板文本() -> str:
    return pyperclip.paste()


def 置剪辑板文本(str):
    pyperclip.copy(str)


def 剪辑板中可有文本() -> bool:
    return 取剪辑板文本() != ""


def 清除剪辑板():
    pyperclip.copy("")


def 取屏幕宽度():
    return GetSystemMetrics(0)


def 取屏幕高度():
    return GetSystemMetrics(1)


# 取鼠标水平位置
# 取鼠标垂直位置
def 取鼠标位置():
    return pyautogui.position()

# -*- coding:utf-8 -*-
from win32api import GetSystemMetrics
import win32gui,win32con,win32api,os,re,subprocess
import win32clipboard as w
from .public import *

#字母键
按键_A,按键_B,按键_C,按键_D,按键_E,按键_F,按键_G,按键_H,按键_I,按键_J,按键_K,按键_L,按键_M,按键_N,按键_O,按键_P,按键_Q,按键_R,按键_S,按键_T,按键_U,按键_V,按键_W,按键_X,按键_Y,按键_Z = 65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90
#字母上的数字键(左边)
按键_0_,按键_1_,按键_2_,按键_3_,按键_4_,按键_5_,按键_6_,按键_7_,按键_8_,按键_9_ = 48,49,50,51,52,53,54,55,56,57
#数字键(右边)
按键_0,按键_1,按键_2,按键_3,按键_4,按键_5,按键_6,按键_7,按键_8,按键_9 = 96,97,98,99,100,101,102,103,104,105
#功能键
按键_F1,按键_F2,按键_F3,按键_F4,按键_F5,按键_F6,按键_F7,按键_F8,按键_F9,按键_F10,按键_F11,按键_F12=112,113,114,115,116,117,118,119,120,121,122,123
#其它键
按键_乘,按键_加,按键_小回车,按键_减,按键_点,按键_除 = 106,107,108,109,110,111
按键_退格,按键_TAB,按键_清除键,按键_回车,按键_SHIFT,按键_CONTROL,按键_ALT,按键_大小写键,按键_ESC,按键_空格,按键_PAGE_UP,按键_PAGE_DOWN,按键_END,按键_HOME,按键_向左,按键_向右=8,9,12,13,16,17,18,20,27,32,33,34,35,36,37,38
按键_向右,按键_向下,按键_INS,按键_DEL,按键_NUM,按键_冒号键,按键_等号键,按键_逗号键,按键_下划线键,按键_句号键,按键_问号键,按键_波浪键,按键_左括号,按键_斜杠键,按键_右括号,按键_引号键=39,40,45,46,144,186,187,188,189,190,191,192,219,220,221,222
按键_音量加,按键_音量减,按键_停止,按键_静音,按键_浏览器,按键_邮件,按键_搜索,按键_搜餐 = 175,174,179,173,172,180,170,171
按键_WIN = 91

@异常处理返回类型逻辑型
def 窗口_置父窗口(子窗口句柄,父窗口句柄):
    '将子窗口嵌入父窗口内'
    return win32gui.SetParent(子窗口句柄, 父窗口句柄)


@异常处理返回类型逻辑型
def 鼠标_移动(x,y):
    '在桌面上移动鼠标位置'
    win32api.SetCursorPos((x, y))


@异常处理返回类型逻辑型
def 鼠标_点击(按键=0,类型=0,x=0,y=0):
    '''
    模拟鼠标点击
    :param 按键: 0.左键 1.中键 2.右键
    :param 类型: 0.单击 1.按下 2.弹起
    :return:
    '''
    代码 = {(0,1):2,(0,2):4,(1,1):32,(1,2):64,(2,1):8,(2,2):16}
    按键类型 = {1:(32,64),2:(8,16)}
    if not (按键,类型) in 代码:
        键码 = 按键类型[按键] if 按键 in 按键类型 else (2,4)
        win32api.mouse_event(键码[0],0,0,0,0)
        win32api.mouse_event(键码[1],0,0,0,0)
    else:
        win32api.mouse_event(代码[(按键,类型)],0,0,0,0)


@异常处理返回类型逻辑型
def 键盘_点击(键码,类型=0):
    '''
    :param 键码: 可直接使用 按键_按键名
    :param 类型: 0.单击 1.按下 2.弹起
    :return:
    '''
    if 类型 == 1:
        win32api.keybd_event(键码, 0, 0, 0)
    elif 类型 == 2:
        win32api.keybd_event(键码, 0, win32con.KEYEVENTF_KEYUP, 0)
    else:
        win32api.keybd_event(键码, 0, 0, 0)
        win32api.keybd_event(键码, 0, win32con.KEYEVENTF_KEYUP, 0)


@异常处理返回类型逻辑型
def 窗口_取窗口句柄(类名=None,标题=None):
    '返回第一个找到的句柄'
    return win32gui.FindWindow(类名, 标题)


@异常处理返回类型逻辑型
def 窗口_取坐标处窗口句柄(x,y):
    return win32gui.WindowFromPoint((x,y))


@异常处理返回类型逻辑型
def 窗口_取窗口类名(窗口句柄):
    return win32gui.GetClassName(窗口句柄)


@异常处理返回类型逻辑型
def 窗口_取窗口标题(窗口句柄):
    return win32gui.GetWindowText(窗口句柄)


@异常处理返回类型逻辑型
def 窗口_取窗口矩形(窗口句柄):
    '成功返回窗口 左边 顶边 右边 底边'
    return win32gui.GetWindowRect(窗口句柄)


@异常处理返回类型逻辑型
def 窗口_枚举子窗口句柄(窗口句柄):
    '成功返回子窗口句柄列表'
    hwndChildList = []
    win32gui.EnumChildWindows(窗口句柄, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList


@异常处理返回类型逻辑型
def 窗口_发送信息(窗口句柄,消息类型,参数1=0,参数2=0):
    return win32gui.PostMessage(窗口句柄,消息类型,参数1,参数2)


@异常处理返回类型逻辑型
def 窗口_发送信息2(窗口句柄,消息类型,参数1=0,参数2=0):
    return win32gui.SendMessage(窗口句柄,消息类型,参数1,参数2)


@异常处理返回类型逻辑型
def 窗口_发送文本(窗口句柄,内容):
    return win32api.SendMessage(窗口句柄, win32con.WM_SETTEXT, 0, 内容)

@异常处理返回类型逻辑型
def 窗口_取窗口文本长度(窗口句柄):
    return win32api.SendMessage(窗口句柄, win32con.WM_GETTEXTLENGTH, 0, 0) +1


@异常处理返回类型逻辑型
def 窗口_取窗口文本内容(窗口句柄):
    bufSize = win32api.SendMessage(窗口句柄, win32con.WM_GETTEXTLENGTH, 0, 0) + 1
    strBuf = win32gui.PyMakeBuffer(bufSize)
    length = win32gui.SendMessage(窗口句柄, win32con.WM_GETTEXT, bufSize, strBuf)
    address, length = win32gui.PyGetBufferAddressAndLen(strBuf)
    text = win32gui.PyGetString(address, length)
    return text[:-1]


@异常处理返回类型逻辑型
def 窗口_关闭窗口(窗口句柄):
    return win32gui.PostMessage(窗口句柄, win32con.WM_CLOSE, 0, 0)


@异常处理返回类型逻辑型
def 窗口_是否最小化(窗口句柄):
    return bool(win32gui.IsIconic(窗口句柄))


@异常处理返回类型逻辑型
def 窗口_最大化(窗口句柄):
    return bool(win32gui.ShowWindow(窗口句柄,win32con.SW_MAXIMIZE))


@异常处理返回类型逻辑型
def 窗口_最大化2(窗口句柄):
    '激活窗口并将其最大化'
    return bool(win32gui.ShowWindow(窗口句柄,win32con.SW_SHOWMAXIMIZED))


@异常处理返回类型逻辑型
def 窗口_最小化(窗口句柄):
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_MINIMIZE))


@异常处理返回类型逻辑型
def 窗口_最小化2(窗口句柄):
    '激活窗口并将其最小化'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWMINIMIZED))


@异常处理返回类型逻辑型
def 窗口_最小化3(窗口句柄):
    '窗口最小化，激活窗口仍然维持激活状态'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWMINNOACTIVE))


@异常处理返回类型逻辑型
def 窗口_隐藏窗口(窗口句柄):
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_HIDE))


@异常处理返回类型逻辑型
def 窗口_显示窗口(窗口句柄):
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOW))


@异常处理返回类型逻辑型
def 窗口_显示窗口2(窗口句柄):
    '以原尺寸恢复显示'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_RESTORE))


@异常处理返回类型逻辑型
def 窗口_显示窗口3(窗口句柄):
    '以窗口原来的状态显示窗口。激活窗口仍然维持激活状态'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWNA))


@异常处理返回类型逻辑型
def 窗口_显示窗口4(窗口句柄):
    '以窗口最近一次的大小和状态显示窗口。激活窗口仍然维持激活状态'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWNOACTIVATE))


@异常处理返回类型逻辑型
def 窗口_显示窗口5(窗口句柄):
    '激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。应用程序在第一次显示窗口的时候应该指定此标志'
    return bool(win32gui.ShowWindow(窗口句柄, win32con.SW_SHOWNORMAL))


@异常处理返回类型逻辑型
def 窗口_调整(窗口句柄,左边,顶边,宽度,高度):
    '移动窗口 调整宽度高度'
    return win32gui.MoveWindow(窗口句柄,左边,顶边,宽度,高度,True)


@异常处理返回类型逻辑型
def 窗口_调整2(窗口句柄,左边,顶边,宽度,高度):
    '移动窗口 调整宽度高度'
    return win32gui.SetWindowPos(窗口句柄, win32con.HWND_TOPMOST,左边,顶边,宽度,高度, win32con.SWP_SHOWWINDOW)


@异常处理返回类型逻辑型
def 窗口_置前台(窗口句柄):
    '指定句柄设置为前台，也就是激活'
    return win32gui.SetForegroundWindow(窗口句柄)


@异常处理返回类型逻辑型
def 窗口_置后台(窗口句柄):
    '设置为后台'
    return win32gui.SetBkMode(窗口句柄, win32con.TRANSPARENT)



def _MyCallback(hwnd, extra):#回调
    windows = extra
    temp = []
    temp.append(hex(hwnd))
    temp.append(win32gui.GetClassName(hwnd))
    temp.append(win32gui.GetWindowText(hwnd))
    windows[hwnd] = temp

@异常处理返回类型逻辑型
def 窗口_取所有顶级窗口句柄():
    '返回一个字典包含 key为句柄 值为列表[16进制的啥,类名,标题]'
    windows = {}
    win32gui.EnumWindows(_MyCallback, windows)
    return windows


@异常处理返回类型逻辑型
def 取剪辑版文本():
    '获取完需要自己解码,常规用utf8带汉字的用gbk等'
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


@异常处理返回类型逻辑型
def 置剪辑版文本(内容):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(内容)
    w.CloseClipboard()
    return True


@异常处理返回类型逻辑型
def 运行程序(文件路径,参数='',初始目录='',显示窗口=True):
    '启动/运行一个文件/程序'
    return win32api.ShellExecute(1, 'open',文件路径,参数,初始目录,显示窗口)


@异常处理返回类型逻辑型
def 信息框(内容,标题='提示',类型=0,图标=0):
    '''
    api创建的信息框
    :param 标题:
    :param 内容:
    :param 类型: 0.通常   1.确定 取消   2.是 否     3.是 否 取消   4.终止 重试 忽略
    :param 图标: 0.没有   1.蓝色提示   2.黄色感叹   3.红色叉叉
    :return: 出错返回0，正常返回值：1.确定 2.取消 3.中止 4.重试 5.忽略 6.是  7.否
    '''
    按钮类型 = {0:win32con.MB_OK,1:win32con.MB_OKCANCEL,2:win32con.MB_YESNO,3:win32con.MB_YESNOCANCEL,4:win32con.MB_ABORTRETRYIGNORE}
    图标类型 = {0:0,1:win32con.MB_ICONASTERISK,2:win32con.MB_ICONEXCLAMATION,3:win32con.MB_ICONERROR}
    return win32api.MessageBox(None,内容,标题,按钮类型[类型]|图标类型[图标])


@异常处理返回类型逻辑型
def 系统_建立关联文件(后缀,程序路径,图标=None):
    '后缀：.pyec,程序路径:完整的路径'
    程序名 = os.path.splitext(程序路径)[0]
    图标 = 图标 if 图标 else 程序路径
    # 创建
    key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, '', 0, win32con.KEY_READ)
    win32api.RegCreateKey(key, 后缀)
    win32api.RegCreateKey(key, 程序名 + '\\BrowserFlags')
    win32api.RegCreateKey(key, 程序名 + '\\EditFlags')
    win32api.RegCreateKey(key, 程序名 + '\\DefaultIcon\\')
    win32api.RegCreateKey(key, 程序名 + '\\shell\\')
    win32api.RegCreateKey(key, 程序名 + '\\shell\\open\\command\\')
    win32api.RegCloseKey(key)
    # 写入默认值
    key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, '', 0, win32con.KEY_READ)
    win32api.RegSetValue(key, '.pyec', win32con.REG_SZ, 程序名)
    win32api.RegSetValue(key, 程序名 + '\\BrowserFlags', win32con.REG_SZ, "8")
    win32api.RegSetValue(key, 程序名 + '\\EditFlags', win32con.REG_SZ, "0")
    win32api.RegSetValue(key, 程序名 + '\\DefaultIcon\\', win32con.REG_SZ,'"{}"'.format(图标))
    win32api.RegSetValue(key, 程序名 + '\\shell\\', win32con.REG_SZ, 'open')
    win32api.RegSetValue(key, 程序名 + '\\shell\\open\\command\\', win32con.REG_SZ,r'{} "%1"'.format(程序路径))
    win32api.RegCloseKey(key)
    return True


@异常处理返回类型逻辑型
def 系统_取Python目录():
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment', 0,win32con.KEY_ALL_ACCESS)
        版本 = win32api.RegQueryValueEx(key, 'Path')  # 遍历注册表下目录
        win32api.RegCloseKey(key)
        匹配 = re.findall(r'\b[A-Z]:\\.*?python\b', 版本[0])
        if 匹配:
            return 匹配[0] + "\\"
    except:
        pass

    try:
        p = subprocess.Popen("where python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        结果 = p.stdout.readlines()[0].decode('utf8')
        if 结果.find("python") != -1:
            return os.path.split(结果.split("\n")[0])[0] + "\\"
    except:
        pass

    try:
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Software\\Python\\PythonCore', 0, win32con.KEY_ALL_ACCESS)
        版本 = win32api.RegEnumKeyEx(key)[0][0]  # 遍历注册表下目录
        win32api.RegCloseKey(key)
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Software\\Python\\PythonCore\\{}\\InstallPath'.format(版本), 0,
                                  win32con.KEY_ALL_ACCESS)
        目录 = win32api.RegQueryValueEx(key, '')[0]
        win32api.RegCloseKey(key)
        if 目录.endswith('\\'):
            return 目录
        return 目录 + "\\"
    except:
        return ''


@异常处理返回类型逻辑型
def 文件_置隐藏Ex(路径):
    '隐藏文件'
    win32api.SetFileAttributes(路径, win32con.FILE_ATTRIBUTE_HIDDEN)
    return True


@异常处理返回类型逻辑型
def 文件_置只读Ex(路径):
    '修改文件为只读'
    win32api.SetFileAttributes(路径, win32con.FILE_ATTRIBUTE_READONLY)
    return True


@异常处理返回类型逻辑型
def 文件_置系统文件Ex(路径):
    '修改文件为系统文件'
    win32api.SetFileAttributes(路径, win32con.FILE_ATTRIBUTE_SYSTEM)
    return True


@异常处理返回类型逻辑型
def 文件_置正常Ex(路径):
    '文件被隐藏等可以使用这个还原显示'
    win32api.SetFileAttributes(路径, win32con.FILE_ATTRIBUTE_NORMAL)
    return True


@异常处理返回类型逻辑型
def 宽带_拨号(宽带名称,宽带账号,宽带密码):
    dos = 'rasdial {} {} {}'.format(宽带名称,宽带账号,宽带密码)
    return False if os.system(dos) else True


@异常处理返回类型逻辑型
def 宽带_断开(宽带名称):
    dos = 'rasdial {} /disconnect'.format(宽带名称)
    return False if os.system(dos) else True



def 取屏幕宽度():
    return GetSystemMetrics(0)


def 取屏幕高度():
    return GetSystemMetrics(1)

# 取鼠标水平位置
# 取鼠标垂直位置
def 取鼠标位置():
    return pyautogui.position()



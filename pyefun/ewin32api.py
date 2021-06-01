from win32api import GetSystemMetrics


def 取屏幕宽度():
    return GetSystemMetrics(0)


def 取屏幕高度():
    return GetSystemMetrics(1)

# 取鼠标水平位置
# 取鼠标垂直位置
def 取鼠标位置():
    return pyautogui.position()
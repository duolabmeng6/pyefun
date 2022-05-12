# pip install pygetwindow

import pygetwindow as gw


class 窗口操作:
    def __init__(self):
        pass

    def 获取窗口(self, 窗口名称):
        窗口 = gw.getWindowsWithTitle(窗口名称)
        if 窗口:
            return 窗口[0]
        else:
            return False
    def 获取所有窗口标题(self):
        return gw.getAllTitles()
    def 获取所有窗口句柄(self):
        return gw.getAllWindows()



if __name__ == "__main__":
    窗口操作 = 窗口操作()
    # 微信窗口 = 窗口操作.获取窗口根据标题("微信")
    # 微信窗口.activate()
    res = 窗口操作.获取所有窗口标题()
    print(res)
    res = 窗口操作.获取所有窗口句柄()
    print(res)





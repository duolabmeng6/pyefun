"""

.. Hint::
    自动化模块 采用 pyautogui 模块进行封装 实现模拟窗口操作的功能 自动模拟人工操作
    需要安装 pip install pyautogui
    需要安装 pip install pyperclip


.. literalinclude:: ../../../pyefun/自动化模块_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

from pyefun import *
import pyautogui
import pyperclip
# import ppppocr
# import winapi
import tempfile


class 自动化模块():
    ocr_md5 = None

    def __init__(self):
        pass

    def 设置保护措施(self, 每一步延迟=2.5):
        # 当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。
        pyautogui.PAUSE = 每一步延迟
        pyautogui.FAILSAFE = True

    def 当前屏幕分辨率(self):
        return pyautogui.size()

    def 找图(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        try:
            return pyautogui.locateOnScreen(图片路径)
        except:
            return False

    def 找图灰度模式(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        try:
            return pyautogui.locateOnScreen(图片路径, grayscale=True)
        except:
            return False

    def 找图所有(self, 图片路径):
        #  返回 [Box(left=0, top=0, width=300, height=400)] #
        try:
            return pyautogui.locateAllOnScreen(图片路径)
        except:
            return False

    def 找图_中心点坐标(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        try:
            return pyautogui.locateOnScreen(图片路径)
        except:
            return False

    def 获取中心点位置(self, 坐标):
        return pyautogui.center(坐标)

    def 获取当前鼠标位置(self):
        #  返回 (x, y) #
        return pyautogui.position()

    def 获取当前鼠标位置颜色(self):
        #  返回 (r, g, b) #
        return pyautogui.screenshot().getpixel(self.获取当前鼠标位置())

    def 截图全屏(self, 图片保存路径):
        pyautogui.screenshot(图片保存路径)  # 截全屏并设置保存图片的位置和名称

    def 检查指定位置的像素值(self, x, y, 颜色值=(255, 255, 245), 误差值=10):
        pyautogui.pixelMatchesColor(x, y, 颜色值, tolerance=误差值)

    def 截图(self, 图片保存路径, 截屏区域=(0, 0, 100, 100)):
        #  例如 auto.截图(截图地址, (left, top, width, height)) #
        pyautogui.screenshot(图片保存路径, region=截屏区域)

    def 鼠标移动(self, x, y, 时间=0):
        pyautogui.moveTo(x, y, duration=时间)

    def 鼠标拖动(self, x, y, 时间=0, 按键="left"):
        # 按键 设置为'left'、'middle'，以及'right'
        pyautogui.dragTo(x, y, 时间, button=按键)

    def 鼠标点击(self, x, y):
        pyautogui.click(x, y)

    def 鼠标右击(self, x, y):
        pyautogui.rightClick(x, y)

    def 鼠标双击(self, x, y):
        pyautogui.doubleClick(x, y)

    def 鼠标三击(self, x, y):
        pyautogui.tripleClick(x, y)

    def 鼠标左键按下(self, x, y):
        pyautogui.mouseDown(x, y)

    def 鼠标左键弹起(self, x, y):
        pyautogui.mouseUp(x, y)

    def 鼠标右键按下(self, x, y):
        pyautogui.rightClick(x, y)

    def 鼠标右键弹起(self, x, y):
        pyautogui.rightClick(x, y)

    def 鼠标滚轮向下(self, x, y):
        pyautogui.scroll(x, y)

    def 鼠标滚轮向上(self, x, y):
        pyautogui.scroll(-x, -y)

    def 鼠标滚轮向左(self, x, y):
        pyautogui.scroll(-x, -y)

    def 鼠标滚轮向右(self, x, y):
        pyautogui.scroll(x, y)

    def 键盘输入文字(self, 内容, 时间=0):
        # 例如 键盘输入文字('hello') #
        pyautogui.typewrite(内容, interval=时间)

    def 键盘按下(self, 键名):
        # 例如: 键盘按下('enter') #
        pyautogui.keyDown(键名)

    def 键盘弹起(self, 键名):
        # 例如 键盘弹起('shift') #
        pyautogui.keyUp(键名)

    def 键盘按下并弹起(self, 键名):
        # 例如 键盘按下并弹起('enter')#
        pyautogui.press(键名)

    def 键盘按下热键(self, *args, **kwargs):
        # 例如 键盘按下热键("ctrl", "c") #
        pyautogui.hotkey(*args, **kwargs)

    def 弹窗提示框(self, 内容, 标题='提示', 按钮='确定'):
        # 例如 弹窗提示('hello') #
        return pyautogui.alert(text=内容, title=标题, button=按钮)

    def 弹窗确认框(self, 内容, 标题='提示', 按钮=('确定', '取消')):
        # 例如 弹窗提示并等待('hello') #
        return pyautogui.confirm(内容, title=标题, buttons=按钮)

    def 弹窗输入框(self, 内容, 标题='提示'):
        return pyautogui.prompt(text=内容, title=标题, default='')

    def 弹出密码输入框(self, 内容, 标题):
        return pyautogui.password(text=内容, title=标题, default='', mask='*')

    def 获取窗口句柄(self, 窗口标题="微信"):
        return pyautogui.getWindowsWithTitle(窗口标题)

    def 粘贴(self, 内容):
        pyperclip.copy(内容)
        pyautogui.hotkey('ctrl', 'v')

    def 可视化工具(self):
        """
        MouseInfo的使用方法有两种。

        方法1：

        勾选3 Sec. Button Delay
        点击copy all(推荐)或者 copy xy 或者copy RGB
        然后在三秒内将鼠标移动到想要选择的位置
        等到3秒时候MouseInfo会记录下当前鼠标位置和颜色
        方法2：

        取消勾选3 Sec. Button Delay
        将鼠标移至想选择的位置
        然后按F1至F8键复制或记录鼠标位置，这样就把这些按键与鼠标记录做了关联映射
        可以MouseInfo窗口顶部的“Copy”和“Log”菜单，以找出按键映射到哪些按钮。
        """
        pyautogui.mouseInfo()

    def 启用ocr(self):
        self.ocr = ppppocr.ppppOcr()

    def ocr(self, 图片地址):
        self.dt_boxes, self.rec_res = self.ocr.ocr(图片地址)
        print(self.dt_boxes, self.rec_res)
        return self.dt_boxes, self.rec_res

    def 获取窗口找字区域(self, 窗口句柄):
        left, top, right, bottom = win32apiUtil.窗口_取窗口矩形(窗口句柄)
        width = right - left + 1
        height = bottom - top + 1
        # print(top, left, width, height)
        # win32apiUtil.窗口_置焦点(窗口句柄)
        return (left, top, width, height)

    def 找字(self, 字, 截图区域=None):
        截图保存地址 = os.path.join(tempfile.gettempdir(), "1.png")
        # print(截图保存地址)
        if 截图区域 == None:
            auto.截图全屏(截图保存地址)
        else:
            auto.截图(截图保存地址, 截图区域)

        # 图像没有变化的话 就继续使用缓存结果了
        _md5 = 取数据md5(读入文件(截图保存地址))
        if self.ocr_md5 != _md5:
            self.dt_boxes, self.rec_res = self.ocr.ocr(截图保存地址)
            self.ocr_md5 = _md5
            删除文件(截图保存地址)

        # print(self.dt_boxes, self.rec_res)
        print(self.rec_res)
        for i in range(len(self.dt_boxes)):
            txt = self.rec_res[i][0]
            x1, y1, x2, y2 = self.dt_boxes[i][0][0], self.dt_boxes[i][0][1], self.dt_boxes[i][2][0], \
                             self.dt_boxes[i][2][1]
            中心点x = x1 + 1
            中心点y = y1 + 1
            if 字 == txt:
                print("找到了,", 字, txt, x1, y1, x2, y2)
                return 中心点x, 中心点y
        return False

#
# if __name__ == '__main__':
#     auto = 自动化模块()
#     auto.启用ocr()
#     # x, y = auto.找字("回收站", (0, 0, 500, 500))
#     # auto.鼠标双击(x, y)
#     # 延时(2)
#     x, y = auto.找字("此电脑")
#     auto.鼠标双击(x, y)
#     延时(3)
#
#     x, y = auto.找字("照片")
#     auto.鼠标双击(x, y)
#     延时(3)
#
#     x, y = auto.找字("本机照片")
#     auto.鼠标双击(x, y)

# auto.可视化工具获取鼠标位置()

#     # 鼠标位置 = auto.获取当前鼠标位置()
#     # print(鼠标位置)
#     # 鼠标位置 = auto.获取当前鼠标位置颜色()
#     # print(鼠标位置)
#     # auto.鼠标移动(14, 20)
#     # 延时(1)
#     # auto.鼠标点击(14, 20)
#     鼠标位置 = auto.截图(r"C:\pyefun\pyefun\a\1.png", (0, 0, 300, 300))
#     图片位置 = auto.找图(r"C:\pyefun\pyefun\a\1.png")
#     print(图片位置)
#     图片中心点位置 = auto.获取中心点位置(图片位置)
#     print(图片中心点位置)

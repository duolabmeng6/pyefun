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
        """
        __init__ 的功能说明（请补充）。

        """
        pass

    def 设置保护措施(self, 每一步延迟=2.5):
        # 当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。
        """
        设置保护措施 的功能说明（请补充）。

        Args:
            每一步延迟 (可选): 参数说明。默认值为 2.5。

        """
        pyautogui.PAUSE = 每一步延迟
        pyautogui.FAILSAFE = True

    def 当前屏幕分辨率(self):
        """
        当前屏幕分辨率 的功能说明（请补充）。

        """
        return pyautogui.size()

    def 找图(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        """
        找图 的功能说明（请补充）。

        Args:
            图片路径: 参数说明。

        """
        try:
            return pyautogui.locateOnScreen(图片路径)
        except:
            return False

    def 找图灰度模式(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        """
        找图灰度模式 的功能说明（请补充）。

        Args:
            图片路径: 参数说明。

        """
        try:
            return pyautogui.locateOnScreen(图片路径, grayscale=True)
        except:
            return False

    def 找图所有(self, 图片路径):
        #  返回 [Box(left=0, top=0, width=300, height=400)] #
        """
        找图所有 的功能说明（请补充）。

        Args:
            图片路径: 参数说明。

        """
        try:
            return pyautogui.locateAllOnScreen(图片路径)
        except:
            return False

    def 找图_中心点坐标(self, 图片路径):
        #  返回 (left=0, top=0, width=300, height=400) #
        """
        找图_中心点坐标 的功能说明（请补充）。

        Args:
            图片路径: 参数说明。

        """
        try:
            return pyautogui.locateOnScreen(图片路径)
        except:
            return False

    def 获取中心点位置(self, 坐标):
        """
        获取中心点位置 的功能说明（请补充）。

        Args:
            坐标: 参数说明。

        """
        return pyautogui.center(坐标)

    def 获取当前鼠标位置(self):
        #  返回 (x, y) #
        """
        获取当前鼠标位置 的功能说明（请补充）。

        """
        return pyautogui.position()

    def 获取当前鼠标位置颜色(self):
        #  返回 (r, g, b) #
        """
        获取当前鼠标位置颜色 的功能说明（请补充）。

        """
        return pyautogui.screenshot().getpixel(self.获取当前鼠标位置())

    def 截图全屏(self, 图片保存路径):
        """
        截图全屏 的功能说明（请补充）。

        Args:
            图片保存路径: 参数说明。

        """
        pyautogui.screenshot(图片保存路径)  # 截全屏并设置保存图片的位置和名称

    def 检查指定位置的像素值(self, x, y, 颜色值=(255, 255, 245), 误差值=10):
        """
        检查指定位置的像素值 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。
            颜色值 (可选): 参数说明。默认值为 (255, 255, 245)。
            误差值 (可选): 参数说明。默认值为 10。

        """
        pyautogui.pixelMatchesColor(x, y, 颜色值, tolerance=误差值)

    def 截图(self, 图片保存路径, 截屏区域=(0, 0, 100, 100)):
        #  例如 auto.截图(截图地址, (left, top, width, height)) #
        """
        截图 的功能说明（请补充）。

        Args:
            图片保存路径: 参数说明。
            截屏区域 (可选): 参数说明。默认值为 (0, 0, 100, 100)。

        """
        pyautogui.screenshot(图片保存路径, region=截屏区域)

    def 鼠标移动(self, x, y, 时间=0):
        """
        鼠标移动 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。
            时间 (可选): 参数说明。默认值为 0。

        """
        pyautogui.moveTo(x, y, duration=时间)

    def 鼠标拖动(self, x, y, 时间=0, 按键="left"):
        # 按键 设置为'left'、'middle'，以及'right'
        """
        鼠标拖动 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。
            时间 (可选): 参数说明。默认值为 0。
            按键 (可选): 参数说明。默认值为 "left"。

        """
        pyautogui.dragTo(x, y, 时间, button=按键)

    def 鼠标点击(self, x, y):
        """
        鼠标点击 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.click(x, y)

    def 鼠标右击(self, x, y):
        """
        鼠标右击 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.rightClick(x, y)

    def 鼠标双击(self, x, y):
        """
        鼠标双击 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.doubleClick(x, y)

    def 鼠标三击(self, x, y):
        """
        鼠标三击 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.tripleClick(x, y)

    def 鼠标左键按下(self, x, y):
        """
        鼠标左键按下 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.mouseDown(x, y)

    def 鼠标左键弹起(self, x, y):
        """
        鼠标左键弹起 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.mouseUp(x, y)

    def 鼠标右键按下(self, x, y):
        """
        鼠标右键按下 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.rightClick(x, y)

    def 鼠标右键弹起(self, x, y):
        """
        鼠标右键弹起 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.rightClick(x, y)

    def 鼠标滚轮向下(self, x, y):
        """
        鼠标滚轮向下 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.scroll(x, y)

    def 鼠标滚轮向上(self, x, y):
        """
        鼠标滚轮向上 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.scroll(-x, -y)

    def 鼠标滚轮向左(self, x, y):
        """
        鼠标滚轮向左 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.scroll(-x, -y)

    def 鼠标滚轮向右(self, x, y):
        """
        鼠标滚轮向右 的功能说明（请补充）。

        Args:
            x: 参数说明。
            y: 参数说明。

        """
        pyautogui.scroll(x, y)

    def 键盘输入文字(self, 内容, 时间=0):
        # 例如 键盘输入文字('hello') #
        """
        键盘输入文字 的功能说明（请补充）。

        Args:
            内容: 参数说明。
            时间 (可选): 参数说明。默认值为 0。

        """
        pyautogui.typewrite(内容, interval=时间)

    def 键盘按下(self, 键名):
        # 例如: 键盘按下('enter') #
        """
        键盘按下 的功能说明（请补充）。

        Args:
            键名: 参数说明。

        """
        pyautogui.keyDown(键名)

    def 键盘弹起(self, 键名):
        # 例如 键盘弹起('shift') #
        """
        键盘弹起 的功能说明（请补充）。

        Args:
            键名: 参数说明。

        """
        pyautogui.keyUp(键名)

    def 键盘按下并弹起(self, 键名):
        # 例如 键盘按下并弹起('enter')#
        """
        键盘按下并弹起 的功能说明（请补充）。

        Args:
            键名: 参数说明。

        """
        pyautogui.press(键名)

    def 键盘按下热键(self, *args, **kwargs):
        # 例如 键盘按下热键("ctrl", "c") #
        """
        键盘按下热键 的功能说明（请补充）。

        Args:
            *args: 参数说明。
            **kwargs: 参数说明。

        """
        pyautogui.hotkey(*args, **kwargs)

    def 弹窗提示框(self, 内容, 标题='提示', 按钮='确定'):
        # 例如 弹窗提示('hello') #
        """
        弹窗提示框 的功能说明（请补充）。

        Args:
            内容: 参数说明。
            标题 (可选): 参数说明。默认值为 '提示'。
            按钮 (可选): 参数说明。默认值为 '确定'。

        """
        return pyautogui.alert(text=内容, title=标题, button=按钮)

    def 弹窗确认框(self, 内容, 标题='提示', 按钮=('确定', '取消')):
        # 例如 弹窗提示并等待('hello') #
        """
        弹窗确认框 的功能说明（请补充）。

        Args:
            内容: 参数说明。
            标题 (可选): 参数说明。默认值为 '提示'。
            按钮 (可选): 参数说明。默认值为 ('确定', '取消')。

        """
        return pyautogui.confirm(内容, title=标题, buttons=按钮)

    def 弹窗输入框(self, 内容, 标题='提示'):
        """
        弹窗输入框 的功能说明（请补充）。

        Args:
            内容: 参数说明。
            标题 (可选): 参数说明。默认值为 '提示'。

        """
        return pyautogui.prompt(text=内容, title=标题, default='')

    def 弹出密码输入框(self, 内容, 标题):
        """
        弹出密码输入框 的功能说明（请补充）。

        Args:
            内容: 参数说明。
            标题: 参数说明。

        """
        return pyautogui.password(text=内容, title=标题, default='', mask='*')

    def 获取窗口句柄(self, 窗口标题="微信"):
        """
        获取窗口句柄 的功能说明（请补充）。

        Args:
            窗口标题 (可选): 参数说明。默认值为 "微信"。

        """
        return pyautogui.getWindowsWithTitle(窗口标题)

    def 粘贴(self, 内容):
        """
        粘贴 的功能说明（请补充）。

        Args:
            内容: 参数说明。

        """
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
        """
        启用ocr 的功能说明（请补充）。

        """
        self.ocr = ppppocr.ppppOcr()

    def ocr(self, 图片地址):
        """
        ocr 的功能说明（请补充）。

        Args:
            图片地址: 参数说明。

        """
        self.dt_boxes, self.rec_res = self.ocr.ocr(图片地址)
        print(self.dt_boxes, self.rec_res)
        return self.dt_boxes, self.rec_res

    def 获取窗口找字区域(self, 窗口句柄):
        """
        获取窗口找字区域 的功能说明（请补充）。

        Args:
            窗口句柄: 参数说明。

        """
        left, top, right, bottom = win32apiUtil.窗口_取窗口矩形(窗口句柄)
        width = right - left + 1
        height = bottom - top + 1
        # print(top, left, width, height)
        # win32apiUtil.窗口_置焦点(窗口句柄)
        return (left, top, width, height)

    def 找字(self, 字, 截图区域=None):
        """
        找字 的功能说明（请补充）。

        Args:
            字: 参数说明。
            截图区域 (可选): 参数说明。默认值为 None。

        """
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

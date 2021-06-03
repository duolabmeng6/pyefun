"""
*******************
浏览器类
*******************

.. contents:: 目录


.. Hint::
    需要安装 selenium chrome浏览器或者Firefox浏览器

    本地调试下需要安装 chrome浏览器 chromedriver驱动 或者 Firefox geckodriver驱动

    window macos ubuntu  使用 浏览器初始化本地环境() 就可以自动检测驱动和自动下载配置

    使用 docker 部署远程浏览器 无需安装驱动

    部署时建议使用docker部署远程浏览器

安装 selenium
================

``pip install selenium``


chromedriver 驱动下载
================

https://chromedriver.chromium.org/

https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/

Firefox 驱动下载
================

https://github.com/mozilla/geckodriver/releases

docker部署远程浏览器
================

linux
-------------------

    ``docker run --name chrome -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug:3.141.59-20210422``

window
-------------------

    ``docker run --name chrome -d -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug:3.141.59-20210422``

vpc连接远程桌面
-------------------

VNC Viewer
https://www.realvnc.com/en/connect/download/viewer/

127.0.0.1:5900 即可连接至远程桌面


.. image:: /_static/vnc_viewer.png



.. literalinclude:: ../../../pyefun/seleniumUtil/seleniumUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:


"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By  # 等待页面加载延时模块
from selenium.webdriver.support import expected_conditions as EC  # 等待页面加载延时模块

from pyefun import *
import requests

键盘_F1 = '\ue031'
键盘_F2 = '\ue032'
键盘_F3 = '\ue033'
键盘_F4 = '\ue034'
键盘_F5 = '\ue035'
键盘_F6 = '\ue036'
键盘_F7 = '\ue037'
键盘_F8 = '\ue038'
键盘_F9 = '\ue039'
键盘_F10 = '\ue03a'
键盘_F11 = '\ue03b'
键盘_F12 = '\ue03c'

键盘_META = '\ue03d'
键盘_COMMAND = '\ue03d'
键盘_ESCAPE = '\ue00c'
键盘_SPACE = '\ue00d'
键盘_PAUSE = '\ue00b'

键盘_向左 = '\ue012'
键盘_向上 = '\ue013'
键盘_向右 = '\ue014'
键盘_向下 = '\ue015'

键盘_INSERT = '\ue016'
键盘_DELETE = '\ue017'
键盘_PAGE_UP = '\ue00e'
键盘_PAGE_DOWN = '\ue00f'
键盘_END = '\ue010'
键盘_HOME = '\ue011'
键盘_ALT = '\ue00a'
键盘_CTRL = '\ue009'
键盘_退格 = '\ue003'
键盘_空格 = '\ue00d'
键盘_TAB = '\ue004'
键盘_ESC = '\ue00c'
键盘_回车 = '\ue007'
键盘_SHIFT = '\ue008'


def 浏览器初始化本地环境():
    """
.. Hint::
    自动检测环境 自动下载驱动 如果使用远程浏览器则无需安装驱动 也无需调用本函数

    """
    if 系统_是否为window系统():
        返回内容 = 运行("chromedriver -v")
        if 判断文本(返回内容, ["ChromeDriver"]) == False:
            驱动路径 = "C:/Windows/chromedriver.exe"
            if 文件是否存在(驱动路径) == False:
                保存路径 = 取运行目录() + "/chromedriver.zip"
                下载地址 = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_win32.zip"
                print("chromedriver 驱动不存在 正在自动下载 %s 保存路径为:%s" % (下载地址, 保存路径))
                下载文件(下载地址, 保存路径)
                解压目录 = "C:/Windows"
                zip解压(保存路径, 解压目录)
                print("chromedriver 解压至:%s" % (驱动路径))
                文件_删除(保存路径)

    if 系统_是否为mac系统():
        返回内容 = 运行("chromedriver -v")
        if 判断文本(返回内容, ["ChromeDriver"]) == False:
            驱动路径 = "/usr/local/bin/chromedriver"
            if 文件是否存在(驱动路径) == False:
                保存路径 = 取运行目录() + "/chromedriver.zip"
                下载地址 = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_mac64.zip"
                print("chromedriver 驱动不存在 正在自动下载 %s 保存路径为:%s" % (下载地址, 保存路径))
                下载文件(下载地址, 保存路径)
                解压目录 = "/usr/local/bin/"
                zip解压(保存路径, 解压目录)
                print("chromedriver 解压至:%s" % (驱动路径))
                文件_删除(保存路径)
                文件_修改权限(驱动路径, stat.S_IRWXU)
    if 系统_是否为linux系统():
        返回内容 = 运行("chromedriver -v")
        if 判断文本(返回内容, ["ChromeDriver"]) == False:
            驱动路径 = "/usr/local/bin/chromedriver"
            if 文件是否存在(驱动路径) == False:
                保存路径 = 取运行目录() + "/chromedriver.zip"
                下载地址 = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip"
                print("chromedriver 驱动不存在 正在自动下载 %s 保存路径为:%s" % (下载地址, 保存路径))
                下载文件(下载地址, 保存路径)
                解压目录 = "/usr/local/bin/"
                zip解压(保存路径, 解压目录)
                print("chromedriver 解压至:%s" % (驱动路径))
                文件_删除(保存路径)
                文件_修改权限(驱动路径, stat.S_IRWXU)


class 浏览器类():

    def 远程浏览器是否就绪(self, 远程浏览器地址="http://127.0.0.1:4444/wd/hub"):
        """
            while 浏览器.远程浏览器是否就绪(远程浏览器地址) == False:
                延时(1)
                print("浏览器未就绪")
        """
        try:
            data = requests.get(远程浏览器地址 + "/status")
            json = data.json()
            ready = json['value']['ready']
        except:
            return False
        return ready

    def 获取远程chrome(self, server_url="http://127.0.0.1:4444/wd/hub"):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:chromeOptions'] = {"args": ["--headless"]}
        driver = webdriver.Remote(
            command_executor=server_url,
            desired_capabilities=capabilities
        )
        self.浏览器 = driver
        return driver

    def 获取本地chrome(self, 驱动路径='chromedriver', ChromeOptions=webdriver.ChromeOptions()):
        # opt = webdriver.ChromeOptions()
        # # opt.add_argument('--headless')
        # opt.add_argument('--disable-gpu')
        # opt.add_argument("blink-settings=imagesEnabled=false")
        # opt.add_argument(
        #     "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
        driver = webdriver.Chrome(驱动路径, options=ChromeOptions)
        self.浏览器 = driver
        return driver

    def 获取本地Firefox(self):
        opt = webdriver.FirefoxOptions()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument("blink-settings=imagesEnabled=false")
        opt.add_argument(
            "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'")
        driver = webdriver.Firefox(options=opt)
        self.浏览器 = driver
        return driver

    def 打开chrome(self, 驱动路径='chromedriver', 无痕模式=True, 无头模式=False, 隐藏自动化提示=True, 隐藏滚动条=False, 禁止加载图片=False,
                 禁用插件=False,
                 禁止Javascript=False, 禁用JAVA=False, 禁止密码保存提示=True, 禁用弹窗=False, 禁止策略化=False, 初始运行=False, 沙盒运行=True,
                 user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                 代理='', 编码='lang=zh_CN.UTF-8', 禁止使用GPU=False, 谷歌浏览器路径=''):
        '代理格式：127.0.0.1:8888  带账号密码验证的自行百度修改'

        chrome_options = webdriver.ChromeOptions()
        if 无痕模式:
            chrome_options.add_argument('--incognito')
        if 无头模式:
            chrome_options.add_argument('--headless')
        if 隐藏自动化提示:
            chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        if 隐藏滚动条:
            chrome_options.add_argument('--hide-scrollbars')
        if 禁止加载图片:
            chrome_options.add_argument('blink-settings=imagesEnabled=false')
        if 禁用插件:
            chrome_options.add_argument('--disable-plugins')
        if 禁止Javascript:
            chrome_options.add_argument('--disable-javascript')
        if 禁止密码保存提示:
            prefs = {}
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            chrome_options.add_experimental_option("prefs", prefs)
        if 禁止策略化:
            chrome_options.add_argument('--disable-infobars')
        if 禁用弹窗:
            chrome_options.add_argument('--disable-popup-blocking')
        if 禁用JAVA:
            chrome_options.add_argument('–disable-java')
        if not 沙盒运行:
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        if user_agent:
            chrome_options.add_argument('User-Agent=' + user_agent)
        if 编码:
            chrome_options.add_argument(编码)
        if 禁止使用GPU:
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        if 代理:
            chrome_options.add_argument('--proxy-server=http://' + 代理)
        if 谷歌浏览器路径:
            chrome_options.binary_location = 谷歌浏览器路径
        if 初始运行:
            chrome_options.add_argument('–first run')

        self.获取本地chrome(驱动路径, chrome_options)

        return True

    def 浏览网页(self, URL地址, 隐藏Navigator=True):
        """
        浏览指定网页。本命令为初级对象成员命令。
        """
        self.浏览器.get(URL地址)
        if 隐藏Navigator:
            script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
            self.浏览器.execute_script(script)
        return True

    def 等待元素加载(self, By元素类型=0, 元素名称="", 等待秒数=60):
        """成功返回真,失败返回假 ,By元素类型参数0是css_selector 谷歌直接复制 1 是id属性 2是name属性, 3 是链接名称 4是xpath属性 5是class_name属性 6是tag_name属性 7,模糊 链接名称"""
        if By元素类型 == 0:
            a = By.CSS_SELECTOR
        elif By元素类型 == 1:
            a = By.ID
        elif By元素类型 == 2:
            a = By.NAME
        elif By元素类型 == 3:
            a = By.LINK_TEXT
        elif By元素类型 == 4:
            a = By.XPATH
        elif By元素类型 == 5:
            a = By.CLASS_NAME
        elif By元素类型 == 6:
            a = By.TAG_NAME
        elif By元素类型 == 7:
            a = By.PARTIAL_LINK_TEXT
        try:
            Wait(self.浏览器, 等待秒数).until(EC.presence_of_element_located((a, 元素名称)))  # 等待页面id为 password 是否加载 完成
            return True
        except Exception as cuowu:
            return False

    def 等待元素显示(self, 等待时间=5, className=""):
        try:
            WebDriverWait(self.浏览器, 等待时间, 0.5, ignored_exceptions=TimeoutException).until(
                lambda x: x.find_element_by_class_name(className).is_displayed())
        except:
            return False
        return True

    def 取页面标题(self):
        return self.浏览器.title

    def 取页面链接(self):
        return self.浏览器.current_url

    def 取页面源码(self):
        return self.浏览器.page_source

    def 关闭当前页面(self):
        '如果只有一个页面标签则会关闭浏览器'
        self.浏览器.close()
        return True

    def 退出(self):
        """
        关闭浏览器
        """
        self.浏览器.quit()
        return True

    def 全屏(self):
        '等于按了F11 浏览器窗口全屏显示'
        self.浏览器.fullscreen_window()
        return True

    def 置浏览器宽度高度(self, 宽度, 高度):
        self.浏览器.set_window_size(宽度, 高度)
        return True

    def 后退(self):
        '控制浏览器后退'
        self.浏览器.back()
        return True

    def 前进(self):
        '控制浏览器前进'
        self.浏览器.forward()
        return True

    def 刷新页面(self):
        self.浏览器.refresh()
        return True

    def 进入Frame页面(self, Frame标识):
        "默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性可以通过定位获取的标识直接传入"
        self.浏览器.switch_to.frame(Frame标识)
        return True

    def 置最外层Frame框架(self):

        self.浏览器.switch_to.frame_content()

    def 置上一层Frame框架(self):

        self.浏览器.switch_to.partent_frame()

    def 退出Frame页面(self):
        self.浏览器.switch_to.default_content()
        return True

    def 取所有页面句柄(self):
        '返回所有窗口的句柄到当前会话'
        return self.浏览器.window_handles

    def 取当前页面句柄(self):
        '获得当前窗口句柄'
        return self.浏览器.current_window_handle

    def 切换页面(self, 页面句柄):
        '用于不同窗口的切换'
        self.switch_to.window(页面句柄)
        return True

    def 提示框同意(self):
        '接受现有警告框'
        self.浏览器.switch_to.alert.accept()
        return True

    def 提示框取消(self):
        '解散现有警告框'
        self.浏览器.switch_to.alert.dismiss()
        return True

    def 提示框发送文本(self, 内容):
        '发送文本至警告框。keysToSend：将文本发送至警告框'
        self.浏览器.switch_to.alert.send_keys(内容)
        return True

    def 提示框取文本(self):
        '返回 alert/confirm/prompt 中的文字信息'
        return self.浏览器.switch_to.alert.text

    def 提示框置焦点(self):
        '返回 alert/confirm/prompt 中的文字信息'
        return self.浏览器.switch_to.alert()

    def 取元素从id(self, id):
        '通过元素id定位,匹配多个则返回对象列表'
        结果 = self.浏览器.find_elements_by_id(id)
        if len(结果) == 0:
            return False
        return 浏览器元素操作(self.浏览器, 结果[0])

    def 取元素从name(self, name):
        '通过元素name定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_name(name)]

    def 取元素从xpath(self, xpath):
        '通过xpath表达式定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_xpath(xpath)]

    def 取元素从link_text(self, text):
        '通过完整超链接定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_link_text(text)]

    def 取元素从partial_link_text(self, text):
        '通过部分链接定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_partial_link_text(text)]

    def 取元素从tag_name(self, tagname):
        '通过标签定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_tag_name(tagname)]

    def 取元素从class_name(self, name):
        '通过类名进行定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_class_name(name)]

    def 取元素从css_selector(self, css):
        '通过css选择器进行定位,匹配多个则返回对象列表'
        return [浏览器元素操作(self.浏览器, x) for x in self.浏览器.find_elements_by_css_selector(css)]

    def 最大化(self):
        "浏览器窗口最大化"
        self.浏览器.maximize_window()
        return True

    def 最小化(self):
        "浏览器窗口最小化"
        self.浏览器.minimize_window()
        return True

    def 取名称(self):
        "查看浏览器的名字"
        return self.浏览器.name

    def 取窗口坐标(self):
        "获取当前窗口的坐标"
        return self.浏览器.get_window_position()

    def 取窗口矩形(self):
        "获取窗口的x，y坐标以及当前窗口的高度和宽度"
        return self.浏览器.get_window_rect()

    def 取窗口宽度高度(self):
        "获取当前窗口的尺寸"
        return self.浏览器.get_window_size()

    def 取所有Cookie(self):
        '获得所有cookie信息'
        return self.浏览器.get_cookies()

    def 取指定Cookie(self, name):
        '返回字典的key为“name”的cookie信息'
        return self.浏览器.get_cookie(name)

    def 添加Cookie(self, cookie_dict):
        '添加cookie。“cookie_dict”指字典对象，必须有name 和value 值'
        self.浏览器.add_cookie(cookie_dict)
        return True

    def 删除指定Cookie(self, name):
        '删除cookie信息。“name”是要删除的cookie的名称'
        self.浏览器.delete_cookie(name)
        return True

    def 删除所有Cookie(self):
        '删除所有cookie信息'
        self.浏览器.delete_all_cookies()
        return True

    def 运行JS(self, *args):
        '执行js代码,算加密需要自己声明调用的对象'
        return self.浏览器.execute_script(*args)

    def 运行JS异步(self, *args):
        '执行js代码'
        return self.浏览器.execute_async_script(*args)

    def 新建页面(self, URL):
        '通过javascript打开新页面'
        js = "window.open('{}')".format(URL)
        self.浏览器.execute_script(js)
        return True

    def 置滚动条位置(self, 横向=0, 纵向=0):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "window.scrollTo({},{});".format(横向, 纵向)
        self.浏览器.execute_script(js)
        return True

    def 滚动条靠左(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollLeft=0"
        self.浏览器.execute_script(js)
        return True

    def 滚动条靠右(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollLeft=10000"
        self.浏览器.execute_script(js)
        return True

    def 滚动条靠顶(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollTop=0"
        self.浏览器.execute_script(js)
        return True

    def 滚动条靠底(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollTop=10000"
        self.浏览器.execute_script(js)
        return True

    def 窗口截图保存(self, 保存地址):
        '将当前窗口的屏幕快照保存到PNG图像文件中'
        self.浏览器.save_screenshot(保存地址)
        return True

    def 截图保存(self, 保存地址):
        '用于截取当前窗口，并把图片保存到本地'
        self.浏览器.get_screenshot_as_file(保存地址)
        return True

    def 截图base64(self):
        '以base64编码的字符串获取当前窗口的屏幕快照'
        return self.浏览器.get_screenshot_as_base64()

    def 截图png(self):
        '以二进制数据获取当前窗口的屏幕快照。'
        return self.浏览器.get_screenshot_as_png()

    def 置页面超时时间(self, 秒数):
        '设置等待页面加载完成的时间'
        self.浏览器.set_page_load_timeout(秒数)
        return True

    def 置JS超时时间(self, 秒数):
        '设置脚本在执行过程中应等待的时间'
        self.浏览器.set_script_timeout(秒数)
        return True

    def 置浏览器位置(self, 左边=None, 顶边=None, 宽度=None, 高度=None):
        '设置窗口的x，y坐标以及当前窗口的高度和宽度。'
        self.浏览器.set_window_rect(左边, 顶边, 宽度, 高度)
        return True

    def 鼠标抬起(self):
        '释放按住的鼠标键'
        ActionChains(self.浏览器).release().perform()
        return True


class 浏览器元素操作():

    def __init__(self, 浏览器, 元素):
        self.元素 = 元素
        self.浏览器 = 浏览器

    def 清空(self):
        self.元素.clear()
        return True

    def 输入(self, *args):
        '模拟按键输入，将密钥发送到当前的焦点元素,包括上传文件可以直接发送文件路径,可使用 键盘_* ,如 按键_输入(键盘_CTRL,"a") 即为全选'
        self.元素.send_keys(*args)
        return True

    def 键盘指定输入(self, 键值):
        '将键发送到元素,可以使用 键盘_*'
        ActionChains(self.浏览器).send_keys_to_element(self.元素, 键值).perform()
        return True

    def 点击(self):
        self.元素.click()
        return True

    def 提交表单(self):
        '查找到表单（from）直接调用submit即可'
        self.元素.submit()
        return True

    def 取属性值(self, 属性名称):
        '获取元素属性值,如：value,str,img等属性'
        return self.元素.get_attribute(属性名称)

    def 取CSS属性值(self, 属性名称):
        '获取CSS属性值'
        return self.元素.value_of_css_property(属性名称)

    def 取坐标(self):
        return self.元素.location

    def 取宽度高度(self):
        return self.元素.size

    def 是否显示可见(self):
        '判断元素是否显示'
        return self.元素.is_displayed()

    def 是否选中(self):
        '判断元素是否选中状态'
        return self.元素.is_selected()

    def 是否启用(self):
        '判断元素是否是否启用'
        return self.元素.is_enabled()

    def 取文本(self):
        '获取文本'
        return self.元素.text

    def 取源码(self):
        '获取文本'
        return self.元素.get_attribute("innerHTML")

    def 取标签名称(self):
        '返回元素的tagName'
        return self.元素.tag_name

    def 鼠标悬停(self):
        '执行鼠标悬停操作,一些网页鼠标悬停后才会加载下拉列表'
        ActionChains(self.浏览器).move_to_element(self.元素).perform()
        return True

    def 鼠标右键按下(self):
        ActionChains(self.浏览器).context_click(self.元素).perform()
        return True

    def 鼠标双击(self):
        ActionChains(self.浏览器).double_click(self.元素).perform()
        return True

    def 鼠标左键按住(self):
        '按下鼠标左键在一个元素上'
        ActionChains(self.浏览器).click_and_hold(self.元素).perform()
        return True

    def 鼠标拖动(self, 目标标识):
        '鼠标拖动(d.标识)'
        ActionChains(self.浏览器).drag_and_drop(self.元素, 目标标识).perform()
        return True

    def 鼠标拖动距离(self, X偏移量, Y偏移量):
        '然后移至目标偏移量并释放鼠标按钮'
        ActionChains(self.浏览器).drag_and_drop_by_offset(self.元素, X偏移量, Y偏移量).perform()
        return True

    def 鼠标原地偏移(self, X偏移量, Y偏移量):
        '将鼠标移动到当前鼠标位置的偏移处'
        ActionChains(self.浏览器).move_by_offset(X偏移量, Y偏移量).perform()
        return True

    def 鼠标移到元素中间(self):
        '将鼠标移到元素的中间'
        ActionChains(self.浏览器).move_to_element().perform()
        return True

    def 鼠标移动(self, X偏移量, Y偏移量):
        '将鼠标移动指定元素的偏移量'
        ActionChains(self.浏览器).move_to_element_with_offset(self.元素, X偏移量, Y偏移量).perform()
        return True

    def 鼠标抬起(self):
        '释放元素上按住的鼠标键'
        ActionChains(self.浏览器).release(self.元素).perform()
        return True

    def 按下全选(self):
        self.元素.send_keys(键盘_CTRL, 'a')
        return True

    def 按下复制(self):
        self.元素.send_keys(键盘_CTRL, 'c')
        return True

    def 按下剪切(self):
        self.元素.send_keys(键盘_CTRL, 'x')
        return True

    def 按下粘贴(self):
        self.元素.send_keys(键盘_CTRL, 'v')
        return True

    def 下拉框选择值(self, value):
        'select标签的value属性的值'
        Select(self.元素).select_by_value(value)
        return True

    def 下拉框选择索引(self, id):
        '下拉框的索引'
        Select(self.元素).select_by_index(id)
        return True

    def 下拉框选择文本(self, text):
        '下拉框的文本值'
        Select(self.元素).select_by_visible_text(text)
        return True

    def 下拉框全部取消选中(self):
        Select(self.元素).deselect_all()
        return True

    def 下拉框取消选中索引(self, id):
        Select(self.元素).deselect_by_index(id)
        return True

    def 下拉框取消选中值(self, value):
        Select(self.元素).deselect_by_value(value)
        return True

    def 下拉框取消选中文本(self, text):
        Select(self.元素).deselect_by_visible_text(text)
        return True

    def 下拉框取全部选中项(self):
        '返回属于此选择标记的所有选择的选项的列表'
        return Select(self.元素).all_selected_options

    def 下拉框取选中项(self):
        '该选择标记中的第一个选择的选项（或正常选择中的当前选择的选项）'
        return Select(self.元素).first_selected_option

    def 下拉框取列表项(self):
        '返回属于该选择标签的所有选项的列表'
        return Select(self.元素).options

    def 取矩形(self):
        return self.元素.rect

    def 截图保存(self, 文件名):
        '将当前元素的屏幕快照保存到PNG图像文件中'
        self.元素.screenshot(文件名)
        return True

    def 截图base64(self):
        '以base64编码字符串的形式获取当前元素的屏幕快照'
        return self.元素.screenshot_as_base64

    def 截图png(self):
        '以二进制数据获取当前元素的屏幕截图'
        return self.元素.screenshot_as_png

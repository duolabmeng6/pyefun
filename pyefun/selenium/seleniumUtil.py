# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from pyefun.public import *

按钮_F1 = '\ue031'  # function  keys
按钮_F2 = '\ue032'
按钮_F3 = '\ue033'
按钮_F4 = '\ue034'
按钮_F5 = '\ue035'
按钮_F6 = '\ue036'
按钮_F7 = '\ue037'
按钮_F8 = '\ue038'
按钮_F9 = '\ue039'
按钮_F10 = '\ue03a'
按钮_F11 = '\ue03b'
按钮_F12 = '\ue03c'

按钮_META = '\ue03d'
按钮_COMMAND = '\ue03d'
按钮_ESCAPE = '\ue00c'
按钮_SPACE = '\ue00d'
按钮_PAUSE = '\ue00b'

按钮_向左 = '\ue012'
按钮_向上 = '\ue013'
按钮_向右 = '\ue014'
按钮_向下 = '\ue015'

按钮_INSERT = '\ue016'
按钮_DELETE = '\ue017'
按钮_PAGE_UP = '\ue00e'
按钮_PAGE_DOWN = '\ue00f'
按钮_END = '\ue010'
按钮_HOME = '\ue011'
按钮_ALT = '\ue00a'
按钮_CTRL = '\ue009'
按钮_退格 = '\ue003'
按钮_空格 = '\ue00d'
按钮_TAB = '\ue004'
按钮_ESC = '\ue00c'
按钮_回车 = '\ue007'
按钮_SHIFT = '\ue008'


class Selenium填表:

    @异常处理返回类型逻辑型
    def 打开谷歌(self, 驱动路径='chromedriver.exe', 无痕模式=True, 隐藏窗口=False, 隐藏自动化提示=True, 隐藏滚动条=False, 禁止加载图片=False, 禁用插件=False,
             禁止Javascript=False, 禁用JAVA=False, 禁止密码保存提示=True, 禁用弹窗=False, 禁止策略化=False, 初始运行=False, 沙盒运行=True,
             协议头='mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/85.0.4183.83 safari/537.36',
             代理='', 编码='lang=zh_CN.UTF-8', 规避BUG=False, 谷歌浏览器路径=''):
        '代理格式：127.0.0.1:8888  带账号密码验证的自行百度修改'
        options = webdriver.ChromeOptions()
        if 无痕模式:
            options.add_argument('--incognito')
        if 隐藏窗口:
            options.add_argument('--headless')
        if 隐藏自动化提示:
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
        if 隐藏滚动条:
            options.add_argument('--hide-scrollbars')
        if 禁止加载图片:
            options.add_argument('blink-settings=imagesEnabled=false')
        if 禁用插件:
            options.add_argument('--disable-plugins')
        if 禁止Javascript:
            options.add_argument('--disable-javascript')
        if 禁止密码保存提示:
            prefs = {}
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            options.add_experimental_option("prefs", prefs)
        if 禁止策略化:
            options.add_argument('--disable-infobars')
        if 禁用弹窗:
            options.add_argument('--disable-popup-blocking')
        if 禁用JAVA:
            options.add_argument('–disable-java')
        if not 沙盒运行:
            options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        if 协议头:
            options.add_argument('User-Agent=' + 协议头)
        if 编码:
            options.add_argument(编码)
        if 规避BUG:
            options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        if 代理:
            options.add_argument('--proxy-server=http://' + 代理)
        if 谷歌浏览器路径:
            options.binary_location = 谷歌浏览器路径
        if 初始运行:
            options.add_argument('–first run')

        self.标识 = webdriver.Chrome(驱动路径, chrome_options=options)
        return True

    @异常处理返回类型逻辑型
    def 进入网页(self, URL, 隐藏Navigator=True):
        '当前页面跳转到新页面，url需要带上http开头'
        self.标识.get(URL)
        if 隐藏Navigator:
            script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
            self.标识.execute_script(script)
        return True

    @异常处理返回类型逻辑型
    def 取页面标题(self):
        return self.标识.title

    @异常处理返回类型逻辑型
    def 取页面链接(self):
        return self.标识.current_url

    @异常处理返回类型逻辑型
    def 取页面源码(self):
        return self.标识.page_source

    @异常处理返回类型逻辑型
    def 关闭当前页面(self):
        '如果只有一个页面标签则会关闭浏览器'
        self.标识.close()
        return True

    @异常处理返回类型逻辑型
    def 关闭浏览器(self):
        self.标识.quit()
        return True

    @异常处理返回类型逻辑型
    def 全屏(self):
        '等于按了F11 浏览器窗口全屏显示'
        self.标识.fullscreen_window()
        return True

    @异常处理返回类型逻辑型
    def 置浏览器宽高(self, 宽度, 高度):
        self.标识.set_window_size(宽度, 高度)
        return True

    @异常处理返回类型逻辑型
    def 后退(self):
        '控制浏览器后退'
        self.标识.back()
        return True

    @异常处理返回类型逻辑型
    def 前进(self):
        '控制浏览器前进'
        self.标识.forward()
        return True

    @异常处理返回类型逻辑型
    def 刷新页面(self):
        self.标识.refresh()
        return True

    @异常处理返回类型逻辑型
    def 进入Frame页面(self, Frame标识):
        "默认可以直接取表单的id 或name属性。如果iframe没有可用的id和name属性可以通过定位获取的标识直接传入"
        self.标识.switch_to.frame(Frame标识)
        return True

    @异常处理返回类型逻辑型
    def 退出Frame页面(self):
        self.标识.switch_to.default_content()
        return True

    @异常处理返回类型逻辑型
    def 取所有页面句柄(self):
        '返回所有窗口的句柄到当前会话'
        return self.标识.window_handles

    @异常处理返回类型逻辑型
    def 取当前页面句柄(self):
        '获得当前窗口句柄'
        return self.标识.current_window_handle

    @异常处理返回类型逻辑型
    def 切换页面(self, 页面句柄):
        '用于不同窗口的切换'
        self.switch_to.window(页面句柄)
        return True

    @异常处理返回类型逻辑型
    def 提示框_同意(self):
        '接受现有警告框'
        self.标识.switch_to.alert.accept()
        return True

    @异常处理返回类型逻辑型
    def 提示框_取消(self):
        '解散现有警告框'
        self.标识.switch_to.alert.dismiss()
        return True

    @异常处理返回类型逻辑型
    def 提示框_发送文本(self, 内容):
        '发送文本至警告框。keysToSend：将文本发送至警告框'
        self.标识.switch_to.alert.send_keys(内容)
        return True

    @异常处理返回类型逻辑型
    def 提示框_取文本(self):
        '返回 alert/confirm/prompt 中的文字信息'
        return self.标识.switch_to.alert.text

    @异常处理返回类型逻辑型
    def 提示框_置焦点(self):
        '返回 alert/confirm/prompt 中的文字信息'
        return self.标识.switch_to.alert()

    @异常处理返回类型逻辑型
    def 元素定位_id(self, id, 匹配多个=False):
        '通过元素id定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_id(id)]
        结果 = self.标识.find_element_by_id(id)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_name(self, name, 匹配多个=False):
        '通过元素name定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_name(name)]
        结果 = self.标识.find_element_by_name(name)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_xpath(self, xpath, 匹配多个=False):
        '通过xpath表达式定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_xpath(xpath)]
        结果 = self.标识.find_element_by_xpath(xpath)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_link_text(self, text, 匹配多个=False):
        '通过完整超链接定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_link_tex(text)]
        结果 = self.标识.find_element_by_link_text(text)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_partial_link_text(self, text, 匹配多个=False):
        '通过部分链接定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_partial_link_text(text)]
        结果 = self.标识.find_element_by_partial_link_text(text)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_tag_name(self, tagname, 匹配多个=False):
        '通过标签定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_tag_name(tagname)]
        结果 = self.标识.find_element_by_tag_name(tagname)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_class_name(self, name, 匹配多个=False):
        '通过类名进行定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_class_name(name)]
        结果 = self.标识.find_element_by_class_name(name)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 元素定位_css_selector(self, css, 匹配多个=False):
        '通过css选择器进行定位,匹配多个则返回对象列表'
        if 匹配多个:
            return [填表元素操作(self.标识, x) for x in self.标识.find_elements_by_css_selector(css)]
        结果 = self.标识.find_elements_by_css_selector(css)
        if 结果:
            return 填表元素操作(self.标识, 结果)

    @异常处理返回类型逻辑型
    def 清除文本(self):
        self.标识.clear()
        return True

    @异常处理返回类型逻辑型
    def 最大化(self):
        "浏览器窗口最大化"
        self.标识.maximize_window()
        return True

    @异常处理返回类型逻辑型
    def 最小化(self):
        "浏览器窗口最小化"
        self.标识.minimize_window()
        return True

    @异常处理返回类型逻辑型
    def 取浏览器名称(self):
        "查看浏览器的名字"
        return self.标识.name

    @异常处理返回类型逻辑型
    def 取窗口坐标(self):
        "获取当前窗口的坐标"
        return self.标识.get_window_position()

    @异常处理返回类型逻辑型
    def 取窗口矩形(self):
        "获取窗口的x，y坐标以及当前窗口的高度和宽度"
        return self.标识.get_window_rect()

    @异常处理返回类型逻辑型
    def 取窗口宽高(self):
        "获取当前窗口的尺寸"
        return self.标识.get_window_size()

    @异常处理返回类型逻辑型
    def 取所有Cookie(self):
        '获得所有cookie信息'
        return self.标识.get_cookies()

    @异常处理返回类型逻辑型
    def 取指定Cookie(self, name):
        '返回字典的key为“name”的cookie信息'
        return self.标识.get_cookie(name)

    @异常处理返回类型逻辑型
    def 添加Cookie(self, cookie_dict):
        '添加cookie。“cookie_dict”指字典对象，必须有name 和value 值'
        self.标识.add_cookie(cookie_dict)
        return True

    @异常处理返回类型逻辑型
    def 删除指定Cookie(self, name):
        '删除cookie信息。“name”是要删除的cookie的名称'
        self.标识.delete_cookie(name)
        return True

    @异常处理返回类型逻辑型
    def 删除所有Cookie(self):
        '删除所有cookie信息'
        self.标识.delete_all_cookies()
        return True

    @异常处理返回类型逻辑型
    def 运行JS(self, *args):
        '执行js代码,算加密需要自己声明调用的对象'
        return self.标识.execute_script(*args)

    @异常处理返回类型逻辑型
    def 运行JS_异步(self, *args):
        '执行js代码'
        return self.标识.execute_async_script(*args)

    @异常处理返回类型逻辑型
    def 新建页面(self, URL):
        '通过javascript打开新页面'
        js = "window.open('{}')".format(URL)
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 置滚动条位置(self, 横向=0, 纵向=0):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "window.scrollTo({},{});".format(横向, 纵向)
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 滚动条_靠左(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollLeft=0"
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 滚动条_靠右(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollLeft=10000"
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 滚动条_靠顶(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollTop=0"
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 滚动条_靠底(self):
        '通过javascript设置浏览器窗口的滚动条位置'
        js = "var q=document.documentElement.scrollTop=10000"
        self.标识.execute_script(js)
        return True

    @异常处理返回类型逻辑型
    def 窗口_截图_保存(self, 保存地址):
        '将当前窗口的屏幕快照保存到PNG图像文件中'
        self.标识.save_screenshot(保存地址)
        return True

    @异常处理返回类型逻辑型
    def 截图_保存(self, 保存地址):
        '用于截取当前窗口，并把图片保存到本地'
        self.标识.get_screenshot_as_file(保存地址)
        return True

    @异常处理返回类型逻辑型
    def 截图_BASE64(self):
        '以base64编码的字符串获取当前窗口的屏幕快照'
        return self.标识.get_screenshot_as_base64()

    @异常处理返回类型逻辑型
    def 截图_二进制(self):
        '以二进制数据获取当前窗口的屏幕快照。'
        return self.标识.get_screenshot_as_png()

    @异常处理返回类型逻辑型
    def 置页面超时时间(self, 秒数):
        '设置等待页面加载完成的时间'
        self.标识.set_page_load_timeout(秒数)
        return True

    @异常处理返回类型逻辑型
    def 置JS超时时间(self, 秒数):
        '设置脚本在执行过程中应等待的时间'
        self.标识.set_script_timeout(秒数)
        return True

    @异常处理返回类型逻辑型
    def 置浏览器坐标_宽高(self, 左边=None, 顶边=None, 宽度=None, 高度=None):
        '设置窗口的x，y坐标以及当前窗口的高度和宽度。'
        self.标识.set_window_rect(左边, 顶边, 宽度, 高度)
        return True

    @异常处理返回类型逻辑型
    def 鼠标_松开(self):
        '释放按住的鼠标键'
        ActionChains(self.标识).release().perform()
        return True


class 填表元素操作:

    def __init__(self, 浏览器标识, 元素标识):
        self.标识 = 元素标识
        self.浏览器标识 = 浏览器标识

    @异常处理返回类型逻辑型
    def 清除文本(self):
        self.标识.clear()
        return True

    @异常处理返回类型逻辑型
    def 按键_输入(self, *args):
        '模拟按键输入，将密钥发送到当前的焦点元素,包括上传文件可以直接发送文件路径,可使用 按钮_* ,如 按键_输入(按钮_CTRL,"a") 即为全选'
        self.标识.send_keys(*args)
        return True

    @异常处理返回类型逻辑型
    def 按键_指定输入(self, 键值):
        '将键发送到元素,可以使用 按钮_*'
        ActionChains(self.浏览器标识).send_keys_to_element(self.标识, 键值).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_单击(self):
        self.标识.click()
        return True

    @异常处理返回类型逻辑型
    def 提交表单(self):
        '查找到表单（from）直接调用submit即可'
        self.标识.submit()
        return True

    @异常处理返回类型逻辑型
    def 取属性值(self, 属性名称):
        '获取元素属性值,如：value,str,img等属性'
        return self.标识.get_attribute(属性名称)

    @异常处理返回类型逻辑型
    def 取CSS属性值(self, 属性名称):
        '获取CSS属性值'
        return self.标识.value_of_css_property(属性名称)

    @异常处理返回类型逻辑型
    def 取元素坐标(self):
        return self.标识.location

    @异常处理返回类型逻辑型
    def 取元素宽高(self):
        return self.标识.size

    @异常处理返回类型逻辑型
    def 是否显示可见(self):
        '判断元素是否显示'
        return self.标识.is_displayed()

    @异常处理返回类型逻辑型
    def 是否选中(self):
        '判断元素是否选中状态'
        return self.标识.is_selected()

    @异常处理返回类型逻辑型
    def 是否启用(self):
        '判断元素是否是否启用'
        return self.标识.is_enabled()

    @异常处理返回类型逻辑型
    def 取文本内容(self):
        '获取元素的文本'
        return self.标识.text

    @异常处理返回类型逻辑型
    def 取元素标签名称(self):
        '返回元素的tagName'
        return self.标识.tag_name

    @异常处理返回类型逻辑型
    def 鼠标_悬停(self):
        '执行鼠标悬停操作,一些网页鼠标悬停后才会加载下拉列表'
        ActionChains(self.浏览器标识).move_to_element(self.标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_右键单击(self):
        ActionChains(self.浏览器标识).context_click(self.标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_双击(self):
        ActionChains(self.浏览器标识).double_click(self.标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_左键按住(self):
        '按下鼠标左键在一个元素上'
        ActionChains(self.浏览器标识).click_and_hold(self.标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_拖动(self, 目标标识):
        '鼠标_拖动(d.标识)'
        ActionChains(self.浏览器标识).drag_and_drop(self.标识, 目标标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_拖动距离(self, X偏移量, Y偏移量):
        '然后移至目标偏移量并释放鼠标按钮'
        ActionChains(self.浏览器标识).drag_and_drop_by_offset(self.标识, X偏移量, Y偏移量).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_原地偏移(self, X偏移量, Y偏移量):
        '将鼠标移动到当前鼠标位置的偏移处'
        ActionChains(self.浏览器标识).move_by_offset(X偏移量, Y偏移量).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_移到元素中间(self):
        '将鼠标移到元素的中间'
        ActionChains(self.浏览器标识).move_to_element().perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_移动(self, X偏移量, Y偏移量):
        '将鼠标移动指定元素的偏移量'
        ActionChains(self.浏览器标识).move_to_element_with_offset(self.标识, X偏移量, Y偏移量).perform()
        return True

    @异常处理返回类型逻辑型
    def 鼠标_松开(self):
        '释放元素上按住的鼠标键'
        ActionChains(self.浏览器标识).release(self.标识).perform()
        return True

    @异常处理返回类型逻辑型
    def 按键_全选(self):
        self.标识.send_keys(按钮_CTRL, 'a')
        return True

    @异常处理返回类型逻辑型
    def 按键_复制(self):
        self.标识.send_keys(按钮_CTRL, 'c')
        return True

    @异常处理返回类型逻辑型
    def 按键_剪切(self):
        self.标识.send_keys(按钮_CTRL, 'x')
        return True

    @异常处理返回类型逻辑型
    def 按键_粘贴(self):
        self.标识.send_keys(按钮_CTRL, 'v')
        return True

    @异常处理返回类型逻辑型
    def 下拉框_选择值(self, value):
        'select标签的value属性的值'
        Select(self.标识).select_by_value(value)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_选择索引(self, id):
        '下拉框的索引'
        Select(self.标识).select_by_index(id)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_选择文本(self, text):
        '下拉框的文本值'
        Select(self.标识).select_by_visible_text(text)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_全部取消选中(self):
        Select(self.标识).deselect_all()
        return True

    @异常处理返回类型逻辑型
    def 下拉框_取消选中_索引(self, id):
        Select(self.标识).deselect_by_index(id)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_取消选中_值(self, value):
        Select(self.标识).deselect_by_value(value)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_取消选中_文本(self, text):
        Select(self.标识).deselect_by_visible_text(text)
        return True

    @异常处理返回类型逻辑型
    def 下拉框_取全部选中项(self):
        '返回属于此选择标记的所有选择的选项的列表'
        return Select(self.标识).all_selected_options

    @异常处理返回类型逻辑型
    def 下拉框_取选中项(self):
        '该选择标记中的第一个选择的选项（或正常选择中的当前选择的选项）'
        return Select(self.标识).first_selected_option

    @异常处理返回类型逻辑型
    def 下拉框_取列表项(self):
        '返回属于该选择标签的所有选项的列表'
        return Select(self.标识).options

    @异常处理返回类型逻辑型
    def 取元素矩形(self):
        return self.标识.rect

    @异常处理返回类型逻辑型
    def 元素_截图_保存(self, 文件名):
        '将当前元素的屏幕快照保存到PNG图像文件中'
        self.标识.screenshot(文件名)
        return True

    @异常处理返回类型逻辑型
    def 元素_截图_BASE64(self):
        '以base64编码字符串的形式获取当前元素的屏幕快照'
        return self.标识.screenshot_as_base64

    @异常处理返回类型逻辑型
    def 元素_截图_二进制(self):
        '以二进制数据获取当前元素的屏幕截图'
        return self.标识.screenshot_as_png

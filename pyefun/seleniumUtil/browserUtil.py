from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from pyefun import *
import logging
import hashlib

logger = logging.getLogger()


def 取md5(内容):
    """
    计算文本的 MD5 十六进制摘要。

    Args:
        内容 (str): 待计算的文本内容。

    Returns:
        str: 32 位小写十六进制摘要。
    """
    m = hashlib.md5(内容.encode("utf8"))
    return m.hexdigest()


def 浏览器_获取远程chrome(server_url="http://127.0.0.1:4444/wd/hub"):
    """
    连接远程 Selenium Grid 并创建 Chrome WebDriver。

    Args:
        server_url (str): 远程 WebDriver 地址，如 "http://127.0.0.1:4444/wd/hub"。

    Returns:
        selenium.webdriver.Remote: 远程 Chrome 驱动实例。
    """
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['goog:chromeOptions'] = {
        "args": [
            # "--headless",
            # "window-size=1366,768"
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
        ]
    }
    driver = webdriver.Remote(
        command_executor=server_url,
        desired_capabilities=capabilities
    )
    return driver


def 浏览器_获取本地chrome():
    """
    启动本机 Chrome 并返回已配置的 WebDriver。

    Returns:
        selenium.webdriver.Chrome: 本地 Chrome 驱动实例。
    """
    opt = webdriver.ChromeOptions()
    # opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    # opt.add_argument("blink-settings=imagesEnabled=false")
    opt.add_argument(
        "user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'")
    # opt.add_argument('--proxy-server=http://%s' % "127.0.0.1:11111")
    driver = webdriver.Chrome(options=opt)

    return driver


def 浏览器_获取本地Firefox():
    """
    启动本机 Firefox 并返回已配置的 WebDriver（无头模式）。

    Returns:
        selenium.webdriver.Firefox: 本地 Firefox 驱动实例。
    """
    opt = webdriver.FirefoxOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument("blink-settings=imagesEnabled=false")
    opt.add_argument(
        "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
    driver = webdriver.Firefox(options=opt)
    return driver


def 浏览器_是否就绪(远程浏览器地址="http://127.0.0.1:4444/wd/hub"):
    """
        while 浏览器_是否就绪(远程浏览器地址) == False:
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


def 浏览器窗口最大化(driver):
    """
    尝试最大化浏览器窗口，若不支持则回退到设置 1920x1080 尺寸。

    Args:
        driver (selenium.webdriver.remote.webdriver.WebDriver): 浏览器驱动。
    """
    try:
        driver.maximize_window()
    except WebDriverException as e:
        driver.set_window_size(1920, 1080)  # 如果最大化失败，设置窗口大小为 1920*1080


def get_path_exists(path):
    """
    返回给定路径列表中第一个存在的路径，否则返回空字符串。

    Args:
        path (Iterable[str]): 待检测的候选路径集合。

    Returns:
        str: 第一个存在的路径；若均不存在，返回空字符串。
    """
    for v in path:
        if os.path.exists(v):
            return v
    return ''


chromeDriverPath = ""
chromeBinaryLocation = ""


def 浏览器_函数计算环境初始化():
    """
    在无头环境（如云函数 / Docker）中初始化 Chrome 运行所需的二进制与驱动。

    - 自动在常见路径中查找 headless-chromium 与 chromedriver。
    - 若无执行权限，则复制到 /tmp 并授权后再使用。

    Returns:
        str | bool: 初始化结果说明；在 Windows 上返回 False。
    """
    if 系统_是否为window系统():
        return False
    global chromeDriverPath
    global chromeBinaryLocation
    if (chromeDriverPath != ""):
        return "浏览器环境已加载"
    # chromeDriverPath = "/opt/chrome86/chromedriver"
    # chromeBinaryLocation = "/opt/chrome86/headless-chromium"
    # data = 运行(chromeDriverPath+" --version") # 调试驱动是否正常
    # logger.info(data)
    # return data
    # return os.listdir("/opt/") # 查看文件是否部署到位

    chromeDriverPath = get_path_exists([
        "./chromedriver",
        "/opt/chromedriver",
        "./chrome86/chromedriver",
        "/opt/chrome86/chromedriver",
        "./chrome69/chromedriver",
        "/opt/chrome69/chromedriver",
    ])
    chromeBinaryLocation = get_path_exists([
        "./headless-chromium",
        "/opt/headless-chromium",
        "./chrome86/headless-chromium",
        "/opt/chrome86/headless-chromium",
        "./chrome69/headless-chromium",
        "/opt/chrome69/headless-chromium",
    ])
    # print("chromeDriverPath:%s" % chromeDriverPath)
    # print("chromeBinaryLocation:%s " % chromeBinaryLocation)
    if chromeDriverPath == "" or chromeBinaryLocation == "":
        exit("浏览器或驱动不存在")

    if os.access(chromeDriverPath, os.X_OK) == False or os.access(chromeBinaryLocation, os.X_OK) == False:
        # 如果没有执行权限那么复制到/tmp目录赋予执行权限
        chromeDriverPathTmp = "/tmp/chromedriver"
        chromeBinaryLocationTmp = "/tmp/headless-chromium"
        shutil.copyfile(chromeDriverPath, chromeDriverPathTmp)
        shutil.copyfile(chromeBinaryLocation, chromeBinaryLocationTmp)
        chromeDriverPath = chromeDriverPathTmp
        chromeBinaryLocation = chromeBinaryLocationTmp
        os.chmod(chromeDriverPath, 0o0700)
        os.chmod(chromeBinaryLocation, 0o0700)
    return "浏览器环境初始化完成"


def 输出(str):
    """
    根据运行平台输出日志：Windows 直接 print，其他平台使用标准 logger。

    Args:
        str (str): 输出文本。
    """
    if 系统_是否为window系统():
        print(str)
    else:
        logger.info(str)


def 浏览器_自动获取chrome():
    """
    根据当前运行环境自动创建 Chrome WebDriver。

    - 在 Windows 上直接返回本地 Chrome 驱动。
    - 在 Linux/Serverless 环境中使用 headless-chromium 与 chromedriver。

    Returns:
        selenium.webdriver.Chrome: Chrome 驱动实例。
    """
    global chromeDriverPath
    global chromeBinaryLocation
    if 系统_是否为window系统():
        return 浏览器_获取本地chrome()
    """
    用方便地将chrome 部署到部署到云上 方便 selenium的使用

    阿里云函数计算 腾讯云函数 linux docker中均可直接运行部署

    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1366x768')
    # chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    # chrome_options.add_argument('--enable-logging')
    # chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--single-process')
    # chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--homedir=/tmp')
    # chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')

    chrome_options.binary_location = chromeBinaryLocation

    chrome = webdriver.Chrome(chromeDriverPath, options=chrome_options)
    return chrome


if __name__ == '__main__':
    pass
    # 远程浏览器地址 = "http://127.0.0.1:4444/wd/hub"
    # while 浏览器_是否就绪(远程浏览器地址) == False:
    #     延时(1)
    #     print("浏览器未就绪")
    #
    # driver = 浏览器_获取远程chrome(远程浏览器地址)

    driver = 浏览器_获取本地chrome()
    data = driver.get("https://www.baidu.com")
    # print(data)
    # print(driver.find_element_by_xpath("//html").text)
    print(driver.find_elements_by_xpath("//html")[0].text)
    # print(driver.title)
    # print(driver.name)
    driver.quit()

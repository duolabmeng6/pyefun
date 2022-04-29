from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from pyefun import *
import logging
import hashlib

logger = logging.getLogger()


def 取md5(内容):
    m = hashlib.md5(内容.encode("utf8"))
    return m.hexdigest()


def 浏览器_获取远程chrome(server_url="http://127.0.0.1:4444/wd/hub"):
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
    try:
        driver.maximize_window()
    except WebDriverException as e:
        driver.set_window_size(1920, 1080)  # 如果最大化失败，设置窗口大小为 1920*1080


def get_path_exists(path):
    for v in path:
        if os.path.exists(v):
            return v
    return ''


chromeDriverPath = ""
chromeBinaryLocation = ""


def 浏览器_函数计算环境初始化():
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
    if 系统_是否为window系统():
        print(str)
    else:
        logger.info(str)


def 浏览器_自动获取chrome():
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

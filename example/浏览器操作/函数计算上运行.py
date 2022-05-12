# -*- coding: utf-8 -*-
import logging
import os
from selenium import webdriver


def 运行(cmd):
    p = os.popen(cmd)
    x = p.read()
    p.close()
    return x


def handler(event, context):
    #chromeDriverPath = "./69_2.43_chrome/chromedriver"
    #chromeBinaryLocation = "./69_2.43_chrome/headless-chromium"

    chromeDriverPath = "./86_chrome/chromedriver"
    chromeBinaryLocation = "./86_chrome/headless-chromium"
    logger = logging.getLogger()
    #return 运行(chromeDriverPath+" --version")
    # return 运行("pwd")
    # return os.listdir("./")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1366x768')
    #chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    #chrome_options.add_argument('--enable-logging')
    #chrome_options.add_argument('--log-level=0')
    #chrome_options.add_argument('--single-process')
    #chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    #chrome_options.add_argument('--homedir=/tmp')
    #chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    chrome_options.binary_location = chromeBinaryLocation

    chrome = webdriver.Chrome(chromeDriverPath,
                              options=chrome_options)
    print(chrome)

    data = chrome.get("https://www.baidu.com")

    print(data)
    print(chrome.find_element_by_xpath("//html").text)

    logger.info(chrome.find_element_by_xpath("//html").text)
    logger.info('hello world')

    return chrome.title


#handler("", "")

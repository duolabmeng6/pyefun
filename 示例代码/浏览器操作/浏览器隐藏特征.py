from pyefun import *
from pyefun.seleniumUtil import *

浏览器初始化本地环境()
浏览器 = 浏览器类()
浏览器.打开chrome()
浏览器.浏览网页("https://bot.sannysoft.com/")
浏览器.隐藏特征()
延时(5)
写到文件("./result.html",浏览器.取页面源码())
浏览器.退出()

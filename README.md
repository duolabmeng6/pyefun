# pyefun 易函数 最好用的中文编程类库

[![github stars](https://img.shields.io/github/stars/duolabmeng6/pyefun?style=social)](https://github.com/duolabmeng6/pyefun)
[![gitee stars](https://gitee.com/duolabmeng666/pyefun/badge/star.svg?theme=dark)](https://gitee.com/duolabmeng666/pyefun/stargazers)
[![Documentation Status](https://readthedocs.org/projects/pyefun/badge/?version=latest)](https://pyefun.readthedocs.io/zh_CN/latest/?badge=latest)
[![pipy](https://github.com/duolabmeng6/pyefun/actions/workflows/python-publish.yml/badge.svg)](https://github.com/duolabmeng6/pyefun/actions/workflows/python-publish.yml)
[![test](https://github.com/duolabmeng6/pyefun/actions/workflows/python-app.yml/badge.svg)](https://github.com/duolabmeng6/pyefun/actions/workflows/python-app.yml)
[![pypi](https://img.shields.io/pypi/v/pyefun.svg)](https://pypi.org/project/pyefun/)

为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数

# 易函数的愿景

* 愿世界上没有难用的编程语言
* 易函数是为了抹平不同编程语言之间的差异使中国人，可以快速上手软件开发
* 易函数不是翻译各个编程语言的类库，而是将最实用的功能通过中文直观地展示出来，使其符合中国人的思维逻辑
* 易函数并不局限于编程语言，所有的编程语言都可以编写易函数并使用易函数
* 易函数已经开发 go语言( [goefun](https://github.com/duolabmeng6/goefun) ) python语言( [pyefun](https://github.com/duolabmeng6/pyefun) ) 未来主流的编程语言都能拥有易函数如（ java语言( [javaefun](https://github.com/duolabmeng6/javaefun) )，c#，c++，php，js）
* 愿更多的国人参与到efun（易函数）的开发中，让世界没有难用的编程语言
* 易函数，以开源，开放，合作，共赢的姿态，迎接中文编程开发者的反哺，易函数的使用者，最终会变成易函数的开发者，持续贡献优秀的代码，形成良好的循环
* 易函数，将打造为是一款模块化、高性能、企业级的python基础开发框架

# 易函数的优势

- 易函数兼容所有 python 运行环境 `window` `macOS` `linux` `ubuntu` `centos` ，支持 docker 部署
- 全中文函数名和注释 以（易语言核心支持库，火山类库，精易模块）命名风格极大地降低了使用门槛
- 超 `1000+` 中文实用函数，涵盖所有技术领域应用（深度学习，图像处理，文字处理，自动化测试），全面简化 python 开发和学习的门槛
- 易函数中所有命令通过均经过测试用例 100% 放心使用，查看测试用例后立即上手使用
- 超丰富的文本处理函数，正则表达式，简单易用快速上手
- 简单易用的线程池，协程池，大大地降低使用的技术门槛
- 最好用的编码转换功能，自动检测编码，自动转换到对应编码
- 超方便的excel操作函数，极大地降低了大数据处理的难度
- 易函数提供一键编译功能将任意python代码，转换为 c 编译的可执行程序
- 易函数界面库为 [qtefun](https://github.com/duolabmeng6/qtefun) 封装以易语言组件库命名开发，降低使用门槛
- `Qt视窗设计器` 配备完整的视窗软件开发生态集成 `开发` `编译` `可视化界面设计` 轻松拖拽组件设计界面，一键编译发布。 支持跨平台可视化窗口程序开发，`window`  `mac OS`  `ubuntu` ，实现一套代码多端运行。

# 文档

* [易函数使用示例代码](https://github.com/duolabmeng6/pyefun/tree/master/示例代码)
* [用易函数将任意python文件编译为exe](https://www.kancloud.cn/duolabmeng/pyefundoc/2334421)
* [用易函数视窗编程系统开发一键编译任意python脚本工具](https://www.kancloud.cn/duolabmeng/pyefundoc/2334755)
* [如何贡献代码到pyefun中教程](https://www.kancloud.cn/duolabmeng/pyefundoc/2335299)

每个模块都有中文注释请阅读源码



# 模块列表

```python
# ========== 核心支持库命令 ==========
from pyefun.核心支持库.算数运算 import *
from pyefun.核心支持库.数组操作 import *
from pyefun.核心支持库.编码转换 import *
from pyefun.核心支持库.磁盘操作 import *
from pyefun.核心支持库.公用函数 import *
from pyefun.核心支持库.文本操作 import *
from pyefun.核心支持库.系统处理 import *
from pyefun.核心支持库.日期时间操作 import *
from pyefun.核心支持库.类型转换 import *
from pyefun.核心支持库.时钟 import *
# ========== 核心支持库命令 ==========

# ========== 核心易函数支持库 ==========
from pyefun.核心易函数支持库.实用函数 import *
from pyefun.核心易函数支持库.文本操作实用函数 import *
from pyefun.核心易函数支持库.正则表达式 import *
from pyefun.核心易函数支持库.正则表达式实用函数 import *
from pyefun.核心易函数支持库.网络请求 import *  # 易函数易用的请求模块
from pyefun.核心易函数支持库.时间统计 import *
from pyefun.核心易函数支持库.线程操作 import *
from pyefun.核心易函数支持库.进程池 import *
from pyefun.核心易函数支持库.json函数 import *
from pyefun.核心易函数支持库.环境变量 import *
from pyefun.核心易函数支持库.配置项 import *
from pyefun.核心易函数支持库.网络实用函数 import *
# ========== 核心易函数支持库 ==========


# ========== 模块 ==========
# from pyefun.模块.javascript引擎 import *  # 执行js脚本
# from pyefun.模块.二维码 import *  # 二维码解析
# from pyefun.模块.剪切板操作 import *  # 剪切板操作
# from pyefun.模块.协程池 import *  # 原生协程池
# from pyefun.模块.协程池Gevent import *  # Gevent协程池
# from pyefun.模块.窗口操作 import *  # 窗口操作
# from pyefun.模块.进度显示 import *  # 进度显示
# from pyefun.模块.缓存工具 import *  # 缓存工具
# from pyefun.模块.邮件 import *  # 邮件
# from pyefun.模块.定时任务 import *  # 定时任务
# from pyefun.模块.winapi import *  # window api
# from pyefun.模块.通用实用函数 import *  # ubelt 封装的实用函数
# from pyefun.模块.苹果系统操作 import *  # 关于苹果系统的函数
# from pyefun.模块.终端类 import *  # 命令输入输出的模块
# ========== 模块 ==========

# ========== 编码解码 ==========
# from pyefun.编码解码.gzip解压缩 import * # gzip 解压缩
# from pyefun.编码解码.zlib解压缩 import * # zlib 解压缩
# from pyefun.编码解码.zip解压缩 import * # zip 解压缩
# from pyefun.编码解码.binary编码解码 import * # 二进制 编码解码
# from pyefun.编码解码.base64编码解码 import * # base64 编码解码
# from pyefun.编码解码.url编码解码 import * # URL 编码解码
# ========== 编码解码 ==========

# ========== 数据库 ==========
# from pyefun.数据库.redis工具类 import * # redis
# from pyefun.数据库.mysql数据库 import * # mysql数据库
# from pyefun.数据库.mongo数据库 import * # mongo数据库
# from pyefun.数据库.peeweeUtil import * # peeweeUtil
# ========== 数据库 ==========

# ========== excel操作 ==========
# from pyefun.excel.excel_xlwr import * # excel操作模块 选其中一个使用即可
# from pyefun.excel.excel_openpyxl import * # excel操作模块 选其中一个使用即可
# ========== excel操作 ==========

# ========== 浏览器自动化操作 ==========
# from pyefun.seleniumUtil import * # 浏览器自动化测试
# ========== 浏览器自动化操作 ==========

# ========== 阿里云SDK ==========
# from pyefun.阿里云SDK.fc.fc import *  # 阿里云函数计算操作
# from pyefun.阿里云SDK.oss.oss import *  # 阿里云oss操作sdk
# ========== 阿里云SDK ==========

# ========== 人工智能 ==========
# from pyefun.人工智能.ONNX分类模型推理 import *  # ONNX分类模型推理
# from pyefun.人工智能.通用文字识别 import *  # 提供通用的中文文字识别功能
# ========== 人工智能 ==========

# ========== 图像处理 ==========
# from pyefun.图像处理 import *  # 图片处理 cv2 以及 pil 的工具类
# from pyefun.图像处理.图像处理 import * # opencv 工具类
# from pyefun.图像处理.图像处理PIL import * # pil 工具类
# ========== 图像处理 ==========
```





# 安装

正式版本(稳定) 定期更新

正式版本 https://pypi.org/project/pyefun/

```
pip install pyefun
```



测试版本 实时更新 如有bug请及时反馈

测试版本 https://test.pypi.org/project/pyefun/

```
pip install -i https://test.pypi.org/simple/ pyefun
```

# 使用

```python
from pyefun import *
```

[易函数使用示例代码](https://github.com/duolabmeng6/pyefun/tree/master/示例代码)

[查看 pyefun 中可导入使用的模块](https://github.com/duolabmeng6/pyefun/blob/master/pyefun/__init__.py)

例如我需要使用通用文字识别 需要安装 ppppocr `pip install ppppocr` 再引入模块 `pyefun.人工智能.通用文字识别` 就可以使用了

```python
from pyefun.人工智能.通用文字识别 import *
```

例如我需要正则表达式 加载ini配置项 加载环境变量文件 selenium浏览器自动化测试 也是同样的道理

```python
# from pyefun.模块.javascript引擎 import *  # 执行js脚本
# from pyefun.模块.二维码 import *  # 二维码解析
# from pyefun.模块.协程池 import *  # 原生协程池
# from pyefun.编码解码.zip解压缩 import * # zip 解压缩
# from pyefun.seleniumUtil import * # 浏览器自动化测试
```


> 提示: 如果你的程序是需要编译为exe的必须使用`import pyefun as efun` 而不能是`import *` 
> [Nuitka python工具使用教程](https://zhuanlan.zhihu.com/p/133303836)

# Qt视窗设计器 [QtEasyDesigner](https://github.com/duolabmeng6/QtEasyDesigner)

一款为中国人入门 python 编程的产品

配备完整的视窗软件开发生态集成 `开发` `编译` `可视化界面设计` 轻松拖拽组件设计界面，一键编译发布。

支持跨平台可视化窗口程序开发，`window`  `mac OS`  `ubuntu` ，实现一套代码多端运行。


## 优势

* **会中文就看得懂**，中文编程，得天独厚，简单，易用。
* **最强开发工具** `Pycharm` 中文软件界面，拼音输入，智能提示。
* **界面设计器**，易函数视窗可视化设计器，轻松拖拽组件，设计界面，所见即所得。
* **中文函数库**， [qtefun](https://github.com/duolabmeng6/qtefun) 全中文函数库，专门为 qt 封装的中文组件，以易语言核心支持库组件库为标准封装的界面库，组件的方法，属性，事件，都是令人熟悉的命名。
* **组件中文命名** 易于理解和使用
* **一键编译**，可执行程序， 支持跨平台编译`window` `macOS` `linux`，易函数提供一键编译功能将任意python代码，转换为 c 编译的可执行程序。

![](https://github.com/duolabmeng6/QtEasyDesigner/raw/main/images/img1.png)

![](https://github.com/duolabmeng6/QtEasyDesigner/raw/main/images/img2.png)




# 安装ide代码提示插件

pycharm 在插件中搜索 chinese 安装两个插件，界面中文汉化语言包和 [拼音提示插件](https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper)


![code](./docs/source/_static/show.png)
![code](./docs/source/_static/efun_view_system/9.png)



# 欢迎加入易函数，参与贡献：提意见、Issue与文档

易函数是开源的、免费的软件，这意味着任何人都可以为其开发和进步贡献力量。易函数的项目源代码目前同时托管在 github（主库）和 gitee（国内）平台上，两个平台的仓库保持即时的同步，代码贡献统一使用github主库。我们非常欢迎有更多的朋友加入到易函数的开发中来，你为易函数所做出的任何贡献都将会被记录到易函数的史册中。

贡献代码请提交到github主库 码云仓库仅作为镜像

github (主库) : https://github.com/duolabmeng6/pyefun

码云 : https://gitee.com/duolabmeng666/pyefun

qq群 : 1017240979

# 参与开源

积极的开发者将获得 jetbrains 全家桶授权一年期~需要积极提交代码即可申请

## 视频讲解如何贡献代码

[如何贡献代码到 pyefun 中 文字教程](https://www.kancloud.cn/duolabmeng/pyefundoc/2335299)


## 参与贡献

易函数代码：参与易函数功能开发、单元测试、ISSUE提交、反馈建议等等，https://github.com/duolabmeng6/pyefun

开发文档：参与WIKI文档的撰写，便于更多的人了解、热爱并加入易函数的开发。

## 贡献流程

首先fork一份仓库代码到自己的版本库中；

在自己的版本库中新建开发分支并对代码做修改，随后提交修改到自己的版本库；

在自己的版本库中创建一个pull request，源分支选择自己的开发分支，目标分支选择主库的master分支：https://help.github.com/en/articles/creating-a-pull-request

提交pull request请求，随后等待由项目的开发作者对提交内容做审核，审核通过之后你将成为易函数的成员之一；

恭喜你，你的名字将永久地载入到易函数源代码的贡献列表中；

## 协作约定

1. 函数名**必须**使用直观易用的**中文命名**。请参考易语言的支持库命名，精易模块、火山开发平台的中文函数命名方式
2. 注释**必须**包括**使用方法**，**代码示例**，**注意事项** ，如果逻辑复杂的程序部分需要阐述实现思路
3. **必须**编写**测试用例**。如此运行单个用例：`$ python -m unittest pyefun.regexpUtil_test`
4. 请保持 Windows、Linux 的兼容性。如果是 Windows 的专有函数不要引入公共库 `pyefun/__init__.py` 中，可参考`pyefun/asyncPoolGevent`、`pyefun/javscript` 的方法封装，使用时单独引入即可
5. 贡献代码时 **务必** 检查代码是否运行正常。
   

请通过github贡献代码。或者通过提交 issues 的方式贡献代码亦可，贡献代码方式多种多样。


# 项目推荐

* [goefun (go易函数) 为golang提供强大且易用的中文函数库，易语言go函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数](https://github.com/duolabmeng6/goefun)

* [ide中文拼音提示插件](https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper)

* [QtEasyDesigner qt视窗设计器](https://github.com/duolabmeng6/QtEasyDesigner)

* [qtefun qt中文组件库](https://github.com/duolabmeng6/qtefun)

# 学习交流

[精易论坛](https://bbs.125.la/forum.php?mod=viewthread&tid=14681745)

# 感谢

<a href="https://www.jetbrains.com/?from=pyefun"><img src="https://goframe.org/download/thumbnails/1114119/jetbrains.png" height="120" alt="JetBrains"/></a>

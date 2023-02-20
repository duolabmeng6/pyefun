# pyefun 易函数 最好用的中文编程类库

[![github stars](https://img.shields.io/github/stars/duolabmeng6/pyefun?style=social)](https://github.com/duolabmeng6/pyefun)
[![gitee stars](https://gitee.com/duolabmeng666/pyefun/badge/star.svg?theme=dark)](https://gitee.com/duolabmeng666/pyefun/stargazers)
[![pipy](https://github.com/duolabmeng6/pyefun/actions/workflows/python-publish.yml/badge.svg)](https://github.com/duolabmeng6/pyefun/actions/workflows/python-publish.yml)
[![test](https://github.com/duolabmeng6/pyefun/actions/workflows/python-app.yml/badge.svg)](https://github.com/duolabmeng6/pyefun/actions/workflows/python-app.yml)
[![pypi](https://img.shields.io/pypi/v/pyefun.svg)](https://pypi.org/project/pyefun/)

pyefun是一个易用的中文函数类库，它封装了易语言核心支持库的所有功能，并提供简单实用的函数，有效提高Python开发效率。我们致力于打造一个模块化、高性能、企业级的Python基础开发框架，让编程变得更加简单易懂。

我们的愿景是让编程变得无难度，使中国人能够轻松学习并掌握不同编程语言的软件开发。我们不仅仅是简单地翻译各种编程语言的类库，更是通过汉语文字直观地表达最实用的功能，符合中国人的思维逻辑，让学习编程变得更加顺畅。

我们已经开发了 Go( [goefun](https://github.com/duolabmeng6/goefun) ) 的版本，未来计划支持其他主流编程语言，如Java( [javaefun](https://github.com/duolabmeng6/javaefun) )、C#、C++、PHP和JS等。

#### 易函数具有以下优势：

1. 跨平台兼容性强，能够在 Windows、MacOS、Linux、Ubuntu 和 Centos 等系统上运行。
2. 所有函数名和注释采用中文，易于理解和使用。
3. 提供企业级实用功能类库，包括深度学习、图像处理、文字处理、自动化测试等，简化 Python 开发和学习的门槛。
4. 所有命令都通过测试用例，100%可靠，使用起来非常方便。
5. 提供一键编译功能，使应用的发布变得轻松简单。
6. 使用最新的 Qt 技术构建视窗软件，提供全中文的组件和函数，实现一套代码多端运行，适用于跨平台应用。


# 文档

* [易函数使用示例代码](https://github.com/duolabmeng6/pyefun/tree/master/示例代码)
* [用易函数将任意python文件编译为exe](https://www.kancloud.cn/duolabmeng/pyefundoc/2334421)
* [用易函数视窗编程系统开发一键编译任意python脚本工具](https://www.kancloud.cn/duolabmeng/pyefundoc/2334755)
* [如何贡献代码到pyefun中教程](https://www.kancloud.cn/duolabmeng/pyefundoc/2335299)

每个模块都有中文注释请阅读源码



# 安装

正式版本 定期更新

```
pip install pyefun
```

升级 pyefun

```
pip install --upgrade pyefun
```

安装最新版 如有bug请及时反馈

```
git clone https://github.com/duolabmeng6/pyefun.git
cd pyefun
python setup.py install
```

# 卸载

```
pip uninstall pyefun
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

## 关于编译

### Pyinstaller

```
pip install auto-py-to-exe
```

启动 Auto PY to EXE

```powershell
auto-py-to-exe
```

安装参数填入即可

### Nuitka 

如果你的程序是需要 Nuitka 编译为exe的必须使用`import pyefun as efun` 而不能是`import *` 否则将会出现编译后无法打开的情况 需要编译的代码也需要遵循此规范

[Nuitka python工具使用教程](https://zhuanlan.zhihu.com/p/133303836)

也可以使用我开发的一键编译工具自动处理各种问题 [一键编译任意python脚本工具](https://www.kancloud.cn/duolabmeng/pyefundoc/2334755)



## 模块列表

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



# Qt视窗设计器 [QtEasyDesigner](https://github.com/duolabmeng6/QtEasyDesigner)

这款产品是专门为中国人入门Python编程打造的。它配备了完整的视窗软件开发生态，集成了开发、编译、可视化界面设计，让用户轻松拖拽组件设计界面，并一键编译发布。

产品支持跨平台可视化窗口程序开发，包括`Windows`、`macOS`和`Ubuntu`，实现了一套代码多端运行的功能。
其优势在于：

- 中文编程，使用方便，易于上手；
- 配备最强开发工具——`PyCharm`中文软件界面，支持拼音输入和智能提示；
- 提供界面设计器，易函数视窗可视化设计器，让用户轻松拖拽组件设计界面，所见即所得；
- 中文函数库——[qtefun](https://github.com/duolabmeng6/qtefun)，全中文函数库，专门为Qt封装的中文组件，组件的方法、属性、事件等都是采用易语言核心支持库组件库为标准封装的，使得用户更容易理解和使用；
- 组件采用中文命名，易于理解和使用；
- 提供一键编译功能，将任意Python代码转换为C编译的可执行程序，支持跨平台编译`Windows`、`macOS`、`Linux`。


![](https://github.com/duolabmeng6/QtEasyDesigner/raw/main/images/img1.png)

![](https://github.com/duolabmeng6/QtEasyDesigner/raw/main/images/img2.png)




# 安装ide代码提示插件

pycharm 在插件中搜索 chinese 安装两个插件，界面中文汉化语言包和 [拼音提示插件](https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper)



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

* [goefun (go易函数) 完整的封装了易语言核心支持库所有功能，和简单易用的函数](https://github.com/duolabmeng6/goefun)

* [ide中文拼音提示插件](https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper)

* [QtEasyDesigner qt视窗设计器](https://github.com/duolabmeng6/QtEasyDesigner)

* [qtefun qt中文组件库](https://github.com/duolabmeng6/qtefun)

# 学习交流

[精易论坛](https://bbs.125.la/forum.php?mod=viewthread&tid=14681745)

# 感谢

<a href="https://www.jetbrains.com/?from=pyefun"><img src="https://goframe.org/download/thumbnails/1114119/jetbrains.png" height="120" alt="JetBrains"/></a>

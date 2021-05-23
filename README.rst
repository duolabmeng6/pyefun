# pyefun (易函数)

为python提供强大且易用的中文函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数

# 易函数的愿景

* 愿世界上没有难用的编程语言
* 易函数是为了抹平不同编程语言之间的差异使中国人，可以快速上手软件开发
* 易函数不是翻译各个编程语言的类库，而是将最实用的功能通过中文直观的展示，使其符合国人的思维逻辑
* 易函数并不局限于编程语言，所有的编程语言都可以编写易函数并使用易函数
* 易函数已经开发 go语言( [goefun](https://github.com/duolabmeng6/goefun) ) python语言( [pyefun](https://github.com/duolabmeng6/pyefun) ) 未来主流的编程语言都能拥有易函数如（ java，c#，c++，php，js）
* 愿更多的国人参与到efun（易函数）的开发中，让世界没有难用的编程语言


# 易函数特性

- 完全兼容window linux mac运行
- 完全兼容python运行环境 支持docker部署
- 全中文函数名和注释 以（易语言核心支持库，火山类库，精易模块）的命名风格极大地降低了使用门槛
- 超300+的实用函数，涵盖所有技术领域应用（深度学习，图像处理，文字处理，自动化测试）
- 全部命令经过测试用例测试 100% 放心使用
- 所有命令均有测试用例可以查看后立即使用
- 超丰富的文本处理函数 正则表达式 简单易用快速上手
- 线程池 协程池 简单易用，大大地降低使用线程，协程的技术门槛
- 全网最好用的编码转换功能 自动检测编码 自动转换到对应编码


# 文档

https://pyefun.readthedocs.io/zh_CN/latest/?badge=latest

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

# 安装ide代码提示插件

https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper

![code](./docs/source/_static/show.png)


# 欢迎贡献代码

贡献代码请提交到github 码云仓库仅作为镜像

github: https://github.com/duolabmeng6/pyefun

码云: https://gitee.com/duolabmeng666/pyefun

qq群 : 1017240979

# 如何贡献代码？

1. 函数名*必须*使用直观易用的*中文命名* （请参考易语言的支持库命名，精易模块，火山开发平台）的中文函数命名方式
2. 注释*必须*包括，*使用方法*，*代码示例*，*注意事项*等
3. *必须*编写*测试用例*
4. 请保持 window，linux，的兼容性，如果是window的专有命令不要引入公共库指`pyefun/__init__.py`中 可参考`pyefun/asyncPoolGevent``pyefun/javscript` 的方法封装，使用时单独引入即可
5. 贡献代码时请务必检测代码是否运行正常 github贡献代码的操作 请百度学习并不困难


# 项目推荐

* goefun(go易函数) 为golang提供强大且易用的中文函数库，易语言go函数库，完整的封装了易语言核心支持库所有功能，以及易语言中简单易用的函数 https://github.com/duolabmeng6/goefun

* ide中文拼音插件 https://github.com/tuchg/ChinesePinyin-CodeCompletionHelper

# 学习交流

[精易论坛](https://bbs.125.la/forum.php?mod=viewthread&tid=14681745)

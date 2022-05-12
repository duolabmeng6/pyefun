"""

.. Hint::
    JavaScript引擎

    在python中运行JavaScript代码

    python调用js的函数

    需要安装 pip install PyExecJS

    需要安装 node 环境

    - PyV8 = "PyV8"
    - Node = "Node"
    - JavaScriptCore = "JavaScriptCore"
    - SpiderMonkey = "SpiderMonkey"
    - JScript = "JScript"
    - PhantomJS = "PhantomJS"
    - SlimerJS = "SlimerJS"
    - Nashorn = "Nashorn"

.. literalinclude:: ../../../pyefun/javscript/javscript_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import execjs


class javscript:
    """
    python调用js的函数
    需要安装 pip install PyExecJS
    需要安装 node 环境
        PyV8 = "PyV8"
        Node = "Node"
        JavaScriptCore = "JavaScriptCore"
        SpiderMonkey = "SpiderMonkey"
        JScript = "JScript"
        PhantomJS = "PhantomJS"
        SlimerJS = "SlimerJS"
        Nashorn = "Nashorn"
    """

    def __init__(self, 运行环境名称: str = "Node"):
        self.设置运行环境(运行环境名称)

    def 取运行环境(self):
        return self.jscript.name

    def 设置运行环境(self, 运行环境名称: str = "Node"):
        self.jscript = execjs.get(运行环境名称)

    def 加载代码(self, js代码: str):
        self.jscript = self.jscript.compile(js代码)

    def 执行(self, 函数名: str, *参数):
        return self.jscript.call(函数名, *参数)

    def 运行(self, js代码: str):
        return self.jscript.eval(js代码)


def 运行js(加载js的代码, 运行js代码, 运行环境名称: str = "Node"):
    ctx = execjs.get(运行环境名称).compile(加载js的代码)
    return ctx.eval(运行js代码)

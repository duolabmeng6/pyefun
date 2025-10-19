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
        """
        __init__ 的功能说明（请补充）。

        Args:
            运行环境名称 (str, 可选): 参数说明。默认值为 "Node"。

        """
        self.设置运行环境(运行环境名称)

    def 取运行环境(self):
        """
        取运行环境 的功能说明（请补充）。

        """
        return self.jscript.name

    def 设置运行环境(self, 运行环境名称: str = "Node"):
        """
        设置运行环境 的功能说明（请补充）。

        Args:
            运行环境名称 (str, 可选): 参数说明。默认值为 "Node"。

        """
        self.jscript = execjs.get(运行环境名称)

    def 加载代码(self, js代码: str):
        """
        加载代码 的功能说明（请补充）。

        Args:
            js代码 (str): 参数说明。

        """
        self.jscript = self.jscript.compile(js代码)

    def 执行(self, 函数名: str, *参数):
        """
        执行 的功能说明（请补充）。

        Args:
            函数名 (str): 参数说明。
            *参数: 参数说明。

        """
        return self.jscript.call(函数名, *参数)

    def 运行(self, js代码: str):
        """
        运行 的功能说明（请补充）。

        Args:
            js代码 (str): 参数说明。

        """
        return self.jscript.eval(js代码)


def 运行js(加载js的代码, 运行js代码, 运行环境名称: str = "Node"):
    """
    运行js 的功能说明（请补充）。

    Args:
        加载js的代码: 参数说明。
        运行js代码: 参数说明。
        运行环境名称 (str, 可选): 参数说明。默认值为 "Node"。

    """
    ctx = execjs.get(运行环境名称).compile(加载js的代码)
    return ctx.eval(运行js代码)

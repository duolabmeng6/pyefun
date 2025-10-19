"""

.. Hint::
    配置项 读取ini配置文件

.. literalinclude:: ../../../pyefun/配置项_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""

import configparser
import io
from pyefun import *


class 配置项(configparser.ConfigParser):
    文件路径 = ""

    def __init__(self, 内容=""):
        """
        __init__ 的功能说明（请补充）。

        Args:
            内容 (可选): 参数说明。默认值为 ""。

        """
        pass
        super().__init__()
        if 内容:
            self.加载(内容)

    def 加载(self, 内容):
        """
        加载 的功能说明（请补充）。

        Args:
            内容: 参数说明。

        """
        self.read_string(内容)  # python3
        return self

    def 加载从文件(self, 文件路径):
        """
        加载从文件 的功能说明（请补充）。

        Args:
            文件路径: 参数说明。

        """
        self.文件路径 = 文件路径
        self.read_string(读入文本(文件路径))  # python3
        return self

    def 保存(self):
        """
        保存 的功能说明（请补充）。

        """
        if self.文件路径:
            文件_保存(self.文件路径, 到字节集(self.取数据()))

    def 取所有项名(self, 节名):
        """
        取所有项名 的功能说明（请补充）。

        Args:
            节名: 参数说明。

        """
        return self.options(节名)

    def 取所有项名和值(self, 节名):
        """
        取所有项名和值 的功能说明（请补充）。

        Args:
            节名: 参数说明。

        """
        return self.items(节名)

    def 取所有节名(self):
        """
        取所有节名 的功能说明（请补充）。

        """
        return self.sections()

    def 读配置项(self, 节名称, 配置项名称, 默认值=""):
        """
        读配置项 的功能说明（请补充）。

        Args:
            节名称: 参数说明。
            配置项名称: 参数说明。
            默认值 (可选): 参数说明。默认值为 ""。

        """
        try:
            return self.get(节名称, 配置项名称)
        except:
            return 默认值

    def 写配置项(self, 节名称, 配置项名称, 值):
        """
        写配置项 的功能说明（请补充）。

        Args:
            节名称: 参数说明。
            配置项名称: 参数说明。
            值: 参数说明。

        """
        if not self.has_section(节名称):
            self.add_section(节名称)
        return self.set(节名称, 配置项名称, 值)

    def 删除配置项(self, 节名称, 配置项名称):
        """
        删除配置项 的功能说明（请补充）。

        Args:
            节名称: 参数说明。
            配置项名称: 参数说明。

        """
        return self.remove_option(节名称, 配置项名称)

    def 删除节名(self, 节名称):
        """
        删除节名 的功能说明（请补充）。

        Args:
            节名称: 参数说明。

        """
        return self.remove_section(节名称)

    def 取数据(self):
        """
        取数据 的功能说明（请补充）。

        """
        fp = io.StringIO()
        self.write(fp)
        text = fp.getvalue()
        fp.close()
        return text

    def 取所有结果(self):
        """
        取所有结果 的功能说明（请补充）。

        """
        字典 = dict()
        所有节名 = self.取所有节名()
        for 节名 in 所有节名:
            字典[节名] = dict()
            for v in self.取所有项名和值(节名):
                字典[节名][v[0]] = v[1]
        return 字典

    def 读配置项逻辑值(self, 节名称, 配置项名称, 默认值=False):
        """
        读配置项逻辑值 的功能说明（请补充）。

        Args:
            节名称: 参数说明。
            配置项名称: 参数说明。
            默认值 (可选): 参数说明。默认值为 False。

        """
        try:
            return self.get(节名称, 配置项名称) == "1"
        except:
            return 默认值

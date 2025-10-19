"""

.. Hint::
    配置项：读取与写入 ini 配置文件。

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
    """对 configparser.ConfigParser 的中文封装。

    提供更易用的中文方法名，支持从文本或文件加载、保存与读取键值等。
    """

    文件路径 = ""

    def __init__(self, 内容=""):
        """创建配置对象，可选择直接加载 ini 文本内容。

        :param 内容: ini 格式字符串
        """
        pass
        super().__init__()
        if 内容:
            self.加载(内容)

    def 加载(self, 内容):
        """从 ini 字符串加载配置。"""
        self.read_string(内容)  # python3
        return self

    def 加载从文件(self, 文件路径):
        """从文件路径加载配置，并记录文件路径以便保存。"""
        self.文件路径 = 文件路径
        self.read_string(读入文本(文件路径))  # python3
        return self

    def 保存(self):
        """保存当前配置到之前记录的文件路径（若已设置）。"""
        if self.文件路径:
            文件_保存(self.文件路径, 到字节集(self.取数据()))

    def 取所有项名(self, 节名):
        """获取某节下所有项名列表。"""
        return self.options(节名)

    def 取所有项名和值(self, 节名):
        """获取某节下所有项名与值的列表。"""
        return self.items(节名)

    def 取所有节名(self):
        """获取所有节名列表。"""
        return self.sections()

    def 读配置项(self, 节名称, 配置项名称, 默认值=""):
        """读取配置项，不存在时返回默认值。"""
        try:
            return self.get(节名称, 配置项名称)
        except:
            return 默认值

    def 写配置项(self, 节名称, 配置项名称, 值):
        """写入配置项，若节不存在则自动创建。"""
        if not self.has_section(节名称):
            self.add_section(节名称)
        return self.set(节名称, 配置项名称, 值)

    def 删除配置项(self, 节名称, 配置项名称):
        """删除指定节下的某配置项。"""
        return self.remove_option(节名称, 配置项名称)

    def 删除节名(self, 节名称):
        """删除整节。"""
        return self.remove_section(节名称)

    def 取数据(self):
        """以字符串形式返回当前配置内容（ini 格式）。"""
        fp = io.StringIO()
        self.write(fp)
        text = fp.getvalue()
        fp.close()
        return text

    def 取所有结果(self):
        """以嵌套字典形式返回完整配置内容。"""
        字典 = dict()
        所有节名 = self.取所有节名()
        for 节名 in 所有节名:
            字典[节名] = dict()
            for v in self.取所有项名和值(节名):
                字典[节名][v[0]] = v[1]
        return 字典

    def 读配置项逻辑值(self, 节名称, 配置项名称, 默认值=False):
        """读取配置项并将其按 "1" 映射为 True，否则为 False。"""
        try:
            return self.get(节名称, 配置项名称) == "1"
        except:
            return 默认值

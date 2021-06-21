"""

.. Hint::
    配置项 读取ini配置文件

.. literalinclude:: ../../../pyefun/configUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""

import configparser
import io

class 配置项(configparser.ConfigParser):
    def __init__(self):
        pass
        super().__init__()

    def 加载(self, 内容):

        self.read_string(内容)  # python3
        return self

    def 取所有项名(self, 节名):
        return self.options(节名)

    def 取所有项名和值(self, 节名):
        return self.items(节名)

    def 取所有节名(self):
        return self.sections()

    def 读配置项(self, 节名称, 配置项名称, 默认值=""):
        try:
            return self.get(节名称, 配置项名称)
        except:
            return 默认值

    def 写配置项(self, 节名称, 配置项名称, 值):
        if not self.has_section(节名称):
            self.add_section(节名称)
        return self.set(节名称, 配置项名称, 值)

    def 删除配置项(self, 节名称, 配置项名称):
        return self.remove_option(节名称, 配置项名称)

    def 删除节名(self, 节名称):
        return self.remove_section(节名称)

    def 取数据(self):
        fp = io.StringIO()
        self.write(fp)
        text = fp.getvalue()
        fp.close()
        return text

    def 取所有结果(self):
        字典 = dict()
        所有节名 = self.取所有节名()
        for 节名 in 所有节名:
            字典[节名]  = dict()
            for v in self.取所有项名和值(节名):
                字典[节名][v[0]] = v[1]
        return 字典

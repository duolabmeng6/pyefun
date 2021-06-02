"""

.. Hint::
    进度显示 使您可以测量和打印迭代过程的进度。这可以通过可迭代的界面或使用手动API来完成。使用可迭代的接口是最常见的。


.. literalinclude:: ../../../pyefun/progiterUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

from ubelt.util_format import *
import ubelt as ub


def 调试输出(obj):
    # data = repr2(obj, nl=2, precision=2)
    data = repr2(obj)
    print(data)


class 进度显示(ub.ProgIter):
    def __init__(self, 迭代对象=None,
                 描述="",
                 总数=None,
                 信息级别=3,
                 显示速率=False,
                 显示时间=False,
                 起始索引=0,
                 进度大小=None,
                 启用=True,
                 输出在同一行=True
                 ):
        "显示 0 不显示 1结束显示 2概率显示 3全部显示"
        # ProgIter(iterable=迭代对象,total=总数, desc=描述, show_times=False, verbose=显示)
        super().__init__(iterable=迭代对象,
                         total=总数,
                         desc=描述,
                         show_times=显示速率,
                         show_wall=显示时间,
                         verbose=信息级别,
                         initial=起始索引,
                         chunksize=进度大小,
                         enabled=启用,
                         clearline=输出在同一行
                         )


    def 下一步(self, 步数=1, 强制显示=False):
        self.step(inc=步数, force=强制显示)

    def 完成(self, 步数=1, 强制显示=False):
        self.end()

    def 开始(self):
        self.begin()

    def 取进度(self):
        data = self.format_message()
        return data

    def 换行(self):
        self.ensure_newline()

    def 输出(self, obj):
        self.ensure_newline()
        print(obj)

    def 附加输出(self, obj):
        self.set_extra(obj)
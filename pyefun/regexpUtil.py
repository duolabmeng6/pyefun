"""

.. Hint::
    正则表达式


.. literalinclude:: ../../../pyefun/regexpUtil_test.py
    :language: python
    :caption: 代码示例
    :linenos:

"""

import re



class 正则:
    """

.. Hint:: 正则的匹配模式

-   re.A
-   re.ASCII
-   让 \w, \W, \b, \B, \d, \D, \s 和 \S 只匹配ASCII，而不是Unicode。这只对Unicode样式有效，会被byte样式忽略。相当于前面语法中的内联标志 (?a) 。

-   注意，为了保持向后兼容， re.U 标记依然存在（还有他的同义 re.UNICODE 和嵌入形式 (?u) ) ， 但是这些在 Python 3 是冗余的，因为默认字符串已经是Unicode了（并且Unicode匹配不允许byte出现)。

-   re.DEBUG
-   显示编译时的debug信息，没有内联标记。

-   re.I
-   re.IGNORECASE
-   进行忽略大小写匹配；表达式如 [A-Z] 也会匹配小写字符。Unicode匹配（比如 Ü 匹配 ü）同样有用，除非设置了 re.ASCII 标记来禁用非ASCII匹配。当前语言区域不会改变这个标记，除非设置了 re.LOCALE 标记。这个相当于内联标记 (?i) 。

-   注意，当设置了 IGNORECASE 标记，搜索Unicode样式 [a-z] 或 [A-Z] 的结合时，它将会匹配52个ASCII字符和4个额外的非ASCII字符： 'İ' (U+0130, 拉丁大写的 I 带个点在上面), 'ı' (U+0131, 拉丁小写没有点的 I ), 'ſ' (U+017F, 拉丁小写长 s) and 'K' (U+212A, 开尔文符号).如果使用 ASCII 标记，就只匹配 'a' 到 'z' 和 'A' 到 'Z' 。

-   re.L
-   re.LOCALE
-   由当前语言区域决定 \w, \W, \b, \B 和大小写敏感匹配。这个标记只能对byte样式有效。这个标记不推荐使用，因为语言区域机制很不可靠，它一次只能处理一个 "习惯”，而且只对8位字节有效。Unicode匹配在Python 3 里默认启用，并可以处理不同语言。 这个对应内联标记 (?L) 。

-   在 3.6 版更改: re.LOCALE 只能用于byte样式，而且不能和 re.ASCII 一起用。

-   在 3.7 版更改: 设置了 re.LOCALE 标记的编译正则对象不再在编译时依赖语言区域设置。语言区域设置只在匹配的时候影响其结果。

-   re.M
-   re.MULTILINE
-   设置以后，样式字符 '^' 匹配字符串的开始，和每一行的开始（换行符后面紧跟的符号）；样式字符 '$' 匹配字符串尾，和每一行的结尾（换行符前面那个符号）。默认情况下，’^’ 匹配字符串头，'$' 匹配字符串尾。对应内联标记 (?m) 。

-   re.S
-   re.DOTALL
-   让 '.' 特殊字符匹配任何字符，包括换行符；如果没有这个标记，'.' 就匹配 除了 换行符的其他任意字符。对应内联标记 (?s) 。

-   re.X
-   re.VERBOSE
-   这个标记允许你编写更具可读性更友好的正则表达式。通过分段和添加注释。空白符号会被忽略，除非在一个字符集合当中或者由反斜杠转义，或者在 *?, (?: or (?P<…> 分组之内。当一个行内有 # 不在字符集和转义序列，那么它之后的所有字符都是注释。

-   例如正则表达式 \d +  # 这是注释

    """
    只匹配ASCII = re.A
    忽略大小写 = re.I
    语言依赖 = re.L
    多行模式 = re.M
    点dot匹配全部字符 = re.S
    只匹配Unicode = re.U
    允许注释 = re.X


class 正则表达式():
    """
    python的正则表达式
    https://docs.python.org/zh-cn/3/library/re.html#re.compile

    例子

        print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).搜索("123456789"))
        print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).替换("替换", "123456798"))

    """

    def __init__(self, 正则表达式文本: str = "", 模式=正则.忽略大小写 | 正则.多行模式):
        self.创建(正则表达式文本, 模式)

    def 创建(self, 正则表达式文本, 模式=正则.忽略大小写 | 正则.多行模式):
        """
        模式 正则.多行模式 | 正则.忽略大小写
            正则.只匹配ASCII = re.A
            正则.忽略大小写 = re.I
            正则.语言依赖 = re.L
            正则.多行模式 = re.M
            正则.点dot匹配全部字符 = re.S
            正则.只匹配Unicode = re.U
            正则.允许注释 = re.X

        :param 正则表达式文本:
        :param 模式:
        :return:

        """
        self.prog = re.compile(正则表达式文本, flags=模式)
        return self

    def 搜索(self, 内容):
        self.res = self.prog.findall(内容)
        return self.res

    def 替换(self, 用作替换的文本: str, 内容: str = "") -> str:
        return re.sub(self.prog, 用作替换的文本, 内容)



class 正则表达式类():
    """
    精易模块的正则表达式类命名方式

    坦率讲 该类是为了精易模块的正则表达式代码能够直接迁移

    python有更好用的方式实现



    传统易语言代码的实现 取子匹配数量 取子匹配文本 在python里面很多余 为了兼容实现了
        zz = 正则表达式类()
        zz.创建(r"\d+", str, 是否区分大小写=True, 是否匹配多行=True)
        for i in range(zz.取匹配数量()):
            print("取匹配文本", zz.取匹配文本(i))
            print("取子匹配数量", zz.取子匹配数量())
            for k in range(zz.取子匹配数量()):
                print("取子匹配文本 i= %s k= %s" % (i, k), zz.取子匹配文本(i, k))
    python的实现
        正则结果 = 正则表达式类(r"\d+", str, 是否区分大小写=True, 是否匹配多行=True).取结果()


    建议使用 正则表达式 代码更加简单 本类 只是为了兼容精易模块的代码降低学习成本

    print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).搜索("123456789"))
    print(正则表达式(r"\d+", 正则.多行模式 | 正则.忽略大小写).替换("替换", "123456798"))

    """

    def __init__(self, 正则表达式文本: str = "", 被搜索的文本: str = "", 是否区分大小写=False, 是否匹配多行=True):
        pass
        self.创建(正则表达式文本, 被搜索的文本, 是否区分大小写, 是否匹配多行)

    def 创建(self, 正则表达式文本: str, 被搜索的文本: str = "", 是否区分大小写=False, 是否匹配多行=True):
        pass
        if 正则表达式文本 == "":
            return self

        self.模式 = 0
        if 是否区分大小写 == False:
            self.模式 = self.模式 | re.I
        if 是否匹配多行:
            self.模式 = self.模式 | re.M
        # if 是否全局匹配: python没

        # print(正则表达式文本)
        # print(被搜索的文本)
        self.正则表达式文本 = 正则表达式文本
        self.prog = re.compile(正则表达式文本, flags=self.模式)

        self.匹配(被搜索的文本)

        return self

    def 匹配(self, 被搜索的文本: str, 模式=0):
        """
        模式
            re.A(只匹配ASCII字符),
            re.I(忽略大小写),
            re.L(语言依赖),
            re.M(多行模式),
            re.S(点dot匹配全部字符),
            re.U(Unicode匹配),
            and re.X(冗长模式)。

        :param 被搜索的文本:
        :param 模式: re.A|re.I
        :return:
        """
        self.被搜索的文本 = 被搜索的文本
        if (模式 == 0):
            self.res = self.prog.findall(self.被搜索的文本)
        else:
            self.res = self.prog.findall(self.被搜索的文本, 模式)

        # print(self.res)
        return self

    def 取匹配数量(self) -> int:
        pass

        return len(self.res)

    def 取匹配文本(self, 匹配索引: int) -> str:
        pass
        try:
            col = self.res[匹配索引]
            return col
        except:
            pass
        return False

    def 取子匹配文本(self, 匹配索引: int, 子表达式索引: int) -> str:
        """

        :param 匹配索引:
        :param 子表达式索引:
        :return:
        """
        # pass
        try:
            col = self.res[匹配索引]
            if (len(col) <= 子表达式索引):
                return False
            return col[子表达式索引]
        except:
            pass
        return False

    def 取子匹配数量(self) -> int:
        # print(self.res[0])
        # print(len(self.res[0]))
        try:
            return len(self.res[0])
        except:
            pass
        return 0

    def 取结果(self) -> str:
        return self.res

    def 替换(self, 用作替换的文本: str, 被搜索的文本: str = "") -> str:
        if (被搜索的文本 != ""):
            self.被搜索的文本 = 被搜索的文本
        return re.sub(self.prog, 用作替换的文本, self.被搜索的文本)


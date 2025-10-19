"""
公用函数：异常处理与动态导包。

提供统一的异常信息提示、装饰器异常捕获封装，以及按需动态导入模块的工具函数。

主要对象：
- 异常处理返回类型逻辑型：用于包装函数，发生异常时打印信息并返回 False。
- 设置_异常处理_显示信息：配置异常显示级别（0/1/2）。
- _动态导包：按需导入模块，不存在时提示 pip 安装命令并抛出 ImportError。
"""
import re, sys, traceback, datetime

异常显示信息 = 2

报错_列表索引 = "取列表内容时，索引超出范围"
报错_层级 = "调用层级如下"
报错_除零 = "请勿除以零"
报错_递归 = "递归过深。请确认: 1、的确需要递归 2、递归的收敛正确"
报错_按索引取项 = "不支持按索引取项"
报错_无属性 = "没有属性"
参考_enter = "\n参考：https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit"


def 设置_异常处理_显示信息(显示信息: int = 2) -> None:
    """
    设置异常处理的输出详细程度。

    Args:
        显示信息 (int): 显示级别。0 不显示，1 显示简要，2 显示详细（默认）。

    Returns:
        None: 无返回值。
    """
    global 异常显示信息
    异常显示信息 = 显示信息


class 层信息:
    """
    回溯层级的行信息。

    Attributes:
        行号 (int): 出错代码的行号。
        内容 (str): 该行的源代码内容。
        文件名 (str): 源文件路径。
    """

    def __init__(self, 行号, 内容, 文件名):
        self.行号, self.内容, self.文件名 = 行号, 内容, 文件名


def 提取(各层):
    """
    提取 traceback 各层为简化后的层信息列表。

    Args:
        各层 (Iterable): 由 traceback.extract_tb 返回的帧列表。

    Returns:
        list[层信息]: 从最内层到最外层的层信息列表。
    """
    各行 = []
    for 层号 in range(len(各层) - 1, -1, -1):
        层 = 各层[层号]
        文件名 = 层.filename
        各行.append(层信息(层.lineno, 层.line, 文件名))

    return 各行


def 报错信息(例外: Exception):
    """
    生成可读的异常信息列表，包含关键提示与调用栈片段。

    Args:
        例外 (Exception): 捕获到的异常对象。

    Returns:
        list[str]: 文本行列表，用于打印显示。
    """
    exc_type, exc_value, 回溯信息 = sys.exc_info()
    各层 = traceback.extract_tb(回溯信息)
    # print(repr(各层))
    各行 = []

    行信息 = 提取(各层)
    类型 = 例外.__class__.__name__
    原信息 = str(例外)
    if len(行信息) > 0:
        关键 = 提示(类型, 原信息)
    各行.append(关键)
    for 行号, 行 in enumerate(行信息, start=1):
        # 在第二层前显示
        if 行号 == 2:
            各行.append(报错_层级)
        各行.append((f"见 File \"{行.文件名}\", ") + f"line {行.行号}：{行.内容}")
    return 各行


def 提示(类型: str, 原信息: str) -> str:
    """
    将异常类型与原始信息转化为更易理解的中文提示。

    Args:
        类型 (str): 异常类型名，例如 NameError、TypeError。
        原信息 (str): 异常的原始信息字符串。

    Returns:
        str: 转换后的中文提示信息。
    """
    if 类型 == 'NameError':
        return re.sub(r"name '(.*)' is not defined", r"请先定义‘\1’再使用", 原信息)
    elif 类型 == 'ZeroDivisionError':
        return 报错_除零
    elif 类型 == 'RecursionError':
        return 报错_递归
    elif 类型 == 'UnboundLocalError':
        return re.sub(
            r"local variable '(.*)' referenced before assignment",
            r"请先对本地变量‘\1’赋值再引用",
            原信息)
    elif 类型 == 'KeyError':
        return "字典中不存在此键：" + 原信息
    elif 类型 == 'TypeError':
        模式 = 'can only concatenate str \\(not "(.*)"\\) to str'
        无法取项 = "'(.*)' object is not subscriptable"
        参数缺失 = "(.*) missing 1 required positional argument: '(.*)'"
        if re.match(模式, 原信息):
            return re.sub(模式, r'字符串只能拼接字符串，请将“\1”先用 str() 转换', 原信息)
        匹配 = re.search(无法取项, 原信息)
        if 匹配:
            return f'{类型中文化(匹配.group(1))}{报错_按索引取项}'
        if re.match(参数缺失, 原信息):
            return re.sub(参数缺失, r'函数“\1”需要“\2”参数', 原信息)
    elif 类型 == 'IndexError' and 原信息 == "list index out of range":
        return 报错_列表索引
    elif 类型 == 'AttributeError':
        信息 = "需要添加此属性：" + 原信息
        if 原信息 == "__enter__":
            信息 += 参考_enter
            return 信息

        无属性 = "'(.*)' object has no attribute '(.*)'"
        匹配 = re.search(无属性, 原信息)
        if 匹配:
            return f'{类型中文化(匹配.group(1))}{报错_无属性}‘{匹配.group(2)}’'
    elif 类型 == 'FileNotFoundError':
        return re.sub(r"\[Errno 2\] No such file or directory: '(.*)'",
                      r"没找到文件或路径：‘\1’",
                      原信息)
    elif 类型 == 'ModuleNotFoundError':
        return re.sub(r"No module named '(.*)'", r"没找到模块：‘\1’", 原信息)
    return 类型 + "：" + 原信息


def 类型中文化(类型: str) -> str:
    """
    将类型名转换为中文描述。

    Args:
        类型 (str): 类型名称，例如 NoneType、int、bool、function。

    Returns:
        str: 中文描述字符串。
    """
    中英表 = {
        "NoneType": "空变量",
        "int": "整数变量",
        "bool": "真假变量",
        "function": "函数",
    }
    return 中英表[类型] if 类型 in 中英表 else 类型


def 异常处理返回类型逻辑型(function):
    """
    将函数包装为异常安全版本，异常时打印信息并返回 False。

    作为装饰器使用：
    - 在被装饰函数抛出异常时，依据显示级别打印简要或详细信息，并统一返回 False。
    - 不改变原函数签名与行为（正常情况仍返回其原返回值）。

    Args:
        function (Callable): 需要包装的函数。

    Returns:
        Callable: 包装后的函数。

    Examples:
        @异常处理返回类型逻辑型
        def 示例函数():
            a = 1 / 0  # 将触发异常
            return True
    """

    def box(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as 例外:
            if 异常显示信息 == 2:
                print("函数异常 %s 时间 %s \r\n%s" % (
                    function.__name__,
                    str(datetime.datetime.now()),
                    "\n".join(报错信息(例外))
                ))
                # 调试用：对比原英文信息
                # print("\n\n" + traceback.format_exc())
            if 异常显示信息 == 1:
                print("函数异常 %s 时间 %s" % (
                    function.__name__,
                    str(datetime.datetime.now()),
                ))

            return False

    return box


# 用于动态导包按需使用
def _动态导包(包名: str, pip包名: str = ""):
    """
    动态导入模块，不存在时给出安装提示并抛出 ImportError。

    Args:
        包名 (str): 要导入的模块名，例如 "pendulum"、"chardet"。
        pip包名 (str, 可选): 安装包名称，默认与包名相同。

    Returns:
        ModuleType: 成功导入的模块对象。

    Raises:
        ImportError: 当模块无法导入时抛出。
    """
    if 包名 in globals():
        return globals()[包名]
    try:
        globals()[包名] = __import__(包名)
        return globals()[包名]
    except ImportError:
        if pip包名 == "":
            pip包名 = 包名
        print(f"系统中没有 {包名} 模块请运行安装 pip install {pip包名}")
        raise

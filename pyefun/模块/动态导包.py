import glob
import importlib
import os


def 导入模块(pathname: str) -> dict:
    """
    导入指定路径或者目录下的模块，并返回模块信息

    :param pathname: 要导入的模块路径(相对路径)，可以导入指定目录下的模块，只要符合glob路径表达式写法即可
    :return: 模块信息字典
    """
    modules_dict = {}
    module_paths = glob.glob(pathname)
    for path in module_paths:
        module_name = path.replace(os.sep, '.')[:-3]
        module = importlib.import_module(module_name)
        for element in dir(module):
            # 获取用户自定义的函数和变量名称
            if not element.startswith('__'):
                modules_dict[element] = eval('module.{}'.format(element))

    return modules_dict


if __name__ == '__main__':
    # 导入views目录下的所有模块，并打印模块信息
    module_info = 导入模块('views/**.py')
    print(module_info)
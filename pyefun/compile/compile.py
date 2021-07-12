import psutil
import pyefun as efun
import os
import subprocess
import pyefun.commonlyUtil as eub
import pyefun.encoding.compress.zip as ezip


class 编译器配置类:
    默认编译器路径 = "C:/efun_view_system/bulidLib/mingw64/bin"


编译器配置 = 编译器配置类()


class 日志类:
    回调日志函数 = print

    def 设置日志回调函数(self, fc):
        self.回调日志函数 = fc

    def 输出(self, info):
        self.回调日志函数(info)


日志 = 日志类()

if efun.系统_是否为window系统():
    import ctypes


@efun.异常处理返回类型逻辑型
def 结束进程和子进程(pid):
    日志.输出("kill proc and all it's subprocesses: {}".format(pid))
    try:
        parent_process = psutil.Process(pid)
    except Exception as ex:
        日志.输出("kill proc failed: " + ex.message)
        return
    parent_process.suspend()
    for p in parent_process.children(recursive=True):
        try:
            日志.输出("kill sub: {}:{} ".format(p.name(), p.pid))
            p.terminate()
        except psutil.NoSuchProcess as ex:
            日志.输出("kill sub proc fail, no such process: " + str(ex.message))
        except Exception as e:
            日志.输出("kill sub: {}:{} failed".format(p.name, p.pid))
            日志.输出(e)
    日志.输出("kill parent: " + parent_process.name())
    try:
        parent_process.kill()
    except Exception:
        日志.输出("kill parent proc: {} failed".format(parent_process.name))


def 运行命令(cmd, 输出=False, 环境变量PATH="", timeout=120, cwd=""):
    global pid
    if (cwd == ""):
        cwd = efun.路径优化(efun.取运行目录() + "/bulidLib")
    my_env = os.environ.copy()
    if 环境变量PATH == "":
        环境变量PATH = 编译器配置.默认编译器路径
    my_env["PATH"] = 环境变量PATH + ";" + my_env["PATH"]
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        env=my_env,
        close_fds=True,
        cwd=cwd
    )
    日志.输出(cmd)
    pid = proc.pid
    proc.stdin.close()
    if 输出:
        try:
            while proc.poll() is None:
                line = proc.stdout.readline()
                line = line.strip()
                if line:
                    日志.输出('{}'.format(line.decode("utf-8")))
        except:
            result = ""
        else:
            try:
                proc = proc.communicate(timeout=timeout)
            except:
                pass
                日志.输出("运行成功 {}".format(proc.pid))
                结束进程和子进程(proc.pid)
                return False
            str = ""
            for v in proc:
                if v != None:
                    try:
                        str = str + v.decode('utf-8')
                    except:
                        pass
            return str
    try:
        result = proc.stdout.read().decode('utf-8')
    except:
        result = ""
    proc.stdout.close()
    return result


def 取gcc版本():
    ret = 运行命令("gcc -v")
    # print(ret)
    if efun.判断文本(ret, ["gcc version"]):
        return efun.strCut(ret, "\r\ngcc version $ ")
    else:
        return '没有找到gcc'


def 取nuitka版本():
    ret = 运行命令("python -m nuitka --version")
    # 日志.输出("检查gcc编译器是否存在 {}".format(ret))
    if efun.判断文本(ret, ["Executable"]):
        return efun.strCut(ret, "$\r\n")
    else:
        return '没有找到nuitka'


def 取python执行路径():
    ret = 运行命令('python -c "import sys;print(sys.executable)"')
    # 日志.输出("检查gcc编译器是否存在 {}".format(ret))
    if efun.判断文本(ret, ["py"]):
        return efun.子文本替换(ret, "\r\n", "")
    else:
        return '没有找到python'


def 取python版本():
    ret = 运行命令('python -V')
    return efun.子文本替换(ret, "\r\n", "")


def 取pythonSitePackages目录():
    ret = 运行命令('python -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())"')
    return efun.子文本替换(ret, "\r\n", "")


def 隐藏控制台窗口():
    """
    Hides the console window in GUI mode. Necessary for frozen application, because
    this application support both, command line processing AND GUI mode and theirfor
    cannot be run via pythonw.exe.
    """
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        # if you wanted to close the handles...
        # ctypes.windll.kernel32.CloseHandle(whnd)


def 显示控制台窗口():
    """Unhides console window"""
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 1)


def 运行设计好的文件(文件路径):
    cmd = r"python {filename}".format(
        filename=文件路径,
    )
    日志.输出("运行 {}".format(cmd))
    ret = 运行命令(cmd, True, cwd=efun.文件_取目录(文件路径))
    日志.输出("运行完毕 {}".format(cmd))


def 解压7z(压缩包, 文件路径):
    cmd = efun.路径优化(efun.取运行目录() + r'\bulidLib\7-Zip\7z.exe') + r' x "{}" -o{} -aos -r'.format(压缩包, 文件路径)
    # 日志.输出(cmd)
    运行命令(cmd)


pid = None


def 停止运行():
    global pid
    if pid == None:
        return
    结束进程和子进程(pid)
    pid = None


def 编译_pyinstaller(文件路径):
    编译目录 = efun.文件_取目录(文件路径)
    str = r"""@echo off
cmd pyinstaller -F {name} > build.log
pause
    """.format(dir=编译目录, name=文件路径)
    cmdfile = 编译目录 + "\\编译.bat"
    efun.写到文件(cmdfile, str.encode("gbk"))
    ret = 运行命令("start {}".format(cmdfile))
    日志.输出(ret)
    return ret


def 设置系统PATH环境变量(value):
    "命令太长直接修改错误..坑爹命令"
    command = r'setx PATH "%PATH%;{}"'.format(value)
    proc = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
    )
    ret = proc.stdout.read().decode("gbk")
    日志.输出(ret)


def _定位模块所在路径(modelName):
    # 编译由于python环境的问题是无法获取系统环境下的文件的
    # 只能用于定位 python运行环境下的
    code = """
import {name}
modelfile = {name}.__file__
""".format(name=modelName)
    loc = locals()
    exec(code, globals(), loc)
    return loc['modelfile']


def 定位模块所在路径(modelName):
    """
    获取系统环境下的python模块所在路径
    """
    code = 'python -c "import {name};print({name}.__file__)"'.format(name=modelName)
    ret = 运行命令(code)
    if efun.判断文本(ret, ["No module", "None"]):
        return ""
    return efun.子文本替换(ret, "\r\n", "")


def cmd回显模式(cmd):
    cmdrtPath = efun.文件从列表中选取存在的文件路径([
        efun.路径优化(r"C:/efun_view_system/resources/cmdrt.exe"),
        efun.路径优化(efun.取运行目录() + r"/resources/cmdrt.exe"),
        efun.路径优化(efun.取运行目录() + r"/bulidLib/cmdrt.exe"),
        efun.路径优化(efun.取运行目录() + r"/cmdrt.exe"),
    ])
    if cmdrtPath == "":
        日志.输出("没有找到文件 cmdrt.exe 请配置易函数视窗编程系统安装包否则可能无法正常运行 现在使用兼容模式")
    else:
        cmd = cmdrtPath + r" " + cmd

    日志.输出(cmd)

    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        close_fds=True,
        cwd=efun.路径优化(efun.取运行目录() + "/bulidLib")
    )
    try:
        proc = proc.communicate(timeout=5)
    except:
        日志.输出("运行超时自动关闭")
        结束进程和子进程(proc.pid)
        return False
    str = ""
    for v in proc:
        if v != None:
            try:
                str = str + v.decode('utf-8')
            except:
                pass
                日志.输出("内容获取失败")
    return str


def 编译_nuitka(文件路径, 编译目录, 编译器目录):
    cmd = r"nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --follow-import-to=need --output-dir={outdir} {filename}".format(
        filename=文件路径,
        outdir=编译目录
    )
    日志.输出("编译 {}".format(cmd))
    ret = 运行命令(cmd, True, 编译器目录)
    日志.输出("编译完成 {}".format(cmd))


上一次依赖 = ""


def 自动处理依赖缺失问题(文件运行路径, 文件运行目录):
    global 上一次依赖
    运行exe返回结果 = cmd回显模式(文件运行路径)
    if (运行exe返回结果 == False):
        日志.输出('编译完成请检查程序是否运行正常 {}'.format(文件运行路径))
        # os.popen("explorer.exe {}".format(文件运行目录))
        return False
    # 从后面取200个字符大概就可以获取到确实的模块名字了
    运行exe返回结果 = 运行exe返回结果[-200:]
    # 日志.输出(运行exe返回结果)

    model = efun.strCut(运行exe返回结果, "No module named '$'")
    日志.输出("缺少模块 {}".format(model))
    if model == "":
        model = efun.strCut(运行exe返回结果, "AttributeError: module '$' has")
        日志.输出("缺少模块 {}".format(model))
    if model == "":
        日志.输出("运行结果 {}".format(运行exe返回结果))
        日志.输出('编译完成请检查程序是否运行正常 {}'.format(文件运行路径))
        # os.popen("explorer.exe {}".format(文件运行目录))
        return False

    copyfile = ""
    file = 定位模块所在路径(model)
    日志.输出("定位模块所在路径 {}".format(file))
    if file == "":
        # 定位模块失败的话 自动从库目录寻找这个文件
        siteDir = 取pythonSitePackages目录()
        ret = list(eub.查找文件或目录("{}*".format(model), siteDir))
        if (len(ret) == 1):
            日志.输出("找到文件 {}".format(ret[0]))
        else:
            日志.输出("找到多个文件 {}".format(ret))
        copyfile = ret[0]
    if file == None and copyfile == "":
        日志.输出("请手动解决错误 \r\n{}".format(运行exe返回结果))
        日志.输出("解决后重新运行编译")
        return False

    if copyfile == "":
        copyfile = file
        if efun.判断文本(copyfile, ["__init__.py"]):
            copyfile = efun.路径优化(efun.子文本替换(copyfile, "__init__.py", ""))

    if (efun.文件_是否为目录(copyfile)):
        新的目录 = 文件运行目录 + "/" + efun.文件_取文件名(copyfile)
        copyfile = efun.路径优化(copyfile + "/")
        新的目录 = efun.路径优化(新的目录 + "/")
        日志.输出("复制文件夹 {} -> {}".format(copyfile, 新的目录))
        efun.复制目录(copyfile, 新的目录)
    else:
        target = 文件运行目录 + "/" + efun.文件_取文件名(copyfile)
        日志.输出("复制文件 {} -> {}".format(copyfile, target))
        efun.复制文件(copyfile, target)
    if (上一次依赖 != copyfile):
        上一次依赖 = copyfile
    else:
        return False
    return True


def 编译文件(文件路径, 编译目录="", 编译器目录="", 不编译=False, 不寻找依赖=False):
    文件路径 = efun.路径优化(文件路径)
    文件目录 = efun.路径优化(efun.文件_取目录(文件路径))
    文件名 = efun.strCut(efun.文件_取文件名(文件路径), "$.")
    if 编译目录 == "":
        编译目录 = efun.路径优化(efun.文件_取目录(文件路径) + r"/o")
    if 编译器目录 == "":
        编译器目录 = 编译器配置.默认编译器路径
    文件运行路径 = efun.路径优化(r"{1}\{0}.dist\{0}.exe".format(文件名, 编译目录))
    文件运行目录 = efun.路径优化(efun.文件_取目录(文件运行路径))
    # 日志.输出("依赖目录 {}".format(依赖目录))
    日志.输出("文件路径 {}".format(文件路径))
    日志.输出("文件名 {}".format(文件名))
    日志.输出("编译目录 {}".format(编译目录))
    日志.输出("文件运行路径 {}".format(文件运行路径))
    日志.输出("文件运行目录 {}".format(文件运行目录))
    if 不编译 == False:
        编译_nuitka(文件路径, 编译目录, 编译器目录)
    if 不寻找依赖 == False:
        日志.输出("复制资源文件夹{} -> {}".format(efun.路径优化(文件目录 + "/resources"), efun.路径优化(文件运行目录 + "/resources")))
        efun.复制目录(efun.路径优化(文件目录 + "/resources"), efun.路径优化(文件运行目录 + "/resources"))
        while 自动处理依赖缺失问题(文件运行路径, 文件运行目录):
            pass


# """
# C:\Users\xxxx\AppData\Local\Nuitka\Nuitka\ccache\v3.7.12
# ccache-3.7.12-windows-32
#
# C:\Users\\AppData\Local\Nuitka\Nuitka\depends\x86_64
# depends22_x64.zip
# https://pypi.org/project/Nuitka/#history
# python -m pip install nuitka
#
# pip install nuitka
# PS C:\pyefun\wxview\create_test> pip uninstall nuitka
# Found existing installation: Nuitka 0.6.15.3
# Uninstalling Nuitka-0.6.15.3:
#   Would remove:
#     c:\users\\anaconda3\lib\site-packages\nuitka-0.6.15.3.dist-info\*
#     c:\users\\anaconda3\lib\site-packages\nuitka\*
#     c:\users\\anaconda3\scripts\nuitka-run.bat
#     c:\users\\anaconda3\scripts\nuitka.bat
#     c:\users\\anaconda3\scripts\nuitka3-run.exe
#     c:\users\\anaconda3\scripts\nuitka3.exe
# """
def 初始化编译环境():
    """该命名需要安装易函数视窗编程系统 否则代码中的文件路径将会找不到"""
    压缩包路径_ccache = efun.路径优化(efun.取运行目录() + "/bulidLib/ccache-3.7.12-windows-32.zip")
    压缩包路径_depends = efun.路径优化(efun.取运行目录() + "/bulidLib/depends22_x64.zip")
    压缩包路径_gcc = efun.路径优化(efun.取运行目录() + "/bulidLib/mingw64.7z")
    filelist = list(eub.查找文件或目录("Nuitka*", efun.取运行目录() + "/bulidLib/Nuitka/"))
    try:
        pip安装包路径 = efun.路径优化(filelist[0])
    except:
        pip安装包路径 = "nuitka"

    安装目录 = eub.系统_设置应用缓存目录("Nuitka", "Nuitka")
    安装目录_ccache = efun.路径优化(安装目录 + "/ccache")
    安装目录_depends = efun.路径优化(安装目录 + "/depends/x86_64")
    安装目录_gcc = efun.路径优化(efun.取运行目录() + "/bulidLib/mingw64")
    安装目录_gcc_2 = efun.路径优化(efun.取运行目录() + "/bulidLib")

    日志.输出("安装目录 {}".format(安装目录))
    日志.输出("安装目录_ccache {}".format(安装目录_ccache))
    日志.输出("安装目录_depends {}".format(安装目录_depends))
    日志.输出("压缩包路径_ccache {}".format(压缩包路径_ccache))
    日志.输出("压缩包路径_depends {}".format(压缩包路径_depends))

    # C:/Users\xxx\AppData\Local\Nuitka\Nuitka\ccache\v3.7.12
    # ccache-3.7.12-windows-32
    #
    # C:\Users\\AppData\Local\Nuitka\Nuitka\depends\x86_64
    # depends22_x64.zip

    # C:\efun_view_system\bulidLib
    # ccache-3.7.12-windows-32.zip
    efun.设置_异常处理_显示信息()
    if not efun.文件是否存在(安装目录_ccache):
        ezip.zip解压(压缩包路径_ccache, 安装目录_ccache)

    if not efun.文件是否存在(安装目录_depends):
        ezip.zip解压(压缩包路径_depends, 安装目录_depends)

    ret = 运行命令("gcc -v")
    日志.输出("检查gcc编译器是否存在 {}".format(ret))
    if efun.判断文本(ret, ["gcc version"]):
        日志.输出("gcc环境通过")
    else:
        日志.输出("gcc 未安装自动安装中")
        if not efun.文件是否存在(安装目录_gcc):
            解压7z(压缩包路径_gcc, 安装目录_gcc_2)

            # ezip.zip解压(压缩包路径_gcc, 安装目录_gcc)

        ret = 运行命令("gcc -v")
        日志.输出("检查gcc编译器是否存在 {}".format(ret))
        if efun.判断文本(ret, ["gcc version"]):
            日志.输出("gcc环境通过")
        else:
            日志.输出("gcc环境配置失败请自行处理后再编译")
            return False

    ret = 运行命令("python -m nuitka --version")
    日志.输出("检查编译器是否存在 {}".format(ret))
    if efun.判断文本(ret, ["No module named nuitka"]):
        日志.输出("安装命令 {}".format("python -m pip install {}".format(pip安装包路径)))

        ret = 运行命令("python -m pip install {}".format(pip安装包路径))
        日志.输出("安装结果 {}".format(ret))

        ret = 运行命令("python -m nuitka --version")
        日志.输出("检查编译器是否存在 {}".format(ret))

    if efun.判断文本(ret, ["Executable"]):
        日志.输出("环境配置成功")
        return True
    else:
        日志.输出("环境配置失败请自行处理")
        return False

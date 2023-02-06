import os
import subprocess
import tempfile


def 苹果系统检查是否为夜间模式() -> bool:
    """
    检查用户是否正在使用夜间模式
    """
    try:
        status = subprocess.check_output(
            "defaults read -g AppleInterfaceStyle".split(),
            stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError:
        return False
    return True


def 系统通知(标题, 提示内容):
    """
    系统通知

    标题   --   消息标题
    提示内容    --  通知说明/摘要
    """

    os.system(
        """osascript -e 'display notification "{}" with title "{}"'""".format(
            提示内容, 标题))

def 系统对话框(标题, 提示内容):
        """
        系统对话框
        osascript -e 'display alert "Hello World!" message "longer text can be added in the message field and it will be all shown on the pop-up alert."'
        """
        os.system("""osascript -e 'display alert "{}" message "{}"'""".format(标题, 提示内容))



def 系统截图():
    """
    Take a screenshot by selecting an area. This just uses
    macOS's default screencapture command
    """
    # Create a temporary file where we can store the screenshot
    # Source: https://stackoverflow.com/a/8577225/9215267
    _, file_path = tempfile.mkstemp()

    # From the man page:
    # -i         capture screen interactively, by selection or window
    # -s         only allow mouse selection mode
    # -x         do not play sounds
    subprocess.run(f"screencapture -i -s -x {file_path}".split())

    # We are checking if a screenshot was taken by checking if the
    # file is empty or not.
    # Source: https://stackoverflow.com/a/2507871/9215267
    if os.stat(file_path).st_size == 0:
        file_path = None
        return False, file_path

    return True, file_path


def 启动MacOS软件(app路径):
    # 例如 /System/Applications/Music.app
    os.system("open -n -a " + app路径)

def 文本朗读(文本):
    """
    朗读文本
    osascript -e 'say "Hello World!"'
    """
    os.system("osascript -e 'say \"" + 文本 + "\"'")

def 显示系统信息():
    """
    osascript -e "system info"
    """
    终端 = os.popen("osascript -e 'system info'")
    返回内容 = 终端.read()
    终端.close()
    return 返回内容

def 获取系统ip():
    """
    获取系统ip
    """
    终端 = os.popen('osascript -e "IPv4 address of (system info)"')
    返回内容 = 终端.read()
    终端.close()
    return 返回内容

def 获取系统cpu信息():
    """
    获取系统cpu信息
    """
    终端 = os.popen('osascript -e "CPU type of (system info)"')
    返回内容 = 终端.read()
    终端.close()
    return 返回内容

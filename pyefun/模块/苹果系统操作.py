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


def 提示框(标题, 提示内容):
    """
    发送通知

    标题   --   消息标题
    提示内容    --  通知说明/摘要
    """
    # rumps.notification doesnt seems to work properly.
    # I should probably use subprocess instead, but I kept messing up the command because
    # of the many quatation marks it has. Will fix later, not high priority at the moment.
    os.system(
        """osascript -e 'display notification "{}" with title "{}"'""".format(
            提示内容, 标题))


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

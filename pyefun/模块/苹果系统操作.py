import os
import subprocess


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
        """osascript -e 'display notification "{}" with 标题 "{}"'""".format(
            提示内容, 标题))
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


def 打开访达(路径):
    """
    打开访达
    """
    os.system("open " + 路径)


def 打开访达下载目录():
    """
    打开访达下载目录
    """
    打开访达("~/Downloads")


def 设置开机自启动项(软件路径):
    """
    设置开机自启动项
    """
    os.system(
        "osascript -e 'tell application \"System Events\" to make login item at end with properties {{path:\"{}\", hidden:false}}'".format(
            软件路径))


def 取消开机自启动项(软件路径):
    """
    取消开机自启动项
    """
    os.system("osascript -e 'tell application \"System Events\" to delete login item \"{}\"'".format(软件路径))


def 使用plist文件设置开机自启动项(软件路径, 工作目录, plist文件名):
    plist文件内容 = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>KeepAlive</key>
    <true/>
    <key>Label</key>
    <string>{plist文件名}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{软件路径}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>{工作目录}</string>
</dict>
</plist>"""
    plist文件路径 = os.path.expanduser(f"~/Library/LaunchAgents/{plist文件名}.plist")
    # print("plist文件路径", plist文件路径)
    with open(plist文件路径, "w") as f:
        f.write(plist文件内容)

    # plutil ~/Library/LaunchAgents/aria2.plist
    # chmod 644 ~/Library/LaunchAgents/aria2.plist
    # launchctl unload ~/Library/LaunchAgents/aria2.plist
    # launchctl load -w ~/Library/LaunchAgents/aria2.plist
    os.system("plutil " + plist文件路径)
    os.system("chmod 644 " + plist文件路径)
    os.system("launchctl unload -w " + plist文件路径)
    os.system("launchctl load -w " + plist文件路径)



def 删除开机自启动项的plist文件(plist文件名):
    plist文件路径 = os.path.expanduser(f"~/Library/LaunchAgents/{plist文件名}.plist")
    cmd = f"launchctl unload -w {plist文件路径}"
    os.system(cmd)
    os.system("rm " + plist文件路径)


def 启动服务(服务名):
    os.system("launchctl start " + 服务名)


def 停止服务(服务名):
    os.system("launchctl stop " + 服务名)

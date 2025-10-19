import subprocess


class 终端类(object):
    def __init__(self):
        """
        __init__ 的功能说明（请补充）。

        """
        pass

    def __del__(self):
        """
        __del__ 的功能说明（请补充）。

        """
        self.s.stdin.close()
        self.s.stdout.close()

    def 运行(self, 命令: str):
        """
        运行 的功能说明（请补充）。

        Args:
            命令 (str): 参数说明。

        """
        pass
        self.s = subprocess.Popen(命令, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

    def 标准输入(self, 命令: any):
        """
        标准输入 的功能说明（请补充）。

        Args:
            命令 (any): 参数说明。

        """
        pass
        self.s.stdin.write(命令)

    def 关闭标准输入(self):
        """
        关闭标准输入 的功能说明（请补充）。

        """
        pass
        self.s.stdin.close()

    def 取返回结果(self):
        """
        取返回结果 的功能说明（请补充）。

        """
        pass
        # out = self.s.stdout.read().decode("GBK")
        out = self.s.stdout.read().decode("utf-8")
        self.s.stdout.close()
        return out


if __name__ == '__main__':
    终端 = 终端类()
    终端.运行("python")
    终端.标准输入(b"import os\n")
    终端.标准输入(b"print(os.environ)")
    终端.关闭标准输入()
    print(终端.取返回结果())

    # 终端.运行("python ./命令行.py")
    # 终端.标准输入(b"123456\n")
    # 终端.关闭标准输入()
    # print(终端.取返回结果())
    # cmd = 'echo {} | sudo -S open -n /Applications/WeChat.app/Contents/MacOS/WeChat'.format('你的密码 password')
    # 终端.运行(cmd)
    # print(终端.取返回结果())
    #

    # print(终端.取返回结果())
    # cmd = '/Applications/WeChat.app/Contents/MacOS/WeChat'
    # 终端.运行(cmd)
    # print(终端.取返回结果())

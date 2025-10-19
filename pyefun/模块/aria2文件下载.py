"""
Aria2 RPC 调用模块

配置教程Aria2教程 https://vccv.cc/article/aria2-mac.html
"""


import xmlrpc.client as xmlrpclib


class Aria2Rpc(object):
    def __init__(self, uri='http://127.0.0.1:6800/rpc', secret=None):
        self.rpc_uri = uri
        self.rpc_secret = secret
        self.server = None

    def connect(self) -> xmlrpclib.ServerProxy:
        if self.server is None:
            self.server = xmlrpclib.ServerProxy(self.rpc_uri, allow_none=True)
        return self.server

    def destroy(self):
        self.server = None

    def call(self, name, *args):
        """通用调用"""
        if self.rpc_secret is not None:
            args = ('token:{}'.format(self.rpc_secret),) + args
        return getattr(self.connect(), name)(*args)

    def ping(self):
        try:
            self.get_version()
            return True
        except:
            return False

    def list_methods(self):
        """添加下载"""
        return self.call('system.listMethods')

    def add_uri(self, uris, options=None, position=None):
        """添加下载"""
        uris = [uris] if isinstance(uris, str) else uris
        return self.call('aria2.addUri', uris, options, position)

    def add_torrent(self, torrent, uris=None, options=None, position=None):
        """添加种子下载"""
        uris = [uris] if isinstance(uris, str) else uris
        torrent = xmlrpclib.Binary(open(torrent, 'rb').read())
        return self.call('aria2.addTorrent', torrent, uris, options, position)

    def add_meta_link(self, meta_link, options=None, position=None):
        """添加源连接下载"""
        meta_link = xmlrpclib.Binary(open(meta_link, 'rb').read())
        return self.call('aria2.addMetalink', meta_link, options, position)

    def remove(self, gid):
        """移除下载"""
        return self.call('aria2.remove', gid)

    def pause(self, gid):
        """暂停下载"""
        return self.call('aria2.pause', gid)

    def un_pause(self, gid):
        """取消暂停"""
        return self.call('aria2.unpause', gid)

    def tell_status(self, gid):
        """返回指定的下载信息"""
        return self.call('aria2.tellStatus', gid)

    def tell_active(self, keys=None):
        """返回正在下载的列表信息"""
        return self.call('aria2.tellActive', keys)

    def tell_waiting(self, offset, num, keys=None):
        """返回等待下载的列表信息"""
        return self.call('aria2.tellWaiting', offset, num, keys)

    def tell_stopped(self, offset, num, keys=None):
        """返回停止下载的列表信息"""
        return self.call('aria2.tellStopped', offset, num, keys)

    def remove_result(self, gid):
        """移除下载结果"""
        return self.call('aria2.removeDownloadResult', gid)

    def purge_result(self, gid):
        """清除下载结果"""
        return self.call('aria2.purgeDownloadResult', gid)

    def get_version(self):
        """获取版本"""
        return self.call('aria2.getVersion')

    def get_global_option(self):
        """获取全局选项"""
        return self.call('aria2.getGlobalOption')


def 发起下载(aria2服务器地址, 服务器密钥=None, URL="", 文件名=""):
    """
    例子:
    发起下载("http://127.0.0.1:6800/rpc", 服务器密钥="1234", URL="https://www.xzmp3.com/down/4874bea05337.mp3",
             文件名="test.mp4")
    """
    if aria2服务器地址 == "":
        aria2服务器地址 = "http://127.0.0.1:6800/rpc"

    rpc = Aria2Rpc(uri=aria2服务器地址, secret=服务器密钥)
    rpc.add_uri(URL, options={"out": 文件名})

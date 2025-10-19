"""
阿里云 oss操作

pip install oss2

https://github.com/aliyun/aliyun-oss-python-sdk?spm=a2c4g.11186623.2.4.391446a1tSs54t

"""
import oss2
from itertools import islice


class 获取授权(oss2.Auth):
    """签名版本1
    """

    def __init__(self, access_key_id, access_key_secret):
        """
        __init__ 的功能说明（请补充）。

        Args:
            access_key_id: 参数说明。
            access_key_secret: 参数说明。

        """
        super(获取授权, self).__init__(access_key_id, access_key_secret)


class 初始化Bucket(oss2.Bucket):
    def __init__(self, auth, endpoint, bucket_name,
                 is_cname=False,
                 session=None,
                 connect_timeout=None,
                 app_name='',
                 enable_crc=True):
        """
        __init__ 的功能说明（请补充）。

        Args:
            auth: 参数说明。
            endpoint: 参数说明。
            bucket_name: 参数说明。
            is_cname (可选): 参数说明。默认值为 False。
            session (可选): 参数说明。默认值为 None。
            connect_timeout (可选): 参数说明。默认值为 None。
            app_name (可选): 参数说明。默认值为 ''。
            enable_crc (可选): 参数说明。默认值为 True。

        """
        super(初始化Bucket, self).__init__(auth, endpoint, bucket_name,
                                     is_cname,
                                     session,
                                     connect_timeout,
                                     app_name,
                                     enable_crc)

    def 上传文件(self, key, data,
             headers=None,
             progress_callback=None):
        """
        上传文件 的功能说明（请补充）。

        Args:
            key: 参数说明。
            data: 参数说明。
            headers (可选): 参数说明。默认值为 None。
            progress_callback (可选): 参数说明。默认值为 None。

        """
        return self.put_object(key, data,
                               headers,
                               progress_callback)

    def 获取文件(self, key,
             byte_range=None,
             headers=None,
             progress_callback=None,
             process=None,
             params=None):
        """
        获取文件 的功能说明（请补充）。

        Args:
            key: 参数说明。
            byte_range (可选): 参数说明。默认值为 None。
            headers (可选): 参数说明。默认值为 None。
            progress_callback (可选): 参数说明。默认值为 None。
            process (可选): 参数说明。默认值为 None。
            params (可选): 参数说明。默认值为 None。

        """
        return self.get_object(key,
                               byte_range,
                               headers,
                               progress_callback,
                               process,
                               params)

    def 删除文件(self, key, params=None, headers=None):
        """
        删除文件 的功能说明（请补充）。

        Args:
            key: 参数说明。
            params (可选): 参数说明。默认值为 None。
            headers (可选): 参数说明。默认值为 None。

        """
        return self.delete_object(key, params=None, headers=None)

    def 上传文件从文件路径(self, key, filename,
                  headers=None,
                  progress_callback=None):
        """
        上传文件从文件路径 的功能说明（请补充）。

        Args:
            key: 参数说明。
            filename: 参数说明。
            headers (可选): 参数说明。默认值为 None。
            progress_callback (可选): 参数说明。默认值为 None。

        """
        return self.put_object_from_file(key, filename,
                                         headers,
                                         progress_callback)

    def 下载文件(self, key, filename,
             byte_range=None,
             headers=None,
             progress_callback=None,
             process=None,
             params=None):
        """
        下载文件 的功能说明（请补充）。

        Args:
            key: 参数说明。
            filename: 参数说明。
            byte_range (可选): 参数说明。默认值为 None。
            headers (可选): 参数说明。默认值为 None。
            progress_callback (可选): 参数说明。默认值为 None。
            process (可选): 参数说明。默认值为 None。
            params (可选): 参数说明。默认值为 None。

        """
        return self.get_object_to_file(key, filename,
                                       byte_range,
                                       headers,
                                       progress_callback,
                                       process,
                                       params)

    def 列举文件(self, 前缀='', delimiter='', marker='', max_keys=100, max_retries=None, headers=None):
        # oss2.ObjectIterator用于遍历文件。
        """
        列举文件 的功能说明（请补充）。

        Args:
            前缀 (可选): 参数说明。默认值为 ''。
            delimiter (可选): 参数说明。默认值为 ''。
            marker (可选): 参数说明。默认值为 ''。
            max_keys (可选): 参数说明。默认值为 100。
            max_retries (可选): 参数说明。默认值为 None。
            headers (可选): 参数说明。默认值为 None。

        """
        list = []
        for b in islice(oss2.ObjectIterator(self,
                                            prefix=前缀,
                                            delimiter=delimiter,
                                            marker=marker,
                                            max_keys=max_keys,
                                            max_retries=max_retries,
                                            headers=headers
                                            ), 10):
            # print(b.key)
            list.append(b.key)
        return list

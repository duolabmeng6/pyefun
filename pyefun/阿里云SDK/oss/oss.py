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
        super(获取授权, self).__init__(access_key_id, access_key_secret)


class 初始化Bucket(oss2.Bucket):
    def __init__(self, auth, endpoint, bucket_name,
                 is_cname=False,
                 session=None,
                 connect_timeout=None,
                 app_name='',
                 enable_crc=True):
        super(初始化Bucket, self).__init__(auth, endpoint, bucket_name,
                                     is_cname,
                                     session,
                                     connect_timeout,
                                     app_name,
                                     enable_crc)

    def 上传文件(self, key, data,
             headers=None,
             progress_callback=None):
        return self.put_object(key, data,
                               headers,
                               progress_callback)

    def 获取文件(self, key,
             byte_range=None,
             headers=None,
             progress_callback=None,
             process=None,
             params=None):
        return self.get_object(key,
                               byte_range,
                               headers,
                               progress_callback,
                               process,
                               params)

    def 删除文件(self, key, params=None, headers=None):
        return self.delete_object(key, params=None, headers=None)

    def 上传文件从文件路径(self, key, filename,
                  headers=None,
                  progress_callback=None):
        return self.put_object_from_file(key, filename,
                                         headers,
                                         progress_callback)

    def 下载文件(self, key, filename,
             byte_range=None,
             headers=None,
             progress_callback=None,
             process=None,
             params=None):
        return self.get_object_to_file(key, filename,
                                       byte_range,
                                       headers,
                                       progress_callback,
                                       process,
                                       params)

    def 列举文件(self, 前缀='', delimiter='', marker='', max_keys=100, max_retries=None, headers=None):
        # oss2.ObjectIterator用于遍历文件。
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

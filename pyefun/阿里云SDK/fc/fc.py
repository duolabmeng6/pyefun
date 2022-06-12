"""

.. Hint::
    阿里云函数计算
    需要安装 pip install aliyun-fc2

.. literalinclude:: ../../../pyefun/阿里云SDK/fc/fc_test.py
    :language: python
    :caption: 代码示例
    :linenos:


"""
import json
import fc2

class 阿里云函数计算(fc2.Client):
    def __init__(self, endpoint, accessKeyID, accessKeySecret, Timeout=60):
        super(阿里云函数计算, self).__init__(
            endpoint=endpoint,
            accessKeyID=accessKeyID,
            accessKeySecret=accessKeySecret,
            Timeout=Timeout)

    def 调用事件函数(self, 服务名称, 函数名称, 参数=None, headers={}, qualifier=None, 异步调用=False):
        """

        参数 = bytes(json.dumps({
            "key": "hello",
            "url": "88888",
        }).encode("utf-8"))

        如果需要异步调用增加参数
        headers = {'x-fc-invocation-type': 'Async'}

        :param 服务名称:
        :param 函数名称:
        :param 参数:
        :param headers:
        :param qualifier:
        :return:

        返回参数

ret.data 字节集 函数的返回结果
ret.headers 头信息

{
	'Access-Control-Expose-Headers': 'Date,x-fc-request-id,x-fc-error-type,x-fc-code-checksum,x-fc-invocation-duration,x-fc-max-memory-usage,x-fc-log-result,x-fc-invocation-code-version',
	'Content-Length': '5',
	'Content-Type': 'application/octet-stream',
	'X-Fc-Code-Checksum': '校验数',
	'X-Fc-Invocation-Duration': '3',
	'X-Fc-Invocation-Service-Version': 'LATEST',
	'X-Fc-Max-Memory-Usage': '10.83',
	'X-Fc-Request-Id': '函数请求的id',
	'Date': 'Thu, 10 Jun 2021 18:46:23 GMT'
}
        """
        if 异步调用:
            headers["x-fc-invocation-type"] = 'Async'

        return self.invoke_function(服务名称, 函数名称, 参数, headers=headers, qualifier=qualifier)

    def 列出服务(self, limit=None, nextToken=None, prefix=None, startKey=None, headers={}, tags=None):
        return self.list_services(limit=limit, nextToken=nextToken, prefix=prefix, startKey=startKey, headers=headers,
                                  tags=tags)

    def 列出函数(self, serviceName, limit=None, nextToken=None, prefix=None, startKey=None, headers={}, qualifier=None):
        return self.list_functions(serviceName=serviceName, limit=limit, nextToken=nextToken, prefix=prefix,
                                   startKey=startKey, headers=headers, qualifier=qualifier)

    def 调用http函数(self, 方法名称, 服务名称, 函数名称, path, headers={}, params=None, body=None):
        """

        :param 方法名称: GET POST
        :param 服务名称:
        :param 函数名称:
        :param path:
        :param headers:
        :param params:
        :param body:
        :return:
        """
        return self.do_http_request(方法名称, 服务名称, 函数名称, path, headers=headers, params=params, body=body)


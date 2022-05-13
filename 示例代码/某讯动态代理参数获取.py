#!/usr/bin/python3
import time
import hashlib

def 获取转发代理参数():
    orderno = "orderno"
    secret = "secret"
    ip = "forward.xdaili.cn"
    port = "80"
    ip_port = ip + ":" + port
    timestamp = str(int(time.time()))
    string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
    string = string.encode()
    md5_string = hashlib.md5(string).hexdigest()
    sign = md5_string.upper()
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
    proxy = {"http": "http://" + ip_port, "https": "http://" + ip_port}
    # headers = {"Proxy-Authorization": auth}
    # print(proxy, auth)
    # r = requests.get("http://pv.sohu.com/cityjson?ie=utf-8", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
    return proxy, auth

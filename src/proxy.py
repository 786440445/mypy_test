def use_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

# proxy_addr = "220.172.41.179:80"
# data = use_proxy(proxy_addr, "http://www.baidu.com")
# print(len(data))

def debug_log(url):
    import urllib.request
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)

    opener = urllib.request.build_opener(httphd, httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url)
    return data

data1 = debug_log("http://edu.51cto.com")
print(data1)
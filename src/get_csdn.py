import urllib.request
# method1 使用build_opener() 修改报头
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent", '''
                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) 
                AppleWebKit/537.36 (KHTML, like Gecko) 
                Chrome/69.0.3497.81 Safari/537.36" \
             ''')

opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

fhandle = open('./config/3.html', 'wb')
fhandle.write(data)
fhandle.close()

# method2 使用add_header() 添加报头
req = urllib.request.Request(url)
req.add_header("User-Agent", '''
                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) 
                AppleWebKit/537.36 (KHTML, like Gecko) 
                Chrome/69.0.3497.81 Safari/537.36" \
             ''')
data = urllib.request.urlopen(req).read()
fhandle = open('./config/4.html', 'wb')
fhandle.write(data)
fhandle.close()



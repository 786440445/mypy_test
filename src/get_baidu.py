import urllib.request
import os
path1 = "./config/baidu.html"
file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
isExists = os.path.exists(path1)
if not isExists:
    print("文件目录不存在")
else:
    handle = open(path1, "wb")
    handle.write(data)
    handle.close()
    print("写文件成功")

filename = urllib.request.urlretrieve("http://edu.51cto.com", filename = "./config/51cto.html")
urllib.request.urlcleanup()
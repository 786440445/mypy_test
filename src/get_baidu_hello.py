import urllib.request
name = "冯成立"
url = "http://www.baidu.com/s?wd="
keyworld = urllib.request.quote(name)
req = urllib.request.Request(url + keyworld)
data = urllib.request.urlopen(req).read()
fhandle = open("./config/fengchengli.html", "wb")
fhandle.write(data)
fhandle.close()
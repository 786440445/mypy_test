import re
import urllib.request
def getlink(url):
    # 模拟浏览器
    headers = ("User-Agent", '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) 
    AppleWebKit/537.36 (KHTML, like Gecko) 
    Chrome/69.0.3497.81 Safari/537.36''')

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    file = urllib.request.urlopen(url)
    data = str(file.read())
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link

url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
    print(link[0])
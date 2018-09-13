import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode(
    {
        "name":"冯成立",
        "pass":"123456"
    }
).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("./config/postfengchengli.html", "wb")
fhandle.write(data)
fhandle.close()
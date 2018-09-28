import re
import urllib.request

def getcontent(url, page, fhandle):
    # 模拟浏览器
    headers = ("User-Agent", '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) 
    AppleWebKit/537.36 (KHTML, like Gecko) 
    Chrome/69.0.3497.81 Safari/537.36''')

    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    data = urllib.request.urlopen(url).read().decode("utf-8")
    # 构建用户正则
    userpat = r'<h2>(.*?)</h2>'

    # 构建内容正则
    contentpat = r'<div class="content">\n<span>(.*?)</span>\n</div>'

    userlist = re.compile(userpat, re.S).findall(data)
    contentlist = re.compile(contentpat, re.S).findall(data)
    x = 1
    for content in contentlist:
        content = content.replace("\n", "")
        name = "content" + str(x)
        exec(name + '= content')
        x+=1
    y = 1
    for user in userlist:
        name = "content"+str(y)
        fhandle.write("用户"+ str(page) + str(y) + "是：" + user)
        fhandle.write("内容是：")
        exec("fhandle.write("+name + ")")
        fhandle.write("\n")
        y+=1

fhandle = open("../config/qiushibaike.txt", "w")
for i in range(1, 20):
    url = "https://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url, i, fhandle)
fhandle.close()

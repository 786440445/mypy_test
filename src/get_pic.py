import urllib.error
import urllib.request
import re

def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0] #??????????????     [src="//(.+?\.jpg)"|data-lazy-img="//(.+?\.jpg)"]
    pat2 = '<img class="err-product" data-img="1" data-img="1" data-lazy-img="//(.+?\.jpg)"'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = "../pic/" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1

for i in range(1, 5):
    url = "https://coll.jd.com/list.html?sub=22594&page=" + str(i)
    craw(url, i)
print("爬图完毕")
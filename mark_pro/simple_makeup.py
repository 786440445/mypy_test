import sys, re
sys.path.append('../')
from tools import *

print("<html><head><title>一个简单的标记程序</title></head><body>")
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print("<h1>")
        print(block)
        print("</h1>")
        title = False
    else:
        print("<p>")
        print(block)
        print("</p>")

print("</body></html>")


class HTMLRederer:
    def start_paragraph(self):
        print("<p>")
    def end_paragraph(self):
        print("</p>")
    def sub_emphasis(self, match):
        return "<em>%s</em>" % match.group(1)
    def feed(self, data):
        print(data)
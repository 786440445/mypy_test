import re
# 匹配网址
def match_url():
    pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
    string = "<a href = 'http://www.baidu.com'>百度首页</a>"
    result = re.search(pattern, string)
    print(result)

# 匹配电话号码
def match_mobile_num():
    pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
    string = "021-645627782343523424"
    result = re.search(pattern, string)
    print(result)

# 匹配电子邮箱
def match_email():
    pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
    string = "<a href = 'http://www.baidu.com'>百度首页</a></br><a href = 'matrix_fengcl@163.com'>电子邮箱地址</a>"
    result = re.search(pattern, string)
    print(result)

match_url()
match_mobile_num()
match_email()
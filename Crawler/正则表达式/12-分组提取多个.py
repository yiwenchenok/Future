
#思考题：判断邮箱是什么邮箱，提取用户的账号和邮箱类型
import re

s1 = "python@163.com python@outlook.com"
"""
（）进行分组提取
"""
rep = '(\w{5,16})@(\w{2,7})\.com'
print(re.findall(rep,s1))# [('python', '163'), ('python', 'outlook')]




import re
#思考：
#网站只允许 163邮箱和qq邮箱注册，不允许126，sina,outlook等邮箱注册
s1 = "python@163.com"
s2 = "python@qq.com"
s3 = "python@outlook.com"
s4 = "python@sina.com"

"""
(?:xxx)分组不提取
"""
rep = '\w{5,16}@(?:163|qq)\.com'  #\.表示.

print(re.findall(rep,s1)) #['python@163.com']
print(re.findall(rep,s2)) #['python@qq.com']
print(re.findall(rep,s3)) #[]
print(re.findall(rep,s4)) #[]



#思考题：判断邮箱是什么邮箱
import re
s1 = "python@163acom"
s2 = "python@qq.com"
s3 = "python@outlook.com"
s4 = "www.baidu.com"

"""
（）进行分组提取
"""

#判断是一个邮箱

rep = '\w{5,16}@\w{2,7}\.com'  #\.表示.
print(re.findall(rep,s1)) #[]
print(re.findall(rep,s2)) #['python@qq.com']
print(re.findall(rep,s3)) #['python@outlook.com']
print(re.findall(rep,s4)) #[]

print("我是分隔符".center(50,"*"))
rep = '\w{5,16}@(\w{2,7})\.com'
print(re.findall(rep,s1)) #[]
print(re.findall(rep,s2)) #['qq']
print(re.findall(rep,s3)) #['outlook']
print(re.findall(rep,s4)) #[]

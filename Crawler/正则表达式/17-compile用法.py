
import re

s1 = "python@163.com python@outlook.com"
"""
（）进行分组提取
"""
# rep = '(\w{5,16})@(\w{2,7})\.com'
# print(re.findall(rep,s1))

rep =re.compile('(\w{5,16})@(\w{2,7})\.com')
print(rep.findall(s1))
#[('python', '163'), ('python', 'outlook')]


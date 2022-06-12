
import re

#用的最多的是findall

st = "996aldkgjkl996agjlka"

#1.match；只能从字符开头匹配，匹配第一个
# print(re.match('996',st).group())

#2.search:可以从字符串任意位置匹配，返回第一个
print(re.search('996',st).group()) #996

#3.findinter返回一个迭代器
result = re.finditer('996',st)
print(next(result).group()) #996
print(next(result).group()) #996
# print(next(result).group())  #StopIteration #只有两个996

#split  todo；重要
st2 = 'https://www.baidu.com/tieba/222999'
print(st2.split("/")) #普通的
#['https:', '', 'www.baidu.com', 'tieba', '222999']
print(re.split("://|/",st2)) #正则的
#['https', 'www.baidu.com', 'tieba', '222999']

st3 = "中国132你好eee22我爱你"
#普通split切不了
print(re.split('[a-zA-Z0-9_]{3,}',st3)) #['中国', '你好', '我爱你']
# print(re.split('\w{3,}',st3))  #\w包括了中文字符

#sub todo：重要
"""
sub(正则表达式，替换后的字符串（也可以是一个函数）,待替换的字符串，替换次数)
"""
print(re.sub("aa",'python','ddddaa.com.aabbb.cccaa.aa',2)) #替换两次
#ddddpython.com.pythonbbb.cccaa.aa
print(re.sub("aa",'python','ddddaa.com.aabbb.cccaa.aa')) #替换全部
#ddddpython.com.pythonbbb.cccpython.python



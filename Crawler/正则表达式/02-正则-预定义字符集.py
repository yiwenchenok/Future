

#思考题：如果判断字符串是不是一个电话号码
import re

st1 = "adjklgklajg"
st2= "123456789"
st3 = "13588889999"
"""
findall(正则表达式，待匹配的字符串)
"""
print(re.findall('1\d\d\d\d\d\d\d\d\d\d',st1)) #[]
print(re.findall('1\d\d\d\d\d\d\d\d\d\d',st2)) #[]
print(re.findall('1\d\d\d\d\d\d\d\d\d\d',st3)) #['13588889999']




#思考题;如何匹配一个邮箱？
# @ com
#\w：匹配单词字符，即 a-z、A-Z、0-9、_
st4 = "aldkgjlkagjlqq.com"
st5 = "2489084156@qq.com"
st6 = "cyc66666@qq.com"
st7 = "cyc66666@qq.tttt"
print(re.findall("\w{3,16}@\w{2,8}.com",st4)) #[]
print(re.findall("\w{3,16}@\w{2,8}.com",st5)) #['2489084156@qq.com']
print(re.findall("\w{3,16}@\w{2,8}.com",st6)) #['cyc66666@qq.com']
print(re.findall("\w{3,16}@\w{2,8}.com",st7)) #[]



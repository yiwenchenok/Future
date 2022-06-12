

#思考题：如果判断字符串是不是一个电话号码
import re

st3 = "13588889999"
st4 = "12588889999"
"""
findall(正则表达式，待匹配的字符串)
"""
#电话号码 [3456789]表示匹配中括号中的任意一个
print(re.findall('1[3456789]\d\d\d\d\d\d\d\d\d',st3))
#['13588889999']
print(re.findall('1[3-9]\d\d\d\d\d\d\d\d\d',st3)) #如果是连续的数字，可以用-省略
#['13588889999']
print(re.findall('1[^012]\d\d\d\d\d\d\d\d\d',st3)) #中括号中加^表示取反
#['13588889999']
print(re.findall('1[^0-2]\d\d\d\d\d\d\d\d\d',st3)) #中括号中加^表示取反
#['13588889999']
print(re.findall('1[3456789]\d\d\d\d\d\d\d\d\d',st4))
#[]


import re

#精确匹配
#思考题：如果判断字符串st中包含abc
st = "adjklgklajgklabcjldkajglk"
#我们学过： in
print("abc" in st)  #True

#todo:正则表示式：一种匹配字符串的规则
"""
findall(正则表达式，待匹配的字符串)
"""
result = re.findall("abc",st)
print(result)  #['abc']





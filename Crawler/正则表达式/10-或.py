
import re
#思考：匹配0-100之间的数字，包括100
# print(re.findall("\d{1,3}",'999'))

st = '99'
result = re.findall("100|\d{1,2}",st)
print(result)  #正确答案
if result and result[0] == st:
    print(f"{st}是0-100之间的数字")
else:
    print(f"{st}不是0-100之间的数字")


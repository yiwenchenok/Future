
import re
"""
{n} :定量
{min,max}:不定量，最少min（0）个，最多max（∞）个
"""

#思考题;如何匹配一个邮箱？
st5 = "248908554156@qq.com"
print(re.findall("\w{3,16}@\w{2,8}.com",st5))
#['248908554156@qq.com']


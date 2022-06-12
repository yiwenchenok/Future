

import re
"""
\u4e00-\u9fa5：并没有包括全角（中文标点），大多数情况够用
"""

print(re.findall("[\u4e00-\u9fa5，。、：；“’！@#￥%……&*（）]{2,}","adjgkaljgkl更好！!dagjajkg大纲和daaa哈"))
#['更好！', '大纲和']

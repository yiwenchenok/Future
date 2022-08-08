# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/28 20:54
# File:test

from dataquery import *


res = Father.query.all()
print(res)

# res = Son.query.all()
# print(res)

#分页
pag = Father.query.paginate(page=1,per_page=3)
print(pag.has_next)  #是否有上一页
print(pag.has_prev)  #是否有下一页

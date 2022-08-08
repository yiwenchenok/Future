# -*- coding: utf-8 -*-
from web.models.food.Food import Food
from application import app, db
from common.libs.Helper import getCurrentDate, getDictFilterField, selectFilterObj
list=Food.query.order_by(Food.id.desc()).limit(5).all()
print(list)
# i=selectFilterObj(list,'price')
# for item in i:
#     print(item)
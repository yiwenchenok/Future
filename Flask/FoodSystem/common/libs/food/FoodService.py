# -*- coding: utf-8 -*-
from application import app,db
from web.models.food.FoodStockChangeLog import FoodStockChangeLog
from web.models.food.Food import Food
from common.libs.Helper import getCurrentDate
class FoodService():
    @staticmethod
    def setStockChangeLog(food_id=0,quantity=0,note=''):#库存变化日志，quantity：库存变化量
        if food_id < 1:
            return False
        food_info = Food.query.filter_by(id=food_id).first()
        if not food_info:
            return False
        model_stock_change = FoodStockChangeLog() #获取库存变化表的实例对象
        model_stock_change.food_id = food_id
        model_stock_change.unit = quantity
        model_stock_change.total_stock = food_info.stock
        model_stock_change.note = note
        model_stock_change.created_time = getCurrentDate()
        db.session.add(model_stock_change)
        db.session.commit()
        return True



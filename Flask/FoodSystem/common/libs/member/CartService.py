# -*- coding: utf-8 -*-
import hashlib, requests, random, string, json
from application import app, db
from web.models.member.MemberCart import MemberCart#购物车
from common.libs.Helper import getCurrentDate

#购物车Service

class CartService():

    @staticmethod
    def deleteItem(member_id=0, items=None):
        if member_id < 1 or not items:
            return False
        for item in items:
            MemberCart.query.filter_by(food_id=item['id'], member_id=member_id).delete()#以商品id和会员id同时匹配后删除购物车信息
        db.session.commit()
        return True
    @staticmethod
    def setItems(member_id=0, food_id=0, number=0):
        if member_id < 1 or food_id < 1 or number < 1:
            return False
        cart_info = MemberCart.query.filter_by(food_id=food_id, member_id=member_id).first()#获取购物车信息
        if cart_info:#如果购物车存在信息
            model_cart = cart_info#返回购物车存在的信息
        else:#购物车不存在信息
            model_cart = MemberCart()#新建购物车订单
            model_cart.member_id = member_id
            model_cart.created_time = getCurrentDate()
        model_cart.food_id = food_id
        model_cart.quantity = number
        model_cart.updated_time = getCurrentDate()
        db.session.add(model_cart)
        db.session.commit()
        return True

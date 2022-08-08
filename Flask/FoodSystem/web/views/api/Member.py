# -*- coding: utf-8 -*-
from web.views.api import route_api
from flask import request, jsonify, g
from application import app, db
import requests, json
from web.models.member.Member import Member
from web.models.member.OauthMemberBind import OauthMemberBind
from web.models.food.WxShareHistory import WxShareHistory
from common.libs.Helper import getCurrentDate
from common.libs.member.MemberService import MemberService


@route_api.route("/member/login", methods=["GET", "POST"])#小程序点击授权登陆触发api/member/login POST请求
def login():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    #print(req)
    '''
    CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('nickName', '微信用户'), 
    ('gender', '0'), ('language', ''), ('city', ''), ('province', ''), ('country', ''), 
    ('avatarUrl', 'https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132'), 
    ('code', '021dMUkl24nSE94aUOkl2wTRWf0dMUkT')])])
    '''
    code = req['code'] if 'code' in req else '' #code：小程序前端传来的状态码
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)
    openid = MemberService.getWeChatOpenId(code) #通过api—url的调用获取用户的信息
    '''
            CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('nickName', '微信用户'), ('gender', '0'), 
            ('language', ''), ('city', ''), ('province', ''), ('country', ''), 
            ('avatarUrl', 'https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132'), 
            ('code', '041bFp0w3uNFZY20ci0w3xPPqn4bFp0m')])])
            {'session_key': 'StjByoapKEdBICvobnYTpw==', 'openid': 'o7ywv4-iMbFPW5TQmNQIrCqAddYo'}
    '''
    #openid ：o7ywv4-iMbFPW5TQmNQIrCqAddYo
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)
    nickname = req['nickName'] if 'nickName' in req else ''#nickname=微信用户
    sex = req['gender'] if 'gender' in req else 0 #sex=0
    avatar = req['avatarUrl'] if 'avatarUrl' in req else ''#avatar=https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132
    '''
        判断是否已经测试过，注册了直接返回一些信息
    '''
    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()#账户来自类型：type=1，微信
    if not bind_info:
        model_member = Member()
        model_member.nickname = nickname
        model_member.sex = sex
        model_member.avatar = avatar
        model_member.salt = MemberService.geneSalt()#长度为16的字符随机组合
        model_member.updated_time = model_member.created_time = getCurrentDate()
        db.session.add(model_member)
        db.session.commit()
        model_bind = OauthMemberBind()
        model_bind.member_id = model_member.id
        model_bind.type = 1
        model_bind.openid = openid
        model_bind.extra = ''
        model_bind.updated_time = model_bind.created_time = getCurrentDate()
        db.session.add(model_bind)
        db.session.commit()
        bind_info = model_bind
    member_info = Member.query.filter_by(id=bind_info.member_id).first()#bind_info.member_id：获取已经绑定的以及正在使用id，返回用户信息
    token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
    resp['data'] = {'token': token}
    #{'code': 200, 'msg': '操作成功~', 'data': {'token': '8b15f29b49b76a3cb36a08754225a904#9'}}
    return jsonify(resp)

# 判断是否登陆绑定过了
@route_api.route("/member/check-reg", methods=["GET", "POST"])
def checkReg():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        resp['code'] = -1
        resp['msg'] = "需要code"
        return jsonify(resp)
    openid = MemberService.getWeChatOpenId(code)
    if openid is None:
        resp['code'] = -1
        resp['msg'] = "调用微信出错"
        return jsonify(resp)
    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        resp['code'] = -1
        resp['msg'] = "未绑定"
        return jsonify(resp)
    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "未查询到绑定信息"
        return jsonify(resp)
    token = "%s#%s" % (MemberService.geneAuthCode(member_info), member_info.id)
    resp['data'] = {'token': token}
    return jsonify(resp)


@route_api.route("/member/share", methods=["POST"])
def memberShare():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    url = req['url'] if 'url' in req else ''
    member_info = g.member_info
    model_share = WxShareHistory()
    if member_info:
        model_share.member_id = member_info.id
    model_share.share_url = url
    model_share.created_time = getCurrentDate()
    db.session.add(model_share)
    db.session.commit()
    return jsonify(resp)


@route_api.route("/member/info")
def memberInfo():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    member_info = g.member_info
    resp['data']['info'] = {
        "nickname": member_info.nickname,
        "avatar_url": member_info.avatar
    }
    return jsonify(resp)

# -*- coding: utf-8 -*-
import hashlib, requests, random, string, json
from application import app


class MemberService():
    @staticmethod
    def geneAuthCode(member_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()
    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))
    @staticmethod
    def getWeChatOpenId(code):#调用weixin的api返回用户的信息，现在微信版本无法获取用户的信息了，全部使用匿名替代，关键是以openid来判断用户是否绑定小程序
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
        r = requests.get(url)
        res = json.loads(r.text)#解析有效的JSON字符串并将其转换为Python字典
        #print(res)
        '''
        CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('nickName', '微信用户'), ('gender', '0'), 
        ('language', ''), ('city', ''), ('province', ''), ('country', ''), 
        ('avatarUrl', 'https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132'), 
        ('code', '041bFp0w3uNFZY20ci0w3xPPqn4bFp0m')])])
        {'session_key': 'StjByoapKEdBICvobnYTpw==', 'openid': 'o7ywv4-iMbFPW5TQmNQIrCqAddYo'}
        '''
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid

# -*- coding: utf-8 -*-
import hashlib,base64,random,string

class UserService():

    @staticmethod
    def geneAuthCode(user_info = None ):
        #产生授权码
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def genePwd( pwd,salt):
        #salt为随机加密密钥，用户的密码pwd-salt组成一个字符串进行加密，也保存在数据库
        m = hashlib.md5()
        str = "%s-%s" % ( base64.encodebytes( pwd.encode("utf-8") ) , salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt( length = 16 ):
        #16位随机数字字母，并且保存在数据库
        keylist = [ random.choice( ( string.ascii_letters + string.digits ) ) for i in range( length ) ]
        return ( "".join( keylist ) )

# -*- coding: utf-8 -*-
import time
from application import app
class UrlManager(object):
    def __init__(self):
        pass
    @staticmethod
    def buildUrl( path ):
        return ""+path
    @staticmethod
    def buildStaticUrl(path):
        ##版本随着时间撮在变，就不需要清理js文件，不需要刷新了，实时刷新
        #每次上线的时候可以定义这个RELEASE_VERSION，这样就不用实时刷新js，根据动态版本号解决js加载问题。
        #自己开发的时候可以定义这个ver随着时间撮变化。
        release_version = app.config.get( 'RELEASE_VERSION' )
        ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        path =  "/static" + path + "?ver=" + ver  #todo：
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildImageUrl( path ):  #图片的地址，在美食列表中set上传图片展示中使用到
        app_config = app.config['APP']  # 'domain':'http://192.168.3.178:8999'
        url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
        return url
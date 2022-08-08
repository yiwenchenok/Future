# -*- coding: utf-8 -*-
from application import  app
from common.libs.Helper import my_render_template
from common.libs.LogService import LogService

@app.errorhandler( 404 )
def error_404( e ):
    LogService.addErrorLog( str( e ) )
    return my_render_template( 'error/error.html',{ 'status':404,'msg':'很抱歉！您访问的页面不存在' } )
# -*- coding: utf-8 -*-
from flask import Blueprint,render_template
from common.libs.Helper import my_render_template
from common.libs.Helper import *
route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    #todo:很多个页面，都传这个current_user不太合适,重写一个render_template

    # current_user = g.current_user
    # return render_template( "index/index.html",current_user = current_user )

    resp_data = {
        'data':{
            'finance':{
                'today':0,
                'month':0
            },
            'member': {
                'today_new': 0,
                'month_new': 0,
                'total': 0
            },
            'order': {
                'today': 0,
                'month': 0
            },
            'shared': {
                'today': 0,
                'month': 0
            },
        }
    }

    return my_render_template( "index/index.html",resp_data )


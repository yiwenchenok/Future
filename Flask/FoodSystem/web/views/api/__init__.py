# -*- coding: utf-8 -*-
from flask import Blueprint
route_api = Blueprint( 'api_page',__name__ )
from web.views.api.Member import *
from web.views.api.Food import *
from web.views.api.Order import *
from web.views.api.My import *
from web.views.api.Cart import *
from web.views.api.Address import *

@route_api.route("/")
def index():
    return "Mina Api V1.0~~"
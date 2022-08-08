# -*- coding: utf-8 -*-
from application import app
from web.views.index import route_index
from web.views.movie.Movie import route_movie

app.register_blueprint( route_index,url_prefix = "/" )
app.register_blueprint( route_movie,url_prefix = "/" )



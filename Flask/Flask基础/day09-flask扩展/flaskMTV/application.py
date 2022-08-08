# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql  #pip install pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

class MyFlask( Flask ):
    def __init__(self,import_name,template_folder=None):
        super( MyFlask,self ).__init__( import_name,template_folder=template_folder )
        self.config.from_pyfile( 'config/base_setting.py' )
        if "configName" in os.environ:
            self.config.from_pyfile( f"config/{os.environ['ops_config'] }_setting.py")
            """
            ops_config是选择local|production中的一个
            linux系统： export configName=production && python manage.py runserver
            """
        else:  # 默认运行用线下模型
            self.config.from_pyfile('config/local_setting.py')

        db.init_app( self )

db = SQLAlchemy()

import os
template_folder=os.getcwd() + "/web/templates/"
app = MyFlask( __name__,template_folder=template_folder )
manager = Manager( app )



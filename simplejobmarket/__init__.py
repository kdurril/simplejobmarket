#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager



#from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
#from flask.ext.moment import Moment
#from flask.ext.pagedown import PageDown
from config import config

#from config import config

app = Flask(__name__)
#app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
login_manager = LoginManager()
login_manager.session_protection = None
login_manager.login_view = 'login'
db = SQLAlchemy()
config_name = 'development'
app.config.from_object(config[config_name])
config[config_name].init_app(app)
login_manager.init_app(app)
db.init_app(app)
from simplejobmarket import urls

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    from simplejobmarket import urls
    
    return app

#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask.ext.login import LoginManager
#from config import config

app = Flask('application')
#app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)

import simplejobmarket.urls

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    pass

    



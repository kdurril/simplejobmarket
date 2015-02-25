#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
import os

app = Flask('application')
#app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRESKEY']

import simplejobmarket.urls



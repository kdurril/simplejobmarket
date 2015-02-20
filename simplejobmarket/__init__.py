#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
app = Flask('application')
#app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

import simplejobmarket.urls



from flask import Flask
app = Flask('application')
#app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

import simplejobmarket.urls


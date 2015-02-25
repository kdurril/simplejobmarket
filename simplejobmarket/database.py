#Database ORM

from simplejobmarket import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kdurril:4054756umd@localhost/postgres'
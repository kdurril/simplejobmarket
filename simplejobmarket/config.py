
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:4054756UMD@localhost/postgres'
    #os.environ['POSTGRESKEY']
    #MAIL_SERVER
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRESKEY']

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRESKEY']

config = {'development':DevelopmentConfig,
          'testing':TestingConfig,
          'production':ProductionConfig,
          'default':DevelopmentConfig
          }

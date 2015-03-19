
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@localhost/postgres'\
                              .format('postgres', '4054756UMD')
                              #'postgres://postgres:4054756UMD@localhost/postgres'
                              #.format(os.environ['USER'], os.environ['POSTGRESKEY'])
    #os.environ['POSTGRESKEY'] 
    #MAIL_SERVER 
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@localhost/postgres'\
                              .format('postgres', '4054756UMD')
                              #.format(os.environ['USER'], os.environ['POSTGRESKEY'])
                              
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@localhost/postgres'\
                              .format('postgres', '4054756UMD')
                              #.format(os.environ['USER'], os.environ['POSTGRESKEY'])

config = {'development':DevelopmentConfig,
          'testing':TestingConfig,
          'production':ProductionConfig,
          'default':DevelopmentConfig
          }

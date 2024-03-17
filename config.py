import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4VeOP4MQiEnjMmevkf6HxtS6I6FDOqDrU0VMALpSu3mW7zBuykLNShSIHQMhsYyrBZErVlWp9SRvAqv4sC1JyHFxiB3aP5dc6gO'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    APP_MAIL_SUBJECT_PREFIX = '[KasiKos]'
    APP_MAIL_SENDER = 'KasiKos Admin <kasikos@gmail.com>'
    APP_ADMIN = os.environ.get('KASIKOS_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://username:password@hostname:port/' + os.path.join(basedir, 'data-dev.sql')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://username:password@hostname:port/' + os.path.join(basedir, 'data-test.sql')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://username:password@hostname:port/' + os.path.join(basedir, 'data.sql')
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

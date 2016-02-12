import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'guess-it-if-u-can'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "timele$$i$"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # poster settings
    POSTER_APPLICATION_ID = ""
    POSTER_APPLICATION_SECRET = ""
    POSTER_REDIRECT_URI = ""
    POSTER_CODE = ""
    # redis and cache settings
    REDIS_HOST = os.environ.get("REDIS_HOST", "redis://localhost:6379")
    RESULT_BACKEND = REDIS_HOST
    BROKER_URL = REDIS_HOST
    CACHE_SETTINGS = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": REDIS_HOST
    }


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb")


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_dev")


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    CACHE_TYPE = None
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://timeless_user:timeless_pwd@localhost/timelessdb_test")

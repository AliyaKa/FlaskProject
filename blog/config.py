import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgres://aliya:RxMI3AlsshkqmNCZNJ0qgzkQDP8DN3nj@dpg-cgk7jh8rddleudtb2oag-a/blog_7ozi"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "80a7a7135a45072ded4c141bb1a4c472"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # CONFIG_NAME = DevConfig

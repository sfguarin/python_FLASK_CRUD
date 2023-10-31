import os
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'jdbc:postgresql://postgres:Onthefuze123.sfguarin@localhost/postgres'
    JWT_SECRET = '123456789'


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Onthefuze123.sfguarin@localhost/postgres'
    JWT_SECRET = '123456789'


import os
from distutils.util import strtobool


class Config(object):
    FLASK_APP = 'api'
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')

    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(strtobool(os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", 'false')))

    JWT_ACCESS_LIFESPAN = {'minutes': 1}

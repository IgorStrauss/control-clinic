import os

from dotenv import load_dotenv
from flask import Config


class TestConfigurations(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY: os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.dev.sqlite'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProductionConfig(Config):
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.prod.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


load_dotenv()

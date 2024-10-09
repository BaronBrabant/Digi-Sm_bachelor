import os, binascii
from flask import Flask, session
from flask_session import Session

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG=False
    # Secret used in encryption
    SECRET_KEY=binascii.hexlify(os.urandom(24))
    # sqlite:///absolute/path/to/database
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'users.db') 

    
    
class ProductionConfig(BaseConfig):
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
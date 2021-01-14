import os
from dotenv import load_dotenv

# loading .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# configuration
class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9b471f1e7466c6e84582d81855994b78'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 9b471f1e7466c6e84582d81855994b78
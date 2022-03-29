import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    ADMINS = ['ikcyprian@ymail.com']
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
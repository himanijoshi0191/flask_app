#Database Configration
import os

class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba267'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'api_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

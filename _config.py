import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'R\\D\x019\x03N\x82\x1c\x04z\xc6\x9c\x9f\x9f\xf5U\xae\xb8\xb0\r\xb9[\xf1'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI ='sqlite:///'+DATABASE_PATH
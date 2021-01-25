# coding=utf-8

SQLALCHEMY_TRACK_MODIFICATIONS = False
# 如果设置成 True (默认情况)，Flask-SQLAlchemy
# 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_ECHO = True
# 打印sql

DEBUG = True

SECRET_KEY = '!@#$%^&*()11'
PERMANENT_SESSION_LIFETIME = 5  # 设置session过期时间

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '10.245.29.91'
PORT = '3306'
DATABASE = 'xpit'
CHARSET = '?UTF8MB4'
SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    DIALECT,
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE

)
JSON_AS_ASCII = False
JSONIFY_MIMETYPE = 'application/json;charset=utf-8'

# coding=utf-8
# 引用Flask
from app import create_app

app = create_app('config.py')

if __name__ == '__main__':
    app.run('127.0.0.1', 8088)

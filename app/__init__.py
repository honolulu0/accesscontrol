# coding=utf-8
from flask import Flask
from .database import db, models
from . import routes


def create_app(config_filename=None):
    app = Flask(__name__)
    if config_filename is not None:
        app.config.from_pyfile(config_filename)  # 初始化配置文件
        configure_database(app)  # 初始化数据库
        routes.init(app)  # 初始化路由 全局拦截器 蓝图加载

    return app


def configure_database(app):
    db.app = app
    db.init_app(app)
    models.init(db)  # 创建数据库表

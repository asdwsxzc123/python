# coding:utf-8
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_session import Session
from flask_wtf import CSRFProtect
from ihome import api_1_0
import redis


# 数据库
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

# 工厂模式,创建app对象的
def create_app(conf_name):
    """ 
    创建flask的应用对象
    :params conf_name: str 配置模式的名字 ('dev', 'prod')
    :return: 
    """
    app = Flask(__name__)

    # 根据服务器的名字获取配置参数的类
    config_class = config_map.get(conf_name)
    app.config.from_object(config_class)

    # 绑定db和app
    db.init_app(app)

    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(
        host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask_session保存到redis中
    Session(app)

    # 为flask补充csrf防护,中间件,对post请求过滤,
    CSRFProtect(app)

    # 注册蓝图
    # app.register_blueprint(api_1_0, url_prefix='/api/v1.0')
    
    return app

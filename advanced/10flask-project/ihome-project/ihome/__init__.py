# coding:utf-8
from flask import Flask, session, blueprints
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_session import Session
from flask_wtf import CSRFProtect
import redis
import logging
from logging.handlers import RotatingFileHandler
# 数据库
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

# 配置日志信息
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)
# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级

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
        host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, password=config_class.REDIS_PWD)

    # 利用flask_session保存到redis中
    Session(app)

    # 为flask补充csrf防护,中间件,对post请求过滤,
    CSRFProtect(app)

    # 注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')
    
    return app

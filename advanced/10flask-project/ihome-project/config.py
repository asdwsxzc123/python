# coding:utf-8
import redis

class Config(object):
    """ 配置信息 """
    SECRET_KEY = 'DSFDS'
    
    # 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://172.16.20.46:3306/ihome'
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    # redis
    REDIS_HOST = '172.16.20.46'
    REDIS_PORT = 6379

    # session
    
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT) 
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400 # session数据的有效期, 单位s

class DevelopmentConfig(Config):
    """ 开发模式的配置信息 """
    DEBUG = True

class ProductionConfig(Config):
    """ 生成环境的配置信息 """
    pass

config_map = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}

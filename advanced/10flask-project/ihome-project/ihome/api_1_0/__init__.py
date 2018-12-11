# coding:utf-8
from flask import Blueprint 
from ihome import db
import logging
from flask import current_app
# 创建蓝图对象
api = Blueprint('api_1_0', __name__)

@api.route('/index')
def index():
    current_app.logger.error('error')
    current_app.logger.warn('warn')
    current_app.logger.info('info')
    current_app.logger.debug('debug')
    return 'hi'

# 导入蓝图的视图函数
from . import demo,verify_code,passport
# coding:utf-8
from flask import Flask, Blueprint
app = Flask(__name__)
# 创建蓝图
admin = Blueprint('admin', __name__)

# 注册蓝图
@admin.route('/admin_index')
def admin_index():
    return 'admin_index'

# app.register_blueprint(admin.url_prefix='/admin')

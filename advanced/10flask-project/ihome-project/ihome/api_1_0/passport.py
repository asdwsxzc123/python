# coding: utf-8
from . import api
from flask import request
@api.route('/users', methods=['POST'])
def register():
    """ 
    注册
    请求的参数: 手机号,短信验证码,密码
    参数格式: json
    """
    # 获取请求的json数据,返回字典
    req_dist = request.get_json()
    mobile = req_dist.get('mobile')
    sms_code = req_dist.get('sms_code')
    password = req_dist.get('password')
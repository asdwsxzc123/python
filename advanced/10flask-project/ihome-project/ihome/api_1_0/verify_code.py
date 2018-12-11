# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import veri_code
from ihome import redis_store,constants, db
from flask import current_app, jsonify, make_response, request
from ihome.utils.response_code import RET
from ihome.models import User
from ihome.libs.yuntongxun.sms import CCP
from io import BytesIO
import random
# 获取参数
# 检验参数
# 业务逻辑处理
# 返回值


@api.route('/image_codes/<image_code_id>')
def get_image_code(image_code_id):
    """ 
    获取图片验证码
    :params image_code_id: 图片验证码变化
    return: 验证码图片
     """
    # 业务逻辑处理
    # 生成验证码图片
    # 名字, 真实文本, 图片数据
    # 将验证码真实值和编号保存到redis中,并设置有效期
    # redis 数据类型 字符串 列表 哈希 set
    # key: xxx
    # image_codes: { 'id1': 'abc'}  哈希 hset('image_codes', 'id1','abc') , hget, hgetall
    # 单条维护记录, 选用字符串
    # 'image_code_编号1': '真实值'
    # 'image_code_编号2': '真实值'
    # redis_store.set('image_code_%s' % image_code_id, text)
    # redis_store.expire('image_code_%s' % image_code_id,
    #                    constants.IMAGE_CODE_REDIS_EXPIRES)
    # out = BytesIO()
    # image.save(out, "png")
    # out.seek(0)
    text, image = veri_code()
    print("图形验证码是：", text.lower())
    print(text)
    try:

        redis_store.setex('image_code_%s' % image_code_id,
                      constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='save image code failed')
    # 返回图片
    resp = make_response(text)
    resp.headers['Content-Type'] = 'image/jpg'
    return resp

@api.route("/sms_codes/<re(r'1[14578]\d{9}'):mobile>")
def get_sms_code(mobile):
    """ 获取短信验证 """
    # 获取参数
    image_code = request.args.get('image_code')
    image_code_id = request.args.get('image_code_id')
    # 校验参数
    if not all([image_code,image_code_id]):
        # 表示参数不完整
        return jsonify(errno=RET.PARAMERR, errmsg='参数不完整')

    # 业务逻辑处理
    # 从redis中取出真实的图片验证码
    try: 
        real_image_code = redis_store.get('image_code_%s' % image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='redis数据库异常')
    # 判断图片验证码是否过期
    if real_image_code is None:
        # 表示图片验证码过期或者没有
        return jsonify(errno=RET.NODATA, errmsg='图片验证失败')
    # 与用户填写的值进行对比
    if real_image_code.lower() != image_code.lower():
        # 表示用户填写错误
        return jsonify(errno=RET.DATAERR, errmsg='图片验证错误')
    # 判断手机号是否存在
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        # 不用终止,可以继续发送短信
    else:
        if user is None:
            # 表示手机号已存在
            return jsonify(errno=RET.DATAEXIST, errmsg='手机号已存在')
    # 如果手机号不存在,则生成短信验证码
    sms_code = '%06d' % random.randint(0,999999)
    # 保存真实的短信验证码
    try:
        redis_store.setex('sms_code_%s' % mobile,constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存发送给这个手机号的记录,防止用户在60s内再次发送短信
        redis_store.setex('send_sms_code_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存短信验证码异常')
    # 发送短信
    ccp = CCP()
    result = ccp.send_template_sms(mobile, [sms_code, int(constants.SMS_CODE_REDIS_EXPIRES/60)],1)
    # 返回值 
    if result == 0:
        # 发送成功
        return jsonify(errno=RET.OK, errmsg='发送成功')
    else:
        return jsonify(errno=RET.THIRDERR, errmsg='发送失败') 

# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import veri_code
from ihome import redis_store
from ihome import constants
from flask import current_app, jsonify, make_response
from ihome.utils.response_code import RET
from io import BytesIO
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

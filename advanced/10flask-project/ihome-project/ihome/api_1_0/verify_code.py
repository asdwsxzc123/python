# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
# 获取参数
# 检验参数
# 业务逻辑处理
# 返回值
@api.route('/image_codes/<image_code_id')
def get_image_code(image_code_id):
   """ 
   获取图片验证码
   :params image_code_id: 图片验证码变化
   return: 验证码图片
    """
    # 业务逻辑处理
    # 生成验证码图片
    # 名字, 真实文本, 图片数据
    name, text, image_data = captcha.generate_captcha()
    # 将验证码真实值和编号保存到redis中,并设置有效期
    # redis 数据类型 字符串 列表 哈希 set
    # key: xxx
    # 返回图片
    
  

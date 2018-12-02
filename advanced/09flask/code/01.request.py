# coding:utf-8
from flask import Flask,request
app = Flask(__name__)

# 192.168.220.138:7788/index?city=shenzhen 查询字符串 querystring

""" 获取请求参数 """
@app.route('/index', methods=['GET', 'POST'])
def index():
    # request中包含了前端发送过来的所有请求数据
    # 通过request.form可以直接提取请求体重的表单格式的数据, 是一个类字典的对象
    # form和data是用来提取请求体数据(POST请求)
    name = request.form.get('name')
    age = request.form.get('age')
    name_li = request.form.getlist('name')
    print(request.data)

    # 用来提取url中的参数(GET请求)
    city = request.args.get('city')
    return 'name = %s, age = %s, city = %s, name_li: %s' % (name, age, city, name_li)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file_obj = request.files.get('pic')
        if file_obj is None:
            # 表示没有发送文件
            return '没有上传文件'

        # 1. 保存文件到本地
        # # 1.创建文件
        # f = open('./demo.jpg', 'wb')
        # # 2. 写入内容
        # data = file_obj.read()
        # f.write(data)
        # # 3. 关闭文件
        # f.close()
        
        # 2. 直接使用上传的文件对象
        file_obj.save('./demo.jpg')
        return '上传成功'
        # f.save()
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7788)


# python2 字符串类型
# str 'utf-8' 'gbk'
# unicode

# a = '中国' #str
# a = u'中国' #unicode
# ASCII cannot decode 
# 在中文字符前加u

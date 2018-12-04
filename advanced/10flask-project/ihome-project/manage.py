# coding:utf-8
from ihome import create_app

# 创建flask应用对象
app = create_app('dev')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7788)
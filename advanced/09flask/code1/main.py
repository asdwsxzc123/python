# coding:utf-8
from flask import Flask
from goods import get_goods
from blueprint import admin
from cart import app_cart
# 循环引用,解决方案,推迟一方一方的导入,让另一方先完成

app = Flask(__name__)

# 通过装饰器获取路径
app.route('/get_goods')(get_goods)

# 注册蓝图
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(app_cart, url_prefix="/cart")

@app.route('/index')
def index():
    
    return 'index page'

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=7788, debug=True)

# gunicorn -w 4 -b 172.16.20.46:7788 --access-logfile ./logs/log main:app;
# gunicorn -w 4 -b 172.16.20.46:5000 --access-logfile ./logs/log main:app;
# gunicorn -w 4 -b 172.16.20.46:5001 --access-logfile ./logs/log1 main:app;
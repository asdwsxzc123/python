# coding:utf-8
from flask import Flask
from goods import get_goods
# 循环引用,解决方案,推迟一方一方的导入,让另一方先完成

app = Flask(__name__)


@app.route('/index')
def index():
    
    return 'index page'

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', port=7788, debug=True)

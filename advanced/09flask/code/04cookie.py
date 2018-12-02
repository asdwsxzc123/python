# coding:utf-8
from flask import Flask, make_response, request,session,current_app

app = Flask(__name__)


@app.route('/index')
def index():
  # 应用上下文
  # current_app.config
  # g变量
  g.username = 'zhangsan '
  g.username = 'zhangsan '
  g.username = 'zhangsan '
    return '111'


@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    # 设置cookie,默认是临时cookie
    resp.set_cookie('type1', 'python1')
    # max_age 设置有效期 单位: 秒
    resp.set_cookie('type2', 'python2', max_age=3600)
    resp.headers['Set-Cookie'] = 'type3=python3;Max-age=3600 '
    return resp


@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get('type1')
    return c


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('del success')
    # 删除cookie,原理是设置让时间到期
    resp.delete_cookie('type1')
    return resp


""" session """
# flask的session需要用到的秘钥字符串
app.config['SECRET_KEY'] = 'asdqwe'

# flask默认吧session保存到了cookie中
@app.route('/set_session')
def set_session():
    session['name'] = 'python'
    session['mobile'] = '18027175287'
    return 'session success'

@app.route('/get_session')
def get_session():
    name = session.get('name')
    return name 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7788,debug=True)

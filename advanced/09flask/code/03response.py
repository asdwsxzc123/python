# coding=utf-8
import json
from flask import Flask, request, abort, Response, make_response,jsonify
app = Flask(__name__)

""" abort """
@app.route('/login', methods=['POST'])
def login():
  name = request.form.get('name')
  pwd = request.form.get('pwd')
  name = ''
  pwd = ''
  if name != 'zhangsan' and pwd != 'admin':
    # 使用abort函数,可以立即终止视图函数的执行,并可以返回给前端,特定的信息
    # 1. 传递状态码信息
    abort(404)
    # 2. 响应体信息
    # resp = Response('login failed')
    # abort(resp)
  return 'login success'


""" 自定义错误处理 """


@app.errorhandler(404)
def handle_404_error(err):
  """ 自定义处理错误方法 """
  # 这个函数的返回值会是前端用户看到的最总结果
  return u'出现了404错误, 错误信息: %s' % err


""" 设置响应体 """


@app.route('/index')
def index():
  # 1. 使用元组,返回自定义的响应信息
  #   响应体  状态码 响应头
  # return 'index page', 400, [('mytype', 'python'), ('city', 'shenzhen')]

  # 2. 使用make_response 来构造响应信息
  resp = make_response('index page 2')
  resp.status = '400 status1'
  resp.headers['city'] = 'sz'
  return resp


""" json格式  """


@app.route('/json1')
def json1():
  # 字典转json json.dumps(data)
  # json转字典 json.loads(data)
  data = {
      "name": "python",
    "age": 15
  }
  # json_str = json.dump(data)
  # print(json_str)
  # return json_str, 200 , {'Content-Type': 'application/json'}
  # jsonify帮助转为json数据,并设置响应头 contenty-type 为 application/json
  # return jsonify(data)
  return jsonify(city='sz', age=18)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7788)

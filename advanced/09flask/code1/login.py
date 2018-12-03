# coding:utf-8
from flask import Flask, request,jsonify
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # 接收参数
    user_name = request.form.get('user_name')
    password = request.form.get('password')

    # 判断参数
    if not all([user_name, password]):
        resp = {
            "code": 1,
            "msg": "invalid params"
        }
        return jsonify(resp)
    if user_name == 'admin' and password == '123456':
        resp = {
            "code": 0,
            "msg": "login success"
        }
        return jsonify(resp)
    else: 
        resp = {
            "code": 2,
            "msg": "wrong user name or password"
        }
        return jsonify(resp)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=7788, debug=True)

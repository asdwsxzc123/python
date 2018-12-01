# coding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'hi'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7788)
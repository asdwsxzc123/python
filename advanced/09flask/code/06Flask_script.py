# coding:utf-8
from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manger = Manager(app)
@app.route('/index')
def index():
   return 'index page'
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=7788, debug=True)
    manger.run()

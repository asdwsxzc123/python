# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
app = Flask(__name__)
manager = Manager(app)

class Config(object):
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:geesunn123@192.168.220.138:3306/books'
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
    # 迷药
    SECRET_KEY = 'sdfgsdf'


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# manager 是flask-script的实例,添加一条db命令
manager.add_commond('db', MigrateCommand)

@app.route('/index')
def index():
   return 'index page'
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=7788, debug=True)
    manger.run()

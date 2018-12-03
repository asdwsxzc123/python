# coding:utf-8
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)

class Config(object):
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.16.20.46:3306/books'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:geesunn123@192.168.220.138:3306/books'
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

# 创建flask脚本对象
manager = Manager(app)

# 创建数据库迁移工具
Migrate(app, db)

# 向manager对象添加数据库操作指令
manager.add_command('db', MigrateCommand)

class Author(db.Model):
    """ 作者 """
    __tablename__ = 'tbl_authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64))
    books = db.relationship('Book', backref='author')

class Book(db.Model):
    """ 书籍 """
    __tablename__ = 'tbl_books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))

# 创建表单模型类


class AuthorBookForm(FlaskForm):
    """ 作者数据模型类 """
    author_name = StringField(label=u"作者", validators=[DataRequired('作者必填')])
    book_name = StringField(label=u"书籍", validators=[DataRequired('书籍必填')])
    submit = SubmitField(label=u"保存")


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        book = Book(name=book_name, id=author.id)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template('author_book.html', authors=author_li, form=form)

""" post json """
# @app.route('/delete_book', methods=['POST'])
# def delete():
#     """ 删除 """
#     # req_data = request.data
#     # json.loads(req_data)
#     # 如果前端是json
#     print(request)
#     req_dict = request.get_json()
#     book_id = req_dict.get('book_id')
#     book = Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     # "Content-Type": 'application/json'
#     return jsonify(code=0, message="ok")

""" get 传参"""
@app.route('/delete_book', methods=['GET'])
def delete():
    """ 删除 """
    print(request)
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    # #生成数据
    # au_xi = Author(name=u'我吃西红柿')
    # au_qian = Author(name=u'萧潜')
    # au_san = Author(name=u'唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()

    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒',author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅',author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨',author_id=au_san.id)
    # #把数据提交给用户会话
    # db.session.add_all([bk_xi,bk_xi2,bk_qian,bk_san])
    # #提交会话
    # db.session.commit()
    # app.run(host="0.0.0.0", port=7788, debug=True)
    
    manager.run()
    # python 10book_tmp.py db init
    # 迁移
    # python 10book_tmp.py db migrate == makemigration
    # 更新数据库
    # python 10book_tmp.py db upgrade == migrate
    # 创建自动迁移脚本
    # python 10book_tmp.py db migrate -m 'init'
    # 查看版本
    # python 10book_tmp.py db history
    # 回滚
    # python 10book_tmp.py db downgrade b1d25a7c7fd6


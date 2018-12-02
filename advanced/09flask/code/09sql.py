# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
app = Flask(__name__)
class Config(object):
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:geesunn123@192.168.220.138:3306/Flask_test'
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 自动更新数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)
# 创建数据库sqlalchemy工具
db = SQLAlchemy(app)

# 表名规范
#  ihome -> ih_user 数据名缩写_表名
#  tbl_user tbl_表名

# 创建数据模型类
class User(db.Model):
    """ 用户表 """
    __tablename__ = 'tbl_users' # 数据库的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email =  db.Column(db.String(128), unique=True)
    password =  db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))

    def __repr__(self):
        """ 定义之后,可以让现实对象的时候更直观 """
        return 'user object: name = %s' % self.name
class Role(db.Model):
    """ 角色表 """
    __tablename__ = 'tbl_roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        """ 定义之后,可以让现实对象的时候更直观 """
        return 'role object: name = %s' % self.name
@app.route('/index')
def index():
    pass

""" 查询 """
def query():
    # 1.对象方式
    # Role.query.all()
    # Role.qeury().get(2)
    # Role.qeury().first()

    # 过滤
    # 多个
    # User.query.filter_by(name='wang', role_id=1).first()
    # 一个
    # user =  User.query.filter(User.name='wang', User.role_id=1).first()
    # 或和模糊查询 (或者关系)
    # user =  User.query.filter( or_(User.name='wang', User.email.endswith('163.com')).all()
    # limit(需要的条数) 和offset (偏移,要跳过的条数)
    # user = User.query.filter().offset().limit().orderby().all()
    # user = User.query.filter().offset(2).limit(1).orderby('-id').all()
    # user = User.query.filter().orderby(User.id.desc()).all()

    # 关联查询
    # ro = Role.query.get(user.role_id)

    # user.role.name

    # 2.原始方法
    # db.session.qeury(Role).all()
    data = db.session.query(User.role_id, func.count(User.role_id)).Group(User.role_id)
    print(data)

""" 修改和删除数据 """
def set():
    # 先查询,在删除和修改
    """ 更新 """
    # 方法1
    # user = User.query.get(1)
    # user.name = 'python'
    # db.session.add(user)
    # db.session.commit()

    # 方法2
    # User.query.filter_by(name='zhang').update({'name': 'python', 'email': 'sdf@124.com'})
    # db.session.commit()

    """ 删除 """
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()
if __name__ == "__main__":
    # 清除数据库所有表
    db.drop_all()
    # 创建所有的表
    db.create_all()

    role1 = Role(name='admin')
    # db.session.add(role1)
    # db.session.commit()

    role2 = Role(name='stuff')
    # db.session.add(role2)
    db.session.add_all([role1, role2])

    db.session.commit()

    # us1 = User(name='wang', email='wang@163.com',
    #            password='123456', role_id=role1.id)
    # us2 = User(name='zhang', email='zhang@189.com',
    #            password='201512', role_id=role2.id)
    # us3 = User(name='chen', email='chen@126.com',
    #            password='987654', role_id=role2.id)
    # us4 = User(name='zhou', email='zhou@163.com',
    #            password='456789', role_id=role1.id)
    # db.session.add_all([us1, us2, us3, us4])
    # db.session.commit()
    # app.run(host="0.0.0.0", port=7788, debug=True)
    # query()

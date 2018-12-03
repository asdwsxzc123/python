""" flask """
# 轻量级框架,需要使用拓展包
# flask-sqlalchemy 数据库操作
# flask-migrate 管理迁移数据库
# flask-mail 邮件
# flask-wtf 表单
# flask-script 插入脚本
# flask-login 认证用户状态
# flask-restful: 开发rest api
# flask-bootstrap
# flask-momnet 本地化日期和时间


# 将包导出
# pip freeze > requirements.txt

# 安装包文件
# pip install -r requirements.txt



# flask的上下文
# 请求上下文
# 线程局部变量,request可以拿到不同用户的信息
request = {
  '线程a': {
    'form': {
      'name': 'zhangsan'
    },
    'args': {}
  },
  '线程a': {
    'form': {
      'name': 'zhangsan'
    },
    'args':{}
  }
}

# 应用上下文
# current_app: 整个应用程序上下文
# g变量,临时存储


# Flask-Script 拓展命令 
pip install Flask-Script
pip install flask_wtf

# flask 变量

# url_for
# request
# config
# flash

""" sql """
pymysql.install_as_mysqldb()
pip install pymysql
pip install flask-sqlalchemy
pip install flask-mysqldb


""" migrate """
pip install flask-migrate
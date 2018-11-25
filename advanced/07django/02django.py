# 安装虚拟环境 virtualenv virtualenvwrapper

# django-admin startproject test1

# __init__.py: 说明是一个python包
# settings.py 项目的配置文件
# urls.py 路由的配置
# wsgi.py web服务器和django交互入口
# manage.py 项目管理的文件

# 创建应用陌路
# python manage.py startapp booktest

# booktest
# models.py 写和数据库项目的内容
# views.py 请求数据,进行处理.定义处理函数,视图函数
# tests.py 写测试代码的文件
# admin.py 网站的后台管理配置

# 建立应用和项目之间的联系,需要对应用进行注册
# 修改settings.py的INSTALLED_APPS配置
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


""" models """
# 生成迁移文件
# python manage.py makemigrations
# 执行迁移文件
# python manage.py migrate
# b.btitle = '天龙八部'
# b.bpub_data = date('1900,1,1')
# b.save()
# b2 = BookInfo.objects.get()
# b2.delete() 
# 查看所有的信息
# BookInfo.objects.all()

# 英雄人物类
# 英雄名 hname
# 性别 hgender
# 年龄 hage
# 备注 hcomment
# 关系属性 hbook建立图书类和英雄人物类之间的一堆多的关系
# class HeroInfo(models.Model):
#     """ 英雄人物模型类 """
#     hname = models.CharField(max_length=20)
#     # 性别,default默认指定类型 False代表男
#     hgender = models.BooleanField(default=False)
#     hage = models.IntegerField()
#     hcomment = models.CharField(max_length=128)
#     hbook = models.ForeignKey('BookInfo')

""" 后台管理 """
# 1.语言和时区本地化, settings
# 2.创建管理员
# python manage.py createuperuser

""" 3. 注册模型类 """
# 在应用下admin.py 中注册模型类

""" 4. 路由 """
urls.py

# 项目的urls
# index
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), #配置项目
    url(r'^', include('booktest.urls')), # 包含booktest应用中的urls文件

]

# 创建应用的urls.py文件
from django.conf.urls import url
from booktest import views
urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index$', views.index), # 建立视图与url的关联
    url(r'^index2$', views.index2)
]

# 在views添加views
from django.http import HttpResponse
# Create your views here.
# 1.定义视图函数，httpresponse
# 2.进行url配置, 简历url地址和视图的对应关系
# 172.16.20.46:7788/index2
def index(request):
    return HttpResponse('hello,world')
def index2(request):
    return HttpResponse('hello,world2')


""" 5. 配置模板"""
# settings.py
# 'DIRS': [os.path.join(BASE_DIR, 'templates')],
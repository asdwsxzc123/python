from django.conf.urls import url
from booktest2 import views
urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index$', views.index), # 渲染图书
    url(r'^create$', views.create), # 新增图书
    url(r'^delete/(\d+)$', views.delete), # 删除图书
]
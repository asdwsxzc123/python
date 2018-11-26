from django.conf.urls import url
from booktest import views
urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index$', views.index), # 建立视图与url的关联
    url(r'^index2$', views.index2),
    url(r'^books$', views.show_books),
    url(r'^books/(\d+)$', views.detail),
]
from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
from django.template import loader, RequestContext
# Create your views here.
# 1.定义视图函数，httpresponse
# 2.进行url配置, 简历url地址和视图的对应关系
# 172.16.20.46:7788/index2


# def render(request, path, options):
#     # 使用模板文件
#     # 1.加载模板文件
#     temp = loader.get_template(path)
#     # 2. 定义模板上下文
#     context = RequestContext(request, options)
#     # 3.渲染模板,产生标准的html内容
#     res_html = temp.render(context)
#     # 4. 返回给浏览器
#     return HttpResponse(res_html)


def index(request):
    return render(request, 'booktest/index.html', {'content': 'hello world', 'list': list(range(0, 10))})


def index2(request):
    return HttpResponse('hello,world2')


def show_books(request):
    """ 显示图书的信息 """
    # 1. 查找图书
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    # 1. 根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2. 查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    # 3. 调用模板
    return render(request, 'booktest/detail.html', {'heros': heros, 'book': book})

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
# Create your views here.
# 1.定义视图函数，httpresponse
# 2.进行url配置, 简历url地址和视图的对应关系
# 172.16.20.46:7788/index2


def index(request):
    # 使用模板文件
    # 1.加载模板文件
    temp = loader.get_template('booktest/index.html')
    # 2. 定义模板上下文
    context = RequestContext(request, {'content':'hello world' , 'list': list(range(0,10))})
    # 3.渲染模板,产生标准的html内容
    res_html = temp.render(context)
    # 4. 返回给浏览器
    return HttpResponse(res_html)
def index2(request):
    return HttpResponse('hello,world2')


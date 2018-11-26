from django.shortcuts import render,redirect
from booktest2.models import BookInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest2/index.html', {'books': books})

def create(request):
    """ 新增图书 """
    # 1. 创建一个bookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    
    # 2. 保存近数据库
    b.save()

    # 3. 返回内容,让浏览器在访问首页
    # return HttpResponse('ok')
    # return HttpResponseRedirect('/index')
    return redirect('/index')

def delete(request,bid):
    # 1. 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2. 删除
    book.delete()
    # 3. 重定向
    # return HttpResponseRedirect('/index')
    return redirect('/index')
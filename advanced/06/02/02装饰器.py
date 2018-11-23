# def foo():
#   print('foo')
# # 匿名函数
# foo = lambda x: x+1


# 开放封闭原则
# 封闭: 已实现的功能代码块
# 开放: 对拓展开发

# 通过装饰器,在不修改代码的原则,做回调
# def w1(func):
#   def inner():
#     # 验证1
#     # 验证2
#     print('---这是权限验证1---')
#     func()
#   return inner
# def w2(func):
#   def inner():
#     # 验证1
#     # 验证2
#     print('---这是权限验证2---')
#     func()
#   return inner

# @w1
# @w2
# def f1():
#   print('f1')
# @w1
# def f2():
#   print('f2')
# @w1
# def f3():
#   print('f3')
# @w1
# def f4():
#   print('f4')

# f1()

# 传递单个参数
# def set_func(func):
#   def call_func(num):
#     print('----')
#     num += 1
#     func(num)
#   return call_func

# @set_func
# def test(num):
#   print(num)
# test(100)

# 多个参数
# def set_func(func):
#   def call_func(*args,**kwargs):
#     print('1111')
#     func(*args,**kwargs)
#   return call_func
# @set_func
# def test(num,*args,**kwargs):
#   print(num)
#   print(args)
#   print(kwargs)
# test(100,200,300,mm=200)
  
  

# 带有返回值的函数进行装饰
# def set_func(func):
#   def call_func(*args,**kwargs):
#     # 普通的函数
#     # func(args,kwargs)
#     # 带返回值的,需要拆包
#     return func(*args,**kwargs)
#   return call_func
# @set_func
# def test(num,*args,**kwargs):
#   print(num)
#   print(args)
#   print(kwargs)
#   return 'ok'

# @set_func
# def test2():
#   pass

# ret = test(100,200,300,mm=200)
# print(ret)
# ret1 = test2()
# print(ret1)

# def add_auth(func):
#   print('---进行装饰去权限1的功能--2-')
#   def call_func(*args,**kwargs):
#     print('权限一3')    
#     return func(*args,**kwargs)
#   return call_func

# def add_xx(func):
#   print('-----装饰xx-----1')
#   def call_func(*args, **kwargs):
#     print('xxx的功能4')
#     return func(*args,**kwargs)
#   return call_func

# @add_auth
# @add_xx
# def test1():
#   print('test15')
# test1()



# def set_func(func):
#   def call_func():
#     str = func()
#     return '<td>' + str + '</td>'
#   return call_func

# # 要加上h1标签
# def setH1(func):
#   def call_func():
#     str = func()
#     return '<h1>' + str + '</h1>'
#   return call_func

# @setH1
# @set_func
# def get_str():
#   return 'haha'
# print(get_str()) # <h1><td>haha</td></h1>

""" 使用类当做装饰器 """

class Test(object):
  def __init__(self,func):
    self.func = func
  def __call__(self):
    return self.func()

@Test # get_str = Test(get_str)
def get_str():
  return  'haha'
print(get_str())


# 静态
# 静态URL:
# 物理路径,真是存在服务器里面
# 优点: 网站打开速度快,不进行运算,有利于记忆,有利于SEO
# 缺点: 对于中大型网站,比较繁琐,占用大量空间

#动态URL
# 带问号的路径,只是一个逻辑地址,并不是真是存在服务器网盘中
# 优点: 适合中大型网站,修改页面方便,占用的硬盘空间较小
# 缺点: 不利于SEO优化

# 伪静态URL
# 弄一个假的html,


# 导入数据
# create database stock_db charset=utf8;
# use stock_db;
# source stock_db.sql;
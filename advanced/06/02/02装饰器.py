# def foo():
#   print('foo')
# # 匿名函数
# foo = lambda x: x+1


# 开放封闭原则
# 封闭: 已实现的功能代码块
# 开放: 对拓展开发

# 通过装饰器,在不修改代码的原则,做回调
def w1(func):
  def inner():
    # 验证1
    # 验证2
    print('---这是权限验证1---')
    func()
  return inner
def w2(func):
  def inner():
    # 验证1
    # 验证2
    print('---这是权限验证2---')
    func()
  return inner

@w1
@w2
def f1():
  print('f1')
@w1
def f2():
  print('f2')
@w1
def f3():
  print('f3')
@w1
def f4():
  print('f4')

f1()

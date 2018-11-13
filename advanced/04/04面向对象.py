#  为了完成比较负责点任务，往往需要多个函数配合
#  当一个函数为了收到一个数据，为了让其他的函数中能够直接使用，很多人想到使用全局变量来实现传递，并发会对同一个全局变量操作

# __dict__ 获取所有的属性
# __class__  

""" 多态 """

""" 多继承 和 MRO"""
# 一个类,可以有多个父类
# 不能把元组和字典当做参数传递

""" proerty属性 """
# class Foo(object):
#   def func(self):
#     pass
#   @property
#   def size(self):
#     return 100
# foo_obj = Foo()
# size = foo_obj.size #调用property属性,获取属性值
# print(size)

# 分页
# class Pager:
#   def __init__(self, current_page):
#     self.current_page = current_page
#     self.per_items = 10
#   @property
#   def start(self):
#     val = (self.current_page -1) *self.per_items
#     return val
#   @property
#   def end(self):
#     val = self.current_page * self.per_items
#     return val
# p = Pager(1)
# p.start
# p.end

# 新式类的三种方式property
class Goods:
# 方式一:
#   @property:
#   def price(self):
#     return 111
#   # 设置属性
#   @price.setter
#   def price(self,value):
#     print('set')
#   # 删除
#   @price.deleter
#   def price(self):
#     print('deleter')
# obj = Goods()
# obj.price
# obj.price = 123
# del obj.price

# 方式二: 通过类属性来创建
# class Foo:
#   def get_bar(self):
#     return 'laowang'
#   def set_bar(self):
#     return 'laowang'
#   BAR = property(get_bar,set_bar)

# obj = Foo()
# result = obj.BAR
# print(result)


# 重写和重载
# 重写 覆盖, 重载是根据传的参数不一样,调用的方法不一样 
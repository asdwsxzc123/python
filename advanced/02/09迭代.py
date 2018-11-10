# 1. 迭代器
# 迭代是访问集合元素的一种方式,迭代器是一个可以记住遍历的位置的对象,迭代器对象从集合的第一元素开始访问,所有元素被访问结束,迭代器只能往前不往后

# 1. 可迭代对象
# 我们把可以for in 拿到数据为遍历,也叫迭代

# isinstance([11,22,33], Iterable)
import time
from collections.abc import Iterable
class Classmate(object):
  def __init__(self):
    self.names = list()
  def add(self, name):
    self.names.append(name)
  # 添加iterable
  def __iter__(self):
    return ClassIterator(self)

class ClassIterator(object):
  def __init__(self, obj):
    self.obj = obj
    
  def __iter__(self):
    pass
  def __next__(self):
    return 11
classmate = Classmate()
classmate.add('老王')
classmate.add('老王1')
classmate.add('老王2')
# print ('判断classmate是否可以迭代的对象:', isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print(next(classmate_iterator))
for name in classmate:
  print(name)
  time.sleep(1)
# python2
# range 是直接生成数据的结果
# xrange 是生成数据的方式,调用的时候才生成

# python3 range 是相当于xrange
import time
from collections.abc import Iterable
from collections.abc import Iterator

# class Classmate(object):
#   def __init__(self):
#     self.names = list()
#     self.current_num = 0
#   def add(self, name):
#     self.names.append(name)
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if len(self.names) > self.current_num:
#       ret = self.names[self.current_num]
#       self.current_num += 1
#       return ret
#     else :
#       raise StopIteration

# classmate = Classmate()
# classmate.add('张三')
# classmate.add('李四')
# classmate.add('王五')

# for name in classmate:
#   print(name)
#   time.sleep(1)

""" 斐波拉其数量 """
# 方法一
# nums = list()
# a = 0
# b = 1
# i = 0
# while i < 10:
#   nums.append(a)
#   a, b = b, a+b
#   i += 1
# for num in nums:
#   print(num)

# 方法二

# class Fibonacci(object):
#   def __init__(self,all_num):
#     self.all_num = all_num
#     self.current_num = 0
#     self.a = 0
#     self.b = 1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if self.all_num < self.current_num:
#       ret = self.a
#       self.a, self.b = self.b, self.a + self.b
#       self.current_num += 1
#       return ret
#     else:
#       raise StopIteration

# fibo = Fibonacci(10)

# for num in fibo:
#   print(num)
#   time.sleep(1)

""" 其他方式也可以接收迭代器 """
# 元组转化成列表.列表转化成元组
list((11,22))
tuple(list(11,22))

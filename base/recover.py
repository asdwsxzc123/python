# 1. 标识符, 关键字
  # if/else/elif/break/continue/for/while/and/or/not/in/
  # True/False/try/except/finally/as/import/from/def/
  # class/return/None/global/lambda

# 2. 变量,输入,输出
#   a = 100

# 3. 字符串,列表,元组,字典,集合,列表生成式,类型转化
#  'aaa'
#   a = 'abcd'
#   a[:3]-->'abc'
#   a[::-1] --> 'dcba'
#   [123,232,42] 列表增删改查
#   (12,44,2,1) 元组只读
#   {1,2,3,4} 集合元素不重复
#   {key:value} 字典,key只能是不可变类型,value都可以
#   可变类型: 列表,字典,集合
#   不可变类型: 数字,字符串,元组

# 4.切片
#   顺序,选择,循环

# 5. if
#   if :
#     pass
#   elif:
#     pass:
#   else:
#     pass

# 6.while

# 7.for
  # for i in a:
  #   pass

# 8.各种嵌套

# 9.函数,参数,返回值,全局/局部变量,多个return,一个return多个返回值
  # def fn(形参):
  #   return 

  # fn(实参)
  # *args元组,**kwargs字典
  # def test(a,b,c=100,*args,**kwargs):
  #   pass

  # global 全局变量

  # 结束一个函数 return
  # 结束一个循环: break/continue
  # 结束一个程序: exit()

# 10.类,对象
# class Animal(父类):
#   # 类属性
#   num = 100
#   实例方法
#   def __init_(self):
#     self.xxx = 100 实例属性
#   实例方法修改类属性
#   def test(self):
#     Animal.num = 300
#   # 类方法
#   @classmethod
#   def xxx(cls):
#     pass
#   静态方法
#   @staticmethod
#   def xxx():
#     pass


# 11.异常
# try :
#   xxxx
# except 异常名:
#   异常处理
# else :
#   没有异常的处理
# finally:
#   不管产不产生异常都执行

# 12.模块.,包
# import 模块.包
# xxx.method()

# from 模块 import test1,test2
# from ... import *

# if __name__ == '__main__':
#   xxx
""" 
实例属性: 和具体的某个实例对象有关系
并且一个实例对象和另一个实例对象不共享方法
类属性: 雷属性所属于类对象
并且多个实例对象之间 共享同一个类属性
# 实例方法 必须有参数self
# 类方法 必须有参数cls @classmethod 可以通过类的名字调用,静态方法,也可以通过实例去调用
# 静态方法 @staticmethod  可以通过类的名字调用,静态方法,也可以通过实例去调用
 """
class Tool(object):
  # 类属性
  num = 0
  # 实例方法
  def __init__(self,new_name):
    # 实例属性
    self.name = new_name
    # 调用类属性
    Tool.num += 1
  def __str__(self):
    return '%s:%d' % (self.name,self.num)
  # 类方法
  @classmethod
  def add_num(cls):
    cls.num = 100
  # 静态方法
  @staticmethod
  def print_menu():
    print('静态方法')
tool1 = Tool('铁锹')
print(tool1)
tool2 = Tool('兵工厂')
# 类方法可以通过类的名字调用,静态方法,也可以通过实例去调用
tool2.add_num()
print(tool2)
Tool.add_num()
tool3 = Tool('水桶')

Tool.print_menu()
tool2.print_menu()
print(tool3)

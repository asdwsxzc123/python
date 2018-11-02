""" 
做了三件事
1. 调用__new__方法来创建对象,然后找了一个变量来接收__new__的返回值,这个返回值表示创建出来的对象的引用
2. __init__(刚刚创建出来的对象的应用)
3. 返回对象的引用

单例: 
不管创建了多少个对象,指向的是同一个class
 """
""" class Dog (object):
  def __init__(self):
    print('---init')
  def __del__(self):
    print('---del')
  def __str__ (self):
    print('---str')
    return '对象的描述'
  def __new__(cls):
    # print(id(cls))
    print('---new--')
    return object.__new__(cls) """

class Dog (object):
  __instance = None
  __init_flag = False
  def __new__(cls,name):
    if cls.__instance == None:
      cls.__instance = object.__new__(cls)
      return cls.__instance
    else:
      return cls.__instance
  def __init__(self,name):
    if Dog.__init_flag == False:
      self.name = name
      Dog.__init_flag = True


xtq =Dog('哮天犬')
print(xtq.name)
xtq1 =Dog('哮天犬1')
print(xtq1.name)
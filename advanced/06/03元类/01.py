# 类也是对象
# __dict__可以看类里面有什么
# 万物都是元类创建的
# type创建一个类
# __class__查找是谁创建的,最终都是元类创造的
class Test1:
  num=10
  num2=200

# 使用class实际上就调用了type
Test1 = type('Test1', (), {'num':10,'num2':200})


def Test_1(self):
  print('实例方法')

Test3 = type('Test3', {}, {'Test_1': Test_1})


@classmethod
def test_3(cls):
  print('类方法')


Test4 = type('Test4', (), {'Test_1': Test_1, 'test_3': test_3})


# 元类
# 1.拦截类的创建
# 2.修改类

# mateclass
# 方法1
def uper_attr(class_name,clas_parents,class_attr):
  new_attr = {}
  for name, value in class_attr.items():
    if not name.startswith('__'):
      new_attr[name.upper()] = value
  return type(class_name, clas_parents, class_attr)
class Foo(object, mateclass=uper_attr):
  bar = 'bip'

# 方法2
class UpperAttrMetaClass(type):
  def __new__(cls,class_name,clas_parents,class_attr):
    new_attr = {}
    for name, value in class_attr.items():
      if not name.startswith('__'):
        new_attr[name.upper()] = value
    return type(class_name, clas_parents, class_attr)
    
class Foo(object, mateclass=uper_attr):
  bar = 'bip'
# 类的构成
# 1. 类名
# 2. 类的属性
# 3. 类的方法

# 类名
class Cat:
  # 属性
  # color: 'yellow'
  # 方法
  # 初始化对象,每次创建对象,都会初始化
  def __init__(self,new_name, new_age):
    print('--init--')
    self.name = new_name
    self.age = new_age
    # 实例return的东西
  def __str__(self):
    return ('%s的年龄是:%d' % (self.name, self.age))
# 创建一个对象
  def eat(self):
    print('猫咪在吃东西')
  def drink(self):
    print('猫咪在喝水')

  def introduce(self):
    print('%s的年龄是:%d' % (self.name, self.age))
# 创建一个对象
tom = Cat('汤姆',12)
lanmao = Cat('蓝猫',12)
print(tom)
# tom.eat()

# 给tom对象添加属性
# tom.name = '汤姆'
# tom.age = 5

# 获取属性的第一种方法
# print('%s的年龄是:%d'%(tom.name,tom.age))

# 获取属性的第2种方法
# tom.introduce()  # 相当于 tom.introduce(tom)


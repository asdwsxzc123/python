# 以y=kx+b, y=ax^2 +bx +c
# 计算一条线上的点,给x值,求y

# 方法1
# def line_2(k,b,x):
#   print(k*x + b)

# line_2(1,2,0)
# line_2(1,2,1)
# line_2(1,2,2)
# 缺点,想要多次计算y的值,需要每次传递

# print('='*50)

# # 方法2
# k =1
# b=2
# def line_2(x):
#   print(k*x + b)

# line_2(0)
# line_2(1)
# line_2(2)
# 缺点:如果计算多条线上的值,那么需要每次对全局变量进行修改,代码会增多,麻烦


# print('='*50)

# # 方法3,缺省参数
# def line_2(x,k=1,b=2):
#   print(k*x + b)

# line_2(0)
# line_2(1)
# line_2(2)

# line_2(0,k=11,b=22)
# line_2(1,k=11,b=22)
# line_2(2,k=11,b=22)
# 优点: 比全局变量更好,可以被修改
# 缺点:如果计算多条线上的值,那么需要每次进行传参,代码会增多,麻烦

# 方法4实例对象
# class Line5(object):
#   def __init__(self,k,b):
#     self.k = k
#     self.b = b
#   def __call__(self,x):
#     print(x*self.k + self.b)

# line_5_1 = Line5(1,2)
# line_5_1(0)
# 缺点有多个实例,浪费资源

# 5.闭包

# def line_6(k,b):
#   def create_y(x):
#     print(k*x+b)
#   return create_y
# line_6_1 = line_6(1,2)
# line_6_1(0)
# line_6_1(1)
# line_6_1(2)

# 传递一个简单的数据和功能,直接可以使用闭包

x = 300
def test1():
  x=200
  def test2():
    nonlocal x
    print('%d----1'%x)
    # 变量相当于js的 let,不会有变量提升
    x=200
    print('%d----2'%x)
  return test2
t1 = test1()
t1()
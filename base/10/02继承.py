""" 
继承
重写
调用父类
私有方法在继承中的表现
多继承
 """
""" # 基类
class Animal:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def eat(self):
        print('吃')
    def __test(self):
        print('我是私有方法')

# 继承
# 子类
class Dog(Animal):
    def bark(self):
        print('--汪汪--')

class Xiaotq(Dog):
    def fly(self):
        print('---飞---')
    # 重写
    def bark(self):
        print('---我汪---')
        # 第一种.调用父类的方法 
        # Dog.bark(self)

        # 第二种.调用父类的方法 
        super().bark()

xiaotianq = Xiaotq()
xiaotianq.bark()
xiaotianq.eat() """

# 多继承
# 顶层继承object，新式类， 什么都不写经典类（过时）


class Base(object):
    def test(self):
        print('--base')


class A(Base):
    def test1(self):
        print('---test1')


class B(Base):
    def test2(self):
        print('--test2')


class C(A, B):
    pass


a = A()
a.test()
c = C()
c.test1()
c.test2()
# print(c.__mro__)

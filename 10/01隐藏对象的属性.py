""" 
私有属性
私有方法
调用私有方法
del方法
引用计数
 """
""" class Dog:
    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age


dog = Dog()
dog.set_age(15)
age = dog.get_age()
print(age)

 """

""" 
class Dog:
    def __init__(self):
        self.num1 = 100
        # 私有属性
        self.__num2 = 200
    #  私有方法 __
    def __send_msg(self):
        print('--正在发短信---')
    # 共有方法

    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print('---共有方法---')


dog = Dog()
dog.send_msg(100000) """

""" del 方法 """

""" 
class Dog:
	# 删除对象时会调用
	def __del__(self):
		print('---英雄over---')

dog1 = Dog()
# 指针指向dog1
dog2 = dog1
# 对象的引用计数
import sys

count = sys.getrefcount(dog2)
print(count)
del dog1
del dog2
print('----------') """


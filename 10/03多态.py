""" 
多态,根据当前的对象,来确定调用的方法
定义时 的类型和运行时的类型不一样,此时就成为多态
 """
class Dog(object):
  def print_self(self):
    print('大家好,我是xxx,请多指教')
  
class Xiaotq(Dog):
  def print_self(self):
    print('hello,我是你们的老大')
  
def introduce(temp):
  temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()
introduce(dog1)

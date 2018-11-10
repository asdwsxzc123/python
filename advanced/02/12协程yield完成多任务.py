# 并发,协程比线程更小
import time
from greenlet import greenlet

# def task_1():
#   while True:
#       print('-----1')
#       time.sleep(0.1)
#       yield
# def task_2():
#   while True:
#       print('-----2')
#       time.sleep(0.1)
#       yield

# def main():
#   t1 = task_1()
#   t2 = task_2()
#   while True:
#     next(t1)
#     next(t2)
# if __name__ == '__main__':
#   main()

""" greenlet """
# gr1 = None
# gr2 = None

# def task_1():
#   global gr2
#   while True:
#       print('-----1')
#       gr2.switch()
#       time.sleep(0.1)
# def task_2():
#   global gr1
#   while True:
#       print('-----2')
#       gr1.switch()
#       time.sleep(0.1)

# def main():
#   global gr2
#   global gr1
#   gr1 = greenlet(task_1)
#   gr2 = greenlet(task_2)
#   # 切换到gr1执行
#   gr1.switch()
# if __name__ == '__main__':
#   main()

""" gevent """
# 协程是将延时的时间利用起来去操作
# 
import gevent
from gevent import monkey
# 这个函数可以将所有的time.sleep()替换成gevent.time()
monkey.patch_all()
def f(n):
  for i in range(n):
    print(gevent.getcurrent(),i)
    # time.sleep(2)
    gevent.sleep(0.5)
def f2(n):
  for i in range(n):
    print(gevent.getcurrent(),i)
    # time.sleep(2)
    gevent.sleep(0.5)
def f3(n):
  for i in range(n):
    print(gevent.getcurrent(),i)
    # time.sleep(2)
    gevent.sleep(0.5)

# 方法一
# print('-----1--')
# g1 = gevent.spawn(f,5)
# print('-----2--')
# g2 = gevent.spawn(f2,5)
# print('-----3--')
# g3 = gevent.spawn(f3,5)
# g1.join()
# g2.join()
# g3.join()

# 方法二
gevent.joinall([
  gevent.spawn(f,5),
  gevent.spawn(f2,5),
  gevent.spawn(f3,5),
])
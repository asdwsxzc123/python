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
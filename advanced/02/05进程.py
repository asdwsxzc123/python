# 进程:
# 程序: xxx.py这是一个程序,是一个静态的
# 进程: 一个程序运行起来后,代码+用到的资源叫做精彩,是操作系统分配资源的基本单元

# 新建,就绪,运行,死亡,等待(堵塞)
# 就绪态:运行的条件都已经慢去
# 执行太:cpu正在执行其功能
# 等待态:等待模型条件满足执行,如sleep
import threading 
import time
import multiprocessing
def test1():
  while True:
    print('-----1')
    time.sleep(1)
def test2():
  while True:
    print('-----2')
    time.sleep(1)
def main():
 #  t1 = threading.Thread(target= test1)
 #  t2 = threading.Thread(target= test2)
 #  t1.start()
 #  t2.start()
  
   t1 = multiprocessing.Process(target= test1)
   t2 = multiprocessing.Process(target= test2)
   t1.start()
   t2.start()
if __name__ == '__main__':

   main()

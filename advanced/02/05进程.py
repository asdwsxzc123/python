# 进程:
# 程序: xxx.py这是一个程序,是一个静态的 ps -aux, kill uid
# 进程: 一个程序运行起来后,代码+用到的资源叫做精彩,是操作系统分配资源的基本单元

# 新建,就绪,运行,死亡,等待(堵塞)
# 就绪态:运行的条件都已经慢去
# 执行太:cpu正在执行其功能
# 等待态:等待模型条件满足执行,如sleep
# import threading 
# import time
# import multiprocessing
# def test1():
#   while True:
#     print('-----1')
#     time.sleep(1)
# def test2():
#   while True:
#     print('-----2')
#     time.sleep(1)
# def main():
#  #  t1 = threading.Thread(target= test1)
#  #  t2 = threading.Thread(target= test2)
#  #  t1.start()
#  #  t2.start()
  
#    t1 = multiprocessing.Process(target= test1)
#    t2 = multiprocessing.Process(target= test2)
#    t1.start()
#    t2.start()
# if __name__ == '__main__':

#    main()

""" 子进程 """
# # 写时拷贝

""" 进程和线程的对比 """
# # 进程: 能够完成多任务,多个qq
#   进程是资源分配的单位
#   一个程序至少有一个进程,和一个线程

# # 线程:能够完成多任务,多个窗口
#   线程是调度的单位
#   线程不能独立运行,需要依存于进程
#   线程执行开销小,但不利于管理和维护,而进程正相反


""" 队列  queue"""
# 通过内存完成进程间通信
# 通过queue解耦

import multiprocessing
q = multiprocessing.Queue(3)
q.put('111')
q.put(111)
q.put([11,22])
q.get()
q.get()
q.get()
q.empty()
q.full()


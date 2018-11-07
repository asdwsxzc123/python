#coding=utf-8
# 线程的运行时没有先后顺序,随机的


# 多任务,一起执行
# 并行是真的多任务
# 并发:假的多任务
import time
import threading
# def sing():
#   '--唱歌五秒'
#   for i in range(5):
#     print('----正在唱菊花台----')
#     time.sleep(1)
# def dance():
#   for i in range(5):
#     print('----正在跳舞---')
#     time.sleep(1)
# def main():
#   t1 = threading.Thread(target = sing)
#   t2 = threading.Thread(target = dance)
#   t1.start()
#   t2.start()
# if __name__ == '__main__':
#   main()

def saySorry():
  print('亲爱的')
  time.sleep(1)

if __name__ == '__main__':
  for i in range(5):
    t = threading.Thread(target = saySorry)
    # 会直接打印5次,开了多线程,
    t.start()
    # enumerate是得到元组
    length = len(threading.enumerate())
    print('当前线程数为:%s'% length)

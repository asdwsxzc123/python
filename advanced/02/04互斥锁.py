import threading
import time
g_nums = [11, 22]
g_num = 0
mutex = threading.Lock()
def test1(temp):
    global g_num
    for i in range(temp):
      mutex.acquire()
      g_num += 1
      # 执行完在解锁
      mutex.release()
    print('------test1-----%s' % str(g_num))


def test2(temp):
    global g_num
    for i in range(temp):
      mutex.acquire()
      g_num += 1
      # 执行完在解锁
      mutex.release()
    print('------test2-----%s' % str(g_num))


def main():
    # args指定将来调用函数的时候,传递什么数据过去
    t1 = threading.Thread(target=test1, args=(10000000,))  # 元组
    t2 = threading.Thread(target=test2, args=(10000000,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()


""" 死锁 """
# 上了别人的锁.这是别人上不了,不能解锁
# 设计需要使用(银行家算法)
# 死锁需要添加超时时间等

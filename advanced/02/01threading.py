# coding=utf-8
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

# def saySorry():
#   print('亲爱的')
#   time.sleep(1)

# if __name__ == '__main__':
#   for i in range(5):
#     t = threading.Thread(target = saySorry)
#     # 会直接打印5次,开了多线程,
#     t.start()
#     # enumerate是得到元组
#     length = len(threading.enumerate())
#     print('当前线程数为:%s'% length)


""" 多线程共享全局变量 """
""" 互斥锁解决资源竞争 """
# 共享的问题:多线程同时操作会出问题:存在资源竞争,都在写入
g_nums = [11, 22]
g_num = 0
mutex = threading.Lock()
def test1(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
        g_num += 1
    # 执行完在解锁
    mutex.release()
    print('------test1-----%s' % str(g_num))


def test2(temp):
    global g_num
    mutex.acquire()
    for i in range(temp):
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

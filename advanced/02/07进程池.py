""" 进程池 """
# 创建的子进程不多时,可以直接利用multiprocessing中的Process动态生成多个进程,如果目标太多,手动创建工作量大,此时可以用到multiprocessing的Pool方法
# pool可以定一个最大进程数,如果池满了等进程结束,才会让新的进来

from multiprocessing import Pool
import os,time,random

def worker(msg):
	t_start = time.time()
	print('%s开始执行,进程号为%d'% (msg,os.getpid()))
	time.sleep(random.random()*2)
	t_stop = time.time()
	print(msg,'执行完毕,耗时%0.2f'% (t_stop-t_start))

po = Pool(3) 
for i in range(0,10):
	po.apply_async(worker,(i,))
print('---start---')
po.close()
po.join() # 等待po中所有子进程执行完毕,必须放在close后
print('---end---')


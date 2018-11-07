import time
import threading
# 继承了threading.Thread类
class MyThread(threading.Thread):
  # 必须定义run方法.start会自动调用run方法
  def run (self):
    for i in range(5):
      time.sleep(1)
      self.test()
      msg = "i'm " + self.name + ' @ ' + str(i)
      print(msg)
  def test(self):
    pass

if __name__ == '__main__':
  t = MyThread()
  t.start()
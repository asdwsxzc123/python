# f = open('./hhh.py', 'wb')
# try:
#   f.wr('ss')
# except IOError:
#   print('error')
# finally:
#   f.close()
  
# # 默认调用f.close()
# with open('./output.txt', 'wb') as f:
#   f.write('sss')

# # /context
# # 上下文管理器 __enter__, __exit__(),实现了这两个方法的对象,就是上下文管理器
# class File():
#   def __init__(self,filename, mode):
#     self.filename = filename
#     self.mode = mode
#   def __enter__(self):
#     print('entering')
#     self.f = open(self.filename, self.mode)
#     return self.f

#   def __exit__(self, *args):
#     print('will exit')
#     self.f.close()

from contextlib import contextmanager
@contextmanager
def my_open(path,mode):
  f = open(path,mode)
  yield f
  f.close()



# coding=utf-8

# with open('./1.text' , 'wb') as f:
#   f.write('hello')
# with在__exit__调用了f.close()

class Foo(object):
  def __enter__(self):
    """ 进入with语句被with调用 """
    print('enter called')
  def __exit__(self, exc_type, exc_val, exc_tb):
    # 离开with被with调用
    print('exit called')
    print('exc_type: %s' % exc_type)
    print('exc_val: %s' % exc_val)
    print('exc_tb: %s' % exc_tb)

with Foo() as foo:
  print('hello python')
  a = 1 / 0
  print('----hello end')
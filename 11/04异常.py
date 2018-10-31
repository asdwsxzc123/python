try:
  open('xxx.txt')
  print(num)
  print('----')
# 写法1:
# except NameError :
#   print('如果捕获到异常后的处理')

# except FileNotFoundError:
#   print('文件不存在')

# # 写法2:
# except (NameError,FileNotFoundError):
#   print('异常处理')

# 写法3
except Exception as err:
  print(err)
  print('捕获所有异常')

else:
  print('没有异常才执行')

finally:
  print('finally')

import time
time.sleep(2)
print('222')

""" 异常传递 """
class ShortInputException(Exception):
  pass

try: 
  s = input('请输入')
  # raise 引发一个自己定义的异常
  raise ShortInputException()
except ShortInputException as result:
  print('11')
else :
  pass
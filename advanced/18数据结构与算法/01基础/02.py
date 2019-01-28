# timeit 测试代码
# timeit.Timer(stmt='pass',setup='pass',timer=<function>)
# timer
import time
start_time = time.time()
""" 175s
1.枚举法
for a in range(0,1001):
  for b in range(0,1001):
    for c in range(0,1001):
      if a + b + c == 1000 and a**2 + b**2 == c**2:
        print('a, b, c: %d, %d, %d' %(a,b,c))
# T = 1000 * 1000 * 1000 * 2
# T(n) = n^3 * 2
"""
""" 1s
for a in range(0,1001):
  for b in range(0,1001):
    c = 1000 - a - b
    if a**2 + b**2 == c**2:
      print('a, b, c: %d, %d, %d' %(a,b,c))
T(n) = n * n * (1 + max(0,1))
     = n^2 * 2
    #  忽略常数项和次要忽略
     = O(n*2)
 """

#  a + b + c == 1000  and a**2 + b**2 == c**2:

 
end_time = time.time()
print('times: %d' %(end_time - start_time)) 
# print('finished')


# lambda 参数:式子

# func = lambda x,y: x+y

# result2 = func(1,2)
# print('result2=%s'%result2)

stus = [
  {'name':'zhangs', "age":24},
  {'name':'zhangs1', "age":14},
  {'name':'zhangs2', "age":34},
]
stus.sort(key = lambda x:x['age'])
print(stus)
a = [100]
def test(num):
  num = num + num
  print(num)
test(a)
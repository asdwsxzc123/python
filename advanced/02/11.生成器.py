""" 生成器 """
# 生成器是一个特殊的迭代器,可以使用forin遍历,也可以使用next()方法,迭代器需要iter方法和next方法,yield可以让一个函数暂停执行,并保存之前的值

# nums = [x*2 for x in range(10)]
# print(nums)

# nums1 = (x*2 for x in range(10))
# for num in nums1:
#   print(num)

# 如果一个函数里面有yield,就是生成器模板,不再是函数
# def create_num(all_num):
#   a, b = 0, 1
#   current_num = 0
#   while current_num < all_num:
#     yield a
#     a, b = b, a + b
#     current_num += 1
#   # 想要得到return需要在异常中获得ret.value
#   return 'ok..'
# # 如果在调用create_num的时候,发现这个函数中有yield,那么此时不是调用函数,而是创建一个生成器对象
# obj = create_num(10)
# ret = next(obj)
# print(ret)
# while True:
#   try:
#     ret = next(obj)
#     print(ret)
#   except Exception as ret:
#     print(ret.value)
#     break

""" 生成器的send """
# send和next都可以启动,d第一次启动最好用next,如果要用send需要传None
def create_num(all_num):
  a, b = 0, 1
  current_num = 0
  while current_num < all_num:
    ret = yield a
    print('----ret---', ret)
    a, b = b, a + b
    current_num += 1
obj = create_num(10)
ret = next(obj)
print(ret)
# send是yield的返回值
ret = obj.send('haha')
print(ret)

ret = next(obj)
print(ret)
ret = obj.send('haha')
print(ret)
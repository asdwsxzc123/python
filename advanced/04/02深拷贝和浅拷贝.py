# 浅拷贝只是复制引用
# 深拷贝复制内容

import copy
# a = [11,22]
# # 浅拷贝,只拷贝了最上面的那层
# c = copy.copy(a)
# # 深拷贝,拷贝了所有的内容
# c = copy.deepcopy(a)
# a.append(33)
# print(c)

# copy.copy元组不拷贝,因为元组是不可变类型

""" 其他方式 """
# 列表的切片也是浅拷贝
d = a[:]

# 字典,有copy方法
# 浅拷贝
d = dist(name = 'zhangsan', age=12)
co = d.copy()
import numpy as np

""" 更多方法 """
# print(t1 < 10)
# t1[t1<10] = 3
# print(t1)
t1 = np.arange(24).reshape((4,6))
# print(t1)
# where(if,a,else b)
# t2 = np.where(t1<10,0,10) # 三元运算符
# print(t2)

# clip 裁切
# 小于10的替换成10,大于18的替换成18
# t3 = t1.clip(10,18)
# print(t3)

# nan 将数字转化成NAN, nan是浮点型,需要将int转换成flout

""" 数组的拼接 """
# np.vstack((t1,t2)) # 竖直拼接, 相当于添加行
# np.hstack((t1,t2)) # 水平拼接, 相当于添加列

# 行列交换
# 逗号表示选取
# t1[[1,2],:] = t1[[2,1],:] 
t1[:,[0,2]] = t1[:,[2,0]]
# print(t1)

""" 其他方法 """ 
# 全为1的两行三列
np.ones((2,3))
# 全为0的
np.zeros((2,3))
# 获取最大值，行
# print(np.argmax(t1,axis=0))
# 最小值， 列
# print(np.argmin(t1,axis=1))
# 正方形,3行3列
np.eye(3)

""" 生成随机数 """
# np.random.rand(d0,d1,..dn)  创建d0-dn维度的均匀分布的随机数,浮点型, 在相同的大小范围内出现的概率是等可能的
# np.random.randn(d0,d1,..dn)  创建d0-dn维度的标准正太分布的随机数,浮点型,钟型,两头低,中间高,左右对称
# np.random.randint(low,high,(shape)) 形状是shape,整数,范围是low,high
# np.random.uniform(low,high,(size)) 均匀分布的数组, size形状,小数
# np.random.normal(loc,scale,(size)) 正太分布中随机抽取样本,分中心是loc(概率分布的均值), 标准差是scale,形状是size
# np.random.seed(s) 随机种子,s是给的种子值,每次生成相同的随机数,设置用的,配合random.randint等,形状都是一样的
np.random.seed(10)
t = np.random.randint(0,20,(3,4))
print(t)

"""  copy和view """
# 深拷贝,ab不相互影响
a = b.copy() 

""" nan和inf """
# 当有缺失的时候,有出现nan
# np.nan表示不是一个数组
# infinity 无穷大和无穷小 inf, -inf
# np.inf

# np.nan==np.nam False
# np.nan!=np.nam True

# 统计不为0的个数
# np.count_nonzero(t2)
# 可以判断nan的个数
# np.count_nonzero(t2!=t2)
# 判断是否为nan
# np.isnan(t) = 0
# np.count_nonzero(np.isnan(t))
# 求和
np.sum()
# 如果有nan
# np.sun() => nan

# 求行的和
np.sum(t1,axis=0)
# 求列的和
np.sum(t1,axis=1)

# nan的赋值
# t1[np.isnan(t1)] = 0
# 一般会吧缺失值替换成均值或中值

""" 常用统计方法 """
求和: t1.sum(axis=None)
均值: t1.mean(a,axis=None)
中值: np.median(t1,axis=None)
最大值: t1.max(axis=None)
最小值: t1.min(axis=None)
极值: np.ptp(t,axis=None) (最大值和最小值的差)
标准差: t1.std(axis=None)

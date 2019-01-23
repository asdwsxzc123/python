""" 介绍 """
# 科学计算的多维数组库

""" 用法 """
import numpy as np
import random

t1 = np.arange(12)
# print(t1.dtype)

# numpy中的数据类型
t5 = np.array(range(12), dtype=float)
t6 = np.array([0,1,0,1],dtype=bool)
t7 = np.array([random.random() for i in range(12)])
t8 = np.round(t7,2)

""" 数组的计算 """
t2 = np.array([[1,2,3],[5,6,7]])
# print(t1)
# print(t1.shape)
# # 12个数.一维数组
# 1行,12列
# print(t2.shape)
# # 2行,3列,二维数组
# (2, 3)

t4 = np.arange(12)
# 将一维数组变成二维,3行,4列,有返回值
t4.reshape((3,4))

# 将多维数组变成一维
t4.flatten()

# 直接将整个数组加2
t4+2
t4*2
t4/2

# 对应位置相加,需要两个数组一至
t4+t2
t4*t2
t4/t2

# 转置 行与列交换
t2.transpose()
t2.T()
t2.swapaxes(0,1)


# 广播原则
如果两个数组的后援维度(从末尾开始算计的维度)的轴长度相符或其中一方的长度为1,则认为它们是广播兼容,广播会在缺失和(或)长度为1的维度上进行
只要是行上的形状一样就可以计算

""" 读取文本数据 """
np.loadtxt(frame.dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
frame: 文件.字符串或产生器,可以是.gz或bz2压缩文件
dtype 数据类型,默认np.float
delimiter: 分割字符串,默认空格
skiprows: 跳过前x行,一般跳过第一行表头
usecols: 读取指定的的列,索引,元组类型
unpack:True读入属性分别写入不同数组变量,False读入数据写入一个数组变量,默认False,行变成了列
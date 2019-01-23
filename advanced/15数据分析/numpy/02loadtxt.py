import numpy as np
us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'
# t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=True)
us_data = np.loadtxt(us_file_path,delimiter=',',dtype='int')
uk_data = np.loadtxt(uk_file_path,delimiter=',',dtype='int')
# print(t1)

""" 索引和切片 """
# 取行,从0开始,除了xpath
# print(t1[2])

# 取多行
# print(t1[2:])

# 取不连续多行
# print(t1[[2,8,10]])

# 取列,逗号前面是行,后面是列
# print(t1[1,:])
# print(t1[2,:])
# print(t1[[2,10],:])

# print(t1[:,0])

# 去连续多列
# print(t1[:,2:])

# 取不连续多列
# print(t1[:,[1,2]])

# 取行列,2行3列
# print(t1[2,3])

# 去多行多列,3-5行,2-4列
# 交叉位置
# print(t1[2:5,1:4])

# 去多个不相邻的点
# 选出来的结果(0,0), (2,1), (2,3)
# print(t1[[0,2,2],[0,1,3]])


""" 合并信息 """
# 保留国家信息,需要添加一列,然后竖直拼接
zoros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((uk_data.shape[0],1)).astype(int)

us_data = np.hstack((us_data, zoros_data))
uk_data = np.hstack((uk_data, ones_data))
# 拼接
final_data = np.vstack((us_data,uk_data))
print(final_data)
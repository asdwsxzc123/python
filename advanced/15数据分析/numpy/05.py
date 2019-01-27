import numpy as np
from matplotlib import pyplot as plt
us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'
# t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=True)
""" us_data = np.loadtxt(us_file_path,delimiter=',',dtype='int')
# 去评论的数据
us_comments = us_data[:, -1]
# 选择比5000小的数据
us_comments = us_comments[us_comments<=5000]
d = 50
bin_nums = (us_comments.max()-us_comments.min()) // d
# 绘图
plt.figure(figsize=(20,8), dpi=80)
plt.hist(us_comments,bin_nums)
plt.grid()
plt.show() """

uk_data = np.loadtxt(uk_file_path,delimiter=',',dtype='int')
uk_data = uk_data[uk_data[:,1]<500000]
uk_commonet = uk_data[:,-1]
uk_like = uk_data[:,1]
plt.figure(figsize=(20,8),dpi=80)
plt.scatter(uk_like,uk_commonet)
plt.show()

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
""" 导游和演员 """
df = pd.read_csv('./IMDB-Movie-Data.csv')
# 导游
# print(len(set(df['Director'].tolist())))
# directors_num = len(df['Director'].unique())
# print()

# # 获取演员的人数
# temp_actors_list = df['Actors'].str.split(', ').tolist()
# print(df['Actors'])
# actors_list = [i for j in temp_actors_list for i in j]
# actors_num = len(actors_list)
# # print(actors_num)

""" 统计电影类型 """
# 统计电影分类情况,做列名分类,初始为0,每次出现+1
# print(df['Genre'])
# 统计分类列表
temp_list = df['Genre'].str.split(',').tolist() # [[],[],[]]
genre_list = list(set([i for j in temp_list for i in j]))
# print(genre_list)
# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zero_df)

# 给每个电影出现分类的位置赋值为1
for i in range(df.shape[0]):
  zero_df.loc[i,temp_list[i]] = 1
  
# print(zero_df.head(3))

# 统计总数
genre_count = zero_df.sum(axis=0)
# print(genre_count)
_x = genre_count.index
_y = genre_count.values
# 画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.grid()
plt.show()
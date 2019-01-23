import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv('./csv911.csv')
# print(df.head(1))
# print(df.info())

# 获取分类
temp_list = df['title'].str.split(': ').tolist()
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))), columns=cate_list)
# print(zeros_df)

# 赋值
# for cate in cate_list:
#   zeros_df[df['title'].str.contains(cate)] = 1
# print(cate_list)

# for i in range(df.shape[0]):
#   zeros_df.loc[i, temp_list[i][0]] = 1
# print(zeros_df)
""" 评分和时长 """
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('./IMDB-Movie-Data.csv')
# print(df.head(1))
# print(df.info())
# df = df[['Title','Rank','Runtime (Minutes)']]
# 直方图
""" runtime """
# runtime_data = df['Runtime (Minutes)'].values
# max_runtime = runtime_data.max()
# min_runtime = runtime_data.min()
# num_bin = (max_runtime - min_runtime) // 5

# plt.figure(figsize=(20,8),dpi=80)
# plt.hist(runtime_data,num_bin)
# plt.xticks(range(min_runtime, max_runtime + 5,5))
# plt.grid()
# plt.show()

""" rate """
runtime_data = df['Rating'].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
num_bin = (max_runtime - min_runtime) // 0.5

plt.figure(figsize=(20,8),dpi=80)
num_bin_list = [1.6]
i=1.6
while i<max_runtime:
  i += 0.5 
  num_bin_list.append(i)
plt.hist(runtime_data,num_bin_list)
# _x = [min_runtime]
# i = min_runtime
# while i<=max_runtime + 0.5:
#   i = i + 0.5
#   _x.append(i)
# plt.xticks(_x)
plt.grid()
plt.show()
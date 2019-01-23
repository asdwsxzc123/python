import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# pd.date_range(start=None,end=None,periods=None,freq='D')
# start='20171230'
# end='20180131'
# freq = 
#     10D 十天
#     M 月
#     D 天
#     H 时
# pd.to_datetime(df['timeStamp'], format='')

# resample 频率的转换(降采样,升采样)

# periodIndex 时间段
pd.PeriodIndex(year=data['year'],month=data['month'],freq='H')


df = pd.read_csv('./csv911.csv')

# print(df.head())

# 统计911数据中不同月份电话次数
""" 
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df.set_index('timeStamp', inplace=True)
count_by_month = df.resample('M').count()['title']
# print(count_by_month)
_x = count_by_month.index
# for i in _x:
#   print(dir(i))
#   break
_x = [i.strftime('%Y-%m-%d') for i in _x]
_y = count_by_month.values
plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.show()
 """
# 不同月份不同类型的电话情况
_x = None
def plot_img(df,label):
  global _x
  count_by_month = df.resample('M').count()['title']
  _x = count_by_month.index
  _x = [i.strftime('%Y-%m-%d') for i in _x]
  _y = count_by_month.values
  plt.plot(range(len(_x)), _y,label=label)


df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# 添加列,表示分类
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
# print(cate_list)
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
print(df['cate'])
df.set_index('timeStamp', inplace=True)

plt.figure(figsize=(20,8), dpi=80)
# 分组
for group_name,group_data in df.groupby(by='cate'):
  plot_img(group_data, group_name)


plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc='best')
plt.show()

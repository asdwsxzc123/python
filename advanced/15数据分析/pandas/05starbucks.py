
import pandas as pd
import numpy as np
df = pd.read_csv('./starbucks_store_worldwide.csv')
# print(df.head(1))
# print(df.info())

""" 获取星巴克中国和美国的品牌数量 """
# 分组DataFrameGroupBy
""" grouped = df.groupby(by='Country')
# print(grouped)
# 可以进行遍历,调用聚合方法
# for i in grouped:
  # print('*' * 100)
  # print(i)
# df[df['Country']='US']
country_count = grouped['Brand'].count()
print(country_count['US'])
print(country_count['CN']) """

""" 统计中国每个省份的国家数量 """
# china_data = df[df['Country']=='CN']
# grouped = china_data.groupby(by='State/Province').count()['Brand']
# print(grouped)

# 数据按照多个条件分组 返回series,复合索引
grouped1 = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
# 返回dataFrame
# grouped =  df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
# print(type(grouped1))

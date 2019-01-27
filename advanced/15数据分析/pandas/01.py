
import pandas as pd
from pymongo import MongoClient
""" 常见数据类型 """
# series 一维数据,带标签数组
# dataFrame 二维数据,series容器
# list可以修改索引
# t = pd.Series([1,2,31,12,3,4],index=list('abcdef'))
# t = {
#   'name': '小红',
#   'age': 125
# }
# t = pd.Series(t)

# print(t['age'])
# print(t[1])
# print(t[['name', 'age']])
# print(t)

""" series的属性 """
# t.index,t.values
# t.where(a > 0)

""" 读取外部数据 """
# csv
# df = pd.read_csv('../youtube_video_data/US_video_data_numbers.csv')

# sql
# df = pd.read_sql()
# print(df)

# DataFrame对象即有行索引也有列索引
# mongodb
client = MongoClient(host='172.16.20.46',port=27017)
collection = client['test1']['test1000']
data = list(collection.find())
# t1 = pd.Series(data[0])
data_list = []
# for t in data:
#   print(t)
#   temp = {}
#   temp['name'] = t['name']
#   data_list.append(temp)
t1 = pd.DataFrame(data)
# print(t1)
# index列索引,columns行索引

# 前两行
# print(t1.head(1))
# 显示后两行
# print(t1.tail(3))
# print(t1.info())
# print(t1.describe())

""" 缺失数据处理 """
# 是否为nan
# pd.isnull(df)
# pd.notnull(df)
# 删除
# axis,删除行,how:all是全部是nan才删,any有一个nan,才删,inplace:是否进行原地修改
pd.dropna(axis=0,how='any',inplace=False)
# 填充数据
t.fillna(t.mean(),t.fiallna(t.median()),t.fillna(0))

# np.nan

# t1.join(t2)
# 确实全部按NaN处理

# 默认情况,内联
# inner,并集, outer,交集, left左边为准,right右边为准NaN补全
# t1.merge(t3,on='a',how='inner')
# t1.merge(t3,left_on='a', right_on="x")

""" 分组和聚合 """
grouped = df.groupby(by='Country')

""" 索引 """
# 获取索引 
print(df.index)
# 对索引赋值
df.index = ['a', 'b']
# 重写设置index
df.reindex(['a', 'b'])
# 吧某一列作为索引 drop是否删除在列删的索引
df.set_index('a', drop=False)
df.set_index(['a','b'], drop=False)
# 返回index的唯一值
df.set_index('Country').index.unique()

# 交换内层和外层索引
# df.swaplevel()
# df.loc['one].loc['h]
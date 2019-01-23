import pandas as pd
df = pd.read_csv('./dogNames2.csv')
# print(df.head())
# print(df.info())
# 排序,
df = df.sort_values(by='Count_AnimalName',ascending=False)
df[:100]
# 如果写数组,表示取值,对行进行操作
# 如果写字符串,表示的去列索引,对列进行操作
# print(df[:100]['Row_Labels'])

# 通过标签索引行数据
# df.loc
# print(df.loc[:,'Row_Labels'])
# 去a行c列
# df.loc[['a','c']]
# 通过位置获取行数据
# df.iloc 
# 1到3行,
# df.iloc(1:3,[2,3])
# df.iloc(1:3,2:3)
# 大于800的
# print(df[df['Count_AnimalName']>800]['Row_Labels'])

# 名字的字符串长度大于4
print(df[(df['Row_Labels'].str.len()>4) & (df['Count_AnimalName']>800)]['Row_Labels'])

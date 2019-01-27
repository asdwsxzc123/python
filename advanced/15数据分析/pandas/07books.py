import pandas as pd
from matplotlib import pyplot as plt
# 钱10000的排名,
# 1.不同的年份数量
df = pd.read_csv('./books.csv')
# print(df.head(1))
print(df.info())
# data1 = df[pd.notnull(df['original_publication_year'])]
# grouped = data1.groupby(by='original_publication_year').count()['title']
# print(grouped)

# 2. 不同年份书的平均评分
data2 = df[pd.notnull(df['original_publication_year'])]
grouped = data2['average_rating'].groupby(by=data2['original_publication_year']).mean()
# grouped = data2['average_rating'].groupby(by=data2['original_publication_year']).count()
print(grouped)
_x = grouped.index
_y = grouped.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=90)
plt.show()


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

df = pd.read_csv('./starbucks_store_worldwide.csv')
""" 使用matplotlib呈现店铺总数排名的前10名国家 """
# 准备数据
# data1 = df.groupby(by='Country')['Brand'].count().sort_values(ascending=False)[:10]

# _x = data1.index
# _y = data1.values

# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x)
# plt.show()

""" 中国每个城市的店铺数 """
data2 = df[df['Country'] == 'CN'].groupby(by='City')['Brand'].count().sort_values(ascending=False)[:40]
_x = data2.index
_y = data2.values
plt.figure(figsize=(20,8), dpi=80)
# plt.bar(range(len(_x)), _y, width=0.3,color='orange')
# plt.xticks(range(len(_x)),_x,rotation=90,fontproperties=my_font)
plt.barh(range(len(_x)), _y, height=0.3,color='orange')
plt.yticks(range(len(_x)),_x,fontproperties=my_font)
plt.show()
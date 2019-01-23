# 查看系统里面的中文字体(linux)
# fc-list :lange=zh

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# font = {
#     'family': 'MicroSoft YaHei',
#     'weight': 'bold',
#     'size': 'larger'
# }
# matplotlib.rc('font', **font)
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
# x = range(0, 120)
# y = [random.randint(20, 35) for i in range(120)]
# plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(x, y)
# # 调整x轴刻度
# _xticks_labels = ['10点{}分'.format(i) for i in range(60)]
# _xticks_labels += ['11点{}分'.format(i-60) for i in range(60, 120)]
# plt.xticks(list(x)[::3], _xticks_labels[::3],
#            rotation=300, fontproperties=my_font)

# # 描述信息
# plt.xlabel('时间', fontproperties=my_font)
# plt.ylabel('温度 单位()', fontproperties=my_font)
# plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)
# plt.show()

""" 交朋友 """
x = range(11,30)
y1 = [1,0,1,1,2,4,3,2,3,4,2,5,6,5,4,3,3,1,1]
y2 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1]
plt.figure(figsize=(20,8), dpi=80)
plt.plot(x,y1, label='自己', color='orange', linestyle=':')
plt.plot(x,y2, label='同桌', color='cyan', linestyle='-.')
_xticks_labels = ['{}岁'.format(i) for i in x]
plt.xticks(list(x),_xticks_labels, fontproperties=my_font)
plt.xlabel('年龄', fontproperties=my_font)
plt.ylabel('个数', fontproperties=my_font)
plt.title('交朋友走势', fontproperties=my_font)

# 绘制网格线
plt.grid(alpha = 0.1)

# 添加图例
plt.legend()

plt.show()
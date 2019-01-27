from matplotlib import pyplot as plt

# 设置图片大小
fig = plt.figure(figsize=(29,8),dpi=80)
x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,24,22,18,15]
# 绘图
plt.plot(x,y)
# x周坐标
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(range(25,50))
plt.yticks(range(min(y), max(y) + 1))
# 保存图片
plt.savefig('./sig_size.png')
plt.show()

# 折线图,显示呼叫的变化趋势,反映事物的变化 scatter
# 直方图: 绘制连续性的数据,展示一组或多组数据的分布状况 hist 用户的年龄分布,一段时间用户点击,用户活跃时间的分布
# 条形图: 绘制离散的数据,能够一眼看出各个数据的大学,比较数据之间的差距 bar 
# 散点图: 用两组数据构成多个坐标点,考察坐标的分布,判断两变量之间是否存在某种关联或总结坐标点的分布模式 plot

""" 常用方法 """
matplotlib.plot(x,y)
matplotlib.bar(x,y)
matplotlib.scatter(x,y)
matplotlib.hist(data,bins,normed)
xticks,yticks
savefig

""" 使用流程 """
1. 明确问题
2. 选择图形的呈现方式
3. 准备数据
4. 绘制和图形完善

# 其他绘制工具
1. echart
2. plotly
3. seaborn
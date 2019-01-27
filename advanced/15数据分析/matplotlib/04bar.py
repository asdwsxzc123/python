from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')


# a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5\n：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

# b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
# # 58921.com
# plt.figure(figsize=(20,8), dpi=80)
# # 横轴
# # plt.barh(range(len(a)),b, height=0.3)
# # plt.xticks(range(len(a)),a, fontproperties=my_font,rotation=90)

# # 纵轴
# plt.barh(range(len(a)),b, height=0.3)
# plt.yticks(range(len(a)),a, fontproperties=my_font)
# plt.grid(alpha=0.3)
# plt.show()



# a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
# # 三天的变化
# b_16 = [15746,312,4497,319]
# b_15 = [12357,156,2045,168]
# b_14 = [2358,399,2358,362]

# bar_width = 0.2
# x_14 = list(range(len(a)))
# x_15 = [i+bar_width for i in x_14]
# x_16 = [i+bar_width * 2 for i in x_14]

# plt.figure(figsize=(20,8),dpi=80)

# plt.bar(range(len(a)), b_14,width=bar_width,label='9月14日')
# plt.bar(x_15, b_15,width=bar_width,label='9月15日')
# plt.bar(x_16, b_16,width=bar_width,label='9月16日')

# # 设置x轴刻度
# plt.xticks(x_15,a,fontproperties=my_font)
# plt.legend(prop=my_font)
# plt.show()

# 区分
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
# 组距
width = [5,5,5,5,5,5,5,5,5,15,30,60]
# 值
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(interval)),quantity,width=1)
_x = [i-0.5 for i in range(len(quantity) + 1)]
_xtick_labels = interval + [150]
plt.xticks(_x,_xtick_labels)
# plt.grid()
plt.show()
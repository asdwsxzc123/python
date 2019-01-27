import numpy as np
import sklearn as sklearn
sklear:
优点: 封装好,简历简单模型,预测简单
缺点: 算法的过程,有些参数都在算法API内部优惠
tensorflow: 封装高低,可以看到内部实现

线性回归: 寻找一种能预测的趋势
线性关系: 二位:直线
y = kx + b
b是偏置
加b: 为了是对单个特征的情况更加统一
一元线性回归: 一个变量
多远线性回归: 两个或两个以上的变量

h(w) = w0 + w1x1 + w2x2 + w3x3 + w4x4 = wtx
w,x为矩阵 
矩阵:大多数算法的计算基础,必须是二维的,矩阵的乘法和加法
矩阵乘法: (m行,i列) * (i行,n列) = (m行,n列)
# np.multiply(a,b)
# np.dot(a,b)

回归算法:
算法, 策略(损失函数), 优化
迭代的算法
神经网络
知道有误差,会去不断的减少误差
1.损失函数(误差大小)
误差平方和,最小二乘法,寻找最优化的W值
最小二乘之正规方程: 一次求出最小值
最小二乘之梯度下降: 慢慢得到最小值;

#  普通最小二乘线性回归
sklearn.linear_model.LinearRegression()
# SGD最小
sklearn.linear_model.SGDRegressor()

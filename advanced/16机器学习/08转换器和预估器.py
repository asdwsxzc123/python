""" 转化器 """
1.实例化,是一个转换器
# 数据集转化
fit_transform() 输入数据,直接转换,平均值
fit() 输入数据,但不做事
+transform() 进行数据的转换, 标准差

""" 预估器 estimator """
# 用于分类
sklearn.neighbor k-近邻算法
sklearn.naive_bayse 贝叶斯
sklearn.linear_model.LogisticRegression 逻辑回归
sklearn.tree 决策树与随机森林

# 用于回归
sklearn.linear_model.LinearRegression 线性回归
sklearn.linear_model.Ridge 岭回归

# 每个算法的API中的参数需要搞懂,
# 训练集和测试
1.调用fit(x_train,y_train)
2.输入测试集数据
    # 获取预测数据
    1. y_predict = predict(x_test)
    # 查看预测准确率
    2. score(x_test,y_test)


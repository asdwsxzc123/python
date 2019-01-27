from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
def myLinear():
    """ 线性回归直接预测房子价格 """
    # 获取数据
    lb = load_boston()
    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(lb.data,lb.target,test_size=0.25)

    # 进行标准化处理, 目标值需要进行标准化处理吗
    # 实例化两个标准化API
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.fit_transform(x_test)
    # 目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train)
    y_test = std_y.fit_transform(y_test)
    # estimator预测
    # 正规方程求解1
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    # 权重参数
    print(lr.coef_)
    # 预测价格
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))
    print('测试集里面每个房子的预测价格: ', y_lr_predict)
    print('正规方程的均方误差:', mean_squared_error(std_y.inverse_transform(y_test), y_lr_predict))
    # 梯度下降进行房子价格预测
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    print(sgd.coef_)
    # 预测测试集的价格
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    print('测试集里面每个房子的预测价格: ', y_sgd_predict)
    print('梯度下降的均方误差:', mean_squared_error(
        std_y.inverse_transform(y_test), y_sgd_predict))

    return None
if __name__ == "__main__":
    myLinear()

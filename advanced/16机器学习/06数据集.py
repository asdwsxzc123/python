# 评估
# 75%训练集
# 25%测试集
# 训练数据: 用于训练,构建模型
# model_selection.train_test_split

# sklearn.datasets
datasets.load_*()
获取小规模数据集,数据包含在datasets里
datasets.fetch_*(data_home=None)
获取大规模数据集,需要从网络上下载,函数的第一个参数是data_home,表示数据集的下载目录

数据类型datasets.base.Bunch()
data:特征数据数组,[n_samples*n_features]的二位numpy.ndarray数组
target: 标签数组,是n_samples的一维numpy.ndarray数组
DESCR: 数据描述
feature_names: 特征名,新闻数据,手写数据
target_names: 标签名称

# 分类数据集
sklearn.datasets.load_iris()
加载并返回数据集
类别:3
特征:4
样本:150
每个类别的数量: 50

sklearn.datasets.load_digits()
# 加载并返回数字数据集
类别: 10
特征 64
样本数量: 1797

# 分割数据集
sklearn.model_selection.train_test_split()

# 大数据集
sklearn.datasets.fetch_20newsgroups(data_home=None,subset='train')


""" 回归数据集 """
sklearn.datasets.load_boston
加载并返回波士顿房价数据集
目标类别 5-50
特征 13
样本数量 506

sklearn.datasets.load_diabetes()
加载并返回糖尿病数据集
目标范围 25-346
特征: 10
样本数量 442
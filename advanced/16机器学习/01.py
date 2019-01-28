# 目的:
# 让机器学习程序替换手动的步骤,减少企业的成本也提高企业的效率

# 机器学习的数据: 文件csv
# mysql:1. 性能瓶颈 2.格式不太符合机器学习要求数据的格式
# 特征工程
pandas: 读取工具 
sklearn: 特征处理

numpy: 释放了gil锁
scikit-learn 数据量量小,学习方便
uci: 收录了360个数据集,覆盖科学,生活,经济
kaggle: 大数据竞赛平台,80万科学家,数据真实

1. 数据处理
2. 特征工程,数据预处理,模型评估,机器学习
3. 离线或在线数据库

""" 特征工程 """
# 定义: 将原始数据转换为更好地代表预测模型的潜在问题的特征的过程,
# 直接影响预测结果

1.scikit-learn

# 特征抽取
# 特征抽取对文本等数据进行特征值化

# 文本特征处理
sklearn.feature_extraction.text.CountVectorizer
统计出现的次数
文本分类
情爱分析
不支持中文,需要通过空格分割 


# 字典特征抽取
sklearn.feature_extraction.dictVectorizer
dictVectorizer(sparse=True)
字典数据抽取:吧字典中一些类别的数据,分别进行转换成特征
数组类型,有类别的这些特征先要转换字典数据
二位数组的数据: One-hot编码


# 朴素贝叶斯
# tf idf
tf: tearm frequency 词的评率 出现的次数
idf: inverse document frequency 逆文档评率 log(总文档数/该次出现的文档数) 
log: 输入的数值越小,结果越小

# 归一化
# MinMaxScaler
# 多个特征同等重要,需要进行归一化
# 容易受异常值影响,鲁棒性交叉

# 标准化
# x = (x-mean)/a
# mean: 平均值, a标准差
# 方差 var = ((x1-mean)^2 +(x2-mean)^2+..)/n(样本数)
# a = ^var
# sklearn.preprocessing.ImputerstandardScaler

# 作用域每一列
# x' = (x-min)/(max-min)
# x'' = x' * (mx-mi) +mi
# mx = 1, mi= 0

# 缺失值处理
1.删除
2.插补
# sklearn.preprocessing.Imputer


# 数值型:标准缩放
# 1. 归一化
# 2. 标准化
# 3. 缺失值
# 类别型数据: one-hot编码
# 时间类型: 时间的切分

# kaggle.com
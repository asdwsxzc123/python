# https://www.kaggle.com/c/facebook-v-predicting-check-ins
# 分类
# 特征值: x,y坐标,定位准确性,时间
# 目标值: 入住位置的id

# 处理:
#     0<x<10  0<y<10
#     1. 数据量大,节约时间x,y缩小
#     2. 时间戳进行(年,月,日,周,时分秒), 当做新的特征
#     3. 几千-几万,少于指定签到人数的位置删除

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
def knncls():
    """ k-近邻算法,后面改成使用交叉网格搜索 """ 
    # 读取数据
    data = pd.read_csv('./data/FBlocation/train.csv')
    # print(data.head(10))

    # 处理数据
    # 1.缩小数据
    data.query('x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75')
    # 2.处理时间的数据
    time_value = pd.to_datetime(data['time'],unit='s')
    # 吧时间转化成字典格式
    time_value = pd.DatetimeIndex(time_value)
    # 构建一些特征,
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday
    # 吧时间戳特征删除
    data = data.drop(['time'],axis=1)
    # 吧签到人数少于n个的目标位置删除
    place_count = data.groupby('place_id').count()
    # reset_index 将索引又转化成列
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]
    # 取出数据当中的特征值和目标值
    y = data['place_id']
    x = data. drop(['place_id'],axis = 1)

    # 进行数据的分割训练集合测试集
    x_train, x_test,y_train,y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程(标准化)
    std = StandardScaler()
    # 对测试集和训练集的特征值进行表标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程,超参数
    # knn = KNeighborsClassifier(n_neighbors=5)
    knn = KNeighborsClassifier()
    # fit, predict,score
    """
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    # 得出预测结果
    y_predict = knn.predict(x_test)
    print('预测的目标签到位置: ', y_predict)
    # 得出准确率
    print('预测的准确率: ', knn.score(x_test,y_test)) """
    # 构建一些参数的值进行搜索
    param = {'n_neighbors':[3,5,10]}
    # 进行网格搜索
    gc = GridSearchCV(knn,param_grid=param,cv=2)
    gc.fit(x_train,y_train)
    # 预测准确率
    print('准确率: ', gc.score(x_test,y_test))
    print('在交叉验证中最好的结果: ', gc.best_score_)
    print('选择的最好模型是: ', gc.best_estimator_)
    print('每个超参数每次交叉验证的结果: ', gc.cv_results_)
def naviebayes():
    """ 朴素贝叶斯 """
    news = fetch_20newsgroups(subset='all')
    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)
    
    # 对数据集进行特征抽取
    tf= TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文字重要性统计[a,b,c,d]
    x_train = tf.fit_transform(x_train)
    # print(tf.get_feature_names())
    x_test = tf.transform(x_test)
    
    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    mlt.fit(x_train,y_train)
    y_predict = mlt.predict(x_test)
    print('预测的文章类别为: ', y_predict)
    print('准确率为: ', mlt.score(x_test,y_test))
    print('在每个类别的精准和召回率: ', classifcation_report(y_test, y_predict,target_name=news.target_names))
def decision():
    """ 决策树对泰坦尼克号进行预测生死 """
    # 获取数据
    titan = pd.read_csv('./titan.text')
    # print(titan.head(1))
    # print(titan.info())
    # 处理数据,找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan['survived']
    x['age'].fillna(x['age'].mean(), inplace=True)
    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # 进行处理(特征工程) 特征=>类别=> on_host编码
    myDict = DictVectorizer(sparse=False)
    x_train = myDict.fit_transform(x_train.to_dict(orient='records'))
    # print(myDict.get_feature_names())
    x_test = myDict.transform(x_test.to_dict(orient='records'))
    
    """ # 用决策树进行预测
    dec = DecisionTreeClassifier(max_depth=5)
    dec.fit(x_train, y_train)
    
    # 预测准确率
    print('预测的准确率为: ', dec.score(x_test, y_test))
    # 导出决策树的结构
    export_graphviz(dec, out_file='./tree.dot', feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性']) """

    # 随机森林进行预测 (超参数调优) 
    rf = RandomForestClassifier()
    # 网格搜索与交叉验证
    param = {
        'n_estimators': [120, 200, 300, 500, 800, 1200],
        'max_depth': [5, 8, 15, 25, 30]
    }
    gc = GridSearchCV(rf, param_grid=param,cv=2)
    gc.fit(x_train,y_train)
    print('准确率为: ', gc.score(x_test,y_test))
    print('查看选择的参数模型: ', gc.best_params_)
if __name__ == "__main__":
    # knncls()
    # naviebayes()
    decision()

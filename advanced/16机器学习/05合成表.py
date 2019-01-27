# kaggle.com
import pandas as pd
from sklearn.decomposition import PCA
prior = pd.read_csv('./data/instacart/order_products_prior.csv')
products = pd.read_csv('./data/instacart/pruducts.csv')
orders = pd.read_csv('./data/instacart/orders.csv')
aisles = pd.read_csv('./data/instacart/aisles.csv')

# 合并四张表到一张表中(用户-物品类别)
_mg = pd.merge(prior,products,on=['product_id','product_id'])
_mg = pd.merge(_mg, orders, on=['order_id', 'order_id'])
mt = pd.merge(_mg, aisles, on=['aisls_id', 'aisls_id'])

mt.head(10)

# 交叉表,用户买的物品
cross = pd.crosstab(mt['user_id'],mt['aisle'])
# 主成分分析
pca = PCA(n_components=0.9)
data = pca.fit_transform(cross)
# data.shape
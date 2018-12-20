from pymongo import MongoClient
client = MongoClient(host='172.16.20.46',port=27017)
collection = client['test1']['test1000'] # 分别是数据库和集合

# 插入数据
# collection.insert({'name':'xioawang',' ':14})

# 插入多条数据
# data_list = [{'name':'test{}'.format(i)} for i in range(10)] 
# ret = collection.insert_many(data_list)
# print(ret)

# 查询一个记录
# ret = collection.find_one({'name':'xiaozhang'})

# # 查询所有记录
# ret = collection.find({'name':'xiaozhang'})
# print(ret)

# # 更新一条
# ret = collection.update_one({'name':'xiaozhang'},{'$set':{'name':'sss'}})

# # 更新所有
# ret = collection.update_many({'name':'xiaozhang'},{'$set':{'name':'sss'}})

# # 删除一条
# ret = collection.remove_one({'name':'xiaozhang'})

# # 删除所有
# ret = collection.remove_many({'name':'xiaozhang'})
data_list = [{'_id':'{}'.format(i), 'name': 'py{}'.format(i)} for i in range(5)]
collection.insert_many(data_list)
# 显示所有数据库
show databases/dbs

# 显示当前数据库
db

# 切换数据库
use db_name

# 删除当前数据库
db.dropDatabase()

# 集合的基本命令
db.createCollection(name, options)
db.createCollection('stu')
# capped: true 设置上限,当前为10字节
db.createCollection('stu', {capped: true, size: 10})

# 删除集合
db.集合名称.drop()

# 查看集合
show collections

# 插入
db.test1000.insert({'name': 'xioawang', 'age': 10})

# 查询
db.test1000.find()

# 保存
db.集合名词.save(document)
# 如果存在,则修改,不存在添加

# 更新
db.集合名称.update( < query > , < update > , {multi: < boolean > })
# 整个全变,age会消失,修改整个数据,更新一条
db.test1000.update({name: 'xiaohong'}, {name: 'xiaozhang'})
# 只修改name,不会修改整个数据,更新一条
db.test1000.update({name: 'xiaohong'}, {$set{name: 'xiaozhang'}})
# 只修改name,不会修改整个数据,更新全部
db.test1000.update({name: 'xiaohong'}, {$set{name: 'xiaozhang'}, {multi: true}})

# 删除
# 默认删除多条
db.集合名称.remove(< qeury > , {justOne: true})

""" 高级用法 """
# 查找
find
findOne()
# 将结果格式化
pretty()

# 比较
# 小于:$lt
# 小于等于:$lte
# 大于:$gt
# 大于等于:$gte
# 不等于: $ne
db.stu.find({age: {$gte: 18}})

# 比较运算符
$in, $nin
db.stu.find({age: {$in: [18, 28, 38]}})

# 逻辑运算符
# and 直接写多个条件
db.stu.find({age: {$lg: 16}, name: 'zhangshan'})
# $or 或
# 年龄20或名字为lisi
db.stu.find({$or: [{age: 20}, {name: 'lisi'}]})

# 正则
db.stu.find({name: / ^abc/})
db.stu.find({name: {$regex: '789$'}})

# limit, skip
# 过两个,在限制两个,建议先过两个
db.stu.find().skip(2).limit(2)

# 自定义查询
db.stu.find({$where: function() {
    return this.age > 30
}})

# 投影
# 只选择需要的字段
# 1显示,0不显示
db.stu.find({age: 20}, {name: 1, age: 0})

# 排序
db.stu.find().sort({age: -1})

# 计数
# 小于等于18的数量
db.stu.find({age: {$lte: 18}}).count()
db.stu.find().count({age: {$lte: 18}})

# 去重
db.stu.distinct('name')

""" 聚合 aggregate """
# 将前一个结果的结果给下一个管道处理
db.stu.aggregate({管道: {表达式}})

# 表达式
# $sum求和
# $avg:计算平均值
# $min,$max
# $push 插入值到一个数组中
# $first 获取第一个文档数据
# $last
# $group 分组
# $project 修改输入文档的结构,如重命名,增删,创建技术
# $match 过滤
# $sort
# $skip
# $limit
# $unwind 拆分数组
# 求gender
db.stu.aggregate(
    {$group: { _id: '$gender', count: {$sum: 1}, age_age: {$avg: '$age'} } },
    {$project: {_id: '$_d', count:1,avg_age:'$avg_age',_id:0}}
)
# 求总人数和平均年龄,只输出数量
db.stu.aggregate({$group: { _id: null, count: {$sum: 1}, age_age: {$avg: '$age'} } },{$project:{_id:0,count:1}})
# $unwind
# 拆分数据,并获取长度
db.stu.insert({_id:1, item:'t-shirt', size:['s','m','l']})
db.stu.aggregate({$unwind:'$size'})
# 获取长度
db.stu.aggregate({$unwind:'$size'},{$group:{_id:null, count:{$sum:1}}})
# 防止空属性被删
db.stu.aggregate({$unwind:{path:'$size',preserveNullAndEmptyArray: true}})

""" 创建索引 """
# 1升序,-1降序,创建索引
db.stu.ensureIndex({name:1})
db.stu.find({name:'test10000'})
db.stu.find({name:'test10000'}).explain('executionStats')

# 获取索引
db.stu.getIndexes()
# 删除索引
db.stu.dropIndex({name:1})
# 索引唯一
db.stu.ensureIndex({name:1},{'unique':true})
# 联合索引
db.stu.ensureIndex({name:1,age:1})

""" 场景 """
# 关键字去重,不能插入重复的
# url地址去重
  # redis
  # 布隆过滤器
  #   使用多个加密算法加密url,得到多个值
  #   往对应值的位置结果设置为1
  #   新来一个url地址,通过加密算法生成多个值
  #   如果对于的值全为1,说明url地址已经抓过
  #   否则没抓过,就把对应位置的值设置为一
# 根据数据本省进行去重


""" 数据类型 """
Object ID: 文档ID
String: 字符串, utf-8
boolean: boolean
integer: 整形 32, 64位
Double: 浮点型
Arrays: 数组
Object: 对象, 用于嵌入文档
Null: 存储null
timestamp: 时间戳, 总秒数
Date: 日期

# 创建日期
new Date('2017-12-20')

ObjectID
前四个自己当前时间戳
在3个字节是机器ID
在两个字节是服务进程ID
最后三个字节是简单的增量
# 可以手动插入


""" 备份和还原 """
mongodump -h dbhost -d dbname -o dbdirectory
mongodump -h 172.16.20.46: 27017 -d test1 -o ~/Desktop/test1bak

mongorestore -d dbname -dir dbdirectory
mongorestore -d test1 - dir ~/Desktop/test1bak

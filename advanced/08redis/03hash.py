# hash
# 存储对象
# hset key field value
# hset user name lisi

# hmset key field1 value1 field2 value2
hmset usr name lisi age 12

# 获取属性
hkeys usr


# 获取一个属性的值
hget key field

# 获取多个属性
hmget key field1 field2

# 获取所有属性值
hvals key

# 删除
hdel key field1 field2
hdel usr age

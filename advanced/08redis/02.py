# string
# 选择数据库
select 0
# 设置键值
# set key value
set name 'lisi'

# get key
get name

# 设置过期时间
# setex name 时间 name
# setex aa 3 aa

# 设置多个键值
mset key1 value1 key2 value2

# 追加
append key value

# 获取多个值
mget key1 key2 key3

# 获取key
# keys pattern 支持正则
keys * 获取所有
keys a* 获取以a开头的

# 获取是否
# exists key

# 获取key对应的value类型
type key

# 删除key
del key key2 

# 设置过期时间,如果没设置过期时间一直存在
expire key seconds
expire a1 3

# 查看key有效时间
ttl key
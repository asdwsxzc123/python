# set 无序的集合
string类型
元素具有唯一性
对集合没有修改操作

# sadd key zhangsan lisi wangwu

# keys *

# 获取所有的元素
smembers key

# 删除指定元素
srem key value


# zset 有序的集合
# 每个元素都会关联一个double类型的score,表示权重,通过权重将元素从小到大排序
zadd key score1 member1 score2 member2

zadd a4 1 zhangsan 2 wangwu 3 lisi

# 0 -1表示最后一个,从小到大排列
zrange key start stop

# 权重在多少之间
zrangebyscore key min max

# 返回权重
zscore key member

# 删指定元素
zrem key member1

# 删除指定权重
zremrangebyscore key min max


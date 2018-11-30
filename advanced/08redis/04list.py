# list 的元素类型 string
# 从左侧插入
lpush key value1 value2

# 从右侧插入
rpush key value1 value2

# 从键a1的列表右侧加入数据
rpush a1 0 1

# 从指定元素的前或者后插入元素(单个)
linsert key before 或 after  元素
linsert a1 before b 123

# 查看列表
lrange key start end
# 查看所有
lrange a1 0 -1

# 设置指定所有位置的元素值
lset key index value
lset a1 1 z

# 删除指定元素
# count > 0 : 从头删除
# count < 0 : 从尾部删
# count = 0 移除所有
lrem key count value

# 从a2列表右侧开始删除2个'b'
lrem a2 -2 b

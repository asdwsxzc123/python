# 对比
# 1. sql适合关系特别复杂的数据查询
# 2. 事务特性,sql支持完善,nosql不支持

redis是开源的,支持网络,基于内存,开源持久化的日志型,key-Value (VMware开发)
多种键值的数据类型,缓存和队列系统

# 特效
1. 支持数据持久化,数据开源保存到磁盘中,重启时再次加载
2. 不只是key-value,还指出list,set,zset,hash等数据结构
3.支持数据备份,master-slave模式

# 优势
1. 性能极高,读写速度快
2. 丰富的数据类型,支持二进制
3. 原子性,支持极高操作合并后的原子性操作
4. 支持publish/subscribe,通知,key过期

场景
1. 做缓存
2. 社交类
3. session共享,购物车

# 配置
bind 127.0.0.1
port 6379

是否开启进程守护, 守护不会在命令行阻塞
非守护当前终端会阻塞
推荐yes
daemonize yes

数据文件
dbfilename dump.rdb

数据文件存储路径(如果没该文件夹,需要创建)
dir /var/lib/redis

日志文件
logfile /var/log/redis/redis-server.log

数据库
database 16

主从备份
slaveof

启动 redis-server /etc/redis/redis.conf
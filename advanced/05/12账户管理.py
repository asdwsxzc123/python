# 在生产环境下操作数据库,不能使用root账户链接.而是创建特定的账户,授权中国账户特定 的操作权限,然后进行操作.数据的crud
# 账户分级:
# 1. 服务实例级账户: 启动mysqld,即为一个数据库实例如root,该账户可以删除所有的数据库,连同这个库中的表
# 2. 数据库级别账户: 对特定数据库执行增删改查的权限
# 3. 数据表级别账户: 对特定表执行增删改查的等所有操作
# 4. 字段级别的权限： 对某些表的特定字段进行操作
# 5. 存储程序级别
# 账户的操作包括： 创建账户，删除账户，修改账户，修改密码

# 创建用户权限
# grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
# grant (select) on jing_dong.* to 'laowang'@'localhost' identified by '123456'
# grant all privileges on jing_dong.* to 'laowang'@'%' identified by '123456'

# 修改权限
# grant 权限列表 on 数据库 to '用户名'@'访问主机' with grant option;
# flush privileges;

# 修改密码
# UPDATE USER SET authentication_string = PASSWORD('新密码') where user='用户名';

# 删除
# drop user '用户名'@'主机';
# delete from user where user='用户名'

# 远程访问
# /etc/mysql/mysql.conf.d/mysqld.cnf
#bind-addr = 127.0.0.1
# .service mysql restart


# 查询权限
# show grants for laowang@localhost;


""" mysql主从 """
# 读写分类,数据备份
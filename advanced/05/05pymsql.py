from pymysql import connect
# 链接数据库

conn = connect(host='172.16.20.46', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
# 获取cursor对象
cs1 = conn.cursor()

# sql注入

# # 执行select语句
# cs1.execute('select * from goods;')
# # print(row)

# for row in cs1.fetchall():
#     print(row)

# 插入数据
cs1.execute('insert into goods_cates (name) values ("硬盘")')
# 插入数据需要提交
conn.commit()
# 删除数据
# conn.rollback()

# 关闭cursor和链接
cs1.close()
conn.close()


from pymysql import connect
# 链接数据库
# host="localhost"
host="172.16.20.46"
port=3306
user='root'
password='123456'
database="jing_dong"
charset="utf8"
conn = connect(host, port , user, password,database,charset)
# 获取cursor对象
cs1 = conn.cursor()

# 执行select语句
row = cs1.execute('select * from goods;')
print('受影响的行数:'+row)

rows = cs1.fetchall()
print(rows)

# 关闭cursor和链接
cs1.close()
conn.close()


# -- 索引
# -- 一种特殊的文件,他对应表里的所有记录的引用指针.索引好比数的目录,能加快查询速度
# -- 索引的目的是在于提高查询效率,可以类比字典,
# -- 例如: 图书的目录,火车站的车次

# create table test_index(tilte varchar(10));

# 开启时间统计
# set profiling=1;

# select * from test_index where tilte = 'ha-99999';
# show profiles;
# create index title_index on test_index(tilte(10));

# 查看索引
# show index from 表名;

# 查询索引
# select * from test_index where tilte = 'ha-99999';

# 删除索引
# drop index 索引名 on 表名
# 注意
# 建立太多索引会影响更新和插入的速度,因为也需要更新每个索引文件,对一个需要经常插入和更新的表格,没有必要建立索引

from pymysql import connect

def main():
    # 链接数据库
    conn = connect(host='172.16.20.46', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    for i in range(100000):
        cs1.execute('insert into test_index values ("ha-%d")'%i)
        conn.commit()
    
if __name__ == "__main__":
    main()


# 用户注册
# 登录
# 用户下单
# 订单表
from pymysql import *


class JD (object):
    def __init__(self):
        self.conn = connect(host='172.16.20.46', port=3306, user='root',
                            password='123456', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()
        self.user_id = 0
        self.run()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

    def get_all_goods(self):
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def get_info_by_name(self):
        find_name = input('请输入商品名: ')
        args = '%' + find_name + '%'
        sql = 'select * from goods where name like %s;'
        self.cursor.execute(sql, [args])
        for row in self.cursor.fetchall():
            print(row)

    def get_all_goods_brands(self):
        sql = 'select * from goods_brands;'
        self.execute_sql(sql)

    def get_all_goods_cates(self):
        sql = 'select * from goods_cates;'
        self.execute_sql(sql)

    def get_all_users(self):
        sql = 'select * from customers;'
        self.execute_sql(sql)

    def add_brands(self):
        brand_name = input('请输入品牌名: ')
        sql = 'insert into goods_brands (name) values (%s);'
        self.cursor.execute(sql, [brand_name])
        self.conn.commit()

    def add_user(self):
        # name = '李四'
        # address = 'WR-506'
        # tel = '18027175287'
        # passwd = '123456'
        name = input('请输入名称: ')
        address = input('请输入地址: ')
        tel = (input('请输入手机号: '))
        passwd = input('请输入密码: ')
        sql = 'insert into customers (name, address, tel, passwd) values (%s,%s,%s,%s);'
        self.cursor.execute(sql, [name, address, tel, passwd])
        self.conn.commit()

    def user_login(self):
        name = input('请输入用户名: ')
        passwd = input('请输入密码: ')
        sql = 'select * from customers where name = %s and passwd = %s'
        self.cursor.execute(sql, [name, address, tel, passwd])
        if (len(self.cursor.fetchall()) > 0) {
            (user_id) = self.cursor.fetchall()
            print(user_id)
            self.user_id = user_id
            print('登录成功')
        }

    @staticmethod
    def print_menu():
        print('='*50)
        print('1. 查询所有商品')
        print('2. 查询所有商品类型')
        print('3. 查询所有商品品牌')
        print('4. 查询商品信息')
        print('5. 添加品牌')
        print('6. 注册用户')
        print('7. 用户登录')
        print('8. 用户登出')
        print('9. 查询所有用户')
        print('10. 用户下单')

    def run(self):
        while True:
            self.print_menu()
            num = int(input('请输入编号: '))
            if num == 1:
                # 查询所有商品
                self.get_all_goods()
            elif num == 2:
                # 查询所有商品类型
                self.get_all_goods_cates()
            elif num == 3:
                # 查询所有商品品牌
                self.get_all_goods_brands()
            elif num == 4:
                # 查询商品信息
                self.get_info_by_name()
            elif num == 5:
                # 添加品牌
                self.add_brands()
            elif num == 6:
                # 注册用户
                self.add_user()
            elif num == 7:
                # 用户登录
                self.user_login()
            # elif num == 8:
                # 用户登出
            #     self.user2order()
            elif num == 9:
                # 查询所有用户
                self.get_all_users()
            else:
                pass


def main():
    jd = JD()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
from pymysql import *
class JD (object):
    def __init__(self):
        try:
            # self.conn = connect(host='192.168.220.135', port=3306, user='root',
            #                     password='geesunn123', database='jing_dong', charset='utf8')
            self.conn = connect(host='172.16.20.46', port=3306, user='root',
                                password='123456', database='jing_dong', charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as ret:
            print(ret)
        else:
            pass
        self.user_id = 0
        self.order_id = 0

        self.run()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)
    def commit_ok(self,content):
        print(content)
        self.conn.commit()

    def get_all_goods(self):
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def get_info_by_name(self):
        find_name = input('请输入商品名:')
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
        name = 'lisi'
        passwd = '123456'
        # name = input('请输入用户名: ')
        # passwd = input('请输入密码: ')
        sql = 'select id from customers where name = %s and passwd = %s'
        row = self.cursor.execute(sql, [name, passwd])
        if (row > 0):
            for item in self.cursor.fetchall():
                print('登录成功')
                print(item[0])
                self.user_id = item[0]
        else:
            print('账户密码错误')

    def user_logout(self):
        self.user_id = 0
        print('退出成功')

    def get_login_info(self):
        sql = 'select * from customers where id = %s'
        row = self.cursor.execute(sql, [self.user_id])
        if row:
            print(self.cursor.fetchall())
        else:
            print('------请登录------')

    def createOrder(self):
        sql = 'insert into orders (customer_id) values(%s);'
        if self.user_id:
            row = self.cursor.execute(sql, [self.user_id])
            if row > 0:
                print('创建成功---%d' % self.cursor.lastrowid)
                # self.order_id = self.conn.insert_id()
                self.order_id = self.cursor.lastrowid
                self.conn.commit()
            else:
                print('创建失败')
        else:
            print('------请登录------')

    def add_goods2order(self):
        self.get_all_goods()
        good_id = input('请输入要购买的商品id:')
        # 1.添加商品good_id,放在一个list里面
        # 判断有没有
            # 有更新,没有插入
        find_sql = 'select quantity from order_detail where order_id= %s and good_id = %s'
        find_row = self.cursor.execute(find_sql, [self.order_id,good_id])

        if find_row > 0:
            quantity = self.cursor.fetchall()[0]
            print('quantity:'+quantity)
            quantity += 1
            sql = 'update order_detail set quantity=%s'
            row = self.cursor.execute(sql,[quantity])
        else: 
            sql = 'insert into order_detail (order_id,good_id,quantity) values(%s,%s,1)'
            row = self.cursor.execute(sql,[self.order_id,good_id])

        if row > 0:
            self.commit_ok('添加成功')
        else: 
            print('添加失败')
    def select_order(self):
    def find_order(self):
        if self.user_id> 0:
            order_sql = 'select * from orders where customer_id=%s;'
            order_num = self.cursor.execute(order_sql, [self.user_id])
            if order_num> 0:
                print('订单id,用户id,创建时间')
                for order in self.cursor.fetchall():
                    print(order)
            else:
                print('该用户,暂无订单')
            order_id = input('请输入想要查询的订单id:')
            order_detail_sql = 'select * from order_detail where order_id=%s;'
            row = self.cursor.execute(order_detail_sql, [order_id])
            if row > 0:
                print('详情id,订单id,商品id,数量')
                for order_detail_row in self.cursor.fetchall():
                    print(order_detail_row)
            else:
                print('该单号再无商品!')
        else:
            print('------请登录------')
        
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
        print('10. 用户创建订单')
        print('11. 获取登录信息')
        print('12. 用户添加商品')
        print('13. 查看订单')

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
            elif num == 8:
                # 用户登出
                self.user_logout()
            elif num == 9:
                # 查询所有用户
                self.get_all_users()
            elif num == 10:
                # 创建订单
                self.createOrder()
            elif num == 11:
                # 获取登录信息
                self.get_login_info()
            elif num == 12:
                # 用户添加商品
                self.add_goods2order()
            elif num == 13:
                # 查看订单
                self.find_order()
            else:
                pass


def main():
    jd = JD()


if __name__ == "__main__":
    main()

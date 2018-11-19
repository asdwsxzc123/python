# 增删改查, 防止sql注入
# 输入 'or 1=1 or'
from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='172.16.20.46', port=3306, user='root',
                            password='123456', database='jing_dong', charset='utf8')
        self.cursor = self.conn.cursor()
        self.run()

    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            print(row)

    def show_all_items(self):
        self.execute_sql('select * from goods;')

    def get_info_by_name(self):
        find_name = input('请输入商品名: ')
        args = '%' + find_name + '%'

        # sql = "select * from goods where name like'%s';" % args
        # print('---->%s<-----' % sql)
        # self.execute_sql(sql)

        sql = "select * from goods where name like %s;"
        # 防止sql注入
        self.cursor.execute(sql,[args])
        print(self.cursor.fetchall())


    def show_all_cates(self):
        self.execute_sql('select * from goods_cates;')

    def show_all_brands(self):
        self.execute_sql('select * from goods_brands;')

    def add_brands(self):
        brand_name = input('请输入品牌名: ')
        sql = 'insert into goods_brands (name) values (%s)'
        self.cursor.execute(sql,[brand_name])
        self.conn.commit()

    # 不需要实例对象和方法的私有属性
    @staticmethod
    def print_menu():
        print('---------京东--------')
        print('1.: 所有的商品')
        print('2.: 所有的商品分类')
        print('3.: 所有的商品品牌分类')
        print('4.: 添加一个商品品牌分类')
        print('5.: 查询商品:')
        return input('亲输入功能对应的序号: ')

    def run(self):
        print(111)
        while True:
            print(22)
            num = self.print_menu()
            if num == '1':
                # 查询所有的商品
                self.show_all_items()
            elif num == '2':
                # 所有的商品分类
                self.show_all_cates()
            elif num == '3':
                # 所有的商品品牌分类
                self.show_all_brands()
            elif num == '4':
                # 添加一个商品品牌分类
                self.add_brands()
            elif num == '5':
                # 查询商品
                self.get_info_by_name()
            else:
                pass


def main():
    # 1. 创建一个京东对象
    jd = JD()
    # 2. 调用这个对象的run方法,让其运行


if __name__ == '__main__':
    main()

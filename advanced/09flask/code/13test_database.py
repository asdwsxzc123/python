# coding:utf-8
import unittest
from book_tmp1 import Author, db, app
class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@172.16.20.46:3306/flask_test'
        db.create_all()
    def test_add_author(self):
        """ 测试添加作者的数据库操作 """
        author = Author(name='zhang', email='1234@126.com')
        db.session.add(author)
        db.session.commit()
        result_author = Author.query.filter_by(name='zhang').first()
        self.assertIsNotNone(result_author)
    # def tearDown(self):
    #     """ 在所有的操作执行后,执行, 通常进行清除操作 """    
    #     db.session.remove()
    #     db.drop_all()

if __name__ == "__main__":
    unittest.main()
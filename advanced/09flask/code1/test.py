# coding:utf-8
""" 单元测试 """
import unittest
from login import app
import json
class LoginTest(unittest.TestCase):
    """ 构建单元测试案例 """
    def test_empty_user_name_password(self):
        """ 测试用户名密码不完整的情况 """
        # 创建进行web请求的客户端,使用flask提供的
        client = app.test_client()

        # 利用client客户端模拟发送web请求
        ret = client.post('/login', data={})

        # ret 是视图的返回的响应对象,data属性是响应体的数据
        resp = ret.data
        print(resp)
        # 因为login是json
        resp = json.loads(resp.decode("utf-8"))

        # 拿到返回值后进行断言
        self.assertIn('code', resp)
        self.assertEqual(resp["code"], 1)

if __name__ == "__main__":
    unittest.main()

# coding:utf-8

def num_div(num1, num2):
    # assert 断言 后面是一个表达式,如果表达式返回true则断言成功,程序能继续执行
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1 / num2)

num_div(100, 50)
num_div('a', 'b')

# 断言
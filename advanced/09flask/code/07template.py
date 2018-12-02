# coding:utf-8
from flask import Flask, render_template, flash
app = Flask(__name__)
flag = True

app.config['SECRET_KEY'] = 'sdfds'

@app.route('/message')
def message():
    global flag
    if flag:
        #  添加闪现信息
        flash('hello')
        flash('hello1')
        flash('hello2')
        flag = False
    return render_template('index.html')


@app.route('/index')
def index():
    data = {
        "name": "python",
        "age": 18,
    }
    # 字符串过滤器
    # safe: 静止转义
    # trim 去叫两边的空格
    # upper: 大写
    # <p > {{' age  world ' | trim | upper}} < /p >

    # 列表过滤器
    # first : 第一个
    # last : 最后个
    return render_template('/index.html', **data)


""" 自定义过滤器 """
# 1. 注册


def list_step_2(li):
    return li[::2]


# 注册过滤器
app.add_template_filter(list_step_2, 'li2')

# 2. 直接使用装饰器


@app.template_filter('li3')
def list_step_3(li):
    return li[::3]


""" 宏的使用 """
# 定义
# {%macro input()%}
# <input type="text" name="username" value="">
# {% endmacro%}
# # 使用
# {{input()}}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7788, debug=True)

# coding:utf-8
# 先找app_cart.py,没有找__init__.py找
from . import app_cart
from flask import render_template

@app_cart.route('/get_cart')
def get_cart():
    return render_template('cart.html')
# coding:utf-8
from . import api

@api.route('/demo')
def demo():
    return 'index v1'
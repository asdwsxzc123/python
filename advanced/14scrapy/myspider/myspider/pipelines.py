# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from myspider.items import TencentItem, SunItem
client = MongoClient()
# collection = client['tencent']['hr']
collection = client['sun']['questions']


class TennetPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            # if spider.name == 'hr':
            print(item)
            collection.insert(dict(item))
        return item


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'itcast':

            print(item)
        # return 是用来给下一个pipline使用
        return item


class MyspiderPipeline1(object):
    def process_item(self, item, spider):
        if spider.name == 'itcast1':
            print(item)
            item['hello'] = 'world'
            print(item)
        return item


class SunPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, SunItem):
            print(item)
            # collection.insert(dict(item))
        return item

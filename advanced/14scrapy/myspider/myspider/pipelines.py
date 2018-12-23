# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
# from pymongo import MongoClient
from myspider.items import TencentItem, SunItem, BookItem
# client = MongoClient()
# collection = client['tencent']['hr']
# collection = client['sun']['questions']


class TennetPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            # if spider.name == 'hr':
            print(item)
            # collection.insert(dict(item))
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
    def open_spider(self, spider):
        spider['hello'] = 'world'

    def process_item(self, item, spider):
        if isinstance(item, SunItem):
            item['content'] = self.process_content(item['content'])
            # collection.insert(dict(item))
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s|\t", "", i) for i in content]
        content = [i for i in content if len(i) > 0]  # 去除空字典


class BookPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BookItem):
            pass
            # collection.insert(dict(item))
        return item

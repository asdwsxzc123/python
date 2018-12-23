# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    position = scrapy.Field()
    publish_date = scrapy.Field()
    
class SunItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    status = scrapy.Field()
    create_user = scrapy.Field()
    create_time = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()


class BookItem(scrapy.Item):
    b_cate = scrapy.Field()
    b_href = scrapy.Field()
    s_cate = scrapy.Field()
    s_href = scrapy.Field()
    book_title = scrapy.Field()
    book_price = scrapy.Field()
    book_img = scrapy.Field()

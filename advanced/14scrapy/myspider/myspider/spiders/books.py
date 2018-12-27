# -*- coding: utf-8 -*-
import scrapy,re
from myspider.items import BookItem
from copy import deepcopy
class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']
    def parse(self, response):
        self.list_base_url = 'https://list.suning.com'

        item_list = response.xpath(
            '//div[@class="menu-list"]/div[@class="menu-item"]')
        for store in item_list:
            item = BookItem()
            item['b_cate'] = store.xpath('.//dt/h3/a/text()').extract_first()
            item['b_href'] = store.xpath('.//dt/h3/a/@href').extract_first()
            a_list = store.xpath('.//dd/a')
            for a in a_list:
                item['s_cate'] = a.xpath('./text()').extract_first()
                item['s_href'] = a.xpath('./@href').extract_first()
                if item['s_href'] is not None:
                    yield scrapy.Request(
                        item['s_href'],
                        callback=self.parse_book_list,
                        meta = {'item':deepcopy(item)}
                    )

    def parse_book_list(self,response):
        item = response.meta['item']
        li_book_list = response.xpath('//div[@id="filter-results"]//ul/li')
        for li in li_book_list:
            book_info = li.xpath('.//div[@class="res-info"]')
            item['book_title'] = book_info.xpath(
                './/p[@class="sell-point"]/a[@class="sellPoint"]/text()').extract_first()
           
            item['book_info_href'] = li.xpath(
                './/div[@class="res-img"]/div[@class="img-block"]/a/@href').extract_first()
            item['book_img'] = li.xpath(
                './/div[@class="res-img"]/div[@class="img-block"]/a/img[@class="search-loading"]/@src2').extract_first()
            if item['book_info_href'] is not None:
                yield scrapy.Request(
                    'https:'+item['book_info_href'],
                    callback=self.parse_book_info,
                    meta={'item':deepcopy(item)}
                )
        # 翻页
        # next_href = self.list_base_url + response.xpath('//a[@id="nextPage"]/@href').extract_first()
        # print(next_href)
        # if next_href is not None:
        #     yield scrapy.Request(
        #         next_href,
        #         callback=self.parse_book_list,
        #         meta={'item': deepcopy(item)}
        #     )
    def parse_book_info(self,response):
        item = response.meta['item']
        item['book_price'] = re.findall("\"itemPrice\":\"'(.*?)'\",",response.body.decode('utf-8'))
        item['book_author'] = response.xpath('//ul[contains(@class,"bk-publis")]/li[1]//text()').extract()
        item['book_press'] = response.xpath('//ul[contains(@class,"bk-publis")]/li[2]//text()').extract()
        item['publish_time'] = response.xpath('//ul[contains(@class,"bk-publis")]/li[3]/span[2]/text()').extract_first()
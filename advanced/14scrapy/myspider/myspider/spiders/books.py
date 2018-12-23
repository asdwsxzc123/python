# -*- coding: utf-8 -*-
import scrapy
from myspider.items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
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
                        meta = {'item':item}
                    )

    def parse_book_list(self,response):
        li_book_list = response.xpath('//div[@id="filter-results"]//ul/li')
        print(item)
        for li in li_book_list:
            book_info = li.xpath('.//div[@class="res-info"]')
            item['book_title'] = book_info.xpath(
                './/p[@class="sell-point"]/a[@class="sellPoint"]/text()')
            item['book_price'] = book_info.xpath(
                './/p[@class="prive-tag"]/em[@class="prive price "]/text()')
            item['book_img'] = li.xpath(
                './/div[@class="res-img"]/div[@class="img-block"]/a/@href')
            print(item)
            return item

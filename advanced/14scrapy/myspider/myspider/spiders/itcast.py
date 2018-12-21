# -*- coding: utf-8 -*-
import scrapy
import logging

logging = logging.getLogger(__name__)
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 处理start_url地址对应的响应
        # ret1 = response.xpath('//div[@class="tea_con"]//h3/text()').extract()
        # print(ret1)
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item = {}
            item['name'] = li.xpath('.//h3/text()').extract_first()
            item['title'] = li.xpath('.//h4/text()').extract()[0]
            # print(item)
            # 使用yield为了减少内存占用
            logging.warning(item)
            yield item

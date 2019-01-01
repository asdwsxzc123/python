# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    rules = (
        # linkextractor 连接提取器,提取url地址
        #  callback 提提取出来url多response会交给callback
        # follow 当前URL地址多响应是能够重新进过rules来提取URL地址
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = re.findall(
            '<!--TitleStart-->(.*?)<!--TitleEnd-->', response.body.decode())[0]
        item['publish_data'] = re.findall("发布时间：(\d{4}-\d{2}-\d{2})", response.body.decode())[0]
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        print(item)

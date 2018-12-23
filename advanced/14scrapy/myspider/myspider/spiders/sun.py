# -*- coding: utf-8 -*-
import scrapy
from myspider.items import SunItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType']

    def parse(self, response):
        print(self.hello)
        # 下标从1开始算
        tr_list = response.xpath(
            '//div[@class="greyframe"]/table[2]//table[@bgcolor="#FBFEFF"]//tr')
        for tr in tr_list:
            item = SunItem()
            item['num'] = tr.xpath('./td[1]/text()').extract_first()
            item['title'] = tr.xpath('./td[2]/a[2]/text()').extract_first()
            item['href'] = tr.xpath('./td[2]/a[2]/@href').extract_first()
            item['status'] = tr.xpath('./td[3]/span/text()').extract_first()
            item['create_user'] = tr.xpath('./td[4]/text()').extract_first()
            item['create_time'] = tr.xpath('./td[5]/text()').extract_first()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': item}
            )
            # yield item
        # 翻页
        # next_url = response.xpath('//div[@class="pagination"]//a[text()=">"]//@href').extract_first()
        # if next_url:
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
    def parse_detail(self, response):
        item = response.meta['item']
        item["content"] = response.xpath(
            '//div[contains(@class,"text14_2")]/div[@class="contentext"]//text()').extract()
        item["content_img"] = response.xpath(
            '//div[contains(@class,"text14_2")]/div[@class="textpic"]//img/@src').extract()
        item['content_img']=['http://wz.sun0769.com' + i for i in item['content_img']]
        yield item

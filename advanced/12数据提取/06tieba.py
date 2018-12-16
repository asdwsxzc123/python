from parse_url import parse_url
import json
from lxml import etree
class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn={}' % tieba_name
        self.part_url = 'https://tieba.baidu.com'
    def get_content_list(self,html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath('//li[contains(@class,"tl_shadow_new")]')
        content_list = []
        for li in li_list:
            item = {}
            item['title'] = li.xpath('./a/div[@class="ti_title"]/span/text()')[0] if len( li.xpath('./a/div[@class="ti_title"]/span/text()')) > 0 else None
            item['href'] = self.part_url + li.xpath('./a[contains(@class,"j_common")]/@href')[
                0] if len(li.xpath('./a[contains(@class,"j_common")]/@href')) > 0 else None
            item['img_list'] = self.get_img_list(item['href'])
            print(item)
            content_list.append(item)
        return content_list
    def get_img_list(self,detail_url):
        #     3.1 提取列表页的url地址和标题
        #     3.2 请求列表url地址，获取详情页的第一页
        if detail_url is not None:
            detail_html_str = parse_url(detail_url)
            detail_html = etree.HTML(detail_html_str)
            #     3.3 提取详情页第一页的图片，提取下一页的地址
            img_list = detail_html.xpath('//img[@class="BDE_Image"]/@src')
            print(detail_html_str)

        #     3.4 获取详情
        else: 
            img_list = []
        return img_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name + '.txt'
        with open(file_path, 'a') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write('\n')
    def run(self):
        # 1. start_url
        pn = 0
        take = 50
        while pn <= 0:
            url = self.start_url.format(pn * take)
            html_str = parse_url(url)
            content_list = self.get_content_list(html_str)
            # 2. 发送请求，获取响应
            # 3. 提取数据，提取下一页的url地址
            #     3.1 提取列表页的url地址和标题
            #     3.2 请求列表url地址，获取详情页的第一页
            #     3.3 提取详情页第一页的图片，提取下一页的地址
            #     3.4 获取详情
            # 4.保存
            self.save_content_list(content_list)
            # 5.请求下一页
            pn += 1

if __name__ == "__main__":
    tieba = TiebaSpider('李毅')
    tieba.run()

from parse_url import parse_url
from lxml import etree


class QiubaiSpider:
    def __init__(self):
        self.url_temp = 'https://www.qiushibaike.com/hot/page/{}/'

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 2)]

    def get_content_list(self, url):
        html_str = parse_url(url)
        html = etree.HTML(html_str)
        content_list = []
        for div in html.xpath("//div[@id='content-left']"):
            item = {}
            item['content'] = div.xpath('.//div[@class="content"]/span/text()')
            item['author_gender'] = div.xpath('..//div[contains(@class,"articleGender")]/@class')
            item['author_gender'] = item['author_gender'][0].split(' ')[-1].replace('Icon', '') if len(item['author_gender']) > 0 else None
            content_list.append(item)
        return content_list
    def save_content_list(self,content_list):
        pass
    def run(self):
        # 获取响应
        for url in self.get_url_list():
            content_list = self.get_content_list(url)
            self.save_content_list(content_list)

if __name__ == "__main__":
    qiushi = QiubaiSpider()
    qiushi.run()

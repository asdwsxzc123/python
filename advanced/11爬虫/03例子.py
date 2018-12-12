import requests
# url = 'https://tieba.baidu.com/f'
# kw = {'kw': '梦幻西游', 'pn': 0}
# # kw = {'kw': '梦幻西游'}

# resp = requests.get(url,headers=headers,params = kw)
# with open('./index.html', 'wb') as f :
#     f.write(resp.content)
#     f.close()


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn={}' % (
            tieba_name)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def get_url_list(self):
        # 1. 构造url列表
        # url_list = []
        # for i in range(5):
        #     url_list.append(self.url_temp.format(i*50))
        # 扁平胜于嵌套
        return [self.url_temp.format(i*50) for i in range(5)]

    def parse_url(self, url):
        # 2. 遍历发送请求,获取响应
        print(url)
        resp = requests.get(url, headers=self.headers)
        return resp.content.decode()
    def save_html(self,html_str,page_num):
        # 3. 保存html字符串
        file_path = './file/{}-第{}页.html'.format(self.tieba_name, page_num)
        with open(file_path, 'w',encoding='utf-8') as f:
            f.write(html_str)
            f.close
    def run(self):
        # 构造url
        url_list = self.get_url_list()
        # 循环遍历
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    tieba_spider = TiebaSpider('梦幻西游')
    tieba_spider.run()
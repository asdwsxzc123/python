from lxml import etree
import requests
import json
import threading
from queue import Queue

# 单线程
""" 
class Movie:
    def __init__(self):
        self.start_url = 'https://www.dy2018.com/html/gndy/jddyy/index_{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers, proxies={
            'http': '115.223.255.187:9000'})
        return response.content.decode('GBK')

    def get_url_list(self):
        return [self.start_url.format(i) for i in range(2, 3)]

    def content_list(self, html_str):
        html = etree.HTML(html_str)
        content_list = []
        for div in html.xpath('//table[contains(@class,"tbspan")]'):
            item = {}
            item['title'] = div.xpath('.//b/a[@class="ulink"]/@title')[0]
            item['time'] = div.xpath('.//font[@color="#8F8C89"]/text()')[0]
            item['href'] = div.xpath('.//b/a[@class="ulink"]/@href')[0]
            content_list.append(item)
        print(content_list)
        return content_list
    def save_content_list(self,content_list):
        for content in content_list:
            with open('./dianyi.json', 'a', encoding="utf-8") as f:
                f.write(json.dumps(content,ensure_ascii=False,indent=4))
    def run(self):
        # url
        for url in self.get_url_list():
            html_str = self.parse_url(url)
            content_list = self.content_list(html_str)
            self.save_content_list(content_list) """


# 多线程
class Movie:
    def __init__(self):
        self.start_url = 'https://www.dy2018.com/html/gndy/jddyy/index_{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        self.count = 0
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
    def get_url_list(self):
        # return [self.start_url.format(i) for i in range(2, 3)]
        for i in range(2, 25):
            self.url_queue.put(self.start_url.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers, proxies={
                'http': '115.223.255.187:9000'})
            self.html_queue.put(response.content.decode('GBK'))
            self.url_queue.task_done()

    def content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            content_list = []
            for div in html.xpath('//table[contains(@class,"tbspan")]'):
                item = {}
                item['title'] = div.xpath('.//b/a[@class="ulink"]/@title')[0]
                item['time'] = div.xpath('.//font[@color="#8F8C89"]/text()')[0]
                item['href'] = div.xpath('.//b/a[@class="ulink"]/@href')[0]
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            for content in content_list:
                with open('./dianyi.json', 'a', encoding="utf-8") as f:
                    f.write(json.dumps(content, ensure_ascii=False, indent=4))
            self.count += len(content_list)
            print(self.count)
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        for i in range(5):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        for i in range(2):
            t_content = threading.Thread(target=self.content_list)
            thread_list.append(t_content)

        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for i in thread_list:
            i.setDaemon(True)
            i.start()
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()
        print('主线程结束')


if __name__ == "__main__":
    movie = Movie()
    movie.run()

from lxml import etree
import json
import requests
import threading
from queue import Queue


class QiubaiSpider:
    def __init__(self):
        self.url_temp = 'https://www.qiushibaike.com/hot/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 4)]
        for i in range(1, 10):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers, proxies={
                                    'http': '115.223.255.187:9000'})
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            content_list = []
            for div in html.xpath("//div[@id='content-left']//div[contains(@class,'article')]"):
                item = {}
                item['content'] = div.xpath(
                    './/div[@class="content"]/span/text()')
                item['author_gender'] = div.xpath(
                    '..//div[contains(@class,"articleGender")]/@class')
                item['author_gender'] = item['author_gender'][0].split(
                    ' ')[-1].replace('Icon', '') if len(item['author_gender']) > 0 else None
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            with open('./qiushi.json', 'a', encoding='utf-8') as f:
                f.write(json.dumps(content_list, ensure_ascii=False, indent=4))
            self.content_queue.task_done()

    def run(self):
        # 获取响应
        thread_list = []

        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        for i in range(20):
            p_url = threading.Thread(target=self.parse_url)
            thread_list.append(p_url)

        for i in range(2):
            g_list = threading.Thread(target=self.get_content_list)
            thread_list.append(g_list)

        s_content = threading.Thread(target=self.save_content_list)
        thread_list.append(s_content)
        for t in thread_list:
            # 吧子线程设置为守护线程,
            t.setDaemon(True)
            t.start()
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            # 让主线程阻塞,等待子线程完成
            q.join()
        print('主线程结束')


if __name__ == "__main__":
    qiushi = QiubaiSpider()
    qiushi.run()

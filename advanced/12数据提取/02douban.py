import requests, json
from parse_url import parse_url
from pprint import pprint
""" 
proxies = { 'http': '223.82.247.121:80' }
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

html_str = parse_url(url, proxies=proxies)

# json.loads吧json字符串转化为python
ret = json.loads(html_str)
with open('./douban.json', 'w',encoding='utf-8') as f:
    # f.write(json.dumps(ret,ensure_ascii=False,indent=4))
    # f.write(str(ret)) """

class  DoubanSpider(object):
    def __init__(self):
        self.start_temp = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit=20'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret['subject_collection_items']
        total = dict_ret['total']
        return content_list,total
    def save_content_list(self,content_list):
        with open('douban.txt', 'a') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write('\n')
        print('保存成功')
        
    def run(self):
        # 1.start_url
        num = 0
        total = 100
        while num<total+18:
            # 2.发送请求
            url = self.start_temp(num)
            json_str = parse_url(url)
            # 3. 提取数据
            content_list,total = self.get_content_list(json_str)
            # 4. 保存
            self.save_content_list(content_list)
            # if len(content_list < 18):
            #     break
            # 5.构造下一页url地址
            num += 18
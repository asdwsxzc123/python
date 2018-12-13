import requests,sys
import json

class Baidu_fanyi:
    def __init__(self, trans_str):
        self.lang_detect_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/basetrans'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'}
        self.trans_str = trans_str

    def parse_url(self, url, data):
        r = requests.post(url, headers=self.headers, data=data)
        return json.loads(r.content.decode())
    def get_ret(self,dict_response):
        ret = dict_response['trans'][0]['dst']
        print('result is : %s' % ret)
    def run(self):
        # 1. 获取语言类型
        # 1.1 准备posturl地址,post_data
        post_data = {'query': self.trans_str}
        # 1.2 发送post清求,获取响应
        r = self.parse_url(self.lang_detect_url, post_data)
        # 1.3 提取语言类型
        lang = r['lan']
        # 2. 准备post数据
        trans_data = { 'query': self.trans_str, 'from': 'zh', 'to': 'en' } if lang == 'zh' else  { 'query': self.trans_str, 'from': 'en', 'to': 'zh' }
        # 3. 发送数据,获取响应
        dict_response = self.parse_url(self.trans_url,trans_data)
        # 4. 提取翻译的结果
        self.get_ret(dict_response)


if __name__ == "__main__":
    trans_str = sys.argv[1]
    baidu_fanyi = Baidu_fanyi(trans_str)
    baidu_fanyi.run()

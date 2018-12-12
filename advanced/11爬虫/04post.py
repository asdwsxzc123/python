# coding:utf-8
import requests,json

url = 'https://fanyi.baidu.com/v2transapi'
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'halo',
    # 'transtype': 'translang',
    # 'simple_means_flag': '3',
    # 'sign': '983644.778605',
    # 'token': 'fb96c232f94e54a210a04211465572ea',
}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}

r = requests.post(url,data=data,headers=headers)
dict_ret = json.loads(r.content.decode())
print(dict_ret)
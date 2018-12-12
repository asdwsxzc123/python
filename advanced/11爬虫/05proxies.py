
""" 代理  """
# https: // proxy.mimvp.com/
# 如果知道最终服务器的地址是正向地址

# proxies
# proxies = {
#     'http': 'http://www.baidu.com',
#     'https': 'https://www.baidu.com'
# }

# 为什么使用代理
# 让服务器以为不是同一个客户端在请求
# 防止我们的真实地址被泄露,防止被追究

import requests
url = 'https://www.baidu.com'
proxies = {
    'http': '111.162.153.182:1080'
}
headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}
r = requests.get(url, proxies=proxies,headers=headers)
print(r.status_code)

"""  使用代理ip """
# 准备一堆的ip地址,组成ip池,随机选择一个ip来使用
# 如何随机选择代理ip
    # {ip:ip, times:0}
    # [{},{}],对这个ip的列表进行排序,按照使用次数进行排序
    # 选择使用次数较少的10个ip地址,从中随机选择一个
    # 给ip地址进行使用次数排序
# 检查ip可用性
#  可以使用requests,添加超时参数,判断ip质量
#  在线代理ip质量检查的网站

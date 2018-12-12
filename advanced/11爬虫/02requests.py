import requests
""" request """
# response = requests.get('https://www.baidu.com')
# # 状态码
# # response.status_code
# assert response.status_code == 200

# # 响应头
# response.headers

# # 请求头
# # user-agent很重要
# response.request.headers

# # 响应的请求头
# response.request.url

# # 响应的url
# response.url

""" get """
# response.content.decode()
url = 'https://www.baidu.com/s'
# headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
# 带参数
kw = {'wd': 'python'}
# response = requests.get(url,headers=headers,params = kw)
url = 'https://www.baidu.com/s?wd={}'.format('python')
response = requests.get(url,headers=headers)
# 文本
# print(response.text)
with open('./index.html', 'wb') as f :
    f.write(response.content)
    f.close()


""" post """
# 文本类型
response.text
# byte类型
response.content
response.content.decode()
response.content.decode('gbk')



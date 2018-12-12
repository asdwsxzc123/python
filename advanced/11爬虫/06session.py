
# session和cookie
# 如果需要获取登录后的页面,需要带上cookies
# cookie池
# session = requests.session()
# response = session.get(url,headers)

# 请求登录之后的网站的思路
# 实例化session
# 先使用session发送请求, 登录网站, 吧cookie保存在session中
# 在使用还能session请求登录之后才能访问的网站, session能够自动的携带登录成功时保存的在其中的cookie

# 不发送post请求,使用cookie获取登录后的页面
# cookie过期时间比较长的网站
# 在cookie过期之前能够拿到所有的数据
# 配合其他程序一起使用,其他程序专门获取cookie,当前程序专门请求页面

import requests
session = requests.session()
dtime = datetime.datetime.now()
ans_time = time.mktime(dtime.timetuple())
url = 'http://www.renren.com/PLogin.do'
data = {
    'email': '1111@126.com',
    'password': '1111',
}
headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}
# 使用session发送post请求,cookie保存在其中
s = session.post(url, data=data, headers=headers)
print(s.content.decode())
# 在使用session进行请求登录之后才能访问的地址
r = session.get('http://www.renren.com/1111/profile', headers=headers)
with  open('renren.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode())
    f.close()



# import requests
# cookies = "_r01_=1; anonymid=jc5kipsc-qynbas; wp=0"
# cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}
# r = requests.get('http://www.renren.com/1111/profile', headers=headers, cookies=cookies)
# with  open('renren.html', 'w', encoding='utf-8') as f:
#     f.write(r.content.decode())
#     f.close()

# 字典推导式
# cookies = "_r01_=1; anonymid=jc5kipsc-qynbas; wp=0"
# cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}

# 列表推导式
# [self.url_temp.format(i*50) for i in range(5)]


# 获取登录后的页面的三种方式
# 实例化session,使用session发送post请求,使用它获取登录后的页面
# headers中添加cookie键值对
# 在请求方法中添加cookie参数,接收字典形式的cookie

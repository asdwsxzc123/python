str类型和bytes类型
bytes: 二进制
str: unicode 

""" 
# 字符
各种文字和符号的总称
# 字符集
多个字符的集合
字符集包括: ASCII字符集, GB2312,gb18030,unicode字符集

ASCII编码是1个字节,unicode编码是2个字节

UTF-8是Unicode的实现方式之一,是一种变长的编码方式,可以是1,2,3 """

# 编码,将字符串转化成types类型
a= '12dsf'
b = a.encode()

# 解码
b.decode('utf8')
b.decode('gbk')

""" http 和 https """
# http
#     超文本传输协议
#     默认端口:80
# https
#     http + ssl(安全套接字层)
#     默认端口: 443
# https更安全,但性能更低

""" 爬虫 """
1.概念
爬虫是模拟浏览器发送请求,获取响应
网络爬虫的模拟客户端发送网络请求,接收请求响应,一种按照一定的规则,自动的抓取互联网信息的程序


2.流程
url=>发送请求,获取响应=>提取数据=>保存
发送请求,获取响应=>提取url

# 爬虫要根据当前url地址对应的响应为准,当前url地址的elements和内容和url的响应不一样
#  爬虫的数据
# 当前的数据在 url地址对应的响应中
# js生成的数据

""" url """
# 形式 scheme://host[:port]/path/.../[?query-string][#anchor]
scheme:协议 (例如: http,https,ftp)
host: 服务器的ip地址或域名
port: 服务器的端口(如果走协议默认端口80 or 443)
path: 访问资源的路径
query-string: 参数,发送http服务器的数据
anchor: 锚(调转到网页的指定锚点位置)


""" 常见请求头 """
1.host
2.connection
3.upgrade-insecure-requests: 1
4.User-Agent(浏览器名称)
5.accept(传输的文件类型)
6.referer(页面调转处)
7.accept encoding: gzip,(文件编解码格式)
8.cookie
9.x-requested-with: XMLHttpRequest(ajax异步请求)

""" 爬虫分类 """
1.通用爬虫: 搜索引擎爬虫
# 90%的内容是没用的
# 图片,音频,视频多媒体的内容通用搜索引擎无能为力
# 不同的用户不用的搜索目的,返回的内容相同
2.聚焦爬虫: 针对爬虫


""" robots协议 """
# 是道德层面的约束
# www.taobao.com/robots.txt

""" 安装源码 """
# 压缩文件,有个setup.py
# python setup.py install
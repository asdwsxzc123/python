异步:
# 调用在发出之后,这个调用就直接返回,不管有没有结果
非阻塞:
# 关注的是程序在等待调用结果时的状态,指在不能立即得到结果之前,该调用不会阻塞当前线程

scrapy engine(引擎) 总指挥,负责数据和信号在不同的模块通讯
scheduler: (调度器) 一个队列,存放引擎发过来的request请求
downloader: (下载器) 下载吧引擎发送过来的requests请求,并返回给引擎
spiders: (爬虫) 处理引擎发送过来的response,提取数据,提取url并交给引擎,自己手写
item pipeline(管道): 处理引擎传过来的数据,比如存储 ,需要手写
downloader middlewares(下载中间件): 可以自定义的下载扩展,比如设置代理
spider middlewarespider(中间件): 可以自定义requests请求和进行response过滤

# 创建一个爬虫项目
scrapy startproject 项目名
# 生成一个爬虫
scrapy genspider itcast 'itcast.cn'
# 提取数据
晚上spider,提供xpath等方法
# 保存数据
pipeline中保存数据

# 运行
scrapy crawl itcast

# log
# settings中
LOG_LEVEL = 'WARNING'
LOG_FILE = './log.log'

# scrapy.Request
callback : 指定传入的url交给那个解析函数去分析
meta: 实现不同的解析函数中传递数据,meta默认会携带部分信息,比如下载延迟,请求深度
dont_filter: 让scrapy的去重不会过滤当前url,scrapy默认有url去重的功能,对需要重复请求的url有重要用途
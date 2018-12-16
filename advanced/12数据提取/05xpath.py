# /路径

# 获取文本
# a/text()

# 获取属性
# a/@href

# //ul[@id="detail-list"]

# li//a li下的任意一个a

# 包含
# //div[contains(@class,'i')]


from lxml import etree
text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''
html = etree.HTML(text)
#获取class为item-1 li下的a的herf
ret1 = html.xpath('//li[@class="item-1"]/a[@href]')

#获取class为item-1 li下的a的文本
ret2 = html.xpath('//li[@class="item-1"]/a/text()')

#每个li是一条新闻，把url和文本组成字典
# for href in ret1:
#     item = {}
#     item['href'] = href
#     item['title'] = ret2[ret1.index(href)]

ret3 = html.xpath('//li[@class="item-1"]')
for i in ret3:
    item = {}
    item['title'] = i.xpath('./a/text()')[0] if len(i.xpath('./a/text()')[0]) > 0 else None
    item['href'] = i.xpath('./a/@href')[0] if len(i.xpath('./a/@href')[0]) > 0 else None

# lxml注意
# 能够修正lxml代码，可能会出错
# 使用etree.tostring,观察修改之后html的样子，根据修改之后的html字符串写xpath
# 提取页面的思路
# 1. 先分组，取到一个包含分组标签的列表
# 2. 遍历，取其中每一组进行数据的提取，不会造成数据的对应错乱

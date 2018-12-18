# 非结构化数据: html
# 处理方法: 正则,xpath

# 结构haunt数据 json,xml
# 处理方法: 转化为字典

""" json注意点 """
# 1.json中的字符串都是用双引号引起来
# 如果不是双引号,
#     1.eval
#     2.replace
# json.dumps json.loads() json字符
# json.dump json.load() 包含json的类文件对象

# 类文件对象
# 具有write和read的对象


# json.load(): 提取类文件对象中的数据
# with open('douban.json' , 'r', encoding="utf-8") as f:
#     ret = json.load(f)
#     print(ret)

# json.dump(): 吧python类型放入类文件对象中
# with open('douban.json' , 'w', encoding="utf-8") as f:
#     ret = {
#         'lisi': '12'
#     }
#     json.dump(ret,f,ensure_ascii=False,indent=4)

""" 正则 """
# 查找
# re.findall('.', '\n', re.DOTALL)
# re.findall('.', '\n', re.S)

# re.findall('<.+?>', html_str, re.S)

# 替换
# re.sub('\d', '-', str)

# re.compile(编译)
# pattern.match(从头找一个)
# pattern.search(找一个)
# pattern.findall(找所有)
# pattern.sub(替换)

# P = re.compile('\d')
# p.findall('_', str)

# '\n' => \n
# r'\n' => \\n

# '\n' =r'\n'

# re.findall(r'a.*bc', 'a\nbc', re.S) => 'a\nbc'
# re.findall(r'a(.*)bc', 'a\nbc', re.S) => '\n'
# 括号前后的内容起到定位和过滤的效果
# 原始字符串r, 如果匹配字符串中有反斜杠的时候,使用r可以忽略反斜杠带来的转义效果

# 点号默认匹配不到\n,

# 爬虫套路
# 准备url
# 代理user-Agent
# 添加随机的代理ip
# 在对方判断出屋面是爬虫之后,添加更多的headers字段,包括cookie
# cookie可以使用session包处理
# 准备一组cookie池
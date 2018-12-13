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

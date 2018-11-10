import re
# 匹配单个字符
# [] 匹配[]列举的字符
# \d 匹配数字
# \D 匹配非数字
# \s 匹配空白,空格
# \S 匹配非空
# \w 匹配单词字符 0-9,a-z,_
# \W 匹配非单词

# {11} 匹配需要有11位
# {1,n} 匹配有1到n
# ? 0或1
# + 1到n
# * 有或者没有,可以无限次
# .  批量任意字符(\n除外),不能匹配回车, re.S有了这个可以匹配到\n

# content = """
# 1111
# dafd222sf
# 333
#  """
# ret = re.match(r'.*', content, re.S)
# # ret.group()
# print(ret.group())

#1. 匹配变量名是否有效
# 英文,下划线
# names = ['name1', '_name', '2_name', '1232', 'age!', 'a#123']
# for name in names:
#   try:
#       ret = re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', name)
#       if (ret):
#         print('符合要求:%s,匹配的数据:%s'%(name,ret.group()))
#       else:
#         print('不符合:%s'%name)

#   except Exception as ret:
#     print('不符合:%s'%name)

# 2. 邮箱,匹配163,之前要有4-20位英文字母下划线数字
email = 'sdfb@163.com'
ret = re.match(r"^[a-zA-Z_0-9]{4-20}@163\.com$", email)
print(ret)
if ret:
  print('验证通过:%s'%email)
else:
  print('不通过:%s'%email)
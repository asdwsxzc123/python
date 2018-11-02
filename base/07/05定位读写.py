# seek(offset, from) 有两个参数
# offset:偏移量
# from: 方向
  # 0: 文件的开头
  # 1: 表示当前位置
  # 2: 文件末尾

f = open('./text/01.txt', "r+", encoding='gb18030', errors='ignore')
content = f.read(1)
print(content)
print(f.read(1))
print(f.read(1))
# 偏移的位置
f.seek(100,0)
print(f.read(2))
f.write('hahah')
f.seek(0,0)
print(f.read(2))
f.close()

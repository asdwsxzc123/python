import os
# os.rename('./text/01.txt', '0101.txt')
# os.remove('./text', 'xxx.txt')

# 创建文件
# os.mkdir('./text/1')

# 修改目录
os.chdir('./text/')

# 获取当前路径
path = os.getcwd()

# 所有文件和文件夹
os.listdir('./')

# 删除文件
os.rmdir('./')
print(path)
# open('')
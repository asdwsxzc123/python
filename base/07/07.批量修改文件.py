import os
# 1. 获取一个要重命名的文件夹的名字
folder_name = input('请输入需要重命名的文件夹:')

#2. 获取的文件夹中所有的文件名称
file_names = os.listdir(folder_name)
#3. 对获取的名字进行重命名
""" 方法1 修改路径 """
# os.chdir(folder_name)
# for name in file_names:
#   print(name)
#   os.rename(name,'[京东出品]-'+name )
""" 方法2 添加路径 """
for name in file_names:
  old_file_name = './%s/%s' % (folder_name, name)
  new_file_name = './%s/[京东出品1]-%s'%(folder_name,name)
  print(old_file_name)
  print(new_file_name)
  os.rename(old_file_name, new_file_name)

import os 
fold_name = input('文件夹:')
file_names = os.listdir(fold_name)
i = 0
for name in file_names:
  old_file_name = './%s/%s'%(fold_name,name)
  new_file_name = '%s-%d'%('hero',i)
  i +=1
  os.rename(old_file_name, new_file_name)

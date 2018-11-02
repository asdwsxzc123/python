import os
fold_name = input('文件夹:')
file_names = os.listdir(fold_name)
i = 0
for name in file_names:
    old_file_name = './%s/%s' % (fold_name, name)
    new_file_name = './%s/%s-%d.png' % (fold_name, fold_name, i)
    i += 1
    print(new_file_name)
    os.rename(old_file_name, new_file_name)

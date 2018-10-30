# 获取要复制的文件名 input
# 打开这个文件
# w打开文件
# 创建新的备份文件xxx[附件].txt

fileName = input('请输入需要备份的文件(带后缀):')
f = open('./text/'+ fileName, "r")
content = f.read()

position = fileName.rfind('.')
newFileName = fileName[0:position] + '[备份]' + fileName[position:]

f_write = open('./text/' + newFileName, 'w')

# 大文件
# f = open('./02str.py', "r")
# while True:
#   content = f.read(1024)
#   if len(content) == 0:
#     break

f_write.write(content)

f.close()
f_write.close()

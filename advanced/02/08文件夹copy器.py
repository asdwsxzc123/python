import multiprocessing
import os
import time


def copy_file(file_name, old_folder_name, new_folder_name, q):
    '''完成文件复制 '''
    print('------copy文件:%s' % file_name)
    f = open(old_folder_name + '/' + file_name, 'rb')
    content = f.read()
    f.close()
    fw = open(new_folder_name + '/' + file_name, 'wb')
    fw.write(content)
    fw.close()
    # 如果拷贝完就向队列写入以消息表示已经完成
    q.put(file_name)

def main():
    # 1. 获取要copy的文件夹名称
    old_folder_name = input('请输入要复制的文件夹名称:')
   
    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + '[复件]'
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取copy文件夹的文件 listdir()
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 创建Queue
    q = multiprocessing.Manager().Queue()
    # 复制源文件夹中的文件到新文件夹中的文件中去
    for file_name in file_names:
        po.apply_async(copy_file, args=(
            file_name, old_folder_name, new_folder_name,q,))
    po.close()
    # po.join()
    all_file_num = len(file_names) #获取所有的文件个数
    copy_num = 0
    while True:
        file_name = q.get()
        copy_num += 1
        print('\r 拷贝的进度为: %.2f %%' % ((copy_num/all_file_num)*100))
        if all_file_num <= copy_num:
            print('拷贝完毕')
            break

if __name__ == '__main__':
    main()

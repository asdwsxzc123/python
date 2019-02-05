# coding: utf-8
def insert_sort(alist):
    """ 插入排序 """
    n = len(alist)
    # 从右边的无序序列中去除多少个元素执行这样的过程
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break